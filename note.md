# Giải Thích Dự Án & Kiến Trúc Memory (Lab 17)

## 1. Dữ liệu lấy ở đâu?
- Dữ liệu thử nghiệm và benchmark nằm tại `data/sessions.json`, chứa các lịch sử hội thoại giả lập của 2 user (`minh-lab17`, `lan-lab17`) và các tài liệu domain KB dùng chung.
- Quy định quyền riêng tư và Opt-in memory được quản lý trong `data/consent.json`. Ingestion sẽ kiểm tra `memory_opt_in == True` trước khi đẩy vào Zep.

## 2. Ngân sách phân chia như thế nào? (Token Budget)
- Agent quy định tổng giới hạn context budget (mặc định **2000 tokens**).
- Phân bổ theo tỷ lệ **10 : 4 : 3 : 3** trong `src/context_budget.py` (`ContextBudgetManager`):
  1. **Short-term Memory**: 1000 tokens (50%) - Ưu tiên hàng đầu (Short-term buffer/summary/sliding).
  2. **Long-term Memory**: 400 tokens (20%) - User summary & profile context block từ Zep.
  3. **Episodic Memory**: 300 tokens (15%) - Lịch sử trải nghiệm / trajectory sự cố cũ.
  4. **Semantic Memory**: 300 tokens (15%) - Quy tắc domain / KB tài liệu dùng chung.
- Thứ tự ưu tiên cắt nén & ghép context: **Short-term -> Long-term -> Episodic -> Semantic**.

## 3. Code Retrieval & Kỹ thuật cập nhật đoạn chat session cũ
- **Code Retrieval (`src/memory_student.py`)**:
  - `retrieve_long_term`: Đẩy turn hiện tại bằng `prime_eval_thread`, lấy `thread.get_user_context` (Context Block) và `graph.search(user_id, scope="edges", limit=20)` để lấy facts kèm mốc thời gian (validity ranges).
  - `retrieve_episodic`: Gọi `graph.search(user_id, scope="episodes", limit=15)` thu thập episodes phản ánh trải nghiệm quá khứ.
  - `retrieve_semantic`: Gọi `graph.search(graph_id="shared-kb", scope="episodes", limit=8)` trên standalone graph dùng chung.
- **Kỹ thuật cập nhật session cũ (Compaction & Sliding Window)**:
  - Khi conversation kéo dài, `ShortTermMemory` kết hợp **Sliding Window** (chỉ giữ 4-6 turn gần nhất cho context ngắn) với **Compaction Summary** (tóm tắt lượt thoại quá hạn) và **Durable Notes** (lưu lại các mốc quan trọng như `REVIEW-DEADLINE-1600`).

## 4. Graph được build như thế nào, có gọi tool gì không?
- Graph được khởi tạo tự động thông qua script `python -m src.seed`:
  - **User Graph**: Tạo user qua `client.user.add(user_id=...)` và đẩy lịch sử nhắn tin qua `client.thread.add_messages(...)`.
  - **Standalone Semantic Graph**: Tạo graph dùng chung qua `client.graph.add(graph_id="shared-kb", ...)` và ingest các tài liệu quy trình.
- **Zep Cloud V3 tự động hoàn toàn (No manual tool calls)**: Khi nhận messages/documents, Zep Cloud tự động chạy pipeline ngầm để trích xuất Entities (nodes), Relations & Temporal Facts (edges với `valid_at`/`invalid_at`), và Episodes mà agent không cần gọi tool trích xuất thủ công.