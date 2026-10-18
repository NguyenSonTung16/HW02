**Nên dùng [Test cases_Template_En.xlsx](https://docs.google.com/spreadsheets/d/16IXhmhLXPKyPVPtjp7BMrIMsWV-zriX4/edit) làm mẫu chung cho cả Domain Testing và Boundary Value Analysis trong HW02**, rồi bổ sung thông tin về EC và biên.

Mẫu này có sẵn các trường mô tả và chạy test: ID, tên test, tiền điều kiện, bước thực hiện, expected/actual, trạng thái, người chạy, ngày chạy và ghi chú.

**Mình đề xuất bổ sung:**

| Trường | Cách dùng |
|---|---|
| Requirement ID | Liên kết test với yêu cầu cần kiểm tra |
| Kỹ thuật | Domain Testing hoặc BVA; ghi cả hai nếu test phục vụ cả hai |
| EC đầu vào/trạng thái | Mã lớp tương đương được kiểm tra |
| EC đầu ra | Mã lớp kết quả mong đợi |
| Dữ liệu kiểm thử | Giá trị cụ thể dùng khi chạy |
| Biên và vị trí kiểm tra | Với BVA: biên nào, giá trị ngay dưới/tại/ngay trên biên khi phù hợp; với Domain thuần có thể để “Không áp dụng” |
| Bằng chứng | Ảnh, log hoặc đường dẫn evidence |

**Bảng test case cần đi kèm phần phân tích riêng:**

- **Domain Testing:** xác định input/output, các EC, chọn giá trị đại diện và bảng bao phủ EC ↔ test case.
- **BVA:** xác định biên từ đặc tả, biên đóng/mở và độ chia nhỏ của dữ liệu; chọn giá trị kiểm tra và bảng bao phủ biên ↔ test case.

Lý do là đề HW02 yêu cầu giải thích cách áp dụng kỹ thuật. Mục 6, trang 3 của [đề gốc](D:/vscode/Software%20testing/HW02/2026.HW02.Domain%20Testing_En.pdf) ghi: “Provide a detailed, step-by-step explanation of how you applied the technique.” Vì vậy, chỉ điền bảng test case sẽ chưa thể hiện đủ quá trình phân tích.

File [Test_Cases.md](D:/vscode/Software%20testing/HW02/FR-02/Test_Cases.md) hiện tại của bạn đã dùng mẫu này và bổ sung các trường EC, kỹ thuật, biên, bằng chứng. **Có thể tiếp tục cấu trúc đó cho HW02**; đây là đề xuất trình bày, chưa có căn cứ coi là mẫu bắt buộc.

Đã ghi audit