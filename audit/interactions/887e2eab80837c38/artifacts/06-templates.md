# Biểu mẫu Domain Testing

Các bảng là khung để điền bằng dữ liệu có căn cứ; không giữ hàng mẫu rỗng như kết quả hoàn thành. Có thể gộp bảng nếu vẫn giữ đầy đủ liên kết.

## Danh mục Input/Output và ngữ cảnh

| ID | Loại Input/Output/State | Biến | Kiểu/đơn vị | Ràng buộc | Nguồn | Điểm chưa rõ |
| --- | --- | --- | --- | --- | --- | --- |

## Điều kiện

| C-ID | Requirement | Biến liên quan | Điều kiện | Expected behavior | Nguồn |
| --- | --- | --- | --- | --- | --- |

## Lớp tương đương

| EC-ID | Input/Output/State ID | C-ID | Miền hoặc điều kiện thành viên | Phân loại | Đại diện | Lý do chia và nguồn |
| --- | --- | --- | --- | --- | --- | --- |

Output có thể phân loại thành công/lỗi mong đợi; không đồng nhất lỗi mong đợi với lỗi phần mềm.

## Test case

| ID | Test case name | Precondition | Test step | Expected Result | Actual Result | Status | Tester | Tested Date | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Theo yêu cầu người dùng 16/10/2026, bảng test cuối chỉ dùng 10 cột trên, một test một hàng trong bảng liên tục; không lặp ba bảng cho mỗi test. Requirement, kỹ thuật, EC Input/Output, biên và evidence đặt trong phần phân tích/bao phủ/run riêng, không thêm cột vào bảng test. Có thể ghi mã bằng chứng ngắn trong Remark. Vẫn giữ phân tích từng bước; không bỏ EC đầu ra để rút gọn.

## Bao phủ thiết kế

| Requirement | C-ID | Input/Output/State ID | EC-ID | TC-ID | Đã có test/Chưa có test | Lý do còn thiếu |
| --- | --- | --- | --- | --- | --- | --- |

Phải có hàng cho cả EC-I và EC-O. Không đổi trạng thái thành đã quan sát output khi chưa chạy. Sau thực thi có thể bổ sung Run-ID và bằng chứng.

## Rà soát và AI Audit

- Review: thời gian thực tế, nội dung AI đề xuất, phản hồi thực tế của người học, chỉnh sửa, điểm còn mở.
- Audit: Interaction-ID, công cụ/model nếu biết, thời gian/múi giờ, prompt đầy đủ, output đầy đủ hoặc link bản lưu, tài liệu đầu vào, người rà soát nếu đã xác nhận.
- Nếu lưu output qua file, liên kết phiên bản/snapshot để lần sửa sau không làm mất output ban đầu.
