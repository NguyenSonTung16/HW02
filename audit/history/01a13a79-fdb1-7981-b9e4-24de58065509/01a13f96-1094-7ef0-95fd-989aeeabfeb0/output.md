Ví dụ dưới đây là **mẫu đầu ra dự kiến** của skill `ai-audit-report`, dựa trên lần tạo test FR-02. Phần đánh giá của bạn sẽ để **chưa rà soát**, không tự điền thay.

---

# Phụ lục A — AI Audit Report

## 1. Khai báo sử dụng AI

Tôi sử dụng công cụ AI cho các nhiệm vụ sau:

- Phân tích yêu cầu FR-02.
- Xác định Input/Output, điều kiện và lớp tương đương.
- Đề xuất test case và bảng bao phủ.

## 2. Nhật ký tương tác

| Trường | Nội dung |
|---|---|
| Interaction ID | AI-FR02-001 |
| Công cụ | Codex |
| Model | Chưa xác minh |
| Thời điểm bắt đầu | 15/10/2026, 11:10:10, UTC+07:00 |
| Chức năng | FR-02 — Đăng nhập và khóa tài khoản |
| Nhiệm vụ | Áp dụng skill `domain-testing` để thiết kế kiểm thử |

**Prompt nguyên văn:**

> chạy thử với FR-02

**Output AI:**

Lưu nguyên văn phản hồi AI trong `interactions/AI-FR02-001/output.md`. Các tài liệu AI tạo được lưu cùng phiên bản ban đầu:

```text
interactions/AI-FR02-001/
├── prompt.md
├── output.md
├── metadata.json
└── artifacts/
    ├── Requirements_Analysis.md
    ├── Domain_Testing.md
    └── Test_Cases.md
```

**Tóm tắt để tra cứu:** AI đề xuất 11 test case, 6 EC đầu vào, 6 EC trạng thái và 14 EC đầu ra. Tất cả test chưa chạy. Tóm tắt này **không thay thế output nguyên văn**.

## 3. Đánh giá từng sản phẩm AI

| Artifact | Output ban đầu | Verdict | Lý do và nguồn đối chiếu | Bản sinh viên sửa |
|---|---|---|---|---|
| Phân tích yêu cầu | `artifacts/Requirements_Analysis.md` | Chưa rà soát | Chưa ghi nhận | Chưa có |
| Phân lớp EC | `artifacts/Domain_Testing.md` | Chưa rà soát | Chưa ghi nhận | Chưa có |
| Bộ test case | `artifacts/Test_Cases.md` | Chưa rà soát | Chưa ghi nhận | Chưa có |

Sau khi bạn đánh giá, **Verdict** được cập nhật thành:

- **VALID:** đúng, chấp nhận nguyên bản.
- **INVALID:** sai, loại bỏ.
- **INCOMPLETE:** thiếu, chấp nhận sau khi bổ sung/chỉnh sửa.

## 4. Lịch sử chỉnh sửa của sinh viên

Chưa có phản hồi rà soát được ghi nhận.

Khi có chỉnh sửa, skill sẽ ghi: **nội dung ban đầu → ý kiến của bạn → nội dung sau sửa → lý do và tài liệu đối chiếu**; giữ cả hai phiên bản để so sánh.

## 5. Kiểm tra tính đầy đủ của nhật ký

| Nội dung | Trạng thái |
|---|---|
| Prompt của lần tương tác | Đã ghi nhận |
| Công cụ và thời gian | Đã ghi nhận |
| Snapshot tài liệu AI tạo | Đã có |
| Phản hồi AI nguyên văn đầy đủ | Cần bổ sung từ lịch sử chat |
| Đánh giá của sinh viên | Chưa có |
| Các tương tác HW02 trước đó | Chưa tổng hợp đầy đủ |

---

**Điểm chính của mẫu này:** tách rõ **AI đã tạo gì**, **bạn đã kiểm tra/sửa gì** và **nhật ký còn thiếu gì**. Nó chưa tự nhận bài đã được bạn duyệt hoặc audit đã đầy đủ.