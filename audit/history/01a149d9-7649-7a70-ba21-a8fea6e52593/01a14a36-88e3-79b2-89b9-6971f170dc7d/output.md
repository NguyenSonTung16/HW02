Các dòng **EC7–EC12 là lớp trạng thái trước khi gửi yêu cầu đăng nhập**, chưa phải test case. `n` là số lần đăng nhập sai liên tiếp đã xảy ra.

| EC | Ý nghĩa | Ví dụ kiểm thử |
|---|---|---|
| **EC7: n = 0** | Chưa có lần đăng nhập sai nào trong chuỗi hiện tại. | Gửi mật khẩu sai → bộ đếm thành 1, chưa khóa. |
| **EC8: n = 1** | Đã sai 1 lần liên tiếp. | Gửi sai thêm lần nữa → bộ đếm thành 2, chưa khóa. |
| **EC9: n = 2** | Đã sai 2 lần liên tiếp. | Gửi sai thêm lần nữa → đạt 3 lần, kích hoạt khóa 30 giây. |
| **EC10: Chưa khóa** | Tài khoản được phép xét email và mật khẩu. | Thông tin đúng → đăng nhập thành công; sai → bị từ chối. |
| **EC11: Đang trong thời hạn khóa** | Khóa đã được kích hoạt và chưa hết hạn. | Dùng mật khẩu đúng vẫn bị từ chối. |
| **EC12: Đã hết thời hạn khóa** | Thời hạn khóa 30 giây đã qua. | Dùng thông tin đúng → đăng nhập thành công. |

**Hai nhóm xét hai khía cạnh khác nhau:** EC7–EC9 xét **bộ đếm**, EC10–EC12 xét **tình trạng khóa**. Một test có thể kết hợp chúng, ví dụ **EC9 + EC10**: tài khoản chưa khóa, đã sai 2 lần; lần sai tiếp theo phải kích hoạt khóa.

Riêng EC12 chỉ nói **hết khóa**, chưa đủ để kết luận bộ đếm tự trở về 0 nếu đặc tả chưa quy định.