**Có. Viết test case xong thì cần chạy các test đó trên eShop thực tế.** Hiện 11 test FR-02 mới là bản thiết kế, đều đang `Not Run`.

Quy trình tiếp theo:

1. **Rà soát test case:** dữ liệu, EC, bước chạy và expected result có đúng đặc tả không.
2. **Chuẩn bị môi trường và dữ liệu:** tài khoản, trạng thái khóa, bộ đếm… đúng tiền điều kiện.
3. **Chạy từng test:** ghi **Actual Result**, so với **Expected Result** để đánh dấu **Pass/Fail**, lưu ảnh hoặc log bằng chứng.
4. **Nếu phát hiện bug:** ghi báo cáo và đăng GitHub Issue kèm ảnh.

Nếu bạn nói **“test lại sau khi đã chạy một lần”**, thì chỉ cần khi có lý do: lần chạy chưa đáng tin cậy, test được sửa, hoặc phần mềm đã sửa bug. Khi bug được sửa, chạy lại test liên quan để xác nhận lỗi đã hết (**Confirmation Testing/Retesting**).

Với FR-02 hiện tại, bước trước mắt là **bạn rà soát bản thiết kế**, bổ sung BVA rồi mới chạy bộ test.