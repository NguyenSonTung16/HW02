# Báo cáo HW02 Domain Testing trên EShop

Cập nhật 16/10/2026. Phạm vi đã chọn: A FR-02, B FR-09, C FR-15; Pool D chờ chốt. Hiện có thiết kế Domain Testing của FR-02 và kết quả TC01 Pass; BVA chưa thực hiện, nên chưa hoàn thành hai yêu cầu kỹ thuật của HW02. Nội dung AI còn chờ sinh viên rà soát đầy đủ.

## 1 Phạm vi phương pháp và môi trường

Nguồn nghiệp vụ: README eShop FR-02. Phương pháp: slide S04 trang 3, 8–11, 21 (Input/Output, EC, đại diện/test); trang 24–27 cho BVA bước sau. Đề HW02 mục 6 yêu cầu giải thích từng bước áp dụng cả hai kỹ thuật. Báo cáo giữ phân tích riêng, bảng test chỉ dùng 10 trường của mẫu giảng viên cung cấp.

Người thực thi kết quả đã ghi: Nguyễn Sơn Tùng. MSSV 23120399 theo mẫu người dùng cung cấp; lớp/nhóm chờ xác nhận. Backend http://localhost:3000, web http://localhost:5173; Node v24.11.1 lúc khởi động. Kiểm bằng browser và PowerShell. Phiên bản browser, source commit SUT và giờ chạy cụ thể cần bổ sung.

## 2 Pool A FR02 Đăng nhập và khóa tài khoản

### 2.1 Yêu cầu làm cơ sở kiểm thử

- Nhập email và mật khẩu; thông tin đúng được đăng nhập khi tài khoản không khóa.
- Mỗi lần đăng nhập sai tăng bộ đếm đúng 1; sai từ 3 lần liên tiếp khóa 30 giây.
- Lỗi phải có thông báo phù hợp, không lộ chi tiết nguyên nhân.
- Thành công trả JWT; client lưu và đính kèm Authorization Bearer trên mọi request cần xác thực.
- Input email có type=email và validation HTML5.

### 2.2 Domain Testing Bước 1 Xác định Input và Output

Đọc từng yêu cầu để liệt kê dữ liệu người dùng nhập và kết quả cần quan sát. Bộ đếm, khóa và đồng hồ là trạng thái/ngữ cảnh, không phải trường nhập. Bộ đếm trước request và đầu ra sau request được tách để kiểm quy tắc tăng đúng 1.

| ID | Loại | Biến | Kiểu/đơn vị | Ràng buộc/nguồn |
| --- | --- | --- | --- | --- |
| FR02-I1 | Input | Email | Chuỗi | Định dạng HTML5, liên hệ tài khoản R1/R7 |
| FR02-I2 | Input | Mật khẩu | Chuỗi | So với thông tin tài khoản R1; không tự đặt min/max |
| FR02-S1 | State | Số lần sai liên tiếp trước request n | Số nguyên không âm | Ngưỡng 3, tăng 1 theo R2/R3 |
| FR02-S2 | State | Trạng thái khóa | Chưa khóa/đang khóa/đã hết thời gian khóa | R3 |
| FR02-S3 | State | Thời gian từ lúc bắt đầu khóa | Thời gian | 30 giây, độ chính xác chưa xác nhận |
| FR02-O1 | Output | Kết quả đăng nhập | Thành công/từ chối/chặn ở UI | R1/R3/R7 |
| FR02-O2 | Output | Thông báo lỗi | Nội dung hiển thị/response | R4; không quy định văn bản chính xác |
| FR02-O3 | Output | JWT trả về | Token hoặc không cấp phiên hợp lệ | R5; không suy ra cấu trúc JSON |
| FR02-O4 | Output | Bộ đếm sau request | Số nguyên/chênh lệch | R2; cần cách quan sát không sửa logic |
| FR02-O5 | Output | Trạng thái khóa sau request | Khóa/chưa khóa | R3 |
| FR02-O6 | Output | Token được client lưu | Quan sát trạng thái client | R6; không ép localStorage hay cookie |
| FR02-O7 | Output | Header request có xác thực | Authorization | R6; không áp cho mọi request công khai |

### 2.3 Domain Testing Bước 2 Xác định điều kiện và EC

Tách điều kiện từ đặc tả, sau đó chia EC cho từng Input/Output và trạng thái liên quan. Mã C/I/O/S dùng prefix FR02. Một giá trị hợp lệ theo một điều kiện chưa chắc hợp lệ toàn bộ.

