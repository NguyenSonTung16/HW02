# Báo cáo HW02 Domain Testing trên EShop

Ngày cập nhật: 16/10/2026.

## 1 Thông tin và phạm vi

Báo cáo trình bày quá trình áp dụng kiểm thử miền (Domain Testing) và phân tích giá trị biên (Boundary Value Analysis) trên EShop. Nội dung hiện có là thiết kế Domain Testing cho FR-02, với TC01 Pass theo kết quả người dùng cung cấp; TC09 kiểm một phần. Các phần còn lại được ghi rõ để tiếp tục bổ sung.

- Họ và tên: chưa cung cấp.
- MSSV: chưa xác nhận trong báo cáo.
- Nhóm: chưa xác nhận trong báo cáo.
- Hạn nộp: kiểm tra trên Moodle, chưa ghi nhận.
- Trạng thái rà soát: bản nháp AI, sinh viên chưa xác nhận nội dung.

| Pool | Chức năng | Trạng thái |
| --- | --- | --- |
| A | FR-02 Đăng nhập và khóa tài khoản | Có thiết kế Domain Testing; TC01 Pass, TC09 kiểm một phần; chưa BVA |
| B | FR-09 Mã giảm giá | Đã chọn, chưa thiết kế hoặc chạy |
| C | FR-15 Quản lý sản phẩm | Đã chọn, chưa thiết kế hoặc chạy |
| D | Mobile App | Chưa chốt chức năng; bổ sung sau |

## 2 Phương pháp và môi trường

Áp dụng các bước của slide S04: xác định Input/Output, điều kiện, EC cho từng Input/Output, chọn đại diện và test case, sau đó phân tích biên. Bảng bao phủ phân biệt test dự kiến với kết quả thực sự quan sát được. Expected result dựa trên đặc tả README, không lấy source implementation làm chuẩn.

Sử dụng AI theo từng bước, lưu bản đề xuất ban đầu, phản hồi rà soát và AI Audit. Backend http://localhost:3000 và web http://localhost:5173 đã khởi động; người dùng kiểm bằng browser và PowerShell. Runtime khởi động Node v24.11.1. Source commit SUT, phiên bản browser và giờ chạy cụ thể cần bổ sung. Git commit của báo cáo không thay thế thông tin phiên bản SUT.

## 3 Pool A FR02 Đăng nhập và khóa tài khoản


### 3.1 Phân tích yêu cầu


Phiên bản thiết kế AI draft v1 ngày 15/10/2026; cập nhật trạng thái 16/10/2026. Chưa được sinh viên rà soát toàn bộ. TC01 đã Pass theo kết quả người dùng, TC09 kiểm một phần; xem Test_Execution.md.

#### Nguồn và phạm vi

- Nghiệp vụ: `eshop-sut/README.md`, mục FR-02, dòng 38–46 tại thời điểm đọc.
- Phương pháp: S04_Domain Testing.pdf, trang 3, 8–11, 21. Bước 1 xác định Input/Output; bước 2 chia EC; bước 3 chọn đại diện/test. BVA thực hiện sau, không bao gồm trong lần thử này.
- Phạm vi: đăng nhập web và các quan sát API/client cần thiết để kiểm tra FR-02. Không áp điều kiện mật khẩu đăng ký FR-01 như quy tắc đầu vào đăng nhập. Không đọc code để tạo expected result.

#### 1. Yêu cầu (Requirements)

| ID | Yêu cầu từ FR-02 | Cách xác nhận dự kiến |
| --- | --- | --- |
| FR02-R1 | Người dùng nhập email và mật khẩu để đăng nhập | Đúng cặp thông tin của tài khoản được phép đăng nhập |
| FR02-R2 | Sau mỗi lần đăng nhập sai, bộ đếm tăng đúng 1 | Đo trước/sau đối với tài khoản đã tồn tại; cần điểm quan sát |
| FR02-R3 | Sai từ 3 lần liên tiếp trở lên thì khóa 30 giây | Thiết lập số lần sai; quan sát chuyển trạng thái và từ chối khi đang khóa |
| FR02-R4 | Thông báo lỗi phù hợp, không lộ chi tiết nguyên nhân | Quan sát thông báo; chưa có bộ tiêu chí chính thức về độ chi tiết |
| FR02-R5 | Thành công trả JWT | Quan sát token, kiểm tra là JWT hợp lệ bằng cơ chế xác thực của backend |
| FR02-R6 | Client lưu token và gửi Authorization: Bearer <token> trong mọi yêu cầu có xác thực | Quan sát lưu trữ và các request thuộc danh mục cần xác thực |
| FR02-R7 | Email dùng type="email", validate định dạng HTML5 | Kiểm tra trường DOM và hành vi submit email sai định dạng |

