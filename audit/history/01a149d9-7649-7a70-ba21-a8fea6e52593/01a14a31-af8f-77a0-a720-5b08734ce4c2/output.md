Đúng. **Bước 1 trong slide chỉ xác định chương trình/chức năng, đầu vào và đầu ra từ đặc tả.** Bảng 5 cột hiện tại là phần mình thêm, vượt quá mức trình bày bạn muốn bám theo.

Với FR-02, có thể viết ngắn bằng văn bản:

- **Chức năng:** Đăng nhập và khóa tài khoản.
- **Đầu vào:** Email, mật khẩu.
- **Đầu ra:** Kết quả đăng nhập, thông báo lỗi, JWT; bộ đếm và trạng thái khóa sau lần đăng nhập; token được client lưu và header xác thực.

Trạng thái trước request như số lần sai, tình trạng khóa và thời gian khóa có thể ghi một dòng **ngữ cảnh/tiền điều kiện**, để phục vụ phân lớp ở bước sau.

Nếu dùng bảng thì chỉ cần **Chức năng | Đầu vào | Đầu ra**. Không cần các cột ID, kiểu/đơn vị và ràng buộc ở bước này.