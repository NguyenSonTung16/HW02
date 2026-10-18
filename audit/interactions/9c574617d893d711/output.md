Đã viết [hướng dẫn thực thi đầy đủ 11 case FR-02](<D:/vscode/Software testing/HW02/FR-02/Execution_Guide.md>), gồm lệnh khởi chạy, chuẩn bị dữ liệu, thao tác và bằng chứng cho từng case.

**Cách chạy chung:**

1. Khởi động backend và frontend web; mở `http://localhost:5173/login` hoặc URL Vite thực tế.
2. Mở **F12 → Network**, bật **Preserve log** để xem request/response đăng nhập.
3. Chuẩn bị đúng bộ đếm và trạng thái khóa trước mỗi case. Mình đã tạo [helper đọc/thiết lập fixture](<D:/vscode/Software testing/HW02/FR-02/tools/auth_fixture.py>), lệnh sử dụng nằm trong hướng dẫn.
4. Chạy test, so Actual với Expected, lưu ảnh/log rồi mới ghi Pass/Fail.

| Case | Thao tác chính | Cần quan sát |
|---|---|---|
| TC01 | Đăng nhập đúng | Thành công, JWT được backend chấp nhận |
| TC02 | Từ n=0, sai một lần | n=1, chưa khóa |
| TC03 | Từ n=1, sai một lần | n=2, chưa khóa |
| TC04 | Từ n=2, sai một lần | n=3, kích hoạt khóa |
| TC05 | Đang khóa, thử đúng mật khẩu sau khoảng 10s | Vẫn bị từ chối |
| TC06 | Dùng email hợp định dạng nhưng không tồn tại | Bị từ chối, không cấp phiên |
| TC07 | Nhập email `abc` | HTML5 chặn submit; kiểm `type=email` và Network |
| TC08 | Tạo khóa mới, chờ khoảng 35s rồi đăng nhập đúng | Được đăng nhập |
| TC09 | Đăng nhập rồi xem Application → Local Storage | Client lưu đúng token |
| TC10 | Kích hoạt các luồng cần xác thực | Request client có header Bearer đúng token |
| TC11 | Đối chiếu lỗi từ TC02/05/06 | Thông báo phù hợp, không lộ chi tiết |

**Lưu ý:** backend hiện reset toàn bộ dữ liệu khi khởi động; sao lưu dữ liệu cần giữ và không restart giữa các case. Nếu TC02 không tạo đúng n=1, đừng tiếp tục rồi nhận TC03 đã đạt tiền điều kiện: ghi sai lệch, sau đó thiết lập fixture riêng nếu muốn kiểm tra cô lập.

Hiện mới có hướng dẫn; **chưa chạy 11 case trên eShop, chưa cập nhật kết quả**. Nên bắt đầu TC01, sau đó TC02.

Đã ghi audit