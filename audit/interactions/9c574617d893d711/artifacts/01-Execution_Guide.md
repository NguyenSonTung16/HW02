# Hướng dẫn thực thi 11 test case FR02

Ngày 16/10/2026. Dùng skill test-execution-reporting. Đây là hướng dẫn, chưa chạy SUT, không đổi trạng thái Not Run của test case và không xác nhận bug.

## 1. Chạy môi trường một lần

Terminal backend:

```powershell
cd 'D:\vscode\Software testing\eshop-sut\backend'
npm install
node server.js
```

Terminal web:

```powershell
cd 'D:\vscode\Software testing\eshop-sut\frontend-web'
npm install
npm run dev
```

Nếu dependencies đã cài thì không cần npm install lại. Mở URL Vite in ra, mặc định http://localhost:5173/login. Backend mặc định http://localhost:3000. FR-02 không cần chạy admin/mobile. Ghi phiên bản source, các thay đổi chưa commit và URL thật vào hồ sơ môi trường.

Lưu ý có căn cứ từ source: database.js gọi initDatabase() khi được import và DROP TABLE/seed lại. Vì vậy khởi động backend này làm mất dữ liệu đang có trong database.sqlite; nếu cần giữ dữ liệu, sao lưu trước khi khởi động. Không restart backend, chạy node database.js hoặc node --watch trong chuỗi test. Hướng dẫn này không tự chạy các lệnh đó.

## 2. Chuẩn bị quan sát

- Mở DevTools bằng F12, tab Network, bật Preserve log, lọc login. Xóa danh sách network cũ trước hành động được đo để không nhầm request.
- Dùng tab Application để quan sát Local Storage của origin web. Source hiện lưu token bằng key token; đó là vị trí quan sát thực tế, không phải thêm yêu cầu phải dùng localStorage.
- Khi cần client sạch, logout rồi xóa riêng key token trên origin test và reload. Nếu user context còn trong bộ nhớ, reload; không xóa dữ liệu site khác. Dùng tab/profile sạch để tránh token cũ gây false pass.
- Dùng tài khoản demo test@eshop.com / Test1234!, mật khẩu sai WrongPass9!. Kiểm tra fixture hiện tại trước khi dùng, không lấy mật khẩu thật từ tài khoản cá nhân.
- Không công bố JWT đầy đủ hoặc mật khẩu cá nhân trong screenshot/log. Ghi việc so token là khớp/không khớp; che giá trị trong evidence.

## 3. Đọc và thiết lập trạng thái trước test

Helper tools/auth_fixture.py đọc mặc định; chỉ thay trạng thái khi thêm --set-attempts. Đường dẫn DB mặc định: eshop-sut/backend/database.sqlite. Không import database.js để đọc DB vì sẽ kích hoạt reset toàn bộ.

Đọc trạng thái:

```powershell
& 'C:\Users\tung1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'D:\vscode\Software testing\HW02\FR-02\tools\auth_fixture.py'
```

Thiết lập n=0, chưa khóa trên DB demo local:

```powershell
& 'C:\Users\tung1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'D:\vscode\Software testing\HW02\FR-02\tools\auth_fixture.py' --set-attempts 0
```

Thay 0 bằng 1 hoặc 2 để chuẩn bị TC03/TC04. Helper sao lưu DB trước khi sửa, chỉ cập nhật login_attempts và locked_until của đúng một tài khoản. Nếu không có hoặc trùng email, không sửa. Không thay mật khẩu, không sửa logic SUT. Đợi request cũ hoàn tất trước khi đọc/reset; không có người dùng hoặc tiến trình khác thao tác cùng fixture.

Đọc xem email U có tồn tại:

```powershell
& 'C:\Users\tung1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'D:\vscode\Software testing\HW02\FR-02\tools\auth_fixture.py' --email hw02-absent@example.com
```

matches=0 mới là fixture U phù hợp. Nếu có, chọn email hợp lệ khác và ghi dữ liệu thực tế.

Có hai kiểu chạy:

- Chuỗi end-to-end: n=0 → sai lần 1 → sai lần 2 → sai lần 3; ghi số đếm thực tế mỗi lần. Không thay số đo thành số mong đợi. Nếu sai lệch làm chuỗi tiếp theo không đạt tiền điều kiện, dừng, ghi trở ngại.
- Case cô lập: dùng helper đặt n=1 hoặc n=2 để kiểm tra riêng logic từ trạng thái đó. Ghi rõ test dùng fixture được thiết lập trực tiếp, không coi đây là bằng chứng hai lần sai thật đã tạo n=2. Với TC04 vẫn cần phép thử chuỗi riêng để chứng minh chữ “liên tiếp”.

## 4. Thực thi từng case

### TC01 Đăng nhập thành công

1. Đặt n=0, chưa khóa, client sạch; ghi trạng thái trước.
2. Đăng nhập đúng A trên web. Xem POST /api/login trong Network, ghi kết quả và có/không có token.
3. Để kiểm token được backend chấp nhận, thực hiện request GET /api/users/me với Authorization: Bearer <token> bằng request thử riêng hoặc luồng client tương ứng. Không chỉ decode JWT rồi kết luận hợp lệ.
4. Expected: đăng nhập thành công, có JWT backend chấp nhận. Ghi riêng assertion token và kết quả UI. Không công bố response users/me nguyên bản nếu chứa dữ liệu nhạy cảm.

### TC02 Sai mật khẩu từ n=0

1. Đặt n=0 và chưa khóa; chụp/log trạng thái trước.
2. Submit A/W đúng một lần; không double click.
3. Đợi request hoàn tất rồi đọc DB. Expected: từ chối, không cấp phiên mới, n=1, chưa khóa.
4. Nếu số thực tế là 2, ghi actual=2, fail assertion tăng đúng 1; không sửa số để test pass.

### TC03 Sai mật khẩu từ n=1

1. Nếu TC02 thực sự tạo n=1, có thể tiếp tục, không thành công xen giữa. Nếu không, chuẩn bị n=1 bằng helper và ghi rõ là chạy cô lập.
2. Submit A/W một lần; đọc DB sau khi request hoàn tất.
3. Expected: n=2, từ chối, chưa khóa. Không reset giữa thời điểm đọc trước và sau.

### TC04 Sai lần thứ ba kích hoạt khóa

1. Đạt n=2 bằng chuỗi thực nếu được; nếu không, đặt fixture n=2 để kiểm chuyển trạng thái riêng.
2. Submit A/W một lần; đọc login_attempts/locked_until và ghi mốc gửi/nhận.
3. Expected n=3 và khóa tạm 30 giây. Phải kiểm cả số đếm và kích hoạt khóa; chỉ thấy khóa không đủ để Pass toàn case.
4. Không coi việc fixture n=2 rồi sai một lần đã chứng minh toàn bộ chuỗi ba lần sai liên tiếp.

### TC05 Đúng mật khẩu trong thời gian khóa

1. Tạo khóa bằng thao tác đăng nhập sai trên fixture sạch và ghi mốc khóa thực tế. Không tạo khóa bằng sửa timestamp rồi nhận đã test cơ chế kích hoạt.
2. Khoảng 10 giây sau mốc bắt đầu khóa, submit mật khẩu đúng.
3. Expected: từ chối, không cấp phiên mới; chụp đồng hồ/mốc và phản hồi. Không tự assert request này gia hạn hay không gia hạn khóa.

### TC06 Email không tồn tại

1. Kiểm U có matches=0. Client sạch, input email hợp định dạng.
2. Nhập U và Test1234!, submit một lần.
3. Expected: từ chối, không cấp phiên hợp lệ, thông báo phù hợp. Không gán expected bộ đếm cho tài khoản không tồn tại.

### TC07 Email sai định dạng HTML5

1. Mở login, DevTools Elements chọn input email; ghi giá trị thuộc tính type thật, không sửa DOM.
2. Nhập abc và mật khẩu không rỗng. Bấm nút submit bình thường và quan sát Network.
3. Expected theo README: type=email, validation HTML5 chặn submit, không gửi request login.
4. Nếu source đang dùng type=text và request được gửi, thu bằng chứng nguyên trạng; không đổi type để làm test pass. Gọi API trực tiếp không chứng minh HTML5 validation.

