# Báo cáo HW02 Domain Testing trên EShop

Cập nhật 16/10/2026. Phạm vi đã chọn: A FR-02, B FR-09, C FR-15; Pool D chờ chốt. Hiện có thiết kế Domain Testing của FR-02 và kết quả TC01 Pass; BVA chưa thực hiện, nên chưa hoàn thành hai yêu cầu kỹ thuật của HW02. Nội dung AI còn chờ sinh viên rà soát đầy đủ.

## 1 Phạm vi kiểm thử

| Pool | Mã FR | Tên chức năng |
| --- | --- | --- |
| A | FR-02 | Đăng nhập và khóa tài khoản |
| B | FR-09 | Mã giảm giá |
| C | FR-15 | Quản lý sản phẩm |
| D | Chưa chọn | Chức năng Mobile |

## 2 Pool A FR02 Đăng nhập và khóa tài khoản

### 2.1 Yêu cầu làm cơ sở kiểm thử

- Nhập email và mật khẩu; thông tin đúng được đăng nhập khi tài khoản không khóa.
- Mỗi lần đăng nhập sai tăng bộ đếm đúng 1; sai từ 3 lần liên tiếp khóa 30 giây.
- Lỗi phải có thông báo phù hợp, không lộ chi tiết nguyên nhân.
- Thành công trả JWT; client lưu và đính kèm Authorization Bearer trên mọi request cần xác thực.
- Input email có type=email và validation HTML5.

### 2.2 Domain Testing Bước 1 Xác định Input và Output

| Chức năng | Đầu vào | Đầu ra |
| --- | --- | --- |
| FR-02 Đăng nhập và khóa tài khoản | Email; mật khẩu. | Kết quả đăng nhập; thông báo lỗi; JWT; bộ đếm và trạng thái khóa sau request; token được client lưu; header Authorization trên request cần xác thực. |

Ngữ cảnh trước request: số lần sai liên tiếp n, trạng thái khóa và thời gian từ lúc bắt đầu khóa. Các trạng thái này được xét khi phân lớp ở bước 2.

### 2.3 Domain Testing Bước 2 Xác định điều kiện và EC

Phân lớp theo điều kiện của Input, trạng thái tài khoản và hành vi Output. Email hợp định dạng được tách thành tồn tại/không tồn tại; n=1 và n=2 được tách vì lần sai tiếp theo dẫn đến chưa khóa hoặc kích hoạt khóa. Output được phân lớp theo kết quả mong đợi; thông báo lỗi trong test âm vẫn là đầu ra đúng. Dữ liệu đại diện và cách chọn test trình bày ở mục 2.4.

| ID | Đầu vào/đầu ra | Lớp tương đương |
| --- | --- | --- |
| EC1 | Email | Email hợp định dạng, tài khoản tồn tại |
| EC2 | Email | Email hợp định dạng, tài khoản không tồn tại |
| EC3 | Email | Email không rỗng, sai định dạng HTML5 |
| EC4 | Mật khẩu | Mật khẩu đúng của tài khoản tồn tại |
| EC5 | Mật khẩu | Mật khẩu sai của tài khoản tồn tại |
| EC6 | Mật khẩu | Mật khẩu chuỗi bất kỳ khi email không tồn tại |
| EC7 | Số lần sai trước request | n=0 trước request |
| EC8 | Số lần sai trước request | n=1 trước request sai |
| EC9 | Số lần sai trước request | n=2 trước request sai |
| EC10 | Trạng thái khóa trước request | Tài khoản chưa khóa |
| EC11 | Trạng thái và thời gian khóa trước request | Tài khoản đang trong thời hạn khóa |
| EC12 | Trạng thái và thời gian khóa trước request | Tài khoản đã hết thời hạn khóa |
| EC13 | Kết quả đăng nhập | Đăng nhập thành công khi thông tin đúng, chưa khóa |
| EC14 | Kết quả đăng nhập | Từ chối khi sai thông tin xác thực |
| EC15 | Kết quả đăng nhập | UI chặn submit email sai định dạng |
| EC16 | Kết quả đăng nhập | Từ chối khi tài khoản đang khóa |
| EC17 | Thông báo lỗi | Thông báo lỗi xác thực phù hợp, không lộ chi tiết |
| EC18 | Thông báo lỗi | Thông báo khóa phù hợp, không lộ chi tiết |
| EC19 | JWT trả về | Có JWT xác thực được khi đăng nhập thành công |
| EC20 | JWT trả về | Không cấp phiên/JWT xác thực được khi bị từ chối |
| EC21 | Bộ đếm sau request | n_after = n_before + 1 khi đăng nhập sai, tài khoản tồn tại chưa khóa |
| EC22 | Trạng thái khóa sau request | Chưa khóa sau lần sai thứ 1 hoặc 2 |
| EC23 | Trạng thái khóa sau request | Kích hoạt khóa 30 giây ở lần sai thứ 3 |
| EC24 | Trạng thái khóa sau request | Hết khóa sau thời hạn; đăng nhập đúng thành công |
| EC25 | Token được client lưu | Client lưu đúng token sau đăng nhập thành công |
| EC26 | Header request cần xác thực | Request cần xác thực gửi Authorization: Bearer <token> đúng token |