R1 có phần diễn giải tất yếu: cặp thông tin đúng được chấp nhận khi không bị khóa; cặp sai bị từ chối. Đặc tả không cho mã HTTP, nội dung lỗi nguyên văn hay định dạng response cụ thể.

#### 2. Danh mục Input, Output và ngữ cảnh

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

State là ngữ cảnh cần thiết lập, không phải các trường nhập thêm trên màn hình. S1 và O4 có cùng dữ liệu nghiệp vụ nhưng khác thời điểm trước/sau hành động.

#### 3. Điều kiện (Conditions)

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

Không dùng khoảng hai phía giả cho biến chỉ có ngưỡng dưới. Số lần sai âm thuộc ngoài miền trạng thái hợp lệ, không giả định người dùng có thể nhập số âm vào màn hình đăng nhập.

#### 4. Điểm chưa rõ và giới hạn

| ID | Điểm cần xác nhận | Tác động và hướng xử lý |
| --- | --- | --- |
| FR02-Q1 | Đăng nhập thành công có reset số lần sai? Sau hết khóa bộ đếm được reset thế nào? | Không tự thêm assertion reset=0. Test chuỗi sai-thành công-sai và tái khóa chờ oracle rõ hơn |
| FR02-Q2 | Sai email không tồn tại hoặc request bị validation UI có bộ đếm nào? Request khi đang khóa có tăng đếm/gia hạn không? | Chỉ assert +1 với tài khoản tồn tại, chưa khóa, request sai đã được gửi; không áp assertion tùy tiện cho các nhóm khác |
| FR02-Q3 | Độ chính xác đồng hồ và mốc bắt đầu khóa? | Lần này test sau hết khóa dùng dư thời gian; BVA đúng 30 giây cần phương pháp riêng |
| FR02-Q4 | Điều gì là lộ chi tiết nguyên nhân? | Không đặt expected lỗi giống hệt cho mọi trường hợp. Đánh giá tối thiểu rò mật khẩu/token/stack và ghi phần cần giảng viên xác nhận; oracle chi tiết còn mở |
| FR02-Q5 | Email/mật khẩu rỗng, thiếu field, trim/case, độ dài, JSON sai kiểu? | Đặc tả không cho đủ quy tắc; ghi EC mở và test bổ sung sau khi xác định oracle, không lấy source làm chuẩn |
| FR02-Q6 | Quan sát bộ đếm, timestamp khóa và xác minh chữ ký JWT bằng cách nào? | Chưa có môi trường chạy; cần kiểm tra quyền đọc dữ liệu/log và cơ chế xác thực hợp lệ, không tuyên bố quan sát được |
| FR02-Q7 | Danh mục đầy đủ request có xác thực của client? | Test một request chưa chứng minh "tất cả"; lập inventory khi khảo sát luồng thực thi |

#### Trạng thái và handoff

Đây là bản phân tích thiết kế. Backend/web đã được khởi động và người dùng đã thực hiện TC01; source commit SUT tại thời điểm chạy chưa xác nhận. Kết quả cập nhật tại Test_Execution.md; chưa có bug report chính thức. Bộ test ở Test_Cases.md sử dụng dữ liệu demo sau khi kiểm tra fixture thật. Các câu hỏi trên không chặn phần có đủ yêu cầu, nhưng chặn kết luận toàn bộ FR-02 đã bao phủ.


### 3.2 Phân tích miền và bảng bao phủ


Ngày 15/10/2026; chưa được sinh viên rà soát. Nguồn và C-ID: Requirements_Analysis.md. Phương pháp S04 trang 3, 8–11, 21. Cập nhật 16/10/2026: TC01 Pass theo kết quả người dùng, TC09 kiểm một phần, còn lại chưa chạy. Bảng dưới là coverage thiết kế, không tự chuyển thành coverage thực thi.

#### Cách chia lớp tương đương (Equivalence Classes)

- Điều kiện bắt buộc: email hợp định dạng/không hợp định dạng; đúng/sai thông tin xác thực.
- Nhóm xử lý khác nhau: email đúng định dạng được tách tồn tại/không tồn tại; trạng thái chưa khóa/đang khóa/đã hết thời gian khóa.
- Bộ đếm có ngưỡng 3, không có giới hạn trên được đặc tả: phân biệt 0, 1..2 trước request chưa khóa; test bổ sung chọn 1 và 2 trong cùng lớp để kiểm tra chuyển trạng thái. Đây là chia nhỏ theo hành vi sau thao tác, không áp máy móc khoảng hai phía.
- Output phân lớp theo hành vi mong đợi. Lỗi xác thực là output đúng của test âm, không phải bug. Các output sai như token hỏng được dùng làm tiêu chí fail, không cố kích hoạt như một hành vi đúng.

