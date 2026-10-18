# Jest — HW02 EShop

Script theo ba FR; 68 mã TC lấy từ `Main_Report.docx` hiện tại được lưu trong `catalog.json`. `specs/fr-02.test.cjs`, `fr-09.test.cjs`, `fr-15.test.cjs` dùng Jest và Playwright thật. Không sửa logic SUT để làm test pass.

## Chạy

Node 24; cài các dependency trong package.json và `sqlite3`, rồi cài Chromium bằng `npx playwright install chromium`. Trong workspace hiện tại, runner tái sử dụng Jest/sqlite3 từ `eshop-sut/testing` và Playwright từ runtime Codex. Có thể đặt `HW02_SUT`, `HW02_NODE_MODULES`, `HW02_CHROMIUM` nếu đường dẫn khác.

```powershell
npm test -- --fr FR-02 --demo
npm test -- --fr FR-02
npm test -- --fr FR-09
npm test -- --fr FR-15
```

Chế độ demo FR-02 chạy TC01, TC02, TC03, TC04, TC07, TC14, cửa sổ Chromium hiển thị và Playwright ghi video WebM. Mỗi run lưu environment, actual, từng assertion, ảnh, kết quả Jest và video tại `runs/<Run-ID>/`. Thanh dưới cùng trong video là **test harness**, hiển thị expected/actual thu được từ request và CSDL; không phải giao diện gốc của EShop. Không lưu JWT hoặc response chứa mật khẩu.

Backend được sao chép nguyên mã nguồn vào `HW02/runtime/jest-sut/<Run-ID>/`, dùng DB riêng. Không reset backend giữa các TC; chỉ thiết lập trạng thái test độc lập qua SQLite. Hash CSDL SUT gốc được đối chiếu trước/sau. Port 3000/5173 phải trống; FR-15 dùng thêm 5174. Server được tắt khi run kết thúc.

FR-02 TC13 giữ Not Run vì expected tại đúng 30 giây chưa được xác nhận. Các điểm thời gian khác ghi khoảng thời gian thực đo được; không khẳng định đã trúng đúng mili giây bằng đồng hồ hệ điều hành. TC14 chờ ít nhất 31 giây thật kể từ khi khóa mới được quan sát. FR-09 có preload đồng hồ kiểm soát riêng cho so sánh `expired_at`; preload không đổi thời gian khi không có giá trị kiểm soát.

FR-09 dùng API và sản phẩm có giá được lưu để chuẩn bị tổng giỏ. FR-15 dùng API cho dữ liệu biên/thiếu/sai kiểu; riêng TC03 đi qua giao diện admin và quan sát cả ngay sau lưu lẫn sau reload. Không coi kiểm API là đã kiểm UI. Các script FR-09/FR-15 chưa được thực thi ở giai đoạn quay video đầu tiên.

Sau video FR-02 phải dừng để sinh viên xem và đồng ý trước hai video tiếp theo. Video này minh họa chạy TC; chưa phải video dùng skill từ đầu đến cuối.

## Nhịp video để người xem theo dõi

Yêu cầu cuối của người dùng: đọc mục tiêu 4 giây; nhập từng ô và dừng 1,5 giây sau mỗi ô; dừng 2 giây trước khi gửi; giữ kết quả 3,5 giây. Không dừng riêng ở tiền điều kiện. Chú thích tiếng Việt. Timestamps lấy lúc request thật được gửi; thời gian gõ không được tính vào phép đo khóa. Ở TC14, nhập sẵn dữ liệu và dành 2 giây cuối của thời gian chờ làm khoảng dừng trước khi gửi quanh mốc 31 giây thật.
