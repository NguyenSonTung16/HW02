**Đúng. Nếu xét riêng ngưỡng khóa ở lần sai thứ 3**, ba điểm cần kiểm tra là:

- **Lần 2:** ngay dưới ngưỡng → chưa khóa.
- **Lần 3:** tại ngưỡng → kích hoạt khóa.
- **Lần gửi thứ 4, khi khóa còn hiệu lực:** sau ngưỡng → tiếp tục bị từ chối.

**Lần sai thứ 1 là test bổ sung về trạng thái ban đầu và tăng bộ đếm**, không phải điểm sát ngưỡng 3. Mình đưa vào phần BVA khiến phạm vi rộng hơn cần thiết. Bạn có thể **bỏ TC02 khỏi bảng 2.5**, giữ nó ở Domain Testing.

Lưu ý: lần gửi thứ 4 không có nghĩa bộ đếm chắc chắn tăng thành 4, vì yêu cầu có thể bị chặn ngay khi tài khoản đang khóa.

Đã ghi audit