### 2.4 Domain Testing Bước 3 Chọn đại diện và xây dựng test case

Chọn một bộ dữ liệu và đầu ra mong đợi cho từng EC, sau đó gộp các dòng có cùng dữ liệu, ngữ cảnh và kết quả. Kết hợp các EC hợp lệ khi phù hợp; mỗi tình huống âm chỉ vi phạm một điều kiện đầu vào.

#### 2.4.1 Các ca kiểm thử bao phủ từng phân vùng

| Phân vùng | Điều kiện kiểm tra | Đầu vào | Đầu ra mong đợi |
| --- | --- | --- | --- |
| EC1 | Email hợp định dạng, tài khoản tồn tại | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Chưa khóa; n=0; client chưa có phiên. Đăng nhập, kiểm JWT, nơi lưu token và request cần xác thực. | Đăng nhập thành công; JWT xác thực được; client lưu đúng token và gửi Authorization: Bearer <token> đúng token trên request cần xác thực. |
| EC2 | Email hợp định dạng, tài khoản không tồn tại | Email: "hw02-absent@example.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Xác nhận email không tồn tại; client chưa có phiên; gửi đăng nhập. | Từ chối; không cấp phiên hợp lệ; lỗi xác thực phù hợp, không lộ chi tiết. Không kết luận bộ đếm của tài khoản không tồn tại. |
| EC3 | Email không rỗng, sai định dạng HTML5 | Email: "abc"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Mở form; mật khẩu không rỗng; submit qua UI. | HTML5 chặn email sai định dạng; không gửi request đăng nhập. |
| EC4 | Mật khẩu đúng của tài khoản tồn tại | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Chưa khóa; n=0; client chưa có phiên. Đăng nhập, kiểm JWT, nơi lưu token và request cần xác thực. | Đăng nhập thành công; JWT xác thực được; client lưu đúng token và gửi Authorization: Bearer <token> đúng token trên request cần xác thực. |
| EC5 | Mật khẩu sai của tài khoản tồn tại | Email: "test@eshop.com"<br>Mật khẩu: "WrongPass9!"<br>Trạng thái ban đầu: Chưa khóa; n=0; gửi một lần đăng nhập sai. | Từ chối; không cấp phiên hợp lệ; n=1; chưa khóa; lỗi xác thực phù hợp, không lộ chi tiết. |
| EC6 | Mật khẩu chuỗi bất kỳ khi email không tồn tại | Email: "hw02-absent@example.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Xác nhận email không tồn tại; client chưa có phiên; gửi đăng nhập. | Từ chối; không cấp phiên hợp lệ; lỗi xác thực phù hợp, không lộ chi tiết. Không kết luận bộ đếm của tài khoản không tồn tại. |
| EC7 | n=0 trước request | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Chưa khóa; n=0; client chưa có phiên. Đăng nhập, kiểm JWT, nơi lưu token và request cần xác thực. | Đăng nhập thành công; JWT xác thực được; client lưu đúng token và gửi Authorization: Bearer <token> đúng token trên request cần xác thực. |
| EC8 | n=1 trước request sai | Email: "test@eshop.com"<br>Mật khẩu: "WrongPass9!"<br>Trạng thái ban đầu: Chưa khóa; n=1; gửi một lần đăng nhập sai. | Từ chối; không cấp phiên hợp lệ; n=2; chưa khóa. |
| EC9 | n=2 trước request sai | Email: "test@eshop.com"<br>Mật khẩu: "WrongPass9!"<br>Trạng thái ban đầu: Chưa khóa; n=2; gửi một lần đăng nhập sai. | Từ chối; n=3; kích hoạt khóa 30 giây; không cấp phiên hợp lệ. |
| EC10 | Tài khoản chưa khóa | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Chưa khóa; n=0; client chưa có phiên. Đăng nhập, kiểm JWT, nơi lưu token và request cần xác thực. | Đăng nhập thành công; JWT xác thực được; client lưu đúng token và gửi Authorization: Bearer <token> đúng token trên request cần xác thực. |
| EC11 | Tài khoản đang trong thời hạn khóa | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Tạo khóa mới; thử đăng nhập đúng sau khoảng 10 giây. | Vẫn từ chối; không cấp phiên hợp lệ; thông báo khóa phù hợp, không lộ chi tiết. |
| EC12 | Tài khoản đã hết thời hạn khóa | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Tạo khóa mới; không có request xen giữa; thử đăng nhập sau khoảng 35 giây. | Hết khóa; đăng nhập thành công và trả JWT. Không kết luận bộ đếm được reset; chưa kiểm đúng biên 30 giây. |
| EC13 | Đăng nhập thành công khi thông tin đúng, chưa khóa | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Chưa khóa; n=0; client chưa có phiên. Đăng nhập, kiểm JWT, nơi lưu token và request cần xác thực. | Đăng nhập thành công; JWT xác thực được; client lưu đúng token và gửi Authorization: Bearer <token> đúng token trên request cần xác thực. |
| EC14 | Từ chối khi sai thông tin xác thực | Email: "test@eshop.com"<br>Mật khẩu: "WrongPass9!"<br>Trạng thái ban đầu: Chưa khóa; n=0; gửi một lần đăng nhập sai. | Từ chối; không cấp phiên hợp lệ; n=1; chưa khóa; lỗi xác thực phù hợp, không lộ chi tiết. |
| EC15 | UI chặn submit email sai định dạng | Email: "abc"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Mở form; mật khẩu không rỗng; submit qua UI. | HTML5 chặn email sai định dạng; không gửi request đăng nhập. |
| EC16 | Từ chối khi tài khoản đang khóa | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Tạo khóa mới; thử đăng nhập đúng sau khoảng 10 giây. | Vẫn từ chối; không cấp phiên hợp lệ; thông báo khóa phù hợp, không lộ chi tiết. |
| EC17 | Thông báo lỗi xác thực phù hợp, không lộ chi tiết | Email: "test@eshop.com"<br>Mật khẩu: "WrongPass9!"<br>Trạng thái ban đầu: Chưa khóa; n=0; gửi một lần đăng nhập sai. | Từ chối; không cấp phiên hợp lệ; n=1; chưa khóa; lỗi xác thực phù hợp, không lộ chi tiết. |
| EC18 | Thông báo khóa phù hợp, không lộ chi tiết | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Tạo khóa mới; thử đăng nhập đúng sau khoảng 10 giây. | Vẫn từ chối; không cấp phiên hợp lệ; thông báo khóa phù hợp, không lộ chi tiết. |
| EC19 | Có JWT xác thực được khi đăng nhập thành công | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Chưa khóa; n=0; client chưa có phiên. Đăng nhập, kiểm JWT, nơi lưu token và request cần xác thực. | Đăng nhập thành công; JWT xác thực được; client lưu đúng token và gửi Authorization: Bearer <token> đúng token trên request cần xác thực. |
| EC20 | Không cấp phiên/JWT xác thực được khi bị từ chối | Email: "test@eshop.com"<br>Mật khẩu: "WrongPass9!"<br>Trạng thái ban đầu: Chưa khóa; n=0; gửi một lần đăng nhập sai. | Từ chối; không cấp phiên hợp lệ; n=1; chưa khóa; lỗi xác thực phù hợp, không lộ chi tiết. |
| EC21 | n_after = n_before + 1 khi đăng nhập sai, tài khoản tồn tại chưa khóa | Email: "test@eshop.com"<br>Mật khẩu: "WrongPass9!"<br>Trạng thái ban đầu: Chưa khóa; n=0; gửi một lần đăng nhập sai. | Từ chối; không cấp phiên hợp lệ; n=1; chưa khóa; lỗi xác thực phù hợp, không lộ chi tiết. |
| EC22 | Chưa khóa sau lần sai thứ 1 hoặc 2 | Email: "test@eshop.com"<br>Mật khẩu: "WrongPass9!"<br>Trạng thái ban đầu: Chưa khóa; n=0; gửi một lần đăng nhập sai. | Từ chối; không cấp phiên hợp lệ; n=1; chưa khóa; lỗi xác thực phù hợp, không lộ chi tiết. |
| EC23 | Kích hoạt khóa 30 giây ở lần sai thứ 3 | Email: "test@eshop.com"<br>Mật khẩu: "WrongPass9!"<br>Trạng thái ban đầu: Chưa khóa; n=2; gửi một lần đăng nhập sai. | Từ chối; n=3; kích hoạt khóa 30 giây; không cấp phiên hợp lệ. |
| EC24 | Hết khóa sau thời hạn; đăng nhập đúng thành công | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Tạo khóa mới; không có request xen giữa; thử đăng nhập sau khoảng 35 giây. | Hết khóa; đăng nhập thành công và trả JWT. Không kết luận bộ đếm được reset; chưa kiểm đúng biên 30 giây. |
| EC25 | Client lưu đúng token sau đăng nhập thành công | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Chưa khóa; n=0; client chưa có phiên. Đăng nhập, kiểm JWT, nơi lưu token và request cần xác thực. | Đăng nhập thành công; JWT xác thực được; client lưu đúng token và gửi Authorization: Bearer <token> đúng token trên request cần xác thực. |
| EC26 | Request cần xác thực gửi Authorization: Bearer <token> đúng token | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Chưa khóa; n=0; client chưa có phiên. Đăng nhập, kiểm JWT, nơi lưu token và request cần xác thực. | Đăng nhập thành công; JWT xác thực được; client lưu đúng token và gửi Authorization: Bearer <token> đúng token trên request cần xác thực. |