| ID | Requirement | Input/Output/State | Điều kiện và hành vi |
| --- | --- | --- | --- |
| FR02-C1 | R7 | I1/O1 | Email hợp định dạng HTML5; sai định dạng bị validation UI |
| FR02-C2 | R1 | I1/I2/O1/O3 | Tài khoản tồn tại và đúng mật khẩu là thông tin xác thực hợp lệ |
| FR02-C3 | R3 | S2/S3/O1/O3 | Đang khóa phải không tạo phiên thành công, kể cả mật khẩu đúng |
| FR02-C4 | R2 | S1/O4 | Đăng nhập sai trên tài khoản tồn tại, chưa khóa: n_after = n_before + 1 |
| FR02-C5 | R3 | S1/O5 | Lần sai làm số đếm đạt 3 phải kích hoạt khóa 30 giây |
| FR02-C6 | R4 | O2 | Lỗi phù hợp, không lộ chi tiết; tiêu chí chi tiết cần xác nhận |
| FR02-C7 | R5 | O3 | Thành công trả JWT xác thực được |
| FR02-C8 | R6 | O6/O7 | Client lưu token và gửi đúng Bearer trên request cần xác thực |

Áp dụng các quy tắc của S04: điều kiện bắt buộc chia thỏa/không thỏa; nhóm có hành vi khác nhau tách riêng; khoảng hai phía xét trong và hai phía ngoài khi đặc tả có khoảng đó. FR-02 không có giới hạn độ dài email/mật khẩu để tự dựng biên. Email hợp định dạng tách tồn tại/không tồn tại. n=1 và n=2 tách vì sau một lần sai dẫn đến chưa khóa hoặc chạm ngưỡng khóa. Output lỗi là đầu ra đúng của test âm, không tự xem là bug.

Bảng sau gộp định nghĩa EC với bao phủ thiết kế để không lặp bảng. Có 6 EC Input, 6 EC State và 14 EC Output. TC-ID cùng prefix FR02. Có test dự kiến không đồng nghĩa đã quan sát output khi thực thi.

