Mình sẽ đối chiếu lại đề HW02 và checklist đã lưu để xác định bước tiếp theo cho ba chức năng đã chọn.


**Bước tiếp theo là bắt đầu phân tích đặc tả FR-02 — Đăng nhập và khóa tài khoản**, tương ứng mục **A-01** trong [checklist HW02](<D:/vscode/Software testing/HW02/HW02_Progress.md>). Nên làm từng chức năng theo thứ tự **FR-02 → FR-09 → FR-15**.

Với FR-02, làm lần lượt:

1. **Xác định đầu vào và đầu ra (Input/Output)**  
   Đầu vào gồm email, mật khẩu; khi phân tích còn phải xét trạng thái tài khoản, số lần sai liên tiếp và thời gian khóa. Đầu ra gồm kết quả đăng nhập, thông báo lỗi và JWT khi thành công.

2. **Tách các điều kiện (Conditions)** từ [đặc tả FR-02](<D:/vscode/Software testing/eshop-sut/README.md:38>)  
   Ví dụ: email đúng định dạng; thông tin đăng nhập đúng; bộ đếm tăng đúng 1; khóa từ lần sai thứ 3; thời gian khóa 30 giây.

3. **Chia lớp tương đương (Equivalence Classes — EC)** cho từng điều kiện  
   Ghi rõ lớp hợp lệ/không hợp lệ, dữ liệu đại diện và kết quả mong đợi. Những chỗ đặc tả chưa rõ phải ghi câu hỏi hoặc giả định riêng.

4. **Chọn test case từ các EC**, rồi bổ sung **giá trị biên (Boundary Values)**  
   Tập trung vào ngưỡng 3 lần sai và thời điểm hết khóa. Không cần ép email hoặc mật khẩu thành bài toán biên độ dài nếu FR-02 không quy định giới hạn đó.

5. **Rà soát thiết kế rồi mới chạy kiểm thử**, ghi kết quả thực tế, bằng chứng và bug.

Ngay từ bước đầu, cần **lưu prompt/output vào AI Audit** và **commit sau từng bước** để đáp ứng yêu cầu quá trình của HW02.

**Việc nên làm ngay lúc này: lập bảng phân tích FR-02 gồm “Yêu cầu → Input/Output → Điều kiện → Expected Result”, rồi mới chuyển sang bảng EC.** Chưa đánh dấu A-01 hoàn thành cho đến khi bảng đó được làm và rà soát.