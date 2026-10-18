**Bảng này nên giữ, nhưng có thể rút gọn cột “Ràng buộc/nguồn”.** Không cần bỏ các biến đang dùng để phân lớp và thiết kế test.

Các câu sau là ghi chú về cách phân tích, có thể bỏ khỏi bảng:

- “không tự đặt min/max”
- “không suy ra cấu trúc JSON”
- “cần cách quan sát không sửa logic”
- “không ép localStorage hay cookie”

Thay bằng nội dung trực tiếp:

| Biến | Ràng buộc ghi gọn |
|---|---|
| Email | Định dạng email HTML5 |
| Mật khẩu | Khớp mật khẩu tài khoản |
| Số lần sai trước request | Tăng 1 sau mỗi lần sai; ngưỡng khóa: 3 |
| Trạng thái khóa | Khóa trong 30 giây |
| Thời gian từ lúc bắt đầu khóa | Thời hạn khóa: 30 giây |
| Kết quả đăng nhập | Thành công hoặc bị từ chối/chặn |
| Thông báo lỗi | Phù hợp, không tiết lộ chi tiết nguyên nhân |
| JWT trả về | Được cấp khi đăng nhập thành công |
| Bộ đếm sau request | Tăng 1 sau lần đăng nhập sai |
| Trạng thái khóa sau request | Khóa khi đủ 3 lần sai liên tiếp |
| Token được client lưu | Lưu token sau đăng nhập thành công |
| Header request có xác thực | `Authorization: Bearer <token>` |

**Cần chỉnh thêm hai điểm:**

- Cột **“Kiểu/đơn vị”** đang trộn kiểu dữ liệu với miền giá trị và cách quan sát. Đổi thành **“Kiểu/giá trị”** sẽ phù hợp hơn; thời gian ghi đơn vị **giây**.
- Chỉ giữ mã **R1–R7** khi mục 2.1 đã định nghĩa rõ các mã đó.

Về trình bày, nên chỉnh độ rộng cột hoặc khoảng cách để dòng **FR02-O7 không nằm riêng ở trang sau**.