#### EC đầu vào và trạng thái

| EC-ID (prefix FR02-) | Biến/C-ID | Miền và đại diện | Phân loại/lý do |
| --- | --- | --- | --- |
| EC-I01 | I1/C1,C2 | Email hợp định dạng, tài khoản tồn tại: test@eshop.com | Hợp lệ; fixture cần xác nhận |
| EC-I02 | I1/C1,C2 | Email hợp định dạng, không có tài khoản: hw02-absent@example.com | Sai xác thực; xác nhận không tồn tại trước chạy |
| EC-I03 | I1/C1 | Email không rỗng, sai HTML5: abc | Sai định dạng; tách khỏi email không tồn tại |
| EC-I04 | I2/C2 | Mật khẩu đúng cho tài khoản đã có: Test1234! | Hợp lệ với fixture mặc định nếu chưa bị đổi |
| EC-I05 | I2/C2 | Mật khẩu sai cho tài khoản đã có: WrongPass9! | Sai xác thực; xác nhận không trùng mật khẩu thật |
| EC-I06 | I2/C2 | Email không tồn tại, mật khẩu chuỗi bất kỳ: Test1234! | Không áp khái niệm đúng/sai mật khẩu tài khoản; không tính là lỗi độc lập thứ hai |
| EC-S01 | S1/C4,C5 | n=0 trước request | Chưa có lần sai; đầu chuỗi |
| EC-S02 | S1/C4,C5 | n=1 trước request sai | Sau +1 vẫn dưới ngưỡng |
| EC-S03 | S1/C4,C5 | n=2 trước request sai | Sau +1 chạm ngưỡng khóa; chia từ nhóm 1..2 vì hành vi khác |
| EC-S04 | S2,S3/C3 | Chưa khóa | Cho phép xét xác thực |
| EC-S05 | S2,S3/C3 | Khóa còn hiệu lực, ví dụ 10 giây sau khi bắt đầu khóa | Không được đăng nhập dù cặp đúng |
| EC-S06 | S2,S3/C3 | Đã qua thời hạn khóa, ví dụ 35 giây sau mốc được xác nhận | Khóa tạm thời phải hết; không assert reset bộ đếm |

#### EC đầu ra (Output EC)

| EC-ID (prefix FR02-) | Biến/C-ID | Kết quả/đại diện và assertion |
| --- | --- | --- |
| EC-O01 | O1/C2,C3 | Đăng nhập thành công với cặp đúng, chưa khóa |
| EC-O02 | O1/C2 | Request sai thông tin bị từ chối |
| EC-O03 | O1/C1 | UI chặn submit email sai định dạng HTML5 |
| EC-O04 | O1/C3 | Request khi đang khóa bị từ chối |
| EC-O05 | O2/C6 | Thông báo lỗi xác thực phù hợp; oracle chi tiết còn Q4 |
| EC-O06 | O2/C6 | Thông báo cho tình huống khóa phù hợp; oracle chi tiết còn Q4 |
| EC-O07 | O3/C7 | Có JWT xác thực được khi thành công |
| EC-O08 | O3/C2,C3 | Không cấp phiên/JWT có thể dùng để vượt xác thực khi bị từ chối; không ép response thiếu field cụ thể |
| EC-O09 | O4/C4 | n_after=n_before+1 khi sai, tài khoản tồn tại chưa khóa |
| EC-O10 | O5/C5 | Sau lần sai thứ 1/2 chưa kích hoạt khóa |
| EC-O11 | O5/C5 | Lần sai thứ 3 kích hoạt khóa tạm 30 giây |
| EC-O12 | O5/C3 | Khóa đã hết sau thời hạn, thể hiện bằng đăng nhập đúng thành công |
| EC-O13 | O6/C8 | Token được client lưu; cơ chế lưu chưa cố định |
| EC-O14 | O7/C8 | Request có xác thực mang Authorization: Bearer <token> đúng token |

#### EC còn mở, chưa có oracle đủ rõ

I1: email rỗng/thiếu, biến thể hoa thường/whitespace, kiểu API không phải chuỗi. I2: rỗng/thiếu, độ dài/kiểu khác. O4: reset sau thành công/hết khóa, request trong thời gian khóa; O2: tiêu chí không lộ nguyên nhân; O7: toàn bộ inventory request. Xem Q1–Q7. Không tạo giới hạn token hay nội dung thông báo chính xác từ suy đoán.

