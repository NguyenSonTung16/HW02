**Không. Slide không bắt buộc đặt mã `EC-I`, `EC-S`, `EC-O`.** Đây là quy ước mình thêm để phân biệt Input, State và Output; trước đó mình chưa làm rõ điều này.

S04 trang 7 dùng mã đơn giản **EC1, EC2, …**, kèm cột **Input/Output** và nội dung lớp tương đương. Bạn có thể dùng:

| EC ID | Biến | Miền/điều kiện của lớp |
|---|---|---|
| EC1 | Email | Hợp định dạng, tài khoản tồn tại |
| EC2 | Email | Hợp định dạng, tài khoản không tồn tại |
| … | … | … |
| EC7 | Số lần sai trước request | n = 0 |

**Trạng thái khóa và số lần sai vẫn cần được xét** vì ảnh hưởng hành vi FR-02, nhưng không bắt buộc tách thành nhóm mã `EC-S`.

Nếu đổi sang EC1, EC2… thì cần cập nhật đồng bộ các mã trong bảng TC.