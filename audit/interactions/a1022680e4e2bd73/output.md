Mở **terminal PowerShell mới** trong VS Code, giữ nguyên terminal đang chạy server. Dán đoạn này:

```powershell
$fr02Token = Read-Host 'Dan token tu Network hoac Local Storage, khong kem dau ngoac kep'

$fr02Response = Invoke-WebRequest `
  -Uri 'http://localhost:3000/api/users/me' `
  -Method Get `
  -Headers @{ Authorization = "Bearer $fr02Token" }

$fr02User = $fr02Response.Content | ConvertFrom-Json

[PSCustomObject]@{
  Status = $fr02Response.StatusCode
  Id     = $fr02User.id
  Email  = $fr02User.email
}
```

Khi terminal hỏi, dán token rồi nhấn **Enter**. Không thêm dấu `"` quanh token.

Kết quả mong đợi:

```text
Status Id Email
------ -- -----
   200  2 test@eshop.com
```

Nếu đúng như trên, bạn đã xác nhận backend chấp nhận token — hoàn tất phần kiểm JWT của **TC01**. Chụp kết quả bảng, tránh chụp dòng nhập token. Đây chưa phải kiểm header tự động của client trong TC10.

Đã ghi audit