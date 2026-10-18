---
name: domain-testing
description: Thiết kế Domain Testing từ đặc tả theo slide S04, xác định EC cho từng Input và Output và lập bảng bao phủ. Dùng khi phân tích miền hoặc thiết kế test theo lớp tương đương; không thay thế BVA hoặc kết quả chạy test.
---

# Domain Testing

## Phạm vi và nguồn

Thiết kế kiểm thử có thể tái sử dụng trên các chức năng khác nhau. Viết tiếng Việt, thêm tiếng Anh trong ngoặc cho thuật ngữ quan trọng. Đọc đặc tả gốc và tài liệu phương pháp được cung cấp; trích nguồn theo trang/đề mục. Không dùng hành vi triển khai làm expected result. Khi làm HW02 eShop, lấy nghiệp vụ từ README, phương pháp từ S04, yêu cầu hồ sơ từ đề HW02. FR-02/09/15 là ví dụ, không phải giới hạn của skill.

Đọc [biểu mẫu](references/templates.md) khi lập báo cáo. Tất cả các giai đoạn dùng quy tắc ghi nhận cuối file này.

## Quy trình

1. **Yêu cầu:** xác định phạm vi, requirement ID, nguồn, hành vi đúng. Phân biệt yêu cầu rõ ràng, suy luận và câu hỏi chưa giải quyết. Chỉ hỏi khi thiếu thông tin ảnh hưởng quyết định; tiếp tục phần độc lập.
2. **Input/Output:** lập danh mục từng đầu vào và từng đầu ra; ghi kiểu, đơn vị, ràng buộc. Ghi trạng thái và thời gian như ngữ cảnh riêng, không giả làm trường nhập. Đầu ra gồm dữ liệu trả về, thông báo và trạng thái quan sát được liên quan đến đặc tả.
3. **Điều kiện (Conditions):** tách C-ID từ đặc tả; ánh xạ về requirement và Input/Output. Một lớp hợp lệ với một điều kiện chưa bảo đảm đầu vào hợp lệ toàn bộ.
4. **EC cho từng Input và Output:** đặt ID phân biệt `EC-I-*`, `EC-O-*`; trạng thái dùng `EC-S-*` nếu cần. Với từng biến, xác định các lớp, điều kiện thành viên, hợp lệ/không hợp lệ nếu thích hợp, đại diện, nguồn và lý do chia. Với output lỗi mong đợi, ghi đây là đầu ra đúng cho tình huống lỗi, không gán nhãn sai vì chứa thông báo lỗi.
   - Khoảng hai phía: xét một lớp trong khoảng và hai lớp ngoài khoảng; xác định chính xác biên đóng/mở và miền kiểu dữ liệu. Nếu kiểu dữ liệu không cho phép một phía, ghi lý do không áp dụng.
   - Điều kiện bắt buộc (Must-be Condition): xét lớp thỏa và không thỏa.
   - Nhóm giá trị được xử lý khác nhau: tách EC riêng cho mỗi nhóm; xét giá trị không được phép nếu có. Không tách mỗi giá trị nếu hành vi tương đương.
   - Nếu phần tử trong một EC có hành vi khác nhau, chia nhỏ và ghi căn cứ. Ví dụ số thập phân và chuỗi chữ có thể cần tách nếu được xử lý khác nhau.
   - Áp dụng cho cả Input/Output; không máy móc tạo miền output không thể xảy ra. Nếu output có miền số/độ dài được đặc tả, xét các lớp tương ứng và cách kích hoạt/quan sát. Ghi mọi biến chưa đủ đặc tả để chia lớp.
5. **Đại diện và test:** chọn ít nhất một test cho mỗi EC. Test hợp lệ kết hợp nhiều lớp hợp lệ khi khả thi. Theo S04 trang 21, mỗi test âm cô lập một lớp đầu vào không hợp lệ, giữ các điều kiện đầu vào khác hợp lệ. EC đầu ra lỗi đi kèm không tính là vi phạm đầu vào thứ hai. Các trường hợp nhiều lỗi đồng thời, nếu cần, đặt riêng là test bổ sung.
6. **Bao phủ:** lập bảng requirement → condition → Input/Output → EC → test. BẮT BUỘC bao gồm EC đầu ra. Mỗi test có EC đầu vào/trạng thái và EC đầu ra mong đợi, tiền điều kiện, dữ liệu, bước chạy, expected result có nguồn. Bao phủ thiết kế chỉ nghĩa có test dự kiến; chỉ kết quả chạy mới chứng minh output được quan sát.
7. **Rà soát:** tìm lớp bỏ sót, chồng lấn, dữ liệu không thuộc lớp, output chưa có assertion và điều kiện bị thay đổi đồng thời. Đưa bản đề xuất cho người học rà soát; ghi đúng ý kiến thực tế và giữ bản ban đầu để phân tích thiếu sót AI. Nếu người dùng yêu cầu làm từng bước, dừng ở bước được yêu cầu; nếu đã yêu cầu toàn bộ, hoàn thành bản nháp toàn bộ và đánh dấu chưa được người học duyệt, không tự tạo chuỗi xin phép.

## Đầu ra và tiêu chí

Đối với báo cáo HW02 của người dùng này, bảng test cuối dùng đúng 10 thuộc tính của Test cases_Template_En.xlsx (xem reference). Để EC, kỹ thuật, source và evidence trong bảng phân tích/bao phủ riêng hoặc Remark ngắn; không thêm cột hay tách thành ba bảng lặp cho mỗi test. Rút gọn văn bản nhưng giữ được các bước kỹ thuật và khả năng truy vết.

Tạo/cập nhật `Requirements_Analysis.md`, `Domain_Testing.md`, `Test_Cases.md` trong thư mục người dùng chọn, hoặc gộp nếu đã có cấu trúc. Dùng ID có prefix chức năng để tránh trùng. Mọi Input/Output phải được xét EC; mọi EC có test hoặc lý do chưa bao phủ. Chuyển sang BVA bằng bảng điều kiện/EC có trạng thái rà soát; không tự tuyên bố đã chạy test.

## Ghi nhận chung

- Với HW02, ghi AI Audit theo từng tương tác: công cụ/model nếu biết, thời gian thực tế với múi giờ, prompt, output hoặc liên kết bản lưu đầy đủ. Ghi human review và thay đổi riêng. Không bịa lịch sử, mốc thời gian hay lời duyệt; ghi rõ phần chưa truy xuất được. Giữ bản đề xuất AI ban đầu.
- Lưu giải thích từng bước để đưa vào báo cáo. Khi người dùng yêu cầu workflow HW02, kiểm tra repo đích rồi commit các file của bước đó theo từng bước thực tế; không gom thay đổi người khác, dựng lịch sử hoặc push khi chưa được yêu cầu. Nếu Git chưa sẵn sàng, ghi rõ thay vì nhận đã commit.
- Checklist tiến độ chỉ tích theo yêu cầu của người dùng. Các thao tác bên ngoài như đăng issue, gửi tin hoặc xuất bản video không được suy ra chỉ từ việc dùng skill.
