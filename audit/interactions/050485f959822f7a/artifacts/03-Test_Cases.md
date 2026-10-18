# FR-02 - Test case Domain Testing, AI draft v1

Thiết kế ngày 15/10/2026; cập nhật kết quả ngày 16/10/2026 theo bằng chứng người dùng cung cấp. TC01 Pass; TC09 đã quan sát một phần, còn chờ xác nhận origin. Chưa rà soát toàn bộ thiết kế. BVA chưa thực hiện. ID EC/C/R tham chiếu Domain_Testing.md và Requirements_Analysis.md, đều dùng prefix FR02-.

## Fixture và cách ghi nhận

- A: tài khoản test@eshop.com, mật khẩu demo Test1234! theo README; cần kiểm tra tồn tại và mật khẩu chưa đổi trước khi dùng. W: WrongPass9!, xác nhận không phải mật khẩu A.
- U: hw02-absent@example.com, phải xác nhận không tồn tại. Không tạo U rồi dùng như tài khoản không tồn tại.
- Chuẩn bị tài khoản không khóa và n chính xác trước mỗi test. Reset bằng cơ chế dữ liệu test đã xác định, không giả định một lần đăng nhập thành công reset n. Chưa thực hiện reset hay đọc DB.
- Ghi timestamp gửi/nhận, request/response đã che bí mật và số đếm trước/sau bằng điểm quan sát được phép. Không chỉ dựa thông báo UI để suy ra đếm chính xác.
- Test khóa cần mốc bắt đầu thật. 10s/35s là giá trị đại diện trong miền, không phải test BVA chính xác tại ngưỡng.
- Không quy định mã HTTP hay chuỗi lỗi nguyên văn khi README chưa cho. Client cũ phải được cô lập để token tồn dư không bị nhầm thành token mới cấp.

## Quy ước bảng test theo mẫu

Tham khảo Test cases_Template_En.xlsx trong thư mục Test Cases của Drive: https://docs.google.com/spreadsheets/d/16IXhmhLXPKyPVPtjp7BMrIMsWV-zriX4/edit

Giữ 10 trường của mẫu: ID, Test case name, Precondition, Test step, Expected Result, Actual Result, Status, Tester, Tested Date, Remark. Bổ sung 5 trường: Kỹ thuật, EC đầu vào và trạng thái, EC đầu ra, Giá trị biên, Bằng chứng. Giá trị biên chưa thiết kế được ghi rõ, không coi test Domain đã là BVA. Metadata requirement/condition và lưu ý cũ giữ trong Remark. Trong Word, mỗi test chia ba nhóm bảng cùng ID để không ép 15 cột lên một trang. Phần giải thích phương pháp và bảng bao phủ vẫn trình bày riêng.

## FR02-TC01 - Đăng nhập thành công

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC01 | Đăng nhập thành công | A chưa khóa, n=0, client sạch phiên. | nhập email A và mật khẩu đúng; submit; quan sát kết quả và JWT; dùng cơ chế xác minh token của backend hoặc request được bảo vệ để chứng minh token được chấp nhận. Chỉ decode chuỗi ba phần không đủ chứng minh JWT hợp lệ. | đăng nhập thành công, có JWT xác thực được (R1,R5). Không assert n reset. | Người dùng đăng nhập thành công, nhận JWT; dùng token gọi GET /api/users/me được HTTP 200, id=2, email=test@eshop.com. Kết quả do người dùng thực thi và gửi trong hội thoại. | Pass | Nguyễn Sơn Tùng (người dùng thực thi) | 16/10/2026; giờ chạy cụ thể chưa ghi nhận | Requirement/Conditions: R1,R5 / C2,C3,C7. EC đầu vào/trạng thái: EC-I01,I04,S01,S04. EC output: EC-O01,O07. Cập nhật theo yêu cầu người dùng; không coi đây là sinh viên đã duyệt toàn bộ thiết kế. Không ghi token/password vào evidence. | Domain Testing | EC-I01,I04,S01,S04 | EC-O01,O07 | Chưa thiết kế BVA; không áp giới hạn độ dài tùy ý | evidence/FR02-TC01-RUN01/User_Provided_Result.md; còn cần ảnh terminal đã che token cho hồ sơ nộp |

## FR02-TC02 - Sai mật khẩu từ n=0

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC02 | Sai mật khẩu từ n=0 | A n=0, chưa khóa, client sạch phiên. | đọc n trước; nhập A/W và submit; đọc n sau; kiểm tra phản hồi và khóa. | từ chối, lỗi phù hợp, không cấp phiên hợp lệ mới; n=1, chưa khóa (R1–R4). Phần chi tiết thông báo cần Q4. | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R1,R2,R3,R4 / C2,C4,C5,C6. Input/State: EC-I01,I05,S01,S04. Output: EC-O02,O05,O08,O09,O10. | Domain Testing | EC-I01,I05,S01,S04 | EC-O02,O05,O08,O09,O10 | BVA chưa làm; n và chuyển trạng thái theo bước test | Chưa có |

## FR02-TC03 - Sai mật khẩu từ n=1

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC03 | Sai mật khẩu từ n=1 | thiết lập n=1, chưa khóa, không thành công xen giữa. | đọc n; submit A/W một lần; đọc n và trạng thái sau. | từ chối; n=2, chưa khóa, không cấp phiên hợp lệ (R1–R3). | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R1,R2,R3 / C2,C4,C5. Input/State: EC-I01,I05,S02,S04. Output: EC-O02,O08,O09,O10. | Domain Testing | EC-I01,I05,S02,S04 | EC-O02,O08,O09,O10 | BVA chưa làm; n và chuyển trạng thái theo bước test | Chưa có |

## FR02-TC04 - Sai lần thứ ba kích hoạt khóa

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC04 | Sai lần thứ ba kích hoạt khóa | n=2 do hai lần sai liên tiếp; chưa khóa. | ghi n trước; submit A/W; ghi n sau và mốc khóa/trạng thái khóa. | n=3, request bị từ chối, khóa tạm 30 giây được kích hoạt (R2,R3). Test này chứng minh kích hoạt; không một mình chứng minh thời lượng chính xác. | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R1,R2,R3 / C2,C4,C5. Input/State: EC-I01,I05,S03,S04. Output: EC-O02,O08,O09,O11. | Domain Testing | EC-I01,I05,S03,S04 | EC-O02,O08,O09,O11 | BVA chưa làm; n và chuyển trạng thái theo bước test | Chưa có |

## FR02-TC05 - Đúng mật khẩu nhưng tài khoản còn khóa

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC05 | Đúng mật khẩu nhưng tài khoản còn khóa | thiết lập khóa có mốc quan sát được; không có request khác xen vào. | khoảng 10s sau mốc khóa, submit A với mật khẩu đúng; quan sát phản hồi. | từ chối, thông báo phù hợp tình huống khóa, không cấp phiên hợp lệ (R3,R4). Không assert đếm giữ nguyên hay gia hạn vì Q2. | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R3,R4 / C3,C6. Input/State: EC-I01,I04,S05. Output: EC-O04,O06,O08. | Domain Testing | EC-I01,I04,S05 | EC-O04,O06,O08 | 10s là đại diện đang khóa, chưa kiểm biên 30s | Chưa có |

## FR02-TC06 - Email hợp định dạng nhưng không tồn tại

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC06 | Email hợp định dạng nhưng không tồn tại | U không tồn tại, client sạch phiên. | submit U với chuỗi mật khẩu Test1234!; quan sát phản hồi. | từ chối, lỗi phù hợp, không cấp phiên hợp lệ (R1,R4). Không assert bộ đếm tài khoản không tồn tại. Mật khẩu không gán là sai thứ hai vì không có tài khoản để so khớp. | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R1,R4 / C2,C6. Input: EC-I02,I06. Output: EC-O02,O05,O08. | Domain Testing | EC-I02,I06 | EC-O02,O05,O08 | Chưa thiết kế BVA; không áp giới hạn độ dài tùy ý | Chưa có |

## FR02-TC07 - Validation HTML5 cho email sai định dạng

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC07 | Validation HTML5 cho email sai định dạng | mở form đăng nhập, không bypass validation; điền mật khẩu đúng của fixture, không để rỗng. | kiểm DOM field email phải có type=email; nhập abc; submit bằng thao tác người dùng; quan sát validity và network. | trình duyệt báo sai định dạng và form không gửi request đăng nhập qua submit thông thường (R7). Không yêu cầu validate HTML5 chặn request API gọi trực tiếp. | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R7 / C1. Input: EC-I03,I04. Output: EC-O03. | Domain Testing | EC-I03,I04 | EC-O03 | Chưa thiết kế BVA; không áp giới hạn độ dài tùy ý | Chưa có |

## FR02-TC08 - Đăng nhập sau khi hết thời gian khóa

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC08 | Đăng nhập sau khi hết thời gian khóa | A đã khóa, ghi mốc; không có request trong thời gian chờ làm thay đổi trạng thái. | đợi khoảng 35s tính từ mốc khóa đã xác nhận; submit A/mật khẩu đúng. | khóa tạm đã hết, thành công và cấp JWT (R1,R3,R5). Không assert n=0; chưa kiểm chính xác 30s và chưa kết luận lỗi thời lượng từ riêng test này. | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R1,R3,R5 / C2,C3,C7. Input/State: EC-I01,I04,S06. Output: EC-O01,O07,O12. | Domain Testing | EC-I01,I04,S06 | EC-O01,O07,O12 | 35s là đại diện sau hết khóa, chưa kiểm biên 30s | Chưa có |

