Mình sẽ đối chiếu lại các bước trong slide và yêu cầu HW02, rồi mô tả rõ đầu vào, cách xử lý, đầu ra và điểm bạn cần rà soát của từng skill. Đây vẫn là bản thiết kế để bạn kiểm tra, chưa tạo skill.


Mình đề xuất giữ **3 skill**, nhưng quy định rõ trách nhiệm để bạn dễ kiểm tra. Hai skill đầu thiết kế kiểm thử; skill thứ ba thực thi và tổng hợp kết quả. **AI Audit và lịch sử rà soát phải được ghi xuyên suốt cả ba skill.**

Thiết kế dựa trên các bước trong slide, đặc biệt trang 3, 21 và 26. Trang 21 yêu cầu:
> “Choose at least one test case from each equivalence class”

:codex-file-citation{path="C:/Users/tung1/Downloads/S04_Domain Testing.pdf" purpose="source"}

Tên file dưới đây là đề xuất tổ chức, không phải tên bắt buộc của HW02.

### 1. `domain-testing` — Phân tích miền và thiết kế test

**Mục tiêu:** chuyển đặc tả thành điều kiện, lớp tương đương và test case có giải thích cách lựa chọn.

**Đầu vào cần có:**

- Đặc tả chức năng, ví dụ FR-02 trong README.
- Tài liệu phương pháp: slide S04.
- Phạm vi kiểm thử: chức năng nào, trên web/mobile/API.
- Các quyết định hoặc chỉnh sửa bạn đã xác nhận trước đó.

**Quy trình skill thực hiện:**

| Bước | Skill phải làm | Bạn cần kiểm tra |
|---|---|---|
| 1. Đọc yêu cầu | Trích yêu cầu, ghi nguồn, đặt mã yêu cầu | Có bỏ sót hoặc hiểu sai đặc tả không? |
| 2. Xác định Input/Output | Liệt kê dữ liệu nhập, đầu ra và trạng thái ảnh hưởng | Có nhầm trạng thái hệ thống thành trường người dùng nhập không? |
| 3. Tách điều kiện | Đặt mã C1, C2…; ghi điều kiện và hành vi mong đợi | Điều kiện có căn cứ trong đặc tả không? |
| 4. Chia lớp tương đương | Đặt mã EC; phân biệt hợp lệ/không hợp lệ; ghi lý do chia | Các lớp có thiếu, chồng lấn hoặc cần chia nhỏ không? |
| 5. Chọn đại diện | Chọn dữ liệu đại diện cho từng EC | Dữ liệu có thật sự thuộc lớp đó không? |
| 6. Thiết kế test | Tạo tiền điều kiện, bước chạy và expected result | Test có cô lập đúng điều kiện cần kiểm tra không? |
| 7. Kiểm tra bao phủ | Ánh xạ yêu cầu → điều kiện → EC → test | Còn yêu cầu hoặc EC nào chưa có test không? |

**Ví dụ với FR-02:**

Skill phải phân biệt:

- **Dữ liệu nhập:** email, mật khẩu.
- **Trạng thái liên quan:** số lần sai liên tiếp, tài khoản đang khóa hay không.
- **Đầu ra:** đăng nhập thành công/thất bại, thông báo, JWT, thay đổi trạng thái khóa.

Không chỉ chia email đúng/sai rồi coi như đã bao phủ toàn bộ FR-02.

**Quy tắc bắt buộc của skill:**

- Expected result lấy từ đặc tả; hành vi source chỉ là đối tượng đem kiểm tra.
- Chỗ chưa rõ được đưa vào danh sách câu hỏi/giả định, không tự biến thành yêu cầu.
- Test hợp lệ có thể bao phủ nhiều EC.
- Theo cách chọn test trong slide, test không hợp lệ cô lập một lớp đầu vào không hợp lệ, giữ các điều kiện khác hợp lệ.
- Lưu bản đề xuất ban đầu và phần bạn chỉnh sửa để có bằng chứng human review.