#### 2.4.2 Tập ca kiểm thử rút gọn

| Test case | Điều kiện kiểm tra | Đầu vào | Đầu ra mong đợi |
| --- | --- | --- | --- |
| TC01 | EC1: Email hợp định dạng, tài khoản tồn tại; EC4: Mật khẩu đúng của tài khoản tồn tại; EC7: n=0 trước request; EC10: Tài khoản chưa khóa; EC13: Đăng nhập thành công khi thông tin đúng, chưa khóa; EC19: Có JWT xác thực được khi đăng nhập thành công; EC25: Client lưu đúng token sau đăng nhập thành công; EC26: Request cần xác thực gửi Authorization: Bearer <token> đúng token | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Tài khoản chưa khóa; chưa có lần sai; client chưa có phiên. | Đăng nhập thành công; JWT xác thực được; client lưu đúng token và gửi Authorization: Bearer <token> đúng token trên request cần xác thực. |
| TC02 | EC1: Email hợp định dạng, tài khoản tồn tại; EC5: Mật khẩu sai của tài khoản tồn tại; EC7: n=0 trước request; EC10: Tài khoản chưa khóa; EC14: Từ chối khi sai thông tin xác thực; EC17: Thông báo lỗi xác thực phù hợp, không lộ chi tiết; EC20: Không cấp phiên/JWT xác thực được khi bị từ chối; EC21: n_after = n_before + 1 khi đăng nhập sai, tài khoản tồn tại chưa khóa; EC22: Chưa khóa sau lần sai thứ 1 hoặc 2 | Email: "test@eshop.com"<br>Mật khẩu: "WrongPass9!"<br>Trạng thái ban đầu: Tài khoản chưa khóa; chưa có lần sai. | Từ chối; không cấp phiên hợp lệ; n=1; chưa khóa; lỗi xác thực phù hợp, không lộ chi tiết. |
| TC03 | EC1: Email hợp định dạng, tài khoản tồn tại; EC5: Mật khẩu sai của tài khoản tồn tại; EC8: n=1 trước request sai; EC10: Tài khoản chưa khóa; EC14: Từ chối khi sai thông tin xác thực; EC20: Không cấp phiên/JWT xác thực được khi bị từ chối; EC21: n_after = n_before + 1 khi đăng nhập sai, tài khoản tồn tại chưa khóa; EC22: Chưa khóa sau lần sai thứ 1 hoặc 2 | Email: "test@eshop.com"<br>Mật khẩu: "WrongPass9!"<br>Trạng thái ban đầu: Tài khoản chưa khóa; đã sai 1 lần liên tiếp. | Từ chối; không cấp phiên hợp lệ; n=2; chưa khóa. |
| TC04 | EC1: Email hợp định dạng, tài khoản tồn tại; EC5: Mật khẩu sai của tài khoản tồn tại; EC9: n=2 trước request sai; EC10: Tài khoản chưa khóa; EC14: Từ chối khi sai thông tin xác thực; EC20: Không cấp phiên/JWT xác thực được khi bị từ chối; EC21: n_after = n_before + 1 khi đăng nhập sai, tài khoản tồn tại chưa khóa; EC23: Kích hoạt khóa 30 giây ở lần sai thứ 3 | Email: "test@eshop.com"<br>Mật khẩu: "WrongPass9!"<br>Trạng thái ban đầu: Tài khoản chưa khóa; đã sai 2 lần liên tiếp. | Từ chối; n=3; kích hoạt khóa 30 giây; không cấp phiên hợp lệ. |
| TC05 | EC1: Email hợp định dạng, tài khoản tồn tại; EC4: Mật khẩu đúng của tài khoản tồn tại; EC11: Tài khoản đang trong thời hạn khóa; EC16: Từ chối khi tài khoản đang khóa; EC18: Thông báo khóa phù hợp, không lộ chi tiết; EC20: Không cấp phiên/JWT xác thực được khi bị từ chối | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Tài khoản đang khóa; thử đăng nhập sau khoảng 10 giây từ lúc khóa. | Vẫn từ chối; không cấp phiên hợp lệ; thông báo khóa phù hợp, không lộ chi tiết. |
| TC06 | EC2: Email hợp định dạng, tài khoản không tồn tại; EC6: Mật khẩu chuỗi bất kỳ khi email không tồn tại; EC14: Từ chối khi sai thông tin xác thực; EC17: Thông báo lỗi xác thực phù hợp, không lộ chi tiết; EC20: Không cấp phiên/JWT xác thực được khi bị từ chối | Email: "hw02-absent@example.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Email đã được xác nhận không tồn tại; client chưa có phiên. | Từ chối; không cấp phiên hợp lệ; lỗi xác thực phù hợp, không lộ chi tiết. Không kết luận bộ đếm của tài khoản không tồn tại. |
| TC07 | EC3: Email không rỗng, sai định dạng HTML5; EC15: UI chặn submit email sai định dạng | Email: "abc"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Mở form đăng nhập; submit qua UI. | HTML5 chặn email sai định dạng; không gửi request đăng nhập. |
| TC08 | EC1: Email hợp định dạng, tài khoản tồn tại; EC4: Mật khẩu đúng của tài khoản tồn tại; EC12: Tài khoản đã hết thời hạn khóa; EC13: Đăng nhập thành công khi thông tin đúng, chưa khóa; EC19: Có JWT xác thực được khi đăng nhập thành công; EC24: Hết khóa sau thời hạn; đăng nhập đúng thành công | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Tạo khóa mới; không gửi yêu cầu xen giữa; thử đăng nhập sau khoảng 35 giây từ lúc khóa. | Hết khóa; đăng nhập thành công và trả JWT. Không kết luận bộ đếm được reset; chưa kiểm đúng biên 30 giây. |

