# Báo Cáo Nộp Bài - Lab 17: Zep Multi-Memory Agent

## 1. Ba câu hỏi cốt lõi
- **Layer quan trọng nhất**: **Long-term Memory** (Context Block + facts) quan trọng nhất trong bộ test này, quyết định các case **E02, E03, E08, E09** (và 7/20 case Golden). Layer này duy trì profile user, công nghệ ưu tiên và ràng buộc dự án qua nhiều session.
- **Trade-off Zep vs Redis+Qdrant**: Zep tự động tổng hợp graph entity, trích xuất fact theo thời gian (temporal validity), nén context và cách ly user out-of-the-box. Ngược lại, Redis+Qdrant tự dựng tốn công xây dựng pipeline chunking, embedding, tự xử lý conflict/recency và bảo trì schema phức tạp.
- **Guardrail chống Memory Poisoning**: Kiểm tra Consent registry (`consent.json`), cô lập namespace theo `user_id`, lọc dữ liệu đầu vào theo provenance/confidence score, và cung cấp Right-to-be-forgotten API (`zep.user.delete` / `forget.py`).

## 2. Phân tích kết quả Benchmark
- **Layer hit rate thấp nhất**: Baseline `no_memory` đạt **18.2%** (chỉ pass 2 case short-term E01, E10 do dữ liệu sẵn ở thread current; fail 9/9 case cross-session/episodic/semantic). Agent `student` phục hồi lên **100% (11/11 PASS)**.
- **Case tốn nhiều token nhất**: **E03** và **E08** (long_term) tốn ~1520-1540 tokens do Zep Context Block tổng hợp toàn bộ user summary và fact lịch sử dự án.
- **Context Assembly E07 (Mixed)**: E07 kết hợp Long-term summary (`ORCHID-27`, Python) và Semantic KB (`PAYMENT-RULE-3`). `ContextBudgetManager` áp dụng token budget **10/4/3/3** (Short 1000, Long 400, Episodic 300, Semantic 300) ghép context gọn gàng theo thứ tự ưu tiên.
- **Token reduction vs Hit rate**: Benchmark `no_memory` giảm **81.8%** token nhưng thất bại do bỏ sót toàn bộ bộ nhớ. Token reduction chỉ có ý nghĩa khi đi kèm **Evidence Hit Rate >= 80%** (như `student`: Hit rate 100%, reduction 14.2%).

## 3. Phân tích Case Đặc Biệt
- **E08 Recency**: Khái niệm fact mới (`BLUEBIRD-42` dùng TypeScript + NestJS) ghi đè lên preference cũ nhờ Zep Graph Edges theo dõi khoảng thời hạn hiệu lực (`valid_at`, `invalid_at`).
- **E10 Compaction**: Sliding window giữ lại 4 lượt chat gần nhất, đồng thời Compaction tổng hợp thông tin quan trọng vào `<SESSION_SUMMARY>` và `<DURABLE_NOTES>` để bảo toàn deadline `REVIEW-DEADLINE-1600`.
