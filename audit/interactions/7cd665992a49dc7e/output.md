**HW02 tập trung vào thiết kế test bằng Domain Testing và BVA, nhưng đề cũng có kỳ vọng bạn thực thi kiểm thử.** Không nên hiểu là chỉ lập bảng test rồi nộp.

Đối chiếu [đề HW02](<D:/vscode/Software testing/HW02/2026.HW02.Domain Testing_En.md>):

- **Mục 6.1–6.2:** yêu cầu rõ việc **thiết kế bộ test case** bằng hai kỹ thuật và giải thích từng bước.
- **Mục 6.4:** yêu cầu báo các bug phát hiện được trong Markdown và GitHub Issues, kèm screenshot.
- **Mục 14:** test summary phải có số test **“designed, executed, passed, failed, and not yet executed”** — đã thiết kế, đã chạy, pass, fail và chưa chạy.

**Điểm cần phân biệt:** đề không viết rõ “phải chạy toàn bộ test case” hoặc quy định số test tối thiểu phải chạy. Việc có mục *not yet executed* cho phép báo cáo trung thực phần chưa chạy; nó không khẳng định rằng không cần chạy test nào.

Với bài của bạn, mình đề xuất **thiết kế đầy đủ Domain Testing + BVA, sau đó chạy các test có thể thực hiện, ghi kết quả và báo bug**. Test chưa chạy ghi `Not Run` cùng lý do. Không có yêu cầu rõ rằng phải tự động hóa; có thể chạy thủ công.

Câu trước mình nói “phải chạy các test” hơi tuyệt đối: chính xác hơn là **đề có yêu cầu hồ sơ kết quả thực thi, nhưng chưa nêu bắt buộc chạy hết bộ test**.

Đã ghi audit