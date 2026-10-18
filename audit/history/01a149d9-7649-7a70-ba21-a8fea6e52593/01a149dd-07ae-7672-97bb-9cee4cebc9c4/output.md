Mình sẽ đối chiếu lại mục 6, 9, 10 và 14 của đề để chốt cấu trúc báo cáo chính, chỉ giữ nội dung được yêu cầu.


Theo mục 6 và 14 của HW02 (trang 3–4), báo cáo chính cần trình bày Domain Testing và BVA cho **4 chức năng, mỗi pool một chức năng**, kèm giải thích các bước áp dụng:

> “Giải thích chi tiết từng bước đã áp dụng kỹ thuật.”

Bạn có thể dùng cấu trúc sau. Các mục con thể hiện quy trình theo S04; đề không quy định nguyên văn tên tiêu đề.

```text
1. Chức năng Pool A — [Mã và tên chức năng]
   1.1. Domain Testing
        1.1.1. Xác định Input và Output từ đặc tả
        1.1.2. Xác định các lớp tương đương cho từng Input/Output
        1.1.3. Chọn giá trị đại diện và xây dựng test case
        1.1.4. Bảng bao phủ lớp tương đương bằng test case

   1.2. Boundary Value Analysis
        1.2.1. Xác định các biên cần kiểm thử
        1.2.2. Chọn giá trị kiểm thử biên và giải thích
        1.2.3. Bộ test case BVA

   1.3. AI gap analysis
        — Test case hoặc bug AI bỏ sót, nếu có
        — Giải thích nguyên nhân bỏ sót

2. Chức năng Pool B — [Mã và tên chức năng]
   [Cấu trúc giống mục 1]

3. Chức năng Pool C — [Mã và tên chức năng]
   [Cấu trúc giống mục 1]

4. Chức năng Pool D — [Tên chức năng Mobile]
   [Cấu trúc giống mục 1]

5. Báo cáo lỗi
   — Các bug phát hiện được
   — Bước tái hiện, kết quả mong đợi và thực tế
   — Ảnh bằng chứng và liên kết GitHub Issues

Phụ lục: AI Audit Report
   — Khai báo sử dụng AI
   — Từng tương tác: tên công cụ, ngày giờ, prompt, output
```

**AI Audit đặt ở phụ lục** theo mục 9. Nếu báo cáo lỗi được nộp thành tệp riêng, mục 5 chỉ cần dẫn tới tệp đó.

**AI Critique 200–300 từ, Git commit log và README tổng kết/tự đánh giá** là các tài liệu nộp kèm theo mục 14, không cần thêm thành chương của báo cáo chính. Báo cáo chính xuất **Markdown + PDF**.