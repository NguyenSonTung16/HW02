**Có. Ảnh là bảng TC ở mục 2.5; bạn có thể gộp mục 2.4 và 2.5** thành **“Chọn đại diện và xây dựng test case”**.

Đoạn giải thích trước bảng chỉ cần:

> Chọn dữ liệu đại diện cho từng EC. Kết hợp các EC hợp lệ trong cùng test khi phù hợp; mỗi test âm chỉ vi phạm một điều kiện đầu vào, giữ các điều kiện khác hợp lệ.

Để dành chỗ cho cột **“EC bao phủ”**:

- Chuyển **Tester** và **Tested Date** sang hồ sơ thực thi nếu không cần giữ mẫu bảng của giảng viên.
- Giữ **Remark** cho ghi chú cần thiết; bỏ các câu nhắc quy trình lặp lại.
- Rút tên cột: “Test case name” → “Tên test”, “Expected Result” → “Expected”, “Actual Result” → “Actual”.

Bảng sẽ gồm:

```text
ID | Tên test | EC bao phủ | Tiền điều kiện | Bước thực hiện
   | Expected | Actual | Status | Remark
```

**Nếu phải giữ nguyên mẫu 10 cột của giảng viên**, nên ghi `EC bao phủ: …` trong **Remark**, không tự bỏ hoặc thay cột. Khi đã thể hiện EC tại bảng TC, có thể bỏ cột “Test bao phủ” ở mục 2.3.