#### Chọn đại diện và bao phủ thiết kế

S04 trang 21: test hợp lệ gộp EC hợp lệ; test âm cô lập một lớp đầu vào sai. Trạng thái khóa hợp lệ của hệ thống là tiền điều kiện, không phải dữ liệu sai thứ hai. Mọi ID bên dưới có prefix `FR02-`; bảng test ghi đầy đủ prefix.

| Requirement | C-ID | Input/Output/State | EC | Test dự kiến | Trạng thái/giới hạn |
| --- | --- | --- | --- | --- | --- |
| R1,R7 | C1,C2 | I1 | EC-I01 | TC01–05,TC07–11 | Có test |
| R1 | C2 | I1 | EC-I02 | TC06,TC11 | Có test |
| R7 | C1 | I1 | EC-I03 | TC07 | Có test |
| R1,R3 | C2,C3 | I2 | EC-I04 | TC01,TC05,TC08,TC09,TC10 | Có test |
| R1,R2 | C2,C4 | I2 | EC-I05 | TC02–04,TC11 | Có test |
| R1 | C2 | I2 | EC-I06 | TC06,TC11 | Có test |
| R2,R3 | C4,C5 | S1 | EC-S01 | TC01,TC02 | Có test |
| R2,R3 | C4,C5 | S1 | EC-S02 | TC03 | Có test |
| R2,R3 | C4,C5 | S1 | EC-S03 | TC04 | Có test |
| R1,R3 | C3 | S2 | EC-S04 | TC01–04 | Có test |
| R3 | C3 | S2,S3 | EC-S05 | TC05 | Có test |
| R3 | C3 | S2,S3 | EC-S06 | TC08 | Có test; không kiểm chính xác biên 30s |
| R1 | C2 | O1 | EC-O01 | TC01,TC08–10 | Có test |
| R1 | C2 | O1 | EC-O02 | TC02–04,TC06 | Có test |
| R7 | C1 | O1 | EC-O03 | TC07 | Có test |
| R3 | C3 | O1 | EC-O04 | TC05 | Có test |
| R4 | C6 | O2 | EC-O05 | TC02,TC06,TC11 | Có test; Q4 chưa rõ |
| R4 | C6 | O2 | EC-O06 | TC05,TC11 | Có test; Q4 chưa rõ |
| R5 | C7 | O3 | EC-O07 | TC01 | Có test; cần phương pháp xác minh JWT |
| R1,R3 | C2,C3 | O3 | EC-O08 | TC02,TC05,TC06 | Có test |
| R2 | C4 | O4 | EC-O09 | TC02–04 | Có test; cần điểm quan sát đếm |
| R3 | C5 | O5 | EC-O10 | TC02,TC03 | Có test |
| R3 | C5 | O5 | EC-O11 | TC04 | Có test; BVA thời lượng để sau |
| R3 | C3 | O5 | EC-O12 | TC08 | Có test |
| R6 | C8 | O6 | EC-O13 | TC09 | Có test |
| R6 | C8 | O7 | EC-O14 | TC10 | Có test; danh mục request còn thiếu |

Các EC còn mở ở mục trên chưa được tính là bao phủ. Không tuyên bố đầy đủ FR-02 chỉ vì các hàng EC đã đặt mã đều có test.

#### Tự kiểm tra AI trước khi giao

- Phân biệt đúng Input/Output/State, có EC output và assertion trong test.
- Đã tách n=1 và n=2 do hậu trạng thái khác nhau.
- Không áp min 8 ký tự của đăng ký lên mật khẩu đăng nhập.
- Chưa có human review toàn bộ; TC01 đã có actual và Pass theo kết quả người dùng. Chưa có bug report chính thức hoặc coverage thực thi toàn bộ. Bộ này cần BVA riêng và giải quyết các Q trước khi kết luận bao phủ đầy đủ.


### 3.3 Test case Domain Testing


Thiết kế ngày 15/10/2026; cập nhật kết quả ngày 16/10/2026 theo bằng chứng người dùng cung cấp. TC01 Pass; TC09 đã quan sát một phần, còn chờ xác nhận origin. Chưa rà soát toàn bộ thiết kế. BVA chưa thực hiện. ID EC/C/R tham chiếu Domain_Testing.md và Requirements_Analysis.md, đều dùng prefix FR02-.

#### Fixture và cách ghi nhận

