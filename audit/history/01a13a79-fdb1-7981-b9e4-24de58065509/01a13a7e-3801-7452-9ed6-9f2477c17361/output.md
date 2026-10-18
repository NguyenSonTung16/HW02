Mình sẽ dùng kỹ năng đọc PDF theo nguồn gốc để xem HW02 yêu cầu làm gì và cần nộp những gì.


**HW02 yêu cầu bạn kiểm thử 4 tính năng của eShop bằng cả Domain Testing và Boundary Value Analysis, rồi nộp báo cáo kèm bằng chứng kiểm thử và nhật ký sử dụng AI.** Đây là bài **cá nhân**, thời lượng dự kiến **10 giờ**.

Nguồn: :codex-file-citation{path="C:/Users/tung1/Downloads/2026.HW02.Domain Testing_En.md.pdf" purpose="source"}

**1. Chọn 4 tính năng — mỗi nhóm chức năng chọn 1**

Trang 3 ghi:
> “every student must select four (4) features — one from each pool”

| Pool | Phạm vi chọn |
|---|---|
| **A** | FR-01 → FR-06: đăng ký, đăng nhập/khóa tài khoản, quên mật khẩu, hồ sơ, tìm kiếm sản phẩm, chi tiết sản phẩm |
| **B** | FR-07 → FR-11: giỏ hàng, thanh toán, coupon, trạng thái đơn hàng, lịch sử đơn hàng |
| **C** | FR-12 → FR-19: các chức năng Web Admin |
| **D** | Một tính năng của **Mobile App** |

Các thành viên cùng nhóm phải phân chia để **không trùng tính năng**. Pool D trong đề không liệt kê chi tiết từng chức năng mobile.

**2. Với mỗi tính năng, phải làm những việc sau** *(trang 3)*

- Áp dụng **Domain Testing** để thiết kế bộ test case và giải thích **từng bước** áp dụng kỹ thuật.
- Áp dụng **Boundary Value Analysis** để thiết kế bộ test case và giải thích **từng bước**.
- Thực hiện kiểm thử, ghi nhận kết quả và bằng chứng để lập báo cáo tổng kết.
- Nếu AI bỏ sót test case hoặc bug, ghi lại phần bỏ sót và phân tích nguyên nhân.
- Báo cáo mọi bug tìm được trong **báo cáo Markdown** và **GitHub Issues của nhóm**; mỗi issue phải có ảnh chụp bug.

Đề **không quy định số test case tối thiểu**; yêu cầu bộ test đủ bao phủ và có chất lượng.

**3. Yêu cầu về AI và quá trình làm bài** *(trang 1–4)*

- Hướng dẫn AI theo từng bước của kỹ thuật đã học; bạn phải kiểm tra và chỉnh sửa kết quả AI.
- Có **AI Audit Report** làm phụ lục, ghi từng tương tác: **tên công cụ, ngày giờ, prompt và output**.
- Có **AI Critique dài 200–300 từ**: AI sai hoặc thiếu ở đâu, vì sao, và bài học khi phối hợp với AI.
- Tạo **Git commit cho mỗi bước kiểm thử của từng tính năng**, rồi xuất commit log ra file văn bản.
- Đề **khuyến khích xây Agent Skills** dùng lại cho hai kỹ thuật. Nếu xây skill, nộp skill cùng **link video YouTube demo toàn bộ quy trình trên một tính năng**. Phần này có **10 điểm** trong rubric.

**4. Những gì phải nộp** *(trang 4–5)*

Nộp một file ZIP lên Moodle, gồm:

- Báo cáo chính **Markdown + PDF**, chứa phần Domain Testing và Boundary Value Analysis.
- Bug report và ảnh bằng chứng trên GitHub Issues.
- **AI Critique + AI Audit Report**, dạng **Markdown + PDF**.
- Git commit log dạng văn bản.
- `README.md` có **bảng tự chấm điểm** và **test summary**: số tính năng; số test case đã thiết kế, đã chạy, pass, fail, chưa chạy; số bug; video demo.
- Các tài liệu hỗ trợ, skill và video nếu có.

Tên file:
`<MSSV>_HW02_AI_DomainTesting_<ĐiểmTựChấm>.zip`

Ví dụ: `25127001_HW02_AI_DomainTesting_090.zip`.

**5. Điểm và quy định cần nhớ** *(trang 5)*

| Hạng mục | Điểm |
|---|---:|
| Tính năng Pool A — Domain + Boundary | 25 |
| Tính năng Pool B — Domain + Boundary | 25 |
| Tính năng Pool C — Domain + Boundary | 25 |
| Tính năng Pool D Mobile — Domain + Boundary | 15 |
| Agent Skills | 10 |
| **Tổng** | **100** |

Hạn nộp xem trên **Moodle**. Đề ghi **không chấp nhận nộp trễ**, **thiếu tài liệu bắt buộc bị 0 điểm**, và **sao chép giữa sinh viên, kể cả prompt, khiến cả hai bị 0 điểm**. Có thể chọn ngẫu nhiên 30% sinh viên để vấn đáp 5–7 phút.