**Đầu ra đề xuất:**

- `Requirements_Analysis.md`
- `Domain_Testing.md`: các bước phân tích, bảng điều kiện, bảng EC, dữ liệu đại diện.
- `Test_Cases.md`: các test Domain Testing.
- Bảng bao phủ và danh sách điểm chưa rõ.

**Hoàn tất khi:** các yêu cầu/EC đều có test hoặc lý do chưa bao phủ; bạn đã rà soát phần phân tích.

### 2. `boundary-value-analysis` — Phân tích và thiết kế test biên

**Mục tiêu:** tìm các ranh giới có ý nghĩa và thiết kế test tại, sát trong, sát ngoài biên.

**Đầu vào cần có:**

- Đặc tả gốc.
- Bảng điều kiện và EC từ skill thứ nhất.
- Các giả định đã được xác nhận.
- Kiểu dữ liệu, độ chính xác và giới hạn giao diện nếu đã biết.

Skill này **có thể dùng riêng** nếu được cung cấp đầy đủ đầu vào, không bắt buộc luôn chạy skill thứ nhất.

**Quy trình skill thực hiện:**

1. **Xác định yếu tố có biên:** độ dài, số lượng, tiền, thời gian, số lần sử dụng…
2. **Mô tả miền hợp lệ:** kiểu dữ liệu, bất đẳng thức, biên đóng/mở, giới hạn một phía/hai phía.
3. **Xác định bước thay đổi:** số nguyên dùng bước 1; tiền và thời gian dùng độ chính xác phù hợp, có căn cứ.
4. **Chọn giá trị biên:** tại biên, ngay bên trong, ngay bên ngoài; thêm giá trị đại diện bên trong miền.
5. **Xem xét giới hạn giao diện:** giá trị nhỏ nhất/lớn nhất nhập được theo sơ đồ trang 26, nếu xác định được.
6. **Tạo test:** giữ các biến khác hợp lệ; ghi expected result và cách chuẩn bị/reset.
7. **Đối chiếu với test Domain Testing:** dùng lại test trùng, gắn cả hai kỹ thuật để tránh đếm hai lần.

**Áp dụng cho ba chức năng:**

| Chức năng | Skill cần xử lý |
|---|---|
| **FR-02** | Số lần đăng nhập sai và thời điểm hết khóa; phải mô tả chuỗi thao tác, không chỉ một con số |
| **FR-09** | Tổng tiền tối thiểu, hạn dùng, số lượt sử dụng; phân biệt “trước hạn” với “bằng hạn” |
| **FR-15** | Độ dài tên tối đa 255, giá > 0; không tự đặt giá tối đa |

**Quy tắc bắt buộc của skill:**

- Không ép mọi phân vùng thành đúng 7 hoặc 9 test.
- Với biên thời gian, ghi rõ mốc bắt đầu, cách đo và độ chính xác.
- Không mặc định `±1` luôn là bước thích hợp.
- Phân biệt giới hạn nghiệp vụ với giới hạn nhập liệu của giao diện.
- Các trường chỉ có nhóm phân loại, không có thứ tự, phải giải thích nếu không áp dụng BVA.

**Đầu ra đề xuất:**

- `Boundary_Value_Analysis.md`: bảng biên, bước thay đổi, dữ liệu và giải thích.
- Bổ sung test BVA vào `Test_Cases.md`.
- Bảng bao phủ biên, điểm chưa rõ và yêu cầu dữ liệu.

**Hoàn tất khi:** mỗi biên đã có test hoặc lý do loại trừ; dữ liệu, expected result và cách tái hiện đủ rõ để chạy.

### 3. `test-execution-reporting` — Chạy test, quản lý bằng chứng và báo cáo

**Mục tiêu:** biến bộ test đã thiết kế thành kết quả kiểm thử có thể kiểm chứng và hồ sơ nộp bài.

