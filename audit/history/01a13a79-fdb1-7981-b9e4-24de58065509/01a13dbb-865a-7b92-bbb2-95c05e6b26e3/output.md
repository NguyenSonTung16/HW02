Mình bổ sung vào **bước 4 — Xác định EC cho từng Input/Output** của skill 1:

| Dạng điều kiện | Quy tắc chia EC |
|---|---|
| **Khoảng hai phía (Two-sided Range)** | Xét **một lớp trong khoảng** và **hai lớp ngoài khoảng**: dưới giới hạn dưới, trên giới hạn trên. Xác định rõ dấu `<` hay `≤`. |
| **Điều kiện bắt buộc (Must-be Condition)** | Xét **lớp thỏa điều kiện** và **lớp không thỏa điều kiện**. |
| **Các nhóm được xử lý khác nhau** | Tách **EC riêng cho từng nhóm có cách xử lý khác nhau**; xét thêm nhóm giá trị không được phép nếu có. |
| **Các phần tử trong một EC có hành vi khác nhau** | **Chia nhỏ EC** cho đến khi các phần tử trong mỗi lớp có thể được xem là xử lý tương đương. |

Ví dụ:

- `1 ≤ x ≤ 99` → `x < 1`, `1 ≤ x ≤ 99`, `x > 99`.
- Ký tự đầu phải là chữ cái → **là chữ cái / không phải chữ cái**.
- Coupon `percent` và `fixed` có công thức khác nhau → **hai EC riêng**.
- “Không phải số nguyên” có thể gồm số thập phân và chuỗi chữ; nếu chúng được xử lý khác nhau thì **tách thành các EC nhỏ hơn**.

Skill phải **ghi lý do chia lớp**, không chỉ liệt kê EC; các quy tắc được áp dụng phù hợp cho cả **đầu vào và đầu ra**.