"""Export user-visible Codex messages only; never export reasoning or instructions."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import json,re,hashlib,argparse

SESSION='01a13a79-fdb1-7981-b9e4-24de58065509'
SOURCE=Path(r'C:\Users\tung1\.codex\sessions\2026\10\14\rollout-2026-10-14T19-53-55-01a13a79-fdb1-7981-b9e4-24de58065509.jsonl')
ROOT=Path(r'D:\vscode\Software testing\HW02\audit')
TZ=timezone(timedelta(hours=7))

def local(t):return datetime.fromisoformat(t.replace('Z','+00:00')).astimezone(TZ).isoformat(timespec='milliseconds')
def text_of(p):return '\n'.join(c['text'] for c in p.get('content',[]) if c.get('type') in ('input_text','output_text') and isinstance(c.get('text'),str))
def excluded(s):return s.strip().startswith(('<environment_context>','<external_codex_apps_open_page>'))
def fence(s):
    longest=max([len(x) for x in re.findall(r'`+',s)]+[2]);mark='`'*(longest+1)
    return mark+'text\n'+s+'\n'+mark+'\n'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--current-output',required=True);args=ap.parse_args()
    raw=SOURCE.read_bytes();rows=raw.splitlines();turns=[];current=None;meta=None;allids=set();filtered=0
    for line_num,line in enumerate(rows,1):
        r=json.loads(line);p=r.get('payload',{});typ=r.get('type')
        if typ=='session_meta':meta=p;assert p['id']==SESSION
        if typ=='event_msg' and p.get('type')=='task_started':
            current={'turn_id':p['turn_id'],'started_at':r['timestamp'],'prompts':[],'outputs':[],'source_lines':[],'model':None,'complete':False}
            turns.append(current)
        if current is None:continue
        if typ=='turn_context' and p.get('turn_id')==current['turn_id']:current['model']=p.get('model')
        if typ=='event_msg' and p.get('type')=='task_complete' and p.get('turn_id')==current['turn_id']:
            current['complete']=True;current['completed_at']=r['timestamp']
        if typ!='response_item' or p.get('type')!='message' or p.get('role') not in ('user','assistant'):continue
        if p.get('id') in allids:continue
        allids.add(p.get('id'))
        if p['role']=='assistant' and p.get('phase') not in ('commentary','final_answer'):continue
        txt=text_of(p)
        if p['role']=='user' and excluded(txt):filtered+=1;continue
        if not txt:continue
        msg={'message_id':p.get('id'),'timestamp_utc':r['timestamp'],'timestamp_local':local(r['timestamp']),'role':p['role'],'phase':p.get('phase'),'text':txt,'source_line':line_num}
        (current['prompts'] if p['role']=='user' else current['outputs']).append(msg)
        current['source_lines'].append(line_num)
    assert meta and meta['id']==SESSION
    turns=[t for t in turns if t['prompts']]
    now=datetime.now(TZ).isoformat(timespec='seconds')
    final=Path(args.current_output).read_text(encoding='utf-8')
    incomplete=[t for t in turns if not any(o['phase']=='final_answer' for o in t['outputs'])]
    assert len(incomplete)<=1
    if incomplete:
        t=incomplete[0]
        assert 'Hãy sử dụng file json của codex' in t['prompts'][0]['text']
        t['outputs'].append({'message_id':None,'timestamp_utc':None,'timestamp_local':now,'role':'assistant','phase':'final_answer','text':final,'source_line':None,'origin':'Prepared current response, persisted before sending; not yet present in source JSONL at extraction.'})
        t['current_response_prepared']=True
    # Retain prior audit data and reports as historical artifacts.
    archive=ROOT/'prior_reports/before_history_import'
    archive.mkdir(parents=True,exist_ok=True)
    for name in ['AI_Audit_Report.md','Appendix_A_Prompt_Log.md','generated_report_state.json']:
        path=ROOT/name
        if path.exists() and not (archive/name).exists():(archive/name).write_bytes(path.read_bytes())
    outdir=ROOT/'history'/SESSION;outdir.mkdir(parents=True,exist_ok=True)
    index=[];reportrows=[];log=['# Appendix A Nhật ký toàn văn phiên HW02\n\n',f'Phiên: {SESSION}. Nguồn JSONL được đọc tại {now}.\n\n',
    'Chỉ xuất các tin nhắn người dùng và phản hồi AI hiển thị (commentary/final). Không xuất system/developer instructions, reasoning, thống kê token hay nội dung tool thô. Prompt có attachment giữ nguyên văn phần mô tả và đường dẫn, không nhúng lại bytes ảnh/PDF.\n\n']
    for n,t in enumerate(turns,1):
        label=f'AI-HW02-{n:03}';folder=outdir/t['turn_id'];folder.mkdir(exist_ok=True)
        t['interaction_id']=label;t['tool']='Codex Desktop';t['extracted_at']=now
        t['source_session']=SESSION;t['source_file']=str(SOURCE)
        target=folder/'record.json'
        if target.exists():
            old=json.loads(target.read_text(encoding='utf-8'))
            # Do not replace saved transcripts on a repeated import.
            assert [m['text'] for m in old['prompts']]==[m['text'] for m in t['prompts']]
            if not old.get('current_response_prepared'):
                assert [m['text'] for m in old['outputs']]==[m['text'] for m in t['outputs']]
        else:target.write_text(json.dumps(t,ensure_ascii=False,indent=2),encoding='utf-8')
        prompt='\n\n'.join(m['text'] for m in t['prompts']);output='\n\n'.join(m['text'] for m in t['outputs'])
        for name,value in [('prompt.md',prompt),('output.md',output)]:
            path=folder/name
            if not path.exists():path.write_text(value,encoding='utf-8')
        timing=local(t['prompts'][0]['timestamp_utc']);base=folder.relative_to(ROOT).as_posix()
        index.append({'interaction_id':label,'turn_id':t['turn_id'],'prompt_time':timing,'model':t['model'],'prompts':len(t['prompts']),'outputs':len(t['outputs']),'record':base+'/record.json','current_response_prepared':bool(t.get('current_response_prepared'))})
        reportrows.append(f"| [{label}]({base}/prompt.md); Codex Desktop; {timing}; {t['model'] or 'model chưa xác minh'} | [Toàn văn]({base}/output.md), [record JSON]({base}/record.json) | Chưa rà soát | Chưa ghi nhận lý do và nguồn đối chiếu | Chưa ghi nhận bản SV sửa |\n")
        log.extend([f'## {label}\n\n',f"### Tên công cụ AI\nCodex Desktop. Model theo turn_context: {t['model'] or 'Chưa xác minh'}.\n\n",f'### Ngày và giờ\nPrompt đầu tiên: {timing}.\n',f"Phản hồi cuối: {t['outputs'][-1]['timestamp_local']}.\n\n",'### Prompt của bạn\n\n'])
        for msg in t['prompts']:
            log.extend([f"Tin nhắn {msg['message_id']}, {msg['timestamp_local']}, dòng nguồn {msg['source_line']}:\n\n",fence(msg['text'])+'\n'])
        log.append('### Output của AI\n\n')
        for msg in t['outputs']:
            log.extend([f"Loại {msg['phase']}, {msg['timestamp_local']}, dòng nguồn {msg['source_line'] if msg['source_line'] is not None else 'phản hồi hiện tại được soạn và lưu trước khi gửi'}:\n\n",fence(msg['text'])+'\n'])
    count=len(turns);completed=sum(not bool(t.get('current_response_prepared')) for t in turns)
    export={'session_id':SESSION,'source_file':str(SOURCE),'source_sha256_at_read':hashlib.sha256(raw).hexdigest(),'source_bytes_at_read':len(raw),'source_lines_at_read':len(rows),'extracted_at':now,'completed_turns_from_jsonl':completed,'current_prepared_turns':count-completed,'interaction_count':count,'user_messages':sum(len(t['prompts']) for t in turns),'assistant_messages':sum(len(t['outputs']) for t in turns),'excluded_context_messages':filtered,'interactions':index}
    (outdir/'index.json').write_text(json.dumps(export,ensure_ascii=False,indent=2),encoding='utf-8')
    log_path=ROOT/'Appendix_A_Prompt_Log.md';log_path.write_text(''.join(log),encoding='utf-8')
    report=f'''# AI Audit Report HW02

Tôi sử dụng công cụ AI cho các nhiệm vụ sau:

- Đọc đề và đặc tả eShop, lựa chọn chức năng và giải thích lý thuyết Domain Testing/BVA.
- Thiết kế, chỉnh sửa skill và tạo bản nháp phân tích/test FR-02.
- Dịch tài liệu, tạo và chỉnh sửa báo cáo, tìm template và lập checklist nộp bài.
- Thu thập và tổng hợp lịch sử tương tác để lập AI Audit.

## 1. Thông tin Sinh viên

| Mục | Giá trị |
| --- | --- |
| Họ tên | NGUYỄN SƠN TÙNG |
| MSSV | 23120399 |
| Nguồn thông tin cá nhân | Mẫu AI-02 HW01 người dùng cung cấp; không sao chép ngày, điểm, chữ ký hoặc verdict HW01 |
| Lớp / Khoá | Chờ xác nhận cho HW02 |
| Mã bài tập | HW02 |
| Thời gian hội thoại | {local(turns[0]['prompts'][0]['timestamp_utc'])} đến {now} |
| Công cụ | Codex Desktop; model từng lượt ghi trong Appendix A và record JSON |

## 2. Hướng dẫn

Giữ nguyên văn prompt và output trong Appendix A, đối chiếu bằng turn ID, message ID và dòng JSONL. Gắn verdict VALID/INVALID/INCOMPLETE sau khi sinh viên thực sự đánh giá; lý do cần dẫn slide, ISTQB hoặc RFC phù hợp. Bản sửa cần có so sánh/tô sáng khi xuất Word. Không dùng bản tóm tắt thay toàn văn.

Đã trích {completed} lượt hoàn tất từ file JSONL. Lượt hiện tại được lưu riêng bằng phản hồi đã soạn trước khi gửi, không giả là đã có trong JSONL. Tổng {count} tương tác trong báo cáo, {export['user_messages']} tin nhắn người dùng (có một phản hồi câu hỏi bổ sung trong lượt lựa chọn chức năng), {export['assistant_messages']} tin nhắn AI gồm commentary và final. Tin nhắn ngữ cảnh máy không được tính là prompt.

## 3. Bảng Audit — 1 hàng / artifact

Mỗi hàng dưới là artifact hội thoại của một tương tác, gồm prompt và các phản hồi AI. Một tương tác có thể tạo thêm nhiều artifact file: do JSONL không bảo đảm chứa đầy đủ bytes của mọi phiên bản file lịch sử, bảng này chưa tách mỗi file lịch sử thành một hàng để tránh nhận nhầm bản hiện tại là output cũ. Snapshot FR-02 đã có vẫn được giữ tại ../FR-02/audit/snapshots/. Khi lập bản nộp, bổ sung hàng cho từng artifact file có bằng chứng phiên bản; liên kết cùng Interaction ID và không nhân đôi prompt.

| (1) Prompt + Công cụ | (2) Output AI | (3) Verdict | (4) Lý do (ISTQB) | (5) Bản SV sửa |
| --- | --- | --- | --- | --- |
'''+''.join(reportrows)+f'''
## 4. Tổng kết Độ chính xác AI

| Chỉ số | Số lượng | Tỉ lệ |
| --- | --- | --- |
| Artifact hội thoại đã ghi | {count} | 100% nhóm hội thoại đã trích |
| Artifact đã được sinh viên gán verdict | 0 | Chưa đánh giá |
| Chưa rà soát | {count} | 100% |
| VALID | Chưa xác nhận | Chưa tính |
| INVALID | Chưa xác nhận | Chưa tính |
| INCOMPLETE | Chưa xác nhận | Chưa tính |

Các prompt góp ý/chỉnh sửa của sinh viên được giữ nguyên trong log nhưng không tự quy đổi thành verdict cho toàn artifact. Chưa tính thống kê độ chính xác khi chưa có đánh giá và nguồn lý do được xác nhận.

## 5. Kết luận — Khi nào nên / không nên dùng AI?

Chưa viết kết luận 80–150 chữ thay sinh viên. Cần bổ sung sau khi rà soát thực tế các artifact; đây không phải AI Critique 200–300 từ của HW02.

## 6. Mandatory Disclosure

Chưa ký hoặc điền câu cam đoan thay sinh viên. Cần xác nhận phạm vi AI sinh, phần sinh viên tự viết/chỉnh sửa và dẫn phụ lục trước khi hoàn thiện câu khai báo của mẫu AI-02.

## Chữ ký

Chưa ký. Ngày ký và giảng viên chưa xác nhận.

## Tham khảo

- Đề HW02, mục 9 và 14.
- Mẫu AI-02 do người dùng cung cấp, cấu trúc sáu mục và bảng năm cột.
- File phiên Codex: `{SOURCE}`; session ID `{SESSION}`.

## Appendix A và nguồn truy vết

- [Nhật ký prompt/output nguyên văn](Appendix_A_Prompt_Log.md).
- [Chỉ mục JSON](history/{SESSION}/index.json) có SHA-256 nguồn, thời điểm đọc, số dòng, turn/message và đường dẫn record.
- [Báo cáo trước khi import](prior_reports/before_history_import/AI_Audit_Report.md) được giữ nguyên; các record audit cũ không bị xóa.
- Không xuất reasoning/system/developer messages, không sao chép toàn bộ JSONL chứa dữ liệu kỹ thuật vào bài nộp. Tool call/output chưa được xuất nguyên văn trong phụ lục này; nội dung AI hướng người dùng và các tham chiếu file được giữ nguyên. Ảnh/file đính kèm chỉ lưu mô tả/đường dẫn trong prompt; muốn nộp bằng chứng phải kiểm tra các file cần thiết còn tồn tại.
'''
    (ROOT/'AI_Audit_Report.md').write_text(report,encoding='utf-8')
    (ROOT/'generated_report_state.json').write_text(json.dumps({'sha256':hashlib.sha256(report.encode()).hexdigest(),'owner':'history-export','session':SESSION}),encoding='utf-8')
    # Confirm exact text round-trips to JSON, plus appendix inclusion for every message.
    check=log_path.read_text(encoding='utf-8')
    for t in turns:
        saved=json.loads((outdir/t['turn_id']/'record.json').read_text(encoding='utf-8'))
        for kind in ['prompts','outputs']:
            assert [m['text'] for m in saved[kind]]==[m['text'] for m in t[kind]]
            for msg in t[kind]:assert msg['text'] in check
    print(json.dumps({k:export[k] for k in ['interaction_count','completed_turns_from_jsonl','current_prepared_turns','user_messages','assistant_messages','excluded_context_messages']},ensure_ascii=False))
    print('Exact prompt/output round-trip and appendix verification passed. Previous audit preserved.')

if __name__=='__main__':main()
