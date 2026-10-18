"""Append an immutable AI interaction and regenerate template-shaped Markdown."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path
from datetime import datetime

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--root',required=True);ap.add_argument('--record',required=True)
    args=ap.parse_args();root=Path(args.root);record=json.loads(Path(args.record).read_text(encoding='utf-8-sig'))
    for key in ['request_key','tool','recorded_at','prompt','final_output','task']:
        if not isinstance(record.get(key),str) or not record[key].strip():raise ValueError('Missing '+key)
    dt=datetime.fromisoformat(record['recorded_at'])
    if dt.utcoffset() is None:raise ValueError('Timezone required')
    rid=hashlib.sha256(record['request_key'].encode()).hexdigest()[:16]
    location=root/'interactions'/rid
    target=location/'record.json'
    if target.exists():
        previous=json.loads(target.read_text(encoding='utf-8'))
        if any(previous[k]!=record[k] for k in ['request_key','tool','prompt','final_output','task']):
            raise ValueError('Existing request_key has different content; do not overwrite history')
        print('Audit already recorded:',rid);return
    paths=[Path(x) for x in record.get('artifacts',[])]
    for path in paths:
        if not path.is_absolute() or not path.is_file():raise ValueError('Missing absolute artifact: '+str(path))
    location.mkdir(parents=True,exist_ok=False)
    snapshots=[]
    for i,path in enumerate(paths,1):
        out=location/'artifacts'/f'{i:02}-{path.name}';out.parent.mkdir(exist_ok=True)
        shutil.copyfile(path,out)
        snapshots.append({'source':str(path),'snapshot':out.relative_to(root).as_posix(),'sha256':hashlib.sha256(out.read_bytes()).hexdigest()})
    record['snapshots']=snapshots;record['interaction_id']=rid
    (location/'prompt.md').write_text(record['prompt'],encoding='utf-8')
    (location/'output.md').write_text(record['final_output'],encoding='utf-8')
    target.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
    records=[json.loads(f.read_text(encoding='utf-8')) for f in (root/'interactions').glob('*/record.json')]
    records.sort(key=lambda r:(r['recorded_at'],r['interaction_id']))
    log=['# Appendix A Nhật ký prompt và output\n']
    report=['# AI Audit Report HW02\n','Tôi sử dụng công cụ AI cho các nhiệm vụ sau:\n']
    report.extend('- '+task+'\n' for task in dict.fromkeys(r['task'] for r in records))
    report+=['\n## 1. Thông tin Sinh viên\n','Chưa điền thông tin cá nhân vào báo cáo này. Mã bài tập: HW02. Ngày giờ và công cụ ghi theo từng tương tác.\n',
    '\n## 2. Hướng dẫn\n','Prompt/output được lưu nguyên văn trong Appendix A và từng thư mục tương tác. Chưa có human review thì không tự gán verdict. Lý do cần dẫn slide/ISTQB/RFC; bản sinh viên sửa phải lưu so sánh. Ngày ghi không thay thế thời gian prompt cũ chưa biết.\n',
    '\n## 3. Bảng Audit — 1 hàng / artifact\n','| (1) Prompt + Công cụ | (2) Output AI | (3) Verdict | (4) Lý do (ISTQB) | (5) Bản SV sửa |\n| --- | --- | --- | --- | --- |\n']
    total=0
    for r in records:
        ident=r['interaction_id'];base='interactions/'+ident
        artifacts=r['snapshots'] or [{'snapshot':base+'/output.md'}]
        for item in artifacts:
            total+=1
            report.append(f"| [{ident}]({base}/prompt.md); {r['tool']}; {r['recorded_at']} | [Output nguyên văn]({base}/output.md); [artifact]({item['snapshot']}) | Chưa rà soát | Chưa ghi nhận | Chưa ghi nhận |\n")
        log.extend([f"\n## Tương tác {ident}\n",f"\n### Tên công cụ AI\n{r['tool']}\n",f"\n### Ngày và giờ\nNgày ghi: {r['recorded_at']}\nThời điểm prompt có chứng cứ: {r.get('source_timestamp','Chưa xác minh riêng; xem ngày ghi')}\n",'\n### Prompt của bạn\n',r['prompt']+'\n','\n### Output của AI\n',r['final_output']+'\n',f"\nPhạm vi log: {r.get('log_scope','Phản hồi cuối và snapshot artifact; chưa có export đầy đủ tool/commentary.')}\n"])
    report.extend(['\n## 4. Tổng kết Độ chính xác AI\n',f'Tổng artifact ghi nhận: {total}. Đã human review: 0. Chưa review: {total}. VALID/INVALID/INCOMPLETE: chưa tính; chưa có đánh giá thực tế.\n',
    '\n## 5. Kết luận — Khi nào nên / không nên dùng AI?\n','Chưa thực hiện kết luận 80–150 chữ vì chưa có đánh giá của sinh viên. Không thay cho AI Critique 200–300 từ.\n',
    '\n## 6. Mandatory Disclosure\n','Chưa điền và chưa ký; cần xác nhận phần AI đóng góp, phần sinh viên sửa/tự viết theo thực tế trước khi dùng câu cam đoan của template.\n',
    '\n## Chữ ký\n','Chưa ký.\n','\n## Tham khảo\n','Đề HW02 mục 9 và template AI-02 do người dùng cung cấp.\n',
    '\n## Appendix A\n','[Nhật ký nguyên văn](Appendix_A_Prompt_Log.md). Các verdict bổ sung sau phải lưu riêng và bảo toàn lịch sử; không sửa snapshot ban đầu. Báo cáo này chỉ chứa record đã thu thập, không phải xác nhận đủ lịch sử HW02.\n'])
    # Do not replace a student-reviewed report with an automatic unreviewed one.
    report_path=root/'AI_Audit_Report.md'
    state_path=root/'generated_report_state.json'
    prior_hash=json.loads(state_path.read_text(encoding='utf-8')).get('sha256') if state_path.exists() else None
    edited=report_path.exists() and hashlib.sha256(report_path.read_bytes()).hexdigest()!=prior_hash
    if report_path.exists() and (edited or (root/'human_review.json').exists()):
        report_path=root/'AI_Audit_Report_Generated.md'
    report_path.write_text(''.join(report),encoding='utf-8')
    if report_path.name=='AI_Audit_Report.md':
        state_path.write_text(json.dumps({'sha256':hashlib.sha256(report_path.read_bytes()).hexdigest()}),encoding='utf-8')
    (root/'Appendix_A_Prompt_Log.md').write_text(''.join(log),encoding='utf-8')
    saved=json.loads(target.read_text(encoding='utf-8'))
    assert saved['prompt']==record['prompt'] and saved['final_output']==record['final_output']
    print('Audit saved and verified:',rid)

if __name__=='__main__':main()