**Đầu vào cần có:**

- Bộ test đã được rà soát.
- Môi trường chạy, phiên bản source và dữ liệu test.
- Phạm vi thao tác được phép.
- Công cụ thực thi sẵn có.

**Quy trình skill thực hiện:**

1. **Ghi môi trường:** source commit, hệ điều hành, trình duyệt, URL, cấu hình liên quan.
2. **Chuẩn bị dữ liệu:** tài khoản, sản phẩm, coupon; cách reset giữa các test.
3. **Thực thi:** chạy bằng công cụ phù hợp hoặc hướng dẫn bạn chạy nếu chưa có công cụ.
4. **Ghi kết quả:** actual result, thời gian, trạng thái, bằng chứng.
5. **Xác nhận sai lệch:** đối chiếu expected/actual, kiểm tra lại điều kiện và dữ liệu trước khi kết luận bug.
6. **Lập bug report:** bước tái hiện, expected/actual, ảnh, test liên quan và nguồn yêu cầu.
7. **Theo dõi GitHub Issues:** chuẩn bị nội dung và đăng khi bạn đã cho phép; lưu link và bảo đảm issue có ảnh.
8. **Tổng kết:** số test thiết kế/đã chạy/pass/fail/chưa chạy, số bug và phần chưa được kiểm tra.
9. **Chuẩn bị báo cáo:** tổng hợp nội dung hai skill đầu, kết quả chạy, AI gap analysis và README.

**Quy tắc bắt buộc của skill:**

- Chưa chạy thì không ghi Pass.
- Đọc code thấy nghi vấn thì ghi nghi vấn, chưa kết luận bug đã xác nhận.
- Không có bằng chứng thì không tự tạo screenshot, log hoặc kết quả.
- Giữ lịch sử các lần chạy; một bug có thể liên quan nhiều test.
- Khi không chạy được, ghi nguyên nhân; không che phần chưa kiểm thử.

**Đầu ra đề xuất:**

- `Test_Execution.md`
- `Bug_Report.md`
- `evidence/`
- `Test_Summary.md`
- `Main_Report.md` và bản PDF.
- Nội dung test summary, link issue và video trong `README.md`.

**Hoàn tất khi:** kết quả và số liệu khớp nhau, mọi bug xác nhận có hồ sơ và bằng chứng, phần chưa chạy được ghi rõ.

### Phần dùng chung cho cả ba skill

| Nội dung | Cách giải quyết |
|---|---|
| **AI Audit** | Ghi công cụ, ngày giờ thực tế, prompt và output từng tương tác; nếu không truy xuất đủ lịch sử thì ghi phần thiếu |
| **Human review** | Lưu ý kiến của bạn, nội dung đã sửa và trạng thái đã/chưa rà soát; không tự ghi bạn đã duyệt |
| **Git** | Tạo commit theo từng bước trong quá trình làm, không dựng lại lịch sử cuối bài |
| **AI gap analysis** | Giữ bản AI ban đầu để so sánh với bản sau rà soát; phân biệt thiếu sót thực tế với suy đoán |
| **AI Critique** | Tổng hợp dẫn chứng để soạn đoạn 200–300 từ cho bạn rà soát |
| **Tiến độ HW02** | Chỉ tích hoàn thành trong checklist khi bạn yêu cầu, theo quy ước đã chốt |
| **Video demo** | Có kịch bản cho thấy đầu vào, từng bước dùng skill, phần bạn rà soát, kết quả và tài liệu đầu ra |

**Cách dùng đề xuất:** chạy từng bước trên **FR-02**, bạn kiểm tra kết quả mỗi bước; sau đó thử lại với **FR-09 và FR-15** để đánh giá skill có tái sử dụng được hay đang viết riêng cho một chức năng. Các bước độc lập vẫn có thể tiếp tục khi còn một điểm chưa rõ; chỉ phần phụ thuộc vào điểm đó mới cần chờ xác nhận.