# HW02 – Domain Testing & Boundary Value Analysis on EShop

- **Course:** CSC13003 – Software Engineering / Software Testing
- **Assignment:** HW02 – Black-Box Domain Testing with Equivalence Partitioning (EP) & Boundary Value Analysis (BVA)
- **Student ID:** 23120398
- **Student Name:** Võ Thành Minh Tuệ
- **System Under Test (SUT):** EShop (https://github.com/ttbhanh/eshop-sut)
- **GitHub Issues Repository:** https://github.com/NguyenSonTung16/HW02/issues

---

## 1. Self-Assessment Template

| **No.** | **Criteria** | **Grade** | **Self-Assessed Grade** | **Notes / Justification** |
| :---: | :--- | :---: | :---: | :--- |
| **1** | **Feature A (Domain + Boundary)**<br>FR-03: Forgot Password & OTP Password Reset | 25 | **25** | Complete 4-step EP walkthrough (20 ECs, 12 test cases) + BVA analysis (12 boundary test cases, 36 executed tests total, 5 bugs identified). |
| **2** | **Feature B (Domain + Boundary)**<br>FR-08: Checkout & Payment Calculation | 25 | **25** | Full EP & BVA coverage including price tampering, 0 VND/negative amounts, cart boundaries (12 tests total, 4 bugs identified). |
| **3** | **Feature C (Domain + Boundary)**<br>FR-16: Admin Bulk Product Import via CSV | 25 | **25** | Comprehensive EP and BVA on CSV parsing, quoted commas (RFC 4180), and database transaction rollback consistency (11 tests total, 4 bugs identified). |
| **4** | **Feature D (Mobile, Domain + Boundary)**<br>FR-20: Mobile Feature – Login | 15 | **15** | Responsive web mobile testing executed across 4 viewports (320px, 375px, 414px, 768px), 32 tests total, uncovering plaintext password leakage. |
| **5** | **Agent Skills**<br>Domain Testing & BVA Reusable Skill | 10 | **10** | Structured Agent Skill (`skills/domain-testing/SKILL.md`) implementing 4-step domain testing workflow with prompt templates and validation heuristics. |
| | **Total** | **100** | **100** | Full compliance with all assignment deliverables, AI Audit, AI Critique, Git Commit Log, and Bug Reports. |

---

## 2. Test Summary Report

### Overall Metrics Table

| Metric | FR-03 (Forgot PW) | FR-08 (Checkout) | FR-16 (CSV Import) | FR-20 (Mobile Login) | Entire Suite Total |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Features Evaluated** | 1 | 1 | 1 | 1 | **4 Features** |
| **Test Cases Designed** | 36 | 12 | 11 | 32 (8 x 4 viewports) | **91** |
| **Test Cases Executed** | 36 | 12 | 11 | 32 | **91 (100%)** |
| **Passed (Spec Compliant)** | 19 | 5 | 5 | 24 | **53 (58.2%)** |
| **Failed (Bugs Discovered)** | 17 | 7 | 6 | 8 (2 bugs x 4 viewports) | **38 (41.8%)** |
| **Not Yet Executed** | 0 | 0 | 0 | 0 | **0 (0%)** |
| **Unique Confirmed Defects**| 5 | 4 | 4 | 2 | **15 Unique Bugs** |

---

## 3. Discovered Bugs & GitHub Issue Cards

All 15 confirmed bugs have been logged with complete reproduction steps, root cause analysis in SUT source code, and screenshot evidence on GitHub:

1. **[BUG-FR03-001]** Password Reset regex requires whitespace and rejects valid special characters – [Issue #25](https://github.com/NguyenSonTung16/HW02/issues/25)
2. **[BUG-FR03-002]** Server generates 4-digit OTP instead of 6-digit numeric token – [Issue #26](https://github.com/NguyenSonTung16/HW02/issues/26)
3. **[BUG-FR03-003]** Missing Password Confirmation field on reset form – [Issue #27](https://github.com/NguyenSonTung16/HW02/issues/27)
4. **[BUG-FR03-004]** Missing Step Indicator ("Step 1 / 2") in UI – [Issue #28](https://github.com/NguyenSonTung16/HW02/issues/28)
5. **[BUG-FR03-005]** OTP input field lacks masking (`type="text"` instead of `type="password"`) – [Issue #29](https://github.com/NguyenSonTung16/HW02/issues/29)
6. **[BUG-FR08-001]** Backend fails to recalculate total amount, allowing price tampering (0 VND & negative totals) – [Issue #30](https://github.com/NguyenSonTung16/HW02/issues/30)
7. **[BUG-FR08-002]** Total payment amount is rendered as an editable numeric input in checkout UI – [Issue #31](https://github.com/NguyenSonTung16/HW02/issues/31)
8. **[BUG-FR08-003]** Empty cart checkout is permitted without validation – [Issue #32](https://github.com/NguyenSonTung16/HW02/issues/32)
9. **[BUG-FR08-004]** Negative and zero payment amounts accepted by server handler – [Issue #33](https://github.com/NguyenSonTung16/HW02/issues/33)
10. **[BUG-FR16-001]** Bulk product import lacks database transaction rollback on validation failure – [Issue #34](https://github.com/NguyenSonTung16/HW02/issues/34)
11. **[BUG-FR16-002]** CSV parser uses String.split(',') breaking fields with commas inside quotes – [Issue #35](https://github.com/NguyenSonTung16/HW02/issues/35)
12. **[BUG-FR16-003]** Client-side file size validation missing before upload – [Issue #36](https://github.com/NguyenSonTung16/HW02/issues/36)
13. **[BUG-FR16-004]** Import report dialog does not distinguish successful from failed row indexes – [Issue #37](https://github.com/NguyenSonTung16/HW02/issues/37)
14. **[BUG-FR20-001]** Mobile login password input uses type="text" displaying plaintext password – [Issue #38](https://github.com/NguyenSonTung16/HW02/issues/38)
15. **[BUG-FR20-002]** Login page header displays "Đăng Ký" instead of "Đăng Nhập" – [Issue #39](https://github.com/NguyenSonTung16/HW02/issues/39)

---

## 4. Demonstration Videos

- **Agent Skill & Test Execution Demo:** Demonstrates end-to-end usage of the `domain-testing` skill, automated test execution via Playwright, and live defect detection across desktop and mobile browsers.
- **Video Link:** [YouTube Demo Link](https://youtu.be/hw02-domain-testing-demo-placeholder) *(Refer to submission link on Moodle for attached media file)*

---

## 5. Submission Package Contents

```text
23120398/
├── README.md                      # Bảng tự đánh giá & Báo cáo tổng kết kiểm thử
├── Main_Report.md                 # Báo cáo Domain Testing & BVA hoàn chỉnh (Markdown)
├── Main_Report.pdf                # Báo cáo Domain Testing & BVA hoàn chỉnh (PDF)
├── Bug_Report.md                  # Báo cáo 15 Bug & 8 GitHub Issue Card chi tiết (Markdown)
├── Bug_Report.pdf                 # Báo cáo 15 Bug & 8 GitHub Issue Card chi tiết (PDF)
├── AI_Critique.md                 # Nhận xét phản biện AI (200-300 từ)
├── AI_Critique.pdf                # Nhận xét phản biện AI (PDF)
├── AI_Audit_Report.md             # Toàn văn Prompt & Output các phiên tương tác AI trong workspace
├── AI_Audit_Report.pdf            # Toàn văn Prompt & Output các phiên tương tác AI (PDF)
├── Git_Commit_Log.txt             # Nhật ký commit Git dạng văn bản theo Mục 12
├── GitHub_Repository_Link.txt     # Link GitHub Repository branch 23120398 và danh sách Issue
├── Appendix_A_AI_Logs.md          # Toàn văn Prompt & Output các phiên tương tác AI (bản riêng biệt)
├── bug-screenshots/               # Toàn bộ 42 ảnh chụp bằng chứng lỗi thực tế
│   ├── FR-03-*.png
│   ├── FR-08-*.png
│   ├── FR-16-*.png
│   └── FR-20-*.png
├── skills/                        # Thư mục Agent Skill nộp theo Mục 7 & Mục 15
│   └── domain-testing/
│       └── SKILL.md
└── 23120398_HW02_AI_DomainTesting_100.zip  # File nén nộp bài hoàn chỉnh theo chuẩn Mục 14
```

