Mình sẽ đối chiếu danh sách tính năng trong README với yêu cầu HW02 để đề xuất phần phù hợp. Mình tạm hiểu A1/B1/C1 là các lựa chọn đầu tiên trong mỗi pool mà nhóm đã chọn.


Các chức năng có ngưỡng rõ như số lần đăng nhập sai, điều kiện coupon và giới hạn tên/giá sản phẩm phù hợp với cả hai kỹ thuật của HW02. Với mobile, hồ sơ cá nhân có biên số điện thoại 10–11 chữ số, nên đây cũng là lựa chọn đáng cân nhắc.


**Nếu FR-01, FR-07 và FR-12 đã được thành viên khác chọn, mình đề xuất bạn chọn: A–FR-02, B–FR-09, C–FR-15 và D–Hồ sơ cá nhân trên mobile.** Bộ này có nhiều điều kiện và ngưỡng rõ, phù hợp để làm cả Domain Testing lẫn Boundary Value Analysis.

Dựa trên [README eShop](<D:/vscode/Software testing/eshop-sut/README.md>):

| Pool | Nên chọn | Vì sao phù hợp với HW02 |
|---|---|---|
| **A** | **FR-02 — Đăng nhập & khóa tài khoản** | Có các miền tài khoản/mật khẩu đúng, sai, đang bị khóa. Có biên **3 lần sai** và thời gian khóa **30 giây**. |
| **B** | **FR-09 — Mã giảm giá** | Đặc tả rõ **5 điều kiện** áp dụng coupon. Có biên tổng tiền tối thiểu, hạn sử dụng và số lượt dùng. Đây là phần có nhiều dữ liệu để phân tích nhất. |
| **C** | **FR-15 — Quản lý sản phẩm** | Có biên tên **255 ký tự**, giá **> 0**, danh mục bắt buộc. Dễ thiết kế test, thao tác trên giao diện và chụp bằng chứng. |
| **D** | **FR-20 — Hồ sơ cá nhân trên mobile** | Có miền số điện thoại đúng/sai và biên độ dài **10–11 chữ số** theo FR-04; phạm vi tương đối gọn. |

Một số hướng test cụ thể:

- **A:** sai lần 2/3/4; đăng nhập ngay trước, tại và sau thời điểm hết khóa. Cần kiểm soát thời gian khi chạy.
- **B:** với `SAVE10`, thử tổng tiền **299.999 / 300.000 / 300.001 ₫**; số lượt dùng ngay dưới/tại giới hạn; trước/tại/sau thời điểm hết hạn.
- **C:** tên **254 / 255 / 256 ký tự**; giá âm, 0, dương; danh mục hợp lệ, thiếu hoặc không tồn tại.
- **D:** số điện thoại **9 / 10 / 11 / 12 chữ số**, bắt đầu bằng `0` hoặc khác `0`, chứa ký tự không phải số.

**Mobile hồ sơ còn có một điểm đáng kiểm tra:** [source hiện tại](<D:/vscode/Software testing/eshop-sut/frontend-mobile/App.js:287>) kiểm tra số điện thoại **9–10 chữ số, bắt đầu bằng 1–9**, khác yêu cầu README là **10–11 chữ số, bắt đầu bằng 0**. Đây là dấu hiệu sai lệch từ việc đọc code; cần chạy app để xác nhận và lấy bằng chứng.

Với **Pool D**, hãy đăng ký lựa chọn này sau khi thầy xác nhận được chọn một chức năng con trong FR-20. Bộ đề xuất cũng cần đối chiếu với các lựa chọn còn lại của nhóm để tránh trùng.