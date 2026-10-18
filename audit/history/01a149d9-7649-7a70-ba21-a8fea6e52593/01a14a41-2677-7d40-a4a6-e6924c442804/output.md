**Đúng về trình tự minh họa trong slide**, nhưng không có nghĩa mỗi EC phải tạo một TC riêng biệt rồi chạy tất cả.

1. **Bảng bao phủ phân vùng:** với từng EC, chọn dữ liệu và expected output để chứng minh EC đó có test kiểm tra. Các dòng có thể trùng dữ liệu.
2. **Bảng TC tối thiểu:** gộp những dòng dùng cùng dữ liệu và expected output, ghi rõ các EC được bao phủ.

Trong ví dụ:

- EC1, EC5, EC9 cùng dùng **A = 10, B = 9 → 19** ⇒ gộp thành **TC1**.
- EC2 và EC10 cùng dùng **A = −102, B = 9 → lỗi** ⇒ gộp thành **TC2**.

**Lưu ý:** “bao quát nhiều EC nhất” áp dụng khi kết hợp phù hợp. Với đầu vào không hợp lệ, mỗi test vẫn chỉ vi phạm **một lớp đầu vào không hợp lệ**, tránh lỗi này che lỗi khác.

Nếu muốn báo cáo FR-02 bám đúng cách trình bày hai slide này, mục 2.4 nên có **bảng chọn đại diện cho từng EC**, sau đó là **bảng TC tối thiểu**. Trước đó mình mới giữ bảng TC cuối, nên chưa thể hiện rõ bước trung gian này.