- A: tài khoản test@eshop.com, mật khẩu demo Test1234! theo README; cần kiểm tra tồn tại và mật khẩu chưa đổi trước khi dùng. W: WrongPass9!, xác nhận không phải mật khẩu A.
- U: hw02-absent@example.com, phải xác nhận không tồn tại. Không tạo U rồi dùng như tài khoản không tồn tại.
- Chuẩn bị tài khoản không khóa và n chính xác trước mỗi test. Reset bằng cơ chế dữ liệu test đã xác định, không giả định một lần đăng nhập thành công reset n. Chưa thực hiện reset hay đọc DB.
- Ghi timestamp gửi/nhận, request/response đã che bí mật và số đếm trước/sau bằng điểm quan sát được phép. Không chỉ dựa thông báo UI để suy ra đếm chính xác.
- Test khóa cần mốc bắt đầu thật. 10s/35s là giá trị đại diện trong miền, không phải test BVA chính xác tại ngưỡng.
- Không quy định mã HTTP hay chuỗi lỗi nguyên văn khi README chưa cho. Client cũ phải được cô lập để token tồn dư không bị nhầm thành token mới cấp.

#### Quy ước bảng test theo mẫu

Tham khảo Test cases_Template_En.xlsx trong thư mục Test Cases của Drive: https://docs.google.com/spreadsheets/d/16IXhmhLXPKyPVPtjp7BMrIMsWV-zriX4/edit

Giữ 10 trường của mẫu: ID, Test case name, Precondition, Test step, Expected Result, Actual Result, Status, Tester, Tested Date, Remark. Bổ sung 5 trường: Kỹ thuật, EC đầu vào và trạng thái, EC đầu ra, Giá trị biên, Bằng chứng. Giá trị biên chưa thiết kế được ghi rõ, không coi test Domain đã là BVA. Metadata requirement/condition và lưu ý cũ giữ trong Remark. Trong Word, mỗi test chia ba nhóm bảng cùng ID để không ép 15 cột lên một trang. Phần giải thích phương pháp và bảng bao phủ vẫn trình bày riêng.

#### FR02-TC01 - Đăng nhập thành công

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC01 | Đăng nhập thành công | A chưa khóa, n=0, client sạch phiên. | nhập email A và mật khẩu đúng; submit; quan sát kết quả và JWT; dùng cơ chế xác minh token của backend hoặc request được bảo vệ để chứng minh token được chấp nhận. Chỉ decode chuỗi ba phần không đủ chứng minh JWT hợp lệ. | đăng nhập thành công, có JWT xác thực được (R1,R5). Không assert n reset. | Người dùng đăng nhập thành công, nhận JWT; dùng token gọi GET /api/users/me được HTTP 200, id=2, email=test@eshop.com. Kết quả do người dùng thực thi và gửi trong hội thoại. | Pass | Nguyễn Sơn Tùng (người dùng thực thi) | 16/10/2026; giờ chạy cụ thể chưa ghi nhận | Requirement/Conditions: R1,R5 / C2,C3,C7. EC đầu vào/trạng thái: EC-I01,I04,S01,S04. EC output: EC-O01,O07. Cập nhật theo yêu cầu người dùng; không coi đây là sinh viên đã duyệt toàn bộ thiết kế. Không ghi token/password vào evidence. | Domain Testing | EC-I01,I04,S01,S04 | EC-O01,O07 | Chưa thiết kế BVA; không áp giới hạn độ dài tùy ý | evidence/FR02-TC01-RUN01/User_Provided_Result.md; còn cần ảnh terminal đã che token cho hồ sơ nộp |

#### FR02-TC02 - Sai mật khẩu từ n=0

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC02 | Sai mật khẩu từ n=0 | A n=0, chưa khóa, client sạch phiên. | đọc n trước; nhập A/W và submit; đọc n sau; kiểm tra phản hồi và khóa. | từ chối, lỗi phù hợp, không cấp phiên hợp lệ mới; n=1, chưa khóa (R1–R4). Phần chi tiết thông báo cần Q4. | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R1,R2,R3,R4 / C2,C4,C5,C6. Input/State: EC-I01,I05,S01,S04. Output: EC-O02,O05,O08,O09,O10. | Domain Testing | EC-I01,I05,S01,S04 | EC-O02,O05,O08,O09,O10 | BVA chưa làm; n và chuyển trạng thái theo bước test | Chưa có |

#### FR02-TC03 - Sai mật khẩu từ n=1

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC03 | Sai mật khẩu từ n=1 | thiết lập n=1, chưa khóa, không thành công xen giữa. | đọc n; submit A/W một lần; đọc n và trạng thái sau. | từ chối; n=2, chưa khóa, không cấp phiên hợp lệ (R1–R3). | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R1,R2,R3 / C2,C4,C5. Input/State: EC-I01,I05,S02,S04. Output: EC-O02,O08,O09,O10. | Domain Testing | EC-I01,I05,S02,S04 | EC-O02,O08,O09,O10 | BVA chưa làm; n và chuyển trạng thái theo bước test | Chưa có |

#### FR02-TC04 - Sai lần thứ ba kích hoạt khóa

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC04 | Sai lần thứ ba kích hoạt khóa | n=2 do hai lần sai liên tiếp; chưa khóa. | ghi n trước; submit A/W; ghi n sau và mốc khóa/trạng thái khóa. | n=3, request bị từ chối, khóa tạm 30 giây được kích hoạt (R2,R3). Test này chứng minh kích hoạt; không một mình chứng minh thời lượng chính xác. | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R1,R2,R3 / C2,C4,C5. Input/State: EC-I01,I05,S03,S04. Output: EC-O02,O08,O09,O11. | Domain Testing | EC-I01,I05,S03,S04 | EC-O02,O08,O09,O11 | BVA chưa làm; n và chuyển trạng thái theo bước test | Chưa có |

#### FR02-TC05 - Đúng mật khẩu nhưng tài khoản còn khóa

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC05 | Đúng mật khẩu nhưng tài khoản còn khóa | thiết lập khóa có mốc quan sát được; không có request khác xen vào. | khoảng 10s sau mốc khóa, submit A với mật khẩu đúng; quan sát phản hồi. | từ chối, thông báo phù hợp tình huống khóa, không cấp phiên hợp lệ (R3,R4). Không assert đếm giữ nguyên hay gia hạn vì Q2. | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R3,R4 / C3,C6. Input/State: EC-I01,I04,S05. Output: EC-O04,O06,O08. | Domain Testing | EC-I01,I04,S05 | EC-O04,O06,O08 | 10s là đại diện đang khóa, chưa kiểm biên 30s | Chưa có |

#### FR02-TC06 - Email hợp định dạng nhưng không tồn tại

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC06 | Email hợp định dạng nhưng không tồn tại | U không tồn tại, client sạch phiên. | submit U với chuỗi mật khẩu Test1234!; quan sát phản hồi. | từ chối, lỗi phù hợp, không cấp phiên hợp lệ (R1,R4). Không assert bộ đếm tài khoản không tồn tại. Mật khẩu không gán là sai thứ hai vì không có tài khoản để so khớp. | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R1,R4 / C2,C6. Input: EC-I02,I06. Output: EC-O02,O05,O08. | Domain Testing | EC-I02,I06 | EC-O02,O05,O08 | Chưa thiết kế BVA; không áp giới hạn độ dài tùy ý | Chưa có |

#### FR02-TC07 - Validation HTML5 cho email sai định dạng

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC07 | Validation HTML5 cho email sai định dạng | mở form đăng nhập, không bypass validation; điền mật khẩu đúng của fixture, không để rỗng. | kiểm DOM field email phải có type=email; nhập abc; submit bằng thao tác người dùng; quan sát validity và network. | trình duyệt báo sai định dạng và form không gửi request đăng nhập qua submit thông thường (R7). Không yêu cầu validate HTML5 chặn request API gọi trực tiếp. | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R7 / C1. Input: EC-I03,I04. Output: EC-O03. | Domain Testing | EC-I03,I04 | EC-O03 | Chưa thiết kế BVA; không áp giới hạn độ dài tùy ý | Chưa có |

#### FR02-TC08 - Đăng nhập sau khi hết thời gian khóa

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC08 | Đăng nhập sau khi hết thời gian khóa | A đã khóa, ghi mốc; không có request trong thời gian chờ làm thay đổi trạng thái. | đợi khoảng 35s tính từ mốc khóa đã xác nhận; submit A/mật khẩu đúng. | khóa tạm đã hết, thành công và cấp JWT (R1,R3,R5). Không assert n=0; chưa kiểm chính xác 30s và chưa kết luận lỗi thời lượng từ riêng test này. | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R1,R3,R5 / C2,C3,C7. Input/State: EC-I01,I04,S06. Output: EC-O01,O07,O12. | Domain Testing | EC-I01,I04,S06 | EC-O01,O07,O12 | 35s là đại diện sau hết khóa, chưa kiểm biên 30s | Chưa có |

