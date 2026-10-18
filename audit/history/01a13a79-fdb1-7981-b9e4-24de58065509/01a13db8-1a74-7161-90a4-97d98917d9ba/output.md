Đúng, mình bổ sung vào thiết kế **skill 1 — `domain-testing`** như sau:

- **Bước 2:** liệt kê từng **Input** và **Output**, đặt mã riêng.
- **Bước 4:** xác định **EC cho từng Input và từng Output**; mỗi EC ghi biến liên quan, mô tả lớp, điều kiện xuất hiện và giá trị/kết quả đại diện.
- **Bước 6:** mỗi test case ghi rõ **EC đầu vào được sử dụng** và **EC đầu ra mong đợi**.
- **Bước 7:** bảng bao phủ phải có **cả EC đầu vào và EC đầu ra**, không chỉ kiểm tra miền dữ liệu nhập.

Ví dụ cấu trúc bảng bao phủ:

| EC | Loại | Input/Output liên quan | Mô tả | Test case bao phủ |
|---|---|---|---|---|
| EC-I01 | Input | Mật khẩu | Đúng với tài khoản | TC01 |
| EC-I02 | Input | Mật khẩu | Sai với tài khoản | TC02 |
| EC-O01 | Output | Kết quả đăng nhập | Thành công, trả JWT | TC01 |
| EC-O02 | Output | Kết quả đăng nhập | Thất bại, thông báo lỗi | TC02 |

**Tiêu chí hoàn tất được sửa thành:** mọi Input/Output đã được xét để xác định EC; mỗi EC đầu vào và đầu ra đều có test bao phủ hoặc lý do chưa bao phủ. Với EC đầu ra, “bao phủ” ở giai đoạn thiết kế nghĩa là **có test dự kiến tạo ra và kiểm tra kết quả đó**; khi chạy mới xác nhận kết quả thực tế.