# FR02 Kết quả thực thi

Cập nhật 16/10/2026 theo hội thoại và yêu cầu người dùng cập nhật report. Múi giờ UTC+07:00; giờ chạy cụ thể chưa xác nhận. Không chạy lại hoặc reset server trong lần cập nhật này.

## TC01

- Run ID: FR02-TC01-RUN01 (mã gán để theo dõi kết quả đã gửi).
- Người thực thi: Nguyễn Sơn Tùng.
- Actual: login báo thành công và trả JWT; GET /api/users/me sử dụng token được HTTP 200, id=2, email=test@eshop.com.
- Status: Pass.
- Evidence: evidence/FR02-TC01-RUN01/User_Provided_Result.md. Chưa có screenshot terminal đã che token trong thư mục nộp.
- Source commit SUT và thời gian chạy chính xác chưa xác nhận. Phần kiểm JWT được kiểm qua API; không dùng kết quả này thay TC10 về header tự đính kèm của client.

## TC09

- Người dùng xác nhận token trong Network và Local Storage khớp hoàn toàn; ảnh có key token.
- Chưa xác nhận origin trong ảnh, có key user của tài khoản khác có thể là dữ liệu cũ.
- Trạng thái: đã kiểm một phần, chưa kết luận; ghi Not Run trong cột trạng thái và chú thích rõ để thống kê chưa hoàn tất, không nhận chưa có bất kỳ thao tác nào.
- Khi xác nhận origin localhost:5173 và bổ sung evidence phù hợp, có thể hoàn tất đánh giá.

## Các case còn lại

TC02–TC08, TC10–TC11: chưa có kết quả thực thi do người dùng cung cấp, giữ Not Run. Tổng 11 TC: 1 Pass, 0 Fail, 10 chưa có kết luận; TC09 nằm trong 10 và đã có quan sát một phần.

## Quan sát bổ sung

Response login người dùng gửi có trường user.password dạng rõ. Lưu như quan sát bảo mật cần hoàn thiện bug report và nguồn yêu cầu tương ứng; không biến thành lỗi của assertion TC01 hoặc tự tính đã có GitHub Issue. Không lưu lại credential trong tài liệu này.