#### FR02-TC09 - Client lưu token sau thành công

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC09 | Client lưu token sau thành công | client sạch phiên, A chưa khóa. | đăng nhập đúng; quan sát cách client giữ token thực tế bằng công cụ phù hợp, đối chiếu token trả về với token được lưu. Che token trong evidence. | token được client lưu để dùng cho yêu cầu có xác thực (R6). Không tự yêu cầu tồn tại sau restart hoặc phải ở localStorage/cookie. | Người dùng cung cấp ảnh Local Storage và hai token đã đối chiếu khớp hoàn toàn. Ảnh chưa hiển thị origin; có key user tài khoản ketoan cũ nên cần xác nhận đúng localhost:5173 trước kết luận. | Not Run | Nguyễn Sơn Tùng (quan sát một phần) | 16/10/2026; chưa hoàn tất | R6 / C8. Input/State: EC-I01,I04,S04. Output: EC-O01,O13. Not Run trong thống kê nghĩa chưa có kết luận cuối; đã kiểm một phần, chờ xác nhận origin. Không tự gán Fail/Pass. | Domain Testing | EC-I01,I04,S04 | EC-O01,O13 | Chưa thiết kế BVA; không áp giới hạn độ dài tùy ý | Test_Execution.md mục TC09; ảnh trong hội thoại chưa lưu bản đã che token vào hồ sơ |

#### FR02-TC10 - Gửi Bearer token trên request có xác thực

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC10 | Gửi Bearer token trên request có xác thực | đăng nhập thành công; khảo sát và lập danh mục request cần xác thực trong phạm vi client. | kích hoạt từng request trong danh mục; quan sát Authorization trên request thực tế, so token được lưu. Ghi endpoint/method và kết quả từng request. | mọi request thuộc danh mục cần xác thực có Authorization: Bearer <token> đúng token (R6). Chưa có inventory thì chỉ là test thiết kế một phần, không nhận bao phủ "tất cả". | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R6 / C8. Input/State: EC-I01,I04,S04. Output: EC-O01,O14. | Domain Testing | EC-I01,I04,S04 | EC-O01,O14 | Chưa thiết kế BVA; không áp giới hạn độ dài tùy ý | Chưa có |

#### FR02-TC11 - Rà soát nội dung lỗi ở các tình huống đại diện

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC11 | Rà soát nội dung lỗi ở các tình huống đại diện | Dùng fixture/reset riêng của TC02/TC05/TC06 | dùng evidence riêng từng tình huống; rà thông báo/UI/response đối với yêu cầu không lộ chi tiết; ghi những nội dung quan sát được và tiêu chí áp dụng. Mỗi tình huống reset độc lập, không tạo một request có nhiều input sai. | lỗi phù hợp, không lộ chi tiết theo R4. Không tự đòi ba thông báo giống hệt. Kiểm không có mật khẩu/token/stack là kiểm tra tối thiểu bổ sung; tiêu chí đầy đủ chờ Q4. Chưa được kết luận Pass toàn bộ R4 khi oracle chưa đủ. | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R4 / C6. Input/State và output của từng lần chạy dùng lại TC02/TC05/TC06: EC-I01,I02,I04,I05,I06,S01,S04,S05; output EC-O05,O06. Đây là test bổ sung đánh giá output, không thay thế test EC chính. | Domain Testing | Dùng EC của TC02/TC05/TC06; xem Remark | EC-O05,O06 | Chưa thiết kế BVA; không áp giới hạn độ dài tùy ý | Chưa có |

#### Tổng kết thiết kế hiện tại

11 TC duy nhất: 1 đã có kết luận (TC01 Pass), 0 Fail, 10 chưa có kết luận (Not Run trong thống kê). Trong 10 case này, TC09 đã quan sát một phần và chờ xác nhận origin; 9 case khác chưa chạy. Executed dùng nghĩa đã hoàn tất đánh giá để không đếm TC09 là Pass hoặc Fail. Không coi số run bằng số TC. 6 EC Input, 6 EC State, 14 EC Output thuộc thiết kế; chưa xác nhận bao phủ thực thi toàn bộ. Xem Test_Execution.md. BVA chưa thực hiện.


### 3.4 Phân tích giá trị biên

Chưa thực hiện. Sẽ bổ sung bảng biên, dữ liệu test, liên kết EC và cách kiểm soát mốc thời gian khóa. Không coi các giá trị đại diện 10s và 35s trong test Domain Testing là kiểm chứng đầy đủ biên 30s.

### 3.5 Kết quả thực thi và bug

TC01 Pass: login thành công, JWT gọi GET /api/users/me được HTTP 200, id=2, email=test@eshop.com, theo terminal người dùng gửi. TC09 đã so khớp token nhưng chờ xác nhận origin. Có 1 test hoàn tất, 0 Fail, 10 chưa kết luận (gồm TC09 kiểm một phần). Evidence ghi tại FR-02/Test_Execution.md và FR-02/evidence/FR02-TC01-RUN01/User_Provided_Result.md; cần bổ sung ảnh terminal đã che token. Response login có user.password dạng rõ là quan sát cần lập hồ sơ lỗi riêng, chưa có issue chính thức.

