Trong ảnh, **bạn đang lọc sai**, chưa phải bằng chứng API không trả response. Network hiển thị **0/13 requests**, còn giao diện đã hiện **“Chào, Test User”**.

Làm như sau:

1. Xóa `POST /api/login` trong ô Filter, thay bằng **`login`**. Nếu request còn được lưu, nó sẽ xuất hiện.
2. Tích **Keep log** để giữ request khi chuyển trang.
3. Nếu vẫn không có: bấm **Thoát**, quay lại đăng nhập rồi thực hiện lại một lần khi Network đang mở.
4. Chọn dòng **login** có phương thức **POST**; nếu có dòng `OPTIONS` thì đó là request kiểm tra trước, không phải request đăng nhập chính.
5. Trong khung chi tiết, chọn **Response** hoặc **Preview** để xem dữ liệu trả về. Tab **Headers** cho biết URL, phương thức và mã trạng thái; **Payload** là dữ liệu bạn gửi.

**Ô Filter chỉ cần nhập `login`, không nhập cả `POST /api/login`.** Khi chụp bằng chứng, che giá trị token.

Đã ghi audit