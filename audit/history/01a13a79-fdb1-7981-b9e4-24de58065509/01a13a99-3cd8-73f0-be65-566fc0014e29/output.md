Với **FR-02, FR-09 và FR-15**, bạn cần làm một bộ kiểm thử và báo cáo cho **từng chức năng**, gồm các phần sau. Pool D bổ sung sau.

**1. Phân tích yêu cầu và thiết kế test bằng hai kỹ thuật**

| Chức năng | Domain Testing: phân tích những miền nào? | Boundary Value Analysis: kiểm tra biên nào? |
|---|---|---|
| **FR-02 — Đăng nhập & khóa tài khoản** | Email/tài khoản hợp lệ hoặc không hợp lệ; mật khẩu đúng/sai; tài khoản bình thường/đang khóa | Số lần sai quanh ngưỡng **3 lần**; thời điểm trước, tại và sau khi hết **30 giây khóa** |
| **FR-09 — Coupon** | Mã tồn tại/không tồn tại; active/inactive; còn hạn/hết hạn; đủ/thiếu tổng tiền; có/không đăng nhập; còn/hết lượt dùng | Tổng tiền ngay dưới, bằng và trên ngưỡng; thời điểm hết hạn; số lượt dùng quanh giới hạn |
| **FR-15 — Quản lý sản phẩm** | Tên hợp lệ/rỗng/quá dài; giá hợp lệ/không hợp lệ; danh mục hợp lệ/thiếu/không tồn tại; thao tác thêm/xem/sửa/xóa | Tên **254/255/256 ký tự**; giá âm, **0**, dương; giá gần 0 theo độ chính xác hệ thống hỗ trợ |

Với mỗi kỹ thuật, phải **giải thích từng bước thiết kế**, không chỉ đưa bảng test case. Expected result phải lấy từ **README**, không lấy hành vi hiện tại của source làm chuẩn.

**2. Viết test case rồi thực hiện kiểm thử**

Mỗi test case nên có:

- ID, yêu cầu được kiểm tra và kỹ thuật sử dụng.
- Điều kiện chuẩn bị, dữ liệu đầu vào.
- Các bước thực hiện.
- Kết quả mong đợi, kết quả thực tế.
- Trạng thái **Pass/Fail/Not Run** và bằng chứng.

Riêng FR-02 cần cách đặt lại trạng thái tài khoản và kiểm soát thời gian; FR-09 cần chuẩn bị coupon/lịch sử sử dụng; FR-15 cần dữ liệu sản phẩm và danh mục để kiểm tra cả việc sửa đúng sản phẩm.

**3. Báo cáo lỗi**

Mọi bug xác nhận được phải ghi vào **báo cáo Markdown** và **GitHub Issues của nhóm**, kèm ảnh. Nội dung nên đủ để tái hiện: môi trường, dữ liệu, bước thực hiện, expected/actual và liên kết test case.

**4. Ghi lại quá trình dùng AI và Git**

- Dùng AI theo từng bước phân tích và thiết kế; bạn kiểm tra, sửa kết quả.
- **AI Audit Report:** tên công cụ, ngày giờ, prompt, output của từng tương tác.
- **AI gap analysis:** test case/bug AI bỏ sót và nguyên nhân, nếu có.
- **AI Critique 200–300 từ:** nhận xét sai sót, hạn chế và bài học phối hợp với AI.
- **Commit sau mỗi bước kiểm thử của từng chức năng**, rồi xuất Git log ra file văn bản.

**5. Tập hợp hồ sơ nộp**

Chuẩn bị báo cáo chính **Markdown + PDF**, bug report, AI Audit/AI Critique **Markdown + PDF**, Git log và `README.md` có bảng tự chấm điểm cùng thống kê test.

Ba chức năng này chiếm **75 điểm** trong rubric. Bạn có thể hoàn thành chúng trước, nhưng bản nộp cuối vẫn cần **Pool D**, các tài liệu bắt buộc và phần Agent Skills nếu muốn đạt điểm hạng mục đó.

Trình tự làm hợp lý là: **đọc bài giảng → phân tích yêu cầu → thiết kế Domain Testing → thiết kế BVA → rà soát test → chạy test → báo bug → tổng kết**, lặp lại cho từng chức năng.