| EC | Biến và điều kiện | Miền hoặc kết quả đại diện | Lý do phân lớp | Test bao phủ |
| --- | --- | --- | --- | --- |
| EC-I01 | I1/C1,C2 | Email hợp định dạng, tài khoản tồn tại: test@eshop.com | Hợp lệ; fixture cần xác nhận | TC01–05,TC07–11 |
| EC-I02 | I1/C1,C2 | Email hợp định dạng, không có tài khoản: hw02-absent@example.com | Sai xác thực; xác nhận không tồn tại trước chạy | TC06,TC11 |
| EC-I03 | I1/C1 | Email không rỗng, sai HTML5: abc | Sai định dạng; tách khỏi email không tồn tại | TC07 |
| EC-I04 | I2/C2 | Mật khẩu đúng cho tài khoản đã có: Test1234! | Hợp lệ với fixture mặc định nếu chưa bị đổi | TC01,TC05,TC08,TC09,TC10 |
| EC-I05 | I2/C2 | Mật khẩu sai cho tài khoản đã có: WrongPass9! | Sai xác thực; xác nhận không trùng mật khẩu thật | TC02–04,TC11 |
| EC-I06 | I2/C2 | Email không tồn tại, mật khẩu chuỗi bất kỳ: Test1234! | Không áp khái niệm đúng/sai mật khẩu tài khoản; không tính là lỗi độc lập thứ hai | TC06,TC11 |
| EC-S01 | S1/C4,C5 | n=0 trước request | Chưa có lần sai; đầu chuỗi | TC01,TC02 |
| EC-S02 | S1/C4,C5 | n=1 trước request sai | Sau +1 vẫn dưới ngưỡng | TC03 |
| EC-S03 | S1/C4,C5 | n=2 trước request sai | Sau +1 chạm ngưỡng khóa; chia từ nhóm 1..2 vì hành vi khác | TC04 |
| EC-S04 | S2,S3/C3 | Chưa khóa | Cho phép xét xác thực | TC01–04 |
| EC-S05 | S2,S3/C3 | Khóa còn hiệu lực, ví dụ 10 giây sau khi bắt đầu khóa | Không được đăng nhập dù cặp đúng | TC05 |
| EC-S06 | S2,S3/C3 | Đã qua thời hạn khóa, ví dụ 35 giây sau mốc được xác nhận | Khóa tạm thời phải hết; không assert reset bộ đếm | TC08 |
| EC-O01 | O1/C2,C3 | Đăng nhập thành công với cặp đúng, chưa khóa | Phân biệt theo hành vi đầu ra mong đợi | TC01,TC08–10 |
| EC-O02 | O1/C2 | Request sai thông tin bị từ chối | Phân biệt theo hành vi đầu ra mong đợi | TC02–04,TC06 |
| EC-O03 | O1/C1 | UI chặn submit email sai định dạng HTML5 | Phân biệt theo hành vi đầu ra mong đợi | TC07 |
| EC-O04 | O1/C3 | Request khi đang khóa bị từ chối | Phân biệt theo hành vi đầu ra mong đợi | TC05 |
| EC-O05 | O2/C6 | Thông báo lỗi xác thực phù hợp; oracle chi tiết còn Q4 | Phân biệt theo hành vi đầu ra mong đợi | TC02,TC06,TC11 |
| EC-O06 | O2/C6 | Thông báo cho tình huống khóa phù hợp; oracle chi tiết còn Q4 | Phân biệt theo hành vi đầu ra mong đợi | TC05,TC11 |
| EC-O07 | O3/C7 | Có JWT xác thực được khi thành công | Phân biệt theo hành vi đầu ra mong đợi | TC01 |
| EC-O08 | O3/C2,C3 | Không cấp phiên/JWT có thể dùng để vượt xác thực khi bị từ chối; không ép response thiếu field cụ thể | Phân biệt theo hành vi đầu ra mong đợi | TC02,TC05,TC06 |
| EC-O09 | O4/C4 | n_after=n_before+1 khi sai, tài khoản tồn tại chưa khóa | Phân biệt theo hành vi đầu ra mong đợi | TC02–04 |
| EC-O10 | O5/C5 | Sau lần sai thứ 1/2 chưa kích hoạt khóa | Phân biệt theo hành vi đầu ra mong đợi | TC02,TC03 |
| EC-O11 | O5/C5 | Lần sai thứ 3 kích hoạt khóa tạm 30 giây | Phân biệt theo hành vi đầu ra mong đợi | TC04 |
| EC-O12 | O5/C3 | Khóa đã hết sau thời hạn, thể hiện bằng đăng nhập đúng thành công | Phân biệt theo hành vi đầu ra mong đợi | TC08 |
| EC-O13 | O6/C8 | Token được client lưu; cơ chế lưu chưa cố định | Phân biệt theo hành vi đầu ra mong đợi | TC09 |
| EC-O14 | O7/C8 | Request có xác thực mang Authorization: Bearer <token> đúng token | Phân biệt theo hành vi đầu ra mong đợi | TC10 |

### 2.4 Domain Testing Bước 3 Chọn đại diện và lập test

Chọn dữ liệu đại diện cho từng EC: email tài khoản demo, email không tồn tại, abc, mật khẩu đúng/sai; thiết lập trạng thái n=0/1/2 và khóa còn/hết hiệu lực. Ghép nhiều EC hợp lệ trong một test khi khả thi. Với test âm, cô lập một lớp đầu vào không hợp lệ, giữ điều kiện khác hợp lệ; output lỗi đi kèm không phải vi phạm đầu vào thứ hai. Trạng thái khóa là tiền điều kiện của test quyền đăng nhập.

Ví dụ TC01 kết hợp email tồn tại, mật khẩu đúng, chưa khóa để kiểm output thành công/JWT. TC02 giữ email đúng và chỉ đổi mật khẩu để kiểm từ chối và tăng đếm. TC07 chỉ sai định dạng email, dùng submit UI để kiểm HTML5. TC03/04 phải phân biệt chuỗi thực và fixture thiết lập trực tiếp. TC11 là đánh giá output bổ sung dựa trên những tình huống đã chạy.

Phạm vi chưa rõ: reset đếm sau thành công/hết khóa; tác động request khi đang khóa; email/mật khẩu thiếu/rỗng và kiểu API; tiêu chí thông báo lỗi; độ chính xác mốc khóa; danh mục request cần xác thực. Chưa đủ oracle thì ghi câu hỏi, không tự tạo expected. Chi tiết Q1–Q7 tại tài liệu phân tích thành phần.

### 2.5 Bảng test case Domain Testing

