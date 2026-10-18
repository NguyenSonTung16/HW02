Mình sẽ tìm README của source eShop và đọc phần tính năng mobile.


Theo [README của eShop — mục 7, FR-20](<D:/vscode/Software testing/eshop-sut/README.md:231>), ứng dụng **Mobile dùng React Native + Expo**, gồm các tính năng:

- **Xem sản phẩm**.
- **Đăng ký, đăng nhập, đăng xuất**.
- **Giỏ hàng**.
- **Thanh toán**.
- **Hồ sơ cá nhân**.
- **Lịch sử đơn hàng**.
- **Hủy đơn hàng**: chỉ được hủy khi trạng thái là `pending` (chờ xác nhận) hoặc `confirmed` (đã xác nhận). Không được hủy khi đang giao, đã giao hoặc đã hủy.

README là **đặc tả yêu cầu để kiểm thử**; danh sách này mô tả chức năng mobile phải có, chưa xác nhận source đã triển khai đúng và đầy đủ.