26 dòng theo EC được gộp thành 8 tình huống TC01–TC08, bao phủ đủ EC1–EC26. TC01 kết hợp kiểm tra đăng nhập, JWT, lưu và gửi token; kiểm tra thông báo lỗi được ghép vào TC02, TC05 và TC06. Đây là bộ thiết kế rút gọn cho các EC đã xác định, chưa phải kết quả thực thi hoặc khẳng định tối thiểu tuyệt đối. Bảng TC01–TC11 và kết quả đã ghi được giữ tại mục 2.6; kết quả Pass cũ không xác nhận toàn bộ TC01 mở rộng. Dữ liệu tài khoản cần xác nhận trước khi chạy; tiêu chí chi tiết của thông báo lỗi còn cần làm rõ.

### 2.5 Boundary Value Analysis

Theo S04 trang 26–27, chọn điểm tại biên và hai phía của biên, giữ các đầu vào còn lại phù hợp. FR-02 có ngưỡng khóa ở lần đăng nhập sai thứ 3 và thời hạn khóa 30 giây (README, mục FR-02).

- Số lần sai: chọn lần sai thứ 2 (dưới ngưỡng), lần sai thứ 3 (tại ngưỡng) và lần gửi sai thứ 4 khi tài khoản còn khóa (sau ngưỡng). TC03–TC04 dùng chung với bảng Domain Testing ở mục 2.4.2; không cộng lại thành test mới.

