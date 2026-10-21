# HW02 – Black-Box Domain Testing & Boundary Value Analysis (eShop SUT)

**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)**  
**Môn học:** CS423 / CSC13003 – Kiểm chứng Phần mềm (AI-augmented · 2026)  
**Học viên thực hiện:** **VÕ THÀNH MINH TUỆ** — MSSV: **23120398** — Lớp: **23_3**  
**Giảng viên:** **Lê Quang Vũ**  

---

## 📁 Hồ sơ Nộp bài Chính thức (Submission Package)

Toàn bộ báo cáo, tài liệu kỹ thuật, mã nguồn kiểm thử và bằng chứng thực nghiệm của sinh viên **23120398** được đóng gói đầy đủ tại thư mục:  
👉 **[./23120398/](./23120398/)**

### 📋 Danh mục các tài liệu bàn giao:
- 📄 **[README.md](./23120398/README.md):** Bảng tự đánh giá điểm (100/100) & Báo cáo tổng kết kiểm thử
- 📄 **[Main_Report.md](./23120398/Main_Report.md)** ([Bản PDF](./23120398/Main_Report.pdf)): Báo cáo Domain Testing (EP) & BVA cho 4 tính năng (**FR-03**, **FR-08**, **FR-16**, **FR-20**) kèm Task 3: AI Gap Analysis
- 📄 **[Bug_Report.md](./23120398/Bug_Report.md)** ([Bản PDF](./23120398/Bug_Report.pdf)): Báo cáo chi tiết 15 lỗi phát hiện & GitHub Issue Cards
- 📄 **[AI_Critique.md](./23120398/AI_Critique.md)** ([Bản PDF](./23120398/AI_Critique.pdf)): Báo cáo nhận xét phản biện AI (200–300 từ)
- 📄 **[AI_Audit_Report.md](./23120398/AI_Audit_Report.md)** ([Bản PDF](./23120398/AI_Audit_Report.pdf)): Nhật ký kiểm toán AI chuẩn FIT@HCMUS 2026 v1.0
- 📄 **[Appendix_A_AI_Logs.md](./23120398/Appendix_A_AI_Logs.md):** Toàn văn 100% Prompt & Output nguyên văn của AI
- 📦 **[23120398_HW02_AI_DomainTesting_100.zip](./23120398/23120398_HW02_AI_DomainTesting_100.zip):** Gói nộp bài nén chuẩn Moodle
- 🖼️ **[bug-screenshots/](./23120398/bug-screenshots/):** Toàn bộ 42 ảnh chụp màn hình bằng chứng lỗi Playwright
- 🤖 **[skills/domain-testing/](./23120398/skills/domain-testing/):** Kỹ năng Agent Skill `domain-testing`
- 📑 **[requirements/](./23120398/requirements/):** Đặc tả đề bài và dữ liệu seeder Faker seed=42

---

## 📊 Bảng Tự Đánh Giá Điểm (Self-Assessment: 100/100)

| No. | Tiêu chí đánh giá | Điểm tối đa | Điểm tự chấm | Ghi chú minh chứng |
| :---: | :--- | :---: | :---: | :--- |
| **1** | Feature A (FR-03: Forgot Password & OTP Reset) | 25 | **25** | Hoàn thành 4 bước EP (20 ECs) + BVA 9-point model (36 TCs, tìm ra 5 bug). |
| **2** | Feature B (FR-08: Checkout & Price Calculation) | 25 | **25** | EP + BVA đầy đủ, phát hiện lỗ hổng client total_amount tampering 0 VND & số âm (12 TCs, 4 bug). |
| **3** | Feature C (FR-16: Admin Bulk Import CSV) | 25 | **25** | EP + BVA trên CSV parsing RFC 4180 và rollback transaction CSDL (11 TCs, 4 bug). |
| **4** | Feature D (FR-20: Mobile Login Responsive) | 15 | **15** | Thực thi trên 4 viewports 320/375/414/768px (32 TCs), tìm ra mật khẩu hiển thị plaintext. |
| **5** | Agent Skills (`domain-testing`) | 10 | **10** | Xây dựng Agent Skill chuẩn hóa `domain-testing` theo đúng quy ước Antigravity. |
| | **Tổng cộng** | **100** | **100** | Đầy đủ mọi tài liệu bắt buộc MD, PDF, Git log, Bug screenshot, Zip archive. |
