**Nhận xét của bạn phù hợp.** FR-15 yêu cầu các sản phẩm khác giữ nguyên khi sửa, nên cần kiểm tra cả giao diện sau khi lưu và dữ liệu sau khi tải lại.

TC03 hiện chỉ kiểm tra **sau khi tải lại**, vì vậy có thể bỏ sót lỗi giao diện tạm thời: tên nhiều sản phẩm cùng đổi, nhưng tải lại thì trở về đúng.

Expected có thể sửa thành:

> Ngay sau khi lưu thành công và sau khi tải lại, chỉ sản phẩm đích thay đổi đúng tên, giá và danh mục đã nhập; các sản phẩm khác giữ nguyên so với trước khi sửa.

**Không cần thêm TC hoặc EC mới**; chỉ bổ sung bước quan sát trước khi tải lại trong TC03. Đây là thiếu sót về điểm quan sát trong test mình thiết kế, chưa phải bug đã được phát hiện trên EShop.

Mình chưa sửa file.

Đã ghi audit