A = test@eshop.com / Test1234!; W = WrongPass9!; U = hw02-absent@example.com (kiểm không tồn tại trước chạy). n là số lần sai liên tiếp. Mỗi test cần reset đúng tiền điều kiện; không restart backend để reset vì source khởi tạo lại toàn bộ DB. Chưa chạy thì Actual/Tester/Tested Date để trống, Status = Not Run.

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC01 | Đăng nhập thành công | A chưa khóa, n=0; client sạch phiên. | 1. Nhập email và mật khẩu đúng của A. 2. Submit một lần. 3. Dùng JWT gọi GET /api/users/me. | Đăng nhập thành công; trả JWT được backend chấp nhận và đúng tài khoản. | Login successful; JWT gọi GET /api/users/me được HTTP 200, id=2, email=test@eshop.com. | Pass | Nguyễn Sơn Tùng | 16/10/2026 | Theo kết quả người dùng gửi; E01. Cần bổ sung ảnh terminal đã che token. |
| FR02-TC02 | Sai mật khẩu từ n=0 | A chưa khóa, n=0. | 1. Ghi n trước. 2. Submit A/W một lần. 3. Đọc n và khóa sau request. | Từ chối; không cấp phiên mới; n=1 và chưa khóa. |  | Not Run |  |  |  |
| FR02-TC03 | Sai mật khẩu từ n=1 | A chưa khóa, n=1; không có lần thành công xen giữa. | 1. Ghi n trước. 2. Submit A/W một lần. 3. Đọc n và khóa. | Từ chối; n=2; chưa khóa; không cấp phiên mới. |  | Not Run |  |  | Nếu đặt n bằng helper, ghi kiểm cô lập; không thay bằng chứng chuỗi thật. |
| FR02-TC04 | Sai lần thứ ba kích hoạt khóa | A chưa khóa, n=2; xác nhận cách đạt tiền điều kiện. | 1. Submit A/W một lần. 2. Đọc n và mốc khóa. 3. Ghi chuỗi thao tác trước đó. | Từ chối; n=3; kích hoạt khóa tạm 30 giây. Thời lượng kiểm tiếp ở BVA. |  | Not Run |  |  | Nếu đặt n bằng helper, ghi kiểm cô lập; không thay bằng chứng chuỗi thật. |
| FR02-TC05 | Đúng mật khẩu nhưng tài khoản còn khóa | A đang khóa; có mốc bắt đầu khóa thực tế. | 1. Sau khoảng 10s, submit A với mật khẩu đúng. 2. Quan sát kết quả. | Vẫn từ chối; không cấp phiên đăng nhập mới; thông báo phù hợp. |  | Not Run |  |  |  |
| FR02-TC06 | Email hợp định dạng nhưng không tồn tại | U hợp định dạng và không tồn tại; client sạch phiên. | 1. Nhập U và mật khẩu Test1234!. 2. Submit. 3. Quan sát phản hồi. | Từ chối; không cấp phiên; thông báo phù hợp. Không assert bộ đếm U. |  | Not Run |  |  |  |
| FR02-TC07 | Validation HTML5 cho email sai định dạng | Mở form login; mật khẩu không rỗng. | 1. Kiểm type của input email. 2. Nhập abc. 3. Submit qua UI, quan sát Network. | Input type=email; HTML5 chặn submit; không gửi request login. |  | Not Run |  |  |  |
| FR02-TC08 | Đăng nhập sau khi hết thời gian khóa | Tạo lần khóa mới; ghi mốc; không request xen giữa. | 1. Đợi khoảng 35s từ mốc khóa. 2. Submit A với mật khẩu đúng. | Khóa đã hết; đăng nhập thành công và trả JWT. Chưa kiểm đúng biên 30s. |  | Not Run |  |  |  |
| FR02-TC09 | Client lưu token sau thành công | A chưa khóa; client sạch phiên. | 1. Đăng nhập đúng. 2. Xem Local Storage đúng origin. 3. So token lưu với response. | Client lưu đúng token để xác thực; giá trị khớp response. | Token Network/Storage khớp; chưa xác nhận origin trong ảnh. | Not Run | Nguyễn Sơn Tùng | 16/10/2026 | Đã kiểm một phần; Not Run nghĩa chưa kết luận. Xác nhận origin localhost:5173. |
| FR02-TC10 | Gửi Bearer token trên request có xác thực | Đã đăng nhập; có danh mục request cần xác thực. | 1. Kích hoạt từng luồng client cần auth. 2. Kiểm Authorization trong Network. | Mỗi request trong danh mục có Bearer đúng token; không dùng request tự gửi thay bằng chứng client. |  | Not Run |  |  | Chưa có inventory thì chưa kết luận tất cả request. |
| FR02-TC11 | Rà soát nội dung lỗi ở các tình huống đại diện | Dùng kết quả độc lập của TC02, TC05, TC06. | 1. Đọc thông báo UI và response từng tình huống. 2. Đối chiếu tiêu chí không lộ chi tiết. | Lỗi phù hợp, không lộ chi tiết nguyên nhân. Phần tiêu chí chưa rõ ghi chờ xác nhận, không ép Pass. |  | Not Run |  |  | Tiêu chí lỗi còn điểm cần xác nhận Q4. |


