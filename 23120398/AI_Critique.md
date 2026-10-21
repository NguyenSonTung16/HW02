# AI Critique: Critical Reflection on AI Collaboration

**Course:** CSC13003 – Software Engineering / Software Testing  
**Assignment:** HW02 – Black-Box Domain Testing with Equivalence Partitioning & Boundary Value Analysis  
**Student ID:** 23120398  
**Student Name:** Võ Thành Minh Tuệ  

---

Trong testing assignment này, AI đã chứng minh hiệu suất vượt trội trong việc drafting các equivalence classes ban đầu và boundary test matrices, tuy nhiên nó bộc lộ những blind spots nghiêm trọng cùng các giả định hời hợt đòi hỏi sự verification chặt chẽ từ con người. Cụ thể, AI gặp khó khăn với các negative boundary scenarios và các lỗ hổng ở cấp độ implementation-level.

Trong FR-03, AI đã generate các regex boundary tests thông thường nhưng thất bại trong việc phát hiện ra rằng regex thực tế của ứng dụng lại nghịch lý ở chỗ bắt buộc phải có khoảng trắng trong khi lại cấm các ký tự đặc biệt hợp lệ như @ hoặc $. Trong FR-08, AI assume rằng backend sẽ validate order totals và ban đầu đã bỏ sót các edge cases về client-side price tampering nơi các tổng âm hoặc bằng 0 có thể được submit trực tiếp. Tương tự, trong FR-16, AI recommend việc split CSV cơ bản mà không lường trước các rủi ro khi parsing theo chuẩn RFC 4180 (dấu phẩy nằm trong ngoặc kép) hoặc cơ chế rollback của atomic database transaction khi xảy ra batch failure. Cuối cùng, trong FR-20, dù AI đã adjust viewports thành công, nó lại bỏ qua việc password input trên mobile sử dụng type="text", làm lộ plaintext passwords trước nguy cơ shoulder surfing.

Những failure này xảy ra do LLM phụ thuộc vào normative training priors—mặc định rằng các standard software practices luôn tồn tại—và hoạt động thuần túy dựa trên các mô tả trong prompt thay vì inspect các thuộc tính DOM thực tế hay các stateful execution paths. Nguyên tắc cốt lõi rút ra là AI phải được coi như một accelerator, không phải một autonomous oracle. Human testers phải trực tiếp dẫn dắt testing strategy, và validate các kết quả automated test so với hành vi runtime thực tế của SUT.