### 3.6 AI gap analysis và rà soát

Đã tự rà soát bản nháp về liên kết EC và test; đã có kết quả TC01 do sinh viên cung cấp, nhưng chưa có đánh giá đầy đủ để kết luận các thiếu sót AI. Các câu hỏi Q1–Q7 là khoảng trống đặc tả đã nhận diện, không tự xem là bug hoặc sai sót AI đã chứng minh.

## 4 Pool B FR09 Mã giảm giá

Đã chọn. Chưa phân tích chi tiết, chưa có test và kết quả.

- Cần phân tích 5 điều kiện coupon, Input/Output, EC và bảng bao phủ.
- Cần phân tích biên tổng tiền, hạn dùng và số lượt sử dụng.
- Cần chuẩn bị dữ liệu, chạy test, lưu bằng chứng, báo bug và AI gap analysis nếu có.

## 5 Pool C FR15 Quản lý sản phẩm

Đã chọn. Chưa phân tích chi tiết, chưa có test và kết quả.

- Cần phân tích thêm, xem, sửa, xóa và yêu cầu tên, giá, danh mục.
- Cần EC Input/Output và BVA độ dài tên tối đa 255, giá lớn hơn 0.
- Cần chạy test, kiểm tra sửa không ảnh hưởng sản phẩm khác, lưu bằng chứng và báo bug.

## 6 Pool D Mobile App

Chưa chốt chức năng. Sẽ bổ sung sau khi xác nhận phạm vi và phân công trong nhóm. Chưa có test hoặc kết quả, chưa đủ bốn pool để nộp bản cuối.

## 7 Agent Skills

Đã tạo bốn skill: domain-testing, boundary-value-analysis, test-execution-reporting và ai-audit-report. Lưu bản nộp trong HW02/skills. Đã kiểm tra cấu trúc, liên kết tài nguyên và bản sao cài đặt. domain-testing đã được áp dụng để tạo bản nháp FR-02; chưa xác nhận hiệu quả bằng human review và thực thi. Chưa demo đầy đủ chu trình ba skill hoặc có video YouTube.

## 8 Tổng kết hiện tại

| Chức năng | Designed | Executed | Pass | Fail | Not Run |
| --- | --- | --- | --- | --- | --- |
| FR-02 | 11 | 1 | 1 | 0 | 10 |
| FR-09 | 0 | 0 | 0 | 0 | 0 |
| FR-15 | 0 | 0 | 0 | 0 | 0 |
| Pool D chưa chọn | 0 | 0 | 0 | 0 | 0 |
| Tổng | 11 | 1 | 1 | 0 | 10 |

Số 0 ở các phần chưa thiết kế không có nghĩa đã hoàn thành. Có ba tính năng đã chọn và một pool chưa chọn. TC01 đã có kết quả Pass; chưa có bug report chính thức. Executed trong bảng là số case đã hoàn tất đánh giá; TC09 mới kiểm một phần nằm trong Not Run và được chú thích ở bảng test. Bảng tự chấm và README nộp bài sẽ bổ sung sau, không tự gán điểm ở giai đoạn này.

## 9 Tài liệu tham khảo và hồ sơ liên quan

- Đề 2026.HW02.Domain Testing_En, mục 2, 5–10, 12–15.
- S04_Domain Testing.pdf, trang 3, 8–11, 21; phần BVA trang 24–27 dùng cho bước sau.
- README của eshop-sut, FR-02, FR-09, FR-15, FR-20.
- FR-02/Requirements_Analysis.md, FR-02/Domain_Testing.md, FR-02/Test_Cases.md: tài liệu thành phần.
- FR-02/audit/AI_Audit_FR02.md và snapshots: log hiện có, chưa phải AI Audit toàn bộ HW02.
- FR-02/Git_Log.txt: log hiện có cho FR-02.
- FR-02/Test_Execution.md và evidence/FR02-TC01-RUN01/User_Provided_Result.md: kết quả người dùng cung cấp.

Bản nộp cuối cần bổ sung báo cáo chính PDF, bug report và GitHub Issues có ảnh, AI Audit và AI Critique Markdown/PDF, Git log, README, skill và video demo cùng tài liệu hỗ trợ. Bản Word là bản chỉnh sửa, không thay thế định dạng PDF mà đề yêu cầu.