- Thời gian khóa: gọi t là thời gian tính từ lúc khóa được kích hoạt; chọn t = 0, 1, 29, 30, 31 giây. Bước 1 giây là khoảng cách chọn điểm trong bản thiết kế, không phải khẳng định độ chính xác của hệ thống. Mỗi test thời gian bắt đầu bằng một lần khóa mới; dùng đồng hồ kiểm soát được để thử đúng mốc.

- Không tự đặt biên độ dài email/mật khẩu khi đặc tả không có. Bộ đếm và thời gian không nhập trực tiếp qua UI; giá trị âm và cực trị UI không áp dụng cho các biến trạng thái này.

| Test case | Điều kiện kiểm tra | Đầu vào | Đầu ra mong đợi |
| --- | --- | --- | --- |
| TC03 | Lần sai thứ 2: ngay dưới ngưỡng 3 lần. | Email: "test@eshop.com"<br>Mật khẩu: "WrongPass9!"<br>Trạng thái ban đầu: Tài khoản chưa khóa; đã sai 1 lần liên tiếp. Gửi thêm một lần đăng nhập. | Từ chối; bộ đếm từ 1 tăng thành 2; chưa khóa; không cấp phiên hợp lệ. |
| TC04 | Lần sai thứ 3: tại ngưỡng kích hoạt khóa. | Email: "test@eshop.com"<br>Mật khẩu: "WrongPass9!"<br>Trạng thái ban đầu: Tài khoản chưa khóa; đã sai 2 lần liên tiếp. Gửi thêm một lần đăng nhập. | Từ chối; bộ đếm từ 2 tăng thành 3; kích hoạt khóa 30 giây; không cấp phiên hợp lệ. |
| TC09 | Lần gửi sai thứ 4: ngay sau lần kích hoạt khóa, trong thời hạn khóa. | Email: "test@eshop.com"<br>Mật khẩu: "WrongPass9!"<br>Trạng thái ban đầu: Tạo 3 lần sai liên tiếp để khóa tài khoản; gửi lần thứ 4 trước khi hết 30 giây. | Tiếp tục bị từ chối; không cấp phiên hợp lệ. Không kết luận bộ đếm tăng thành 4 hoặc khóa được gia hạn vì đặc tả chưa quy định. |
| TC10 | t = 0 giây: tại mốc bắt đầu khóa. | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Tạo khóa mới; giữ đồng hồ tại thời điểm khóa vừa kích hoạt; thử đăng nhập đúng. | Tài khoản đang khóa; từ chối đăng nhập; không cấp phiên hợp lệ. |
| TC11 | t = 1 giây: ngay sau mốc bắt đầu khóa theo bước chọn 1 giây. | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Tạo khóa mới; thử đăng nhập đúng tại t = 1 giây. | Tài khoản còn khóa; từ chối đăng nhập; không cấp phiên hợp lệ. |
| TC12 | t = 29 giây: ngay trước thời hạn 30 giây theo bước chọn 1 giây. | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Tạo khóa mới; thử đăng nhập đúng tại t = 29 giây. | Tài khoản còn khóa; từ chối đăng nhập; không cấp phiên hợp lệ. |
| TC13 | t = 30 giây: tại đúng thời hạn khóa. | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Tạo khóa mới; dùng đồng hồ kiểm soát được để thử đăng nhập đúng tại t = 30 giây. | Cần xác nhận quy ước xử lý đúng mốc hết hạn (t ≥ 30 hay t > 30) và độ chính xác thời gian trước khi chốt expected; chưa kết luận Pass/Fail. |
| TC14 | t = 31 giây: ngay sau thời hạn 30 giây theo bước chọn 1 giây. | Email: "test@eshop.com"<br>Mật khẩu: "Test1234!"<br>Trạng thái ban đầu: Tạo khóa mới; không có yêu cầu xen giữa; thử đăng nhập đúng tại t = 31 giây. | Khóa đã hết hiệu lực; đăng nhập thành công và trả JWT. Không kết luận bộ đếm được reset. |

