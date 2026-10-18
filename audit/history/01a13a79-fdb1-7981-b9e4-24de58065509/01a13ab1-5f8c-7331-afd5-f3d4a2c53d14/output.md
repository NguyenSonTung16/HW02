**C là điều kiện (Condition), còn EC là lớp tương đương (Equivalence Class).** Các số 1, 2, 3… là số thứ tự để đặt tên.

Trong ví dụ “nhập một số nguyên dương nhỏ hơn 100”:

| Điều kiện | Các lớp tương đương của điều kiện đó |
|---|---|
| **C1:** phải là số nguyên | **EC1:** là số nguyên → hợp lệ với C1, ví dụ `5`. **EC2:** không phải số nguyên → không hợp lệ, ví dụ `5.5`, `"abc"`. |
| **C2:** phải thuộc khoảng `0 < x < 100` | **EC3:** `0 < x < 100` → hợp lệ với C2. **EC4:** `x ≤ 0` → không hợp lệ. **EC5:** `x ≥ 100` → không hợp lệ. |

**Một đầu vào được chấp nhận khi thỏa cả C1 và C2**, tức là nằm trong **EC1 và EC3**:

- `5`: số nguyên, nằm giữa 0 và 100 → **hợp lệ**.
- `5.5`: nằm giữa 0 và 100 nhưng không phải số nguyên → **không hợp lệ**.
- `100`: là số nguyên nhưng không nhỏ hơn 100 → **không hợp lệ**.

Vì vậy, chữ “hợp lệ” ở **EC1** chỉ có nghĩa là **thỏa điều kiện C1**, chưa có nghĩa đầu vào đó thỏa toàn bộ yêu cầu.