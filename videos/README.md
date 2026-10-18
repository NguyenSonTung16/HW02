# Video thực thi test

Nhịp đã được người dùng duyệt: mục tiêu 4 giây, dừng 1,5 giây sau từng ô nhập, dừng 2 giây trước khi gửi và giữ kết quả 3,5 giây. Video ghi trình duyệt thật; chú thích tiếng Việt, không có âm thanh.

- [FR-02 — Đăng nhập và khóa tài khoản](FR-02-demo-paced.webm): khoảng 2 phút 16 giây; 6 TC, 1 Pass / 5 Fail.
- [FR-09 — Mã giảm giá](FR-09-demo.webm): khoảng 1 phút 24 giây; 6 TC, 2 Pass / 4 Fail.
- [FR-15 — Quản lý sản phẩm CRUD](FR-15-demo.webm): khoảng 1 phút 37 giây; 6 TC, 3 Pass / 3 Fail.

FR-09 minh họa áp dụng mã tại checkout với tổng giỏ lấy từ sản phẩm thử; TC09 mở route checkout trực tiếp khi chưa đăng nhập để kiểm tra điều kiện JWT. FR-15 minh họa CRUD và dữ liệu biên trên giao diện admin; TC03 giữ cảnh ngay sau lưu và sau reload. Fixtures được chuẩn bị riêng, không sửa logic SUT.

Thanh HW02 TEST HARNESS là phần minh họa của runner. Video này là thực thi TC, khác với video dùng skill thiết kế end-to-end. Chưa đăng YouTube. Lịch sử các take ở thư mục run/audit được giữ nguyên.
