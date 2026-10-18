Mình đề xuất quay **một video khoảng 10–15 phút trên FR-02**, đi từ dùng skill thiết kế test đến chạy và ghi kết quả. Đây là thời lượng gợi ý; đề chỉ yêu cầu video thể hiện quá trình từ đầu đến cuối trên một chức năng hoàn chỉnh (mục 7, trang 3).

| Phần quay | Thao tác và nội dung cần nói |
| --- | --- |
| **1. Giới thiệu ngắn** | Nêu FR-02 và quy tắc chính: đăng nhập, sai 3 lần khóa 30 giây. Mở đặc tả và slide S04 làm căn cứ. |
| **2. Cho thấy skill được dùng** | Mở `SKILL.md` của `domain-testing` và `boundary-value-analysis`, chỉ ra quy trình và mẫu đầu ra. Khi gọi skill, quay cả thao tác AI đọc skill. |
| **3. Demo Domain Testing** | Yêu cầu AI thực hiện lần lượt: Input/Output → EC → đại diện từng EC → TC rút gọn. Đối chiếu kết quả với cấu trúc 2.1–2.4 và giải thích một ví dụ gộp nhiều EC thành một TC. |
| **4. Demo BVA và rà soát** | Dùng skill BVA chọn điểm quanh ngưỡng khóa và thời hạn 30 giây. Mở mục 2.6 để giải thích sai sót thực tế đã phát hiện: lần sai thứ 1 không phải điểm sát ngưỡng 3. |
| **5. Chạy test** | Thực hiện bộ test FR-02, thể hiện dữ liệu, trạng thái ban đầu, expected/actual và kết luận. Có thể tua nhanh đoạn chờ khóa, nhưng giữ rõ mốc thời gian. |
| **6. Tổng kết** | Mở kết quả chạy và README; nêu số test đã chạy, pass/fail/chưa chạy, bug nếu có. Cho thấy audit ghi lại prompt/output và nơi lưu các skill. |

Bạn có thể dùng hai prompt sau khi quay:

**Demo Domain Testing:**

> Dùng skill domain-testing cho FR-02, dựa trên README EShop và S04. Trình bày lần lượt yêu cầu, Input/Output, EC, bảng đại diện từng EC và bảng TC rút gọn theo cấu trúc đã chốt. Giải thích ngắn lý do phân lớp và gộp test. Trước mắt trình bày trong chat, chưa sửa báo cáo hiện tại.

**Demo BVA:**

> Dùng skill boundary-value-analysis cho FR-02 theo S04 trang 26–27. Xác định ngưỡng, chọn điểm dưới/tại/trên ngưỡng và lập bảng test gồm điều kiện kiểm tra, đầu vào, đầu ra mong đợi. Phân biệt lần gửi đăng nhập với bộ đếm; chỉ rõ phần chưa đủ đặc tả để chốt expected. Chưa thực thi test.

**Phần bạn giải thích trực tiếp là quan trọng:** vì sao chọn EC, vì sao gộp TC, vì sao chọn điểm biên và bạn đã sửa AI như thế nào. Không cần đọc lại toàn bộ bảng.

Riêng **TC tại đúng 30 giây hiện còn chờ xác nhận**: trước khi quay bản hoàn chỉnh, cần chốt expected và cách kiểm soát thời gian. Nếu chưa giải quyết, thể hiện đúng là chưa kết luận, không báo Pass.

Cuối cùng, đăng video lên YouTube và đặt liên kết trong README.

Đã ghi audit