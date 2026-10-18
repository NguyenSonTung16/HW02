Ảnh xác nhận **có token được lưu trong Local Storage**. Tuy nhiên, key `user` đang ghi `username: "ketoan", role: "KeToan"`, khác response `Test User` vừa gửi. Có thể là dữ liệu cũ; ảnh cũng chưa cho thấy origin đang chọn.

Trước khi kết luận **TC09 Pass**, xác nhận:

- Origin là **`http://localhost:5173`**.
- Giá trị key `token` **khớp toàn bộ** token của response login vừa nhận.

Sau đó kiểm tiếp TC01: trong **Console của trang eShop**, chạy:

```javascript
fetch('http://localhost:3000/api/users/me', {
  headers: {
    Authorization: `Bearer ${localStorage.getItem('token')}`
  }
}).then(async response => {
  const user = await response.json();
  console.log({
    status: response.status,
    id: user.id,
    email: user.email
  });
});
```

Expected: **status `200`, id `2`, email `test@eshop.com`**. Lệnh chỉ in các trường cần kiểm tra, không in token hoặc password. Nếu trình duyệt chặn dán Console, có thể dùng Postman thay thế.

Kết quả này kiểm tra backend chấp nhận token; **TC10 vẫn cần quan sát header do chính ứng dụng gửi**, không dùng request Console để thay thế.

Đã ghi audit