## FR02-TC09 - Client lưu token sau thành công

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC09 | Client lưu token sau thành công | client sạch phiên, A chưa khóa. | đăng nhập đúng; quan sát cách client giữ token thực tế bằng công cụ phù hợp, đối chiếu token trả về với token được lưu. Che token trong evidence. | token được client lưu để dùng cho yêu cầu có xác thực (R6). Không tự yêu cầu tồn tại sau restart hoặc phải ở localStorage/cookie. | Người dùng cung cấp ảnh Local Storage và hai token đã đối chiếu khớp hoàn toàn. Ảnh chưa hiển thị origin; có key user tài khoản ketoan cũ nên cần xác nhận đúng localhost:5173 trước kết luận. | Not Run | Nguyễn Sơn Tùng (quan sát một phần) | 16/10/2026; chưa hoàn tất | R6 / C8. Input/State: EC-I01,I04,S04. Output: EC-O01,O13. Not Run trong thống kê nghĩa chưa có kết luận cuối; đã kiểm một phần, chờ xác nhận origin. Không tự gán Fail/Pass. | Domain Testing | EC-I01,I04,S04 | EC-O01,O13 | Chưa thiết kế BVA; không áp giới hạn độ dài tùy ý | Test_Execution.md mục TC09; ảnh trong hội thoại chưa lưu bản đã che token vào hồ sơ |

## FR02-TC10 - Gửi Bearer token trên request có xác thực

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC10 | Gửi Bearer token trên request có xác thực | đăng nhập thành công; khảo sát và lập danh mục request cần xác thực trong phạm vi client. | kích hoạt từng request trong danh mục; quan sát Authorization trên request thực tế, so token được lưu. Ghi endpoint/method và kết quả từng request. | mọi request thuộc danh mục cần xác thực có Authorization: Bearer <token> đúng token (R6). Chưa có inventory thì chỉ là test thiết kế một phần, không nhận bao phủ "tất cả". | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R6 / C8. Input/State: EC-I01,I04,S04. Output: EC-O01,O14. | Domain Testing | EC-I01,I04,S04 | EC-O01,O14 | Chưa thiết kế BVA; không áp giới hạn độ dài tùy ý | Chưa có |

## FR02-TC11 - Rà soát nội dung lỗi ở các tình huống đại diện

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark | Kỹ thuật | EC đầu vào và trạng thái | EC đầu ra | Giá trị biên | Bằng chứng |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR02-TC11 | Rà soát nội dung lỗi ở các tình huống đại diện | Dùng fixture/reset riêng của TC02/TC05/TC06 | dùng evidence riêng từng tình huống; rà thông báo/UI/response đối với yêu cầu không lộ chi tiết; ghi những nội dung quan sát được và tiêu chí áp dụng. Mỗi tình huống reset độc lập, không tạo một request có nhiều input sai. | lỗi phù hợp, không lộ chi tiết theo R4. Không tự đòi ba thông báo giống hệt. Kiểm không có mật khẩu/token/stack là kiểm tra tối thiểu bổ sung; tiêu chí đầy đủ chờ Q4. Chưa được kết luận Pass toàn bộ R4 khi oracle chưa đủ. | Chưa quan sát | Not Run | Chưa thực hiện | Chưa chạy | R4 / C6. Input/State và output của từng lần chạy dùng lại TC02/TC05/TC06: EC-I01,I02,I04,I05,I06,S01,S04,S05; output EC-O05,O06. Đây là test bổ sung đánh giá output, không thay thế test EC chính. | Domain Testing | Dùng EC của TC02/TC05/TC06; xem Remark | EC-O05,O06 | Chưa thiết kế BVA; không áp giới hạn độ dài tùy ý | Chưa có |

## Tổng kết thiết kế hiện tại

11 TC duy nhất: 1 đã có kết luận (TC01 Pass), 0 Fail, 10 chưa có kết luận (Not Run trong thống kê). Trong 10 case này, TC09 đã quan sát một phần và chờ xác nhận origin; 9 case khác chưa chạy. Executed dùng nghĩa đã hoàn tất đánh giá để không đếm TC09 là Pass hoặc Fail. Không coi số run bằng số TC. 6 EC Input, 6 EC State, 14 EC Output thuộc thiết kế; chưa xác nhận bao phủ thực thi toàn bộ. Xem Test_Execution.md. BVA chưa thực hiện.
