Đúng, nhưng cần phân biệt **một yêu cầu có nhiều EC** và **một test case bao phủ nhiều EC**.

- **Một yêu cầu** có thể chia thành nhiều EC: ví dụ trên có EC1–EC5.
- **Một test case hợp lệ** có thể bao phủ nhiều EC cùng lúc. Ví dụ `x = 5` bao phủ **EC1** (số nguyên) và **EC3** (`0 < x < 100`).
- **Với test case không hợp lệ**, theo cách chọn test trong slide, mỗi test chỉ nên vi phạm **một lớp không hợp lệ**, để xác định điều kiện nào gây lỗi.

Ví dụ:

| Test | Dữ liệu | EC được bao phủ |
|---|---|---|
| TC1 | `5` | EC1 + EC3 — hợp lệ |
| TC2 | `5.5` | EC2 — sai kiểu số nguyên, vẫn nằm trong khoảng |
| TC3 | `0` | EC1 + EC4 — đúng kiểu số nguyên, sai khoảng |
| TC4 | `100` | EC1 + EC5 — đúng kiểu số nguyên, sai khoảng |

Vậy **một test case có thể bao phủ nhiều EC**, nhưng các EC đó phải cùng phù hợp với dữ liệu của test.