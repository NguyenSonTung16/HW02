Vì **EC1 và EC2 đại diện cho hai nhóm đầu vào cần được xử lý khác nhau** đối với điều kiện C1 “phải là số nguyên”:

- **EC1 — Là số nguyên:** ví dụ `5`, `10`, `20`. Đạt điều kiện C1.
- **EC2 — Không phải số nguyên:** ví dụ `5.5`, `"abc"`. Không đạt C1, chương trình phải từ chối.

Chia như vậy giúp bạn **chọn dữ liệu kiểm thử có cơ sở**. Nếu chỉ thử `5`, `10`, `20`, bạn mới kiểm tra EC1 và có thể bỏ sót lỗi chương trình chấp nhận số thập phân.

Thay vì thử mọi giá trị, bạn chọn đại diện từ mỗi lớp, chẳng hạn:

| Dữ liệu | Lớp | Kết quả mong đợi |
|---|---|---|
| `5` | EC1: số nguyên | Chấp nhận vì cũng thỏa `0 < x < 100` |
| `5.5` | EC2: không phải số nguyên | Từ chối |

**Nếu các giá trị trong EC2 có thể được xử lý khác nhau**, chẳng hạn số thập phân và chuỗi chữ, bạn có thể chia EC2 thành các lớp nhỏ hơn để kiểm thử riêng.