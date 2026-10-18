Mình sẽ kiểm tra các skill trong thư mục Software testing và thư mục skill cá nhân, xem đã có skill chuyên ghi AI Audit hay phần nào đang đảm nhiệm việc đó.


**Có, nên tạo một skill chuyên AI Audit** để ghi log thống nhất cho cả Domain Testing, BVA và chạy test.

Mình đã kiểm tra thư mục `D:\vscode\Software testing` và thư mục skill cá nhân. **Hiện chưa có skill chuyên AI Audit.** Bộ hiện tại chỉ có:

- `domain-testing`
- `boundary-value-analysis`
- `test-execution-reporting`

Cả ba đều có **hướng dẫn ghi audit**, nhưng chưa có bộ xử lý riêng để thu thập và tổng hợp nhật ký. Đã có [AI_Audit_FR02.md](<D:/vscode/Software testing/HW02/FR-02/audit/AI_Audit_FR02.md>), nhưng mới ghi lần thử FR-02, **chưa bao phủ toàn bộ quá trình HW02**.

Skill mới có thể tên **`ai-audit-report`**, giải quyết:

1. Ghi từng tương tác: **công cụ, ngày giờ, prompt nguyên văn, output nguyên văn**.
2. Lưu snapshot output và file được tạo để các lần sửa sau không làm mất bản đầu.
3. Ghi phần bạn rà soát theo mẫu AI-02: **VALID/INVALID/INCOMPLETE, lý do và bản chỉnh sửa**.
4. Tổng hợp thành **AI Audit Report Markdown**, chuẩn bị bản PDF và phụ lục báo cáo chính.
5. Kiểm tra tương tác thiếu thông tin, liên kết hỏng hoặc chưa được bạn đánh giá.

**Giới hạn cần ghi rõ:** skill không tự bảo đảm lấy được toàn bộ lịch sử chat. Nó chỉ ghi những tương tác truy xuất được; thiếu prompt, output hoặc thời gian thì phải báo thiếu, không tự dựng lại.