### 2.6 Boundary Value Analysis

Chưa thực hiện. Cần xác định biên của số lần sai và thời gian khóa, kiểu/độ chính xác và điểm tại/trong/ngoài biên; chọn dữ liệu, expected và test; giải thích từng bước theo S04. Khoảng 10s/35s ở test Domain chỉ là đại diện, không thay test BVA tại ngưỡng 30s. Không tự nhận bảng hiện tại đã đáp ứng BVA.

### 2.7 Kết quả bằng chứng và nhận xét AI

TC01 Pass theo kết quả người dùng: đăng nhập thành công, token gọi GET /api/users/me được HTTP 200, id=2, email=test@eshop.com. TC09 đã so token khớp nhưng chưa xác nhận origin ảnh; chưa chốt Pass. E01 là bản chép kết quả terminal trong FR-02/evidence/FR02-TC01-RUN01/User_Provided_Result.md; cần bổ sung ảnh đã che token. Test_Execution.md giữ thông tin run. Response login có user.password dạng rõ là quan sát cần lập báo cáo lỗi riêng, chưa có issue chính thức.

Chưa có đánh giá đầy đủ của sinh viên để kết luận các thiếu sót AI. Ghi nhận từng chỉnh sửa và nguồn đối chiếu trong AI Audit; không tự gán verdict. Các điểm chưa rõ trong đặc tả không tự xem là bug hay thiếu sót AI đã chứng minh.

## 3 Pool B FR09 Mã giảm giá

Đã chọn, chưa thiết kế/chạy. Sẽ trình bày lần lượt Input/Output → điều kiện/EC → đại diện và bảng test Domain; sau đó các bước BVA, bảng test biên, kết quả/bug và AI gap analysis.

## 4 Pool C FR15 Quản lý sản phẩm

Đã chọn, chưa thiết kế/chạy. Áp dụng cùng cấu trúc, tập trung tên tối đa 255 ký tự, giá lớn hơn 0, danh mục bắt buộc và thao tác CRUD không ảnh hưởng sản phẩm khác.

## 5 Pool D Mobile

Chưa chốt chức năng. Bản cuối vẫn cần một chức năng Pool D, không được bỏ qua.

## 6 Tổng kết và hồ sơ hỗ trợ

| Chức năng | Designed | Executed | Pass | Fail | Not Run |
| --- | --- | --- | --- | --- | --- |
| FR-02 | 11 | 1 | 1 | 0 | 10 |
| FR-09 | 0 | 0 | 0 | 0 | 0 |
| FR-15 | 0 | 0 | 0 | 0 | 0 |
| Pool D chưa chọn | 0 | 0 | 0 | 0 | 0 |
| Tổng | 11 | 1 | 1 | 0 | 10 |

Executed là số test đã hoàn tất đánh giá; TC09 kiểm một phần nằm trong 10 chưa kết luận. Không đếm trùng Domain/BVA. Các số 0 ở phần chưa làm không có nghĩa đã hoàn thành.

Đã có bốn skill trong skills/: domain-testing, boundary-value-analysis, test-execution-reporting, ai-audit-report; chưa có video demo hoàn chỉnh. Hồ sơ còn cần BVA, các pool chưa làm, bug report/issue nếu có bug, AI Critique, AI Audit và Git log tổng hợp, README tự chấm, PDF và video. Bản Word chỉ hỗ trợ chỉnh sửa, không thay PDF.

## 7 Tài liệu tham khảo

- Đề HW02 mục 6, 9 và 14; slide S04 Domain Testing.
- README eshop-sut, FR-02/09/15/20.
- Test cases_Template_En.xlsx trong tài liệu môn học.
- FR-02/Requirements_Analysis.md, Domain_Testing.md, Test_Cases.md, Test_Execution.md và evidence/: tài liệu chi tiết.
- audit/AI_Audit_Report.md: bản audit hiện tại; chưa tích hợp toàn văn thành phụ lục trong bản chính này. Bản nộp cần hoàn thiện phụ lục theo yêu cầu đã thống nhất.
