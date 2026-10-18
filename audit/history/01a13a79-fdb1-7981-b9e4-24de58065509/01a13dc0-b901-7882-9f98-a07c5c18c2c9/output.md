Mình sẽ chạy thử skill `domain-testing` cho FR-02: phân tích yêu cầu, chia EC cho từng Input/Output và lập test case cùng bảng bao phủ để bạn rà soát. Lần này là thử bước thiết kế; chưa chạy đăng nhập thực tế.


FR-02 có vài chỗ chưa quy định rõ: cách reset bộ đếm, xử lý request khi đang khóa và mức chi tiết được phép của thông báo lỗi. Mình đã ghi riêng các điểm này và vẫn thiết kế test cho phần có đủ đặc tả. Bảng bao phủ sẽ phân biệt “có test dự kiến” với “đã quan sát kết quả”.


Bản nháp hiện có 11 test case và bảng bao phủ 6 EC đầu vào, 6 EC trạng thái, 14 EC đầu ra. Mình đang kiểm tra lại các liên kết EC–test, lưu snapshot cho AI Audit và ghi Git log. Tất cả test vẫn là `Not Run`, chờ bạn rà soát.


Đã chạy thử **skill `domain-testing` cho FR-02**, tạo:

- [Phân tích yêu cầu và Input/Output](<D:/vscode/Software testing/HW02/FR-02/Requirements_Analysis.md>).
- [Điều kiện, EC và bảng bao phủ](<D:/vscode/Software testing/HW02/FR-02/Domain_Testing.md>): **6 EC đầu vào, 6 EC trạng thái, 14 EC đầu ra**.
- [11 test case](<D:/vscode/Software testing/HW02/FR-02/Test_Cases.md>).
- [AI Audit](<D:/vscode/Software testing/HW02/FR-02/audit/AI_Audit_FR02.md>) và [Git log](<D:/vscode/Software testing/HW02/FR-02/Git_Log.txt>), kèm snapshot bản nháp ban đầu.

**Đây là bản thiết kế chờ bạn rà soát:** chưa làm BVA, chưa chạy ứng dụng; toàn bộ test là `Not Run`.

Bạn nên đọc **Requirements_Analysis.md trước**, đặc biệt các điểm chưa rõ về reset bộ đếm, thời gian khóa và thông báo lỗi. Mình chưa tích hoàn thành checklist.