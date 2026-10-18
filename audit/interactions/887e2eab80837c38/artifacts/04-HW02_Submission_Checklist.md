# Quy định và checklist đối chiếu hồ sơ nộp HW02

Ngày lưu: 15/10/2026. Nguồn chính: đề `2026.HW02.Domain Testing_En.md`, mục 14 và 15; đối chiếu thêm mục 5–10, 12 và 17. File này dùng để kiểm tra trong quá trình làm và trước khi nộp; không thay thế báo cáo hoặc README của bài nộp.

## Cách sử dụng

- Đọc file này khi tạo, cập nhật hoặc tổng hợp hồ sơ HW02.
- `[ ]` nghĩa là chưa được xác nhận đạt; có file không đồng nghĩa nội dung đã hoàn chỉnh.
- Chỉ đánh dấu `[x]` khi người dùng yêu cầu xác nhận mục đã hoàn thành, theo quy ước tại `HW02_Progress.md`.
- Các tên Main_Report, Bug_Report, AI_Critique, AI_Audit_Report và Git_Commit_Log là quy ước tổ chức đề xuất. Đề chỉ quy định chính xác tên `README.md`, tên ZIP và các định dạng bắt buộc.
- Khi thay đổi test hoặc kết quả chạy, đối chiếu số liệu giữa báo cáo, bảng test, bug report và README. Bản Markdown và PDF phải cùng phiên bản nội dung.

## 1. File ZIP và nơi nộp

- [ ] Tên file theo mẫu `<StudentID>_HW02_AI_DomainTesting_<SelfAssessedGrade>.zip`.
- [ ] StudentID là MSSV của người nộp, được xác nhận trước đóng gói.
- [ ] SelfAssessedGrade là điểm tự chấm gồm 3 chữ số từ `000` đến `100`, khớp bảng tự đánh giá trong README.
- [ ] Ví dụ định dạng: `25127001_HW02_AI_DomainTesting_090.zip`.
- [ ] Hạn nộp được kiểm tra tại liên kết nộp trên Moodle; không dùng thời lượng 10 giờ làm hạn nộp.
- [ ] ZIP mở được, không thiếu file và các liên kết tài liệu nội bộ còn sử dụng được.
- [ ] Nộp trên Moodle trước hạn, lưu xác nhận nộp.

## 2. Danh sách file bắt buộc trong ZIP theo mục 14

| Hạng mục | File đề xuất | Định dạng đề yêu cầu | Nội dung phải đối chiếu |
| --- | --- | --- | --- |
| Báo cáo chính | `Main_Report.md` và `Main_Report.pdf` | Markdown + PDF | Gồm báo cáo Domain Testing và Boundary Value Analysis |
| Báo cáo lỗi | `Bug_Report.md` | Mục 14 không chỉ định đuôi riêng; mục 6 yêu cầu báo lỗi trong báo cáo Markdown và GitHub Issues | Mọi bug phát hiện; screenshot trên từng GitHub Issue; liên kết giữa bug, test và bằng chứng |
| Nhận xét phản biện AI | `AI_Critique.md` và `AI_Critique.pdf` | Markdown + PDF | Đoạn 200–300 từ theo mục 10 |
| Báo cáo kiểm toán sử dụng AI | `AI_Audit_Report.md` và `AI_Audit_Report.pdf` | Markdown + PDF | Phụ lục bắt buộc; khai báo và log từng tương tác theo mục 9 |
| Nhật ký Git | `Git_Commit_Log.txt` | Tệp văn bản | Commit cho từng bước kiểm thử của mỗi chức năng theo mục 12 |
| README bài nộp | `README.md` | Markdown, tên README.md theo đề | Bảng tự đánh giá, test summary và video demo |
| Tài liệu hỗ trợ | Các file/thư mục sử dụng thực tế | Theo loại tài liệu | Ảnh, log, dữ liệu, script, tài liệu bổ sung được viện dẫn trong bài |

Word `Main_Report.docx` là bản hỗ trợ chỉnh sửa, không thay thế PDF bắt buộc. Không tự thêm yêu cầu bắt buộc một bản PDF riêng cho Bug_Report khi đề không quy định.

## 3. Nội dung cần kiểm tra trong báo cáo chính

- [ ] Có đủ bốn chức năng, mỗi pool A/B/C/D một chức năng, không trùng với thành viên khác trong nhóm.
- [ ] A: FR-02 Đăng nhập và khóa tài khoản, đúng lựa chọn người dùng đã chốt.
- [ ] B: FR-09 Mã giảm giá, đúng lựa chọn người dùng đã chốt.
- [ ] C: FR-15 Quản lý sản phẩm, đúng lựa chọn người dùng đã chốt.
- [ ] D: đã xác nhận và bổ sung chức năng Mobile; hiện chưa chốt.
- [ ] Mỗi chức năng có Domain Testing và BVA, giải thích chi tiết từng bước theo bài giảng.
- [ ] Có test case và kết quả thực tế; chưa chạy ghi Not Run, không bịa Pass/Fail hoặc bằng chứng.
- [ ] Có AI gap analysis nếu AI bỏ sót test case/bug, giải thích nguyên nhân có căn cứ.
- [ ] Bug report và evidence được liên kết rõ trong báo cáo.
- [ ] Nội dung Markdown/PDF đồng nhất, PDF hiển thị đúng chữ, bảng và trang.

Quy ước cập nhật 16/10/2026: bảng EC xét từng Input/Output; bảng bao phủ có EC đầu ra. Bảng test dùng đúng 10 thuộc tính của `Test cases_Template_En.xlsx`: ID, Test case name, Precondition, Test step, Expected Result, Actual Result, Status, Tester, Tested Date, Remark. Kỹ thuật, EC, giá trị biên và evidence giữ trong phần phân tích/bao phủ/run riêng, không thêm cột hay lặp bảng cho mỗi test. Đây là cách tổ chức đã chọn, không phải yêu cầu nguyên văn về tên cột trong đề.

## 4. Báo cáo lỗi và bằng chứng

- [ ] Mọi bug đã xác nhận có mô tả Markdown và GitHub Issue của nhóm.
- [ ] Từng issue có ảnh chụp bug, không chỉ có mô tả văn bản.
- [ ] Bug có tiền điều kiện, dữ liệu, bước tái hiện, expected/actual và test liên quan.
- [ ] Link issue và ảnh truy cập được; evidence trong ZIP có tên và vị trí nhất quán.
- [ ] Nếu không phát hiện bug, ghi số liệu và phạm vi đã chạy trung thực; không tạo bug giả để điền mẫu.

## 5. AI Audit Report và AI Critique

- [ ] Có khai báo dùng AI cho những nhiệm vụ nào, phản ánh đúng việc sử dụng thực tế.
- [ ] Từng tương tác có tên công cụ AI, ngày giờ, prompt và output.
- [ ] Prompt/output nguyên văn hoặc bản lưu đầy đủ được liên kết; tóm tắt không thay thế output đầy đủ.
- [ ] Phần lịch sử chưa thu thập được ghi rõ; không dựng lại thời gian, hội thoại hay kết quả rà soát.
- [ ] Audit được trình bày/liên kết như phụ lục của báo cáo chính.
- [ ] Có bằng chứng human review/chỉnh sửa thực tế; nếu theo mẫu AI-02, điền verdict, lý do và bản sinh viên sửa khi đã đánh giá.
- [ ] AI Critique dài 200–300 từ, trả lời AI sai/thiếu/thiên lệch ở đâu, vì sao và bài học phối hợp với AI.
- [ ] Hai hạng mục có đủ Markdown + PDF, cùng phiên bản nội dung.

## 6. README và bảng tự đánh giá

- [ ] README chứa số chức năng.
- [ ] README chứa số test case đã thiết kế, đã chạy, pass, fail và chưa chạy.
- [ ] README chứa số bug, phân biệt bug duy nhất với số test fail.
- [ ] README có video demo hoặc link demo tương ứng với nội dung thực hiện.
- [ ] Không đếm trùng một TC được gắn cả Domain Testing và BVA.
- [ ] Quy ước thống kê rõ: nếu dùng trạng thái cuối mỗi TC, executed = pass + fail; designed = executed + not run; blocked nếu có được giải thích.
- [ ] Bảng tự chấm đã điền và tổng đúng, phù hợp điểm trong tên ZIP.

| Tiêu chí theo mục 15 | Điểm tối đa | Điểm tự chấm |
| --- | --- | --- |
| Chức năng A Domain + Boundary | 25 | Chưa tự chấm |
| Chức năng B Domain + Boundary | 25 | Chưa tự chấm |
| Chức năng C Domain + Boundary | 25 | Chưa tự chấm |
| Chức năng D Mobile Domain + Boundary | 15 | Chưa tự chấm |
| Agent Skills | 10 | Chưa tự chấm |
| Tổng | 100 | Chưa tự chấm |

## 7. Agent Skills do người dùng đã chọn thực hiện

Mục 7 khuyến khích làm skill, bảng điểm dành 10 điểm riêng. Người dùng đã chọn làm, nên hồ sơ thực hiện hạng mục này cần:

- [ ] Nộp các thư mục skill và tài nguyên cần thiết, bản nộp khớp bản đã dùng.
- [ ] Có video demo end-to-end áp dụng skill trên một chức năng hoàn chỉnh.
- [ ] Đưa link YouTube vào hồ sơ/README; kiểm tra truy cập được.
- [ ] Phân biệt kiểm tra cấu trúc skill với demo thực tế; chưa có video thì không nhận đã hoàn thành phần demo.

## 8. Tình trạng quan sát được khi tạo checklist

Các ghi nhận dưới đây chỉ mô tả file hiện có, không đánh dấu hạng mục đã hoàn thành:

- Có `Main_Report.md` và `Main_Report.docx`; chưa có bản PDF chính thức tại thư mục HW02. PDF xem trước trong tmp chỉ dùng QA.
- FR-02 có bản nháp Domain Testing và 11 TC Not Run; chưa BVA và chưa thực thi.
- Có `FR-02/audit/AI_Audit_FR02.md`, mới ghi một tương tác thiết kế và snapshot, chưa là audit đầy đủ toàn HW02.
- Có `FR-02/Git_Log.txt`, chưa là Git log tổng hợp cuối bài.
- Có ba skill trong `skills/`; chưa có video demo hoàn chỉnh.
- FR-09, FR-15 chưa thiết kế/chạy; Pool D chưa chốt.
- Chưa có AI_Critique, AI_Audit_Report tổng hợp, Bug_Report và README bài nộp hoàn chỉnh.

## 9. Quy định khác cần nhớ

- Không chấp nhận nộp trễ.
- Thiếu bất kỳ tài liệu bắt buộc nào bị 0 điểm.
- Sao chép giữa sinh viên, bao gồm prompt, khiến cả hai bị 0 điểm.

## Nhật ký

| Ngày | Nội dung |
| --- | --- |
| 15/10/2026 | Lưu quy định nộp và danh sách hồ sơ để đối chiếu theo yêu cầu người dùng; chưa đánh dấu hoàn thành hạng mục nào. |
