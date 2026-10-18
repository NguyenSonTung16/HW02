Để đúng tinh thần HW02, hãy làm theo chuỗi **AI đề xuất → bạn rà soát → chạy test → đối chiếu kết quả → ghi bằng chứng và nhận xét AI**. Kết quả phải lấy từ lần chạy thực tế.

**1. Bạn rà soát thiết kế trước khi chạy**

Đọc [phân tích FR-02](<D:/vscode/Software testing/HW02/FR-02/Requirements_Analysis.md>), [bảng EC](<D:/vscode/Software testing/HW02/FR-02/Domain_Testing.md>) và đối chiếu README:

- Sai mật khẩu: bộ đếm tăng **đúng 1**.
- Sai **3 lần liên tiếp**: khóa **30 giây**.
- Thành công: trả JWT, client lưu và gửi Bearer khi cần xác thực.
- Email: `type="email"`, có validation HTML5.

Ghi rõ bạn chấp nhận/sửa điều kiện, EC hoặc test nào và vì sao. **BVA chưa được thiết kế**, nên 11 case hiện tại chưa hoàn thành toàn bộ FR-02 của HW02; vẫn có thể chạy phần Domain Testing trước.

**2. Chuẩn bị quan sát**

Trên trang đăng nhập, nhấn **F12 → Network**, bật **Preserve log**, lọc `login`. Ghi môi trường, phiên bản source và ngày giờ chạy. Không restart backend giữa các case vì source này khởi tạo lại dữ liệu khi khởi động.

Trong PowerShell:

```powershell
$fr02Python = 'C:\Users\tung1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$fr02Helper = 'D:\vscode\Software testing\HW02\FR-02\tools\auth_fixture.py'
```

Đặt tài khoản demo chưa khóa, bộ đếm bằng 0:

```powershell
& $fr02Python $fr02Helper --set-attempts 0
```

Đây là chuẩn bị dữ liệu, không phải kết quả kiểm thử. Helper sao lưu trước khi sửa trạng thái tài khoản.

**3. Thực hiện TC01 — đăng nhập đúng**

1. Bảo đảm client sạch phiên và tài khoản chưa khóa.
2. Nhập `test@eshop.com` / `Test1234!`, submit một lần.
3. Trong Network, chọn `POST /api/login`; xem response có token không và quan sát UI.
4. Kiểm tra token được backend chấp nhận qua request có xác thực, chẳng hạn `GET /api/users/me`. Chỉ thấy chuỗi token chưa đủ chứng minh token hợp lệ.
5. Lưu ảnh/log, che token; ghi actual rồi mới kết luận các assertion đã kiểm đủ có Pass hay không.

**4. Thực hiện TC02 — sai mật khẩu một lần**

1. Đăng xuất, làm sạch phiên và đặt lại `--set-attempts 0`.
2. Đọc trạng thái trước:

```powershell
& $fr02Python $fr02Helper
```

3. Nhập email đúng và mật khẩu `WrongPass9!`; submit **đúng một lần**.
4. Đợi request hoàn tất, chạy lại lệnh đọc trạng thái.
5. Expected: **0 → 1**, chưa khóa, đăng nhập bị từ chối.

Nếu thực tế là **0 → 2**, ghi đúng số đo và đánh dấu assertion tăng đếm bị Fail. **Không sửa expected theo source hoặc sửa code trước khi thu bằng chứng.**

**5. Tiếp tục các case còn lại**

| Case | Việc cần làm |
|---|---|
| TC03–04 | Xác nhận n=1/n=2 trước request. Nếu case trước không tạo đúng trạng thái, ghi trở ngại; có thể đặt fixture riêng và ghi rõ kiểm thử cô lập |
| TC05 | Tạo khóa bằng thao tác thật, ghi mốc; thử mật khẩu đúng sau khoảng 10 giây |
| TC06–07 | Thử email không tồn tại và sai định dạng; TC07 phải quan sát UI/DOM/Network |
| TC08 | Tạo khóa mới; không gửi request xen giữa; sau khoảng 35 giây đăng nhập đúng |
| TC09–10 | Kiểm token được lưu và header do chính client gửi trên các request cần xác thực |
| TC11 | Rà thông báo lỗi của các tình huống đã chạy; ghi phần tiêu chí chưa đủ rõ |

Các bước chi tiết nằm trong [Execution_Guide.md](<D:/vscode/Software testing/HW02/FR-02/Execution_Guide.md>).

**6. Ghi kết quả và phần đóng góp của bạn**

Điền **Actual Result, Status, Tester, Tested Date, Bằng chứng** trong [Test_Cases.md](<D:/vscode/Software testing/HW02/FR-02/Test_Cases.md>). Mỗi lần chạy có Run-ID; giữ ảnh, request/response và trạng thái DB liên quan. Test chưa chạy hoặc thiếu tiền điều kiện không tự ghi Pass.

Bug xác nhận được thì lập báo cáo và GitHub Issue kèm ảnh. Nhận xét output AI bằng **VALID / INVALID / INCOMPLETE** sau khi bạn thực sự rà soát; lưu phần chỉnh sửa và lý do. Commit theo từng bước có ý nghĩa.

**Hãy bắt đầu TC01 và TC02 trước**, để nắm cách quan sát và lưu bằng chứng rồi mới chạy chuỗi khóa tài khoản.

Đã ghi audit