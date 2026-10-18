# FR02 Test case Domain Testing

Cập nhật 16/10/2026. Bảng dùng đúng 10 thuộc tính của Test cases_Template_En.xlsx. EC, kỹ thuật và giải thích lựa chọn được trình bày trong Domain_Testing.md, không lặp thành cột hay bảng riêng cho từng test.

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

## Kết quả và bằng chứng

11 test: 1 Pass (TC01), 0 Fail, 10 chưa có kết luận cuối. Trong 10 case này, TC09 đã kiểm một phần và chờ origin; 9 case khác chưa chạy. Executed trong thống kê là số test đã hoàn tất đánh giá. Không coi TC09 đã Pass hoặc đã kiểm xong.

E01: evidence/FR02-TC01-RUN01/User_Provided_Result.md, chép kết quả người dùng gửi; chưa có ảnh terminal gốc đã che token trong thư mục nộp. Chi tiết run và TC09 tại Test_Execution.md. Chưa BVA.
