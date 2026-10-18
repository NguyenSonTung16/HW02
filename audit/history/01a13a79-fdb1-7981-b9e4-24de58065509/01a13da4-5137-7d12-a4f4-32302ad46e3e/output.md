Mình đề xuất **một bộ gồm 3 skill chuyên biệt**, dùng chung biểu mẫu báo cáo. Mục tiêu là **hỗ trợ từng bước kiểm thử theo bài giảng, có điểm dừng để bạn rà soát**, đồng thời tạo tài liệu phục vụ HW02.

Đây là thiết kế đề xuất; đề không quy định phải có bao nhiêu skill.

**1. Skill phân tích miền và thiết kế test — `domain-testing`**

Skill này xử lý phần Domain Testing theo đúng trình tự trong slide:

- Đọc đặc tả chức năng; ghi nguồn yêu cầu.
- Xác định **đầu vào/đầu ra (Input/Output)** và các trạng thái liên quan.
- Tách **điều kiện (Conditions)**, đặt mã C1, C2…
- Chia **lớp tương đương (Equivalence Classes)** hợp lệ và không hợp lệ, đặt mã EC1, EC2…
- Chọn dữ liệu đại diện và tạo test case.
- Lập bảng ánh xạ **Requirement → Condition → EC → Test Case** để kiểm tra bao phủ.

**Quy tắc quan trọng:**

- Expected result phải dựa vào đặc tả.
- Không tự đặt thêm giới hạn hoặc hành vi chưa được quy định.
- Ghi riêng chỗ mơ hồ, câu hỏi và giả định.
- Test hợp lệ có thể bao phủ nhiều lớp; test không hợp lệ cô lập một điều kiện sai theo cách chọn test trong slide.
- Trình bày kết quả từng bước để bạn kiểm tra trước khi chuyển bước.

**Đầu ra:** phân tích yêu cầu, bảng điều kiện, bảng EC, bảng test case và bảng bao phủ.

**2. Skill phân tích giá trị biên — `boundary-value-analysis`**

Skill này nhận đặc tả và bảng phân tích miền đã được rà soát, rồi:

- Xác định các trường hoặc điều kiện có thứ tự và có biên.
- Xác định **biên dưới/biên trên (Lower/Upper Boundary)**, bao gồm biên đóng hoặc mở.
- Chọn giá trị tại biên, ngay bên trong và ngay bên ngoài.
- Chọn giá trị đại diện trong miền; xem xét giới hạn nhập của giao diện theo sơ đồ bài giảng.
- Với nhiều biến, giữ các biến còn lại ở giá trị hợp lệ khi kiểm tra một biên.
- Ánh xạ test biên về yêu cầu và EC; nhận diện test trùng.

**Quy tắc quan trọng:** không ép mọi trường thành mẫu 7 hoặc 9 giá trị. Chọn bước thay đổi phù hợp với kiểu dữ liệu; ghi rõ cách kiểm soát thời gian và trạng thái.

| Chức năng | Phần skill cần xử lý tốt |
|---|---|
| **FR-02** | Chuỗi đăng nhập sai, ngưỡng 3 lần và thời gian khóa 30 giây |
| **FR-09** | Ngưỡng tổng tiền, thời điểm hết hạn, số lượt sử dụng |
| **FR-15** | Độ dài tên tối đa 255 và giá lớn hơn 0 |

**Đầu ra:** bảng phân tích biên, test case BVA, expected result và yêu cầu chuẩn bị dữ liệu.

**3. Skill thực thi, bằng chứng và báo cáo — `test-execution-reporting`**

Skill này dùng bộ test đã được bạn duyệt để:

- Ghi môi trường, phiên bản source và cách chuẩn bị/reset dữ liệu.
- Hướng dẫn chạy hoặc chạy test khi có công cụ và phạm vi được cho phép.
- Ghi **Actual Result**, trạng thái **Pass/Fail/Not Run** và đường dẫn bằng chứng.
- Soạn bug report có bước tái hiện, expected/actual, ảnh và test liên quan.
- Tổng hợp số test đã thiết kế, đã chạy, pass, fail, chưa chạy và số bug.
- So sánh bản thiết kế AI ban đầu với bản bạn đã sửa để lập **AI gap analysis**.

**Quy tắc quan trọng:** chưa chạy thì ghi `Not Run`; đọc code thấy nghi vấn chưa được coi là bug đã xác nhận. Skill có thể chuẩn bị nội dung GitHub Issue; việc đăng issue cần nằm trong phạm vi bạn cho phép.

**Đầu ra:** bảng kết quả, bug report, test summary và nội dung cập nhật README.

**Cả 3 skill cần dùng chung các yêu cầu sau**

- **AI Audit:** lưu công cụ, thời gian thực tế, prompt, output; ghi thêm phần bạn rà soát/chỉnh sửa. Không dựng lại hội thoại hoặc thời gian không có bằng chứng.
- **Git:** hỗ trợ tạo commit sau từng bước, không đợi cuối bài mới tạo một commit.
- **Biểu mẫu Markdown:** thống nhất mã requirement, condition, EC, test case, bug và liên kết bằng chứng.
- **Human review:** phân biệt rõ “AI đề xuất” với “đã được sinh viên rà soát”.
- **AI Critique:** tổng hợp dẫn chứng thực tế để bạn viết đoạn 200–300 từ, tránh tự bịa nhận xét.
- **Demo:** lưu hướng dẫn tái hiện để quay video toàn bộ quy trình trên một chức năng.

**Nên xây và thử bộ skill trên FR-02 trước**, vì phạm vi gọn nhưng có cả dữ liệu, trạng thái và thời gian. Sau khi bạn rà soát quy trình, dùng lại trên FR-09 và FR-15 để chứng minh khả năng tái sử dụng.