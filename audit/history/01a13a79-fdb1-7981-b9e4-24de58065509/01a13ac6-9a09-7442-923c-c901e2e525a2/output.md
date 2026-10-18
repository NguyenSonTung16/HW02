**Giá trị biên (Boundary Value)** là giá trị nằm tại ranh giới giữa các miền đầu vào, chẳng hạn nơi đầu vào chuyển từ **không hợp lệ sang hợp lệ**.

Với yêu cầu **“số nguyên dương nhỏ hơn 100”**, các số hợp lệ là **1 đến 99**:

| Vị trí | Giá trị kiểm thử | Mong đợi |
|---|---|---|
| Ngay dưới biên dưới | `0` | Không hợp lệ |
| **Biên dưới (Lower Boundary)** | **`1`** | Hợp lệ |
| Ngay trên biên dưới | `2` | Hợp lệ |
| Ngay dưới biên trên | `98` | Hợp lệ |
| **Biên trên (Upper Boundary)** | **`99`** | Hợp lệ |
| Ngay trên biên trên | `100` | Không hợp lệ |

**Phân tích giá trị biên (Boundary Value Analysis — BVA)** chọn các giá trị **tại biên và sát hai bên biên** để kiểm thử.

Ví dụ, nếu chương trình viết nhầm `x <= 100` thay vì `x < 100`, thử `50` sẽ không phát hiện lỗi, nhưng thử **`100`** sẽ phát hiện được.