### TC08 Đúng mật khẩu sau hết thời gian khóa

1. Dùng lần tạo khóa mới, ghi mốc; không dùng lần đã có request thử trong lúc khóa nếu chưa rõ tác động gia hạn.
2. Không gửi request thêm. Khoảng 35 giây sau mốc khóa, submit đúng mật khẩu.
3. Expected: được đăng nhập và có JWT. Nếu vẫn khóa, ghi khoảng thời gian đo được, response và timestamp khóa để điều tra.
4. Đây là đại diện sau thời hạn 30s, chưa thay bộ test BVA ngay trước/tại/sau ngưỡng.

### TC09 Client lưu token

1. Client sạch, A chưa khóa; đăng nhập thành công.
2. So token response với Application → Local Storage → origin web → token.
3. Expected: client lưu đúng token để dùng xác thực. Che token khi lưu ảnh. Không ép token phải tồn tại sau đóng browser nếu đặc tả không yêu cầu.

### TC10 Header Bearer cho request có xác thực

1. Đăng nhập thành công; lập danh mục endpoint/method cần auth của các luồng trong phạm vi: hồ sơ, đơn hàng, checkout… bằng source và network thực tế.
2. Với từng request client gửi, xem Network → Headers → Request Headers → Authorization.
3. Expected: Bearer và đúng token được lưu. Ghi endpoint/method và evidence từng luồng.
4. Request tự gửi bằng Postman/PowerShell chỉ chứng minh API chấp nhận token, không chứng minh client tự đính kèm header. Mới kiểm một endpoint thì chưa Pass yêu cầu tất cả request.

### TC11 Nội dung thông báo lỗi

1. Dùng ảnh/response của TC02, TC05, TC06; mỗi tình huống chạy với tiền điều kiện riêng.
2. Ghi thông báo nguyên văn và xem có lộ password/token/stack hoặc chi tiết không phù hợp không.
3. Không yêu cầu các thông báo giống hệt khi đề chưa nói. Với phần “không để lộ chi tiết nguyên nhân” chưa có oracle đủ cụ thể, ghi đã kiểm tiêu chí nào và phần chờ xác nhận; không ép Pass toàn R4.

## 5. Lưu bằng chứng và cập nhật kết quả

Mỗi lần chạy đặt Run-ID riêng, ví dụ FR02-TC02-RUN01. Lưu ảnh UI/Network, trạng thái DB trước và sau, thời gian vào `evidence/FR02-TC02-RUN01/`. Ghi đầy đủ Actual Result, Status, Tester, Tested Date, Bằng chứng trong Test_Cases.md; nếu chạy lại giữ lịch sử lần trước. Chỉ ghi Pass khi mọi assertion trong phạm vi đã được kiểm tra và đúng.

Ví dụ cách ghi, không phải kết quả đã đo:

- Actual: n trước=0, n sau=[số quan sát]; phản hồi=[thông báo thật]; token mới=[có/không]; khóa=[trạng thái thật].
- Status: dựa so sánh expected/actual; thiếu quan sát thì ghi chưa kiểm đủ, không tự gán Pass.
- Tested Date: giờ và ngày thực tế, UTC+07:00.
- Evidence: đường dẫn tương đối ảnh/log của Run-ID.

Nếu tiền điều kiện bị lỗi trước chặn, ghi Not Run/Blocked và lý do cho test phụ thuộc. Khi chuyển sang fixture trực tiếp để chạy cô lập, phân biệt rõ kết quả đó với luồng end-to-end. Không ghi Fail cho phần chưa thực thi.

## 6. Dấu hiệu cần xác minh bằng chạy thực tế

Đọc source server.js thấy `login_attempts + 2` và thời gian khóa `180000` ms; Login.jsx có input email type=text. Đây là dấu hiệu sai lệch so README (+1, 30 giây, type=email), chưa phải bug đã xác nhận bằng thực thi. Không sửa logic trước khi thu bằng chứng. Đọc code chỉ dùng để tìm điểm quan sát và thiết lập test; expected vẫn lấy README.

Hướng dẫn này không thay báo cáo BVA chưa thực hiện, không tăng executed/pass/fail và không tích checklist hoàn thành.
