**Mục này đã ngắn, không cần bỏ ý nào.** Chỉ nên sửa câu cho gọn và rõ hơn:

**2.1 Yêu cầu làm cơ sở kiểm thử**

- Đăng nhập bằng email và mật khẩu đúng khi tài khoản không bị khóa.
- Mỗi lần đăng nhập sai tăng bộ đếm 1; sai 3 lần liên tiếp thì khóa 30 giây.
- Thông báo lỗi phù hợp, không tiết lộ chi tiết nguyên nhân.
- Đăng nhập thành công trả JWT; client lưu token và gửi `Authorization: Bearer <token>` trong các request cần xác thực.
- Trường email dùng `type="email"` và validation HTML5.

Nếu các bảng phía sau vẫn tham chiếu **R1–R7**, cần thống nhất mã với các yêu cầu ở đây; hiện 5 gạch đầu dòng chưa cho biết mã nào tương ứng.