Các dòng trên là thiết kế, chưa phải kết quả chạy. Đo t tại thời điểm hệ thống xử lý yêu cầu; đợi bằng đồng hồ bấm tay không chứng minh đã kiểm đúng t = 30 giây. Mốc đúng hạn ở TC13 còn chờ xác nhận, theo điểm chưa rõ về đồng hồ trong phân tích FR-02.


### 2.6 AI gap analysis

- Thiếu sót của AI: đưa TC02 (lần đăng nhập sai thứ 1) vào bảng BVA kiểm tra ngưỡng khóa 3 lần, dù đây không phải điểm sát ngưỡng đang xét.

- Nguyên nhân: AI gộp kiểm tra trạng thái ban đầu và quy tắc tăng bộ đếm vào phần kiểm thử biên mà chưa phân biệt rõ mục tiêu của từng test.

- Sinh viên phát hiện khi đối chiếu S04: với ngưỡng 3 lần, các điểm cần xét là lần sai thứ 2, lần sai thứ 3 và lần gửi sai thứ 4 khi tài khoản còn khóa.

- Hiệu chỉnh: bỏ TC02 khỏi mục 2.5, giữ trong Domain Testing; phần ngưỡng số lần ở BVA giữ TC03, TC04 và TC09. Lần gửi thứ 4 không đồng nghĩa bộ đếm tăng thành 4. Đây là test thừa so với phạm vi biên đang xét, không phải bug của hệ thống.

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
