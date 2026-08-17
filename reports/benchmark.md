# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **3/11**
- Evidence hit rate: **27.3%**
- Average retrieval latency: **792.8 ms**
- Average token reduction vs full source context: **59.1%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| E06 | semantic | PASS | 2383.7 | 148 | 67.8% |  |
| E09 | long_term | FAIL | 1094.9 | 23 | 47.7% | missing=LOTUS-88, Java, Spring Boot |
| E10 | short_term | PASS | 0.2 | 195 | 0.0% |  |
| E02 | long_term | FAIL | 1059.4 | 116 | 47.5% | missing=Python |
| E03 | long_term | FAIL | 1055.4 | 116 | 47.5% | missing=benchmark report, 16:00 |
| E04 | episodic | FAIL | 347.4 | 22 | 90.0% | missing=ClientSession, concurrency=20, ASYNC-FIX-20 |
| E05 | episodic | FAIL | 221.4 | 22 | 90.0% | missing=connection churn, timeout threshold |
| E07 | mixed | FAIL | 1298.3 | 184 | 67.4% | missing=Python |
| E11 | semantic | FAIL | 217.6 | 0 | 100.0% | missing=connection pooling, CONN-POOL-FIRST |
| E08 | long_term | FAIL | 1042.7 | 24 | 91.7% | missing=BLUEBIRD-42, TypeScript, NestJS |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata=`

### E09 - long_term

`<USER_SUMMARY> user with the id of lan-lab17, name of Lan Tran and email . </USER_SUMMARY>`

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`<USER_SUMMARY> user with the id of minh-lab17, name of Minh Nguyen and email . </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 16:54:23     Source: message     Content: [user] {   "user_id": "minh-lab17",   "first_name": "Minh",   "last_name": "Nguyen",   "user_alias": "Evaluation User" }: Hay chon huong dan code retry payment phu hop voi preference ca nhan cua Minh. </EPISODES>`

### E03 - long_term

`<USER_SUMMARY> user with the id of minh-lab17, name of Minh Nguyen and email . </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 16:54:23     Source: message     Content: [user] {   "user_id": "minh-lab17",   "first_name": "Minh",   "last_name": "Nguyen",   "user_alias": "Evaluation User" }: Hay chon huong dan code retry payment phu hop voi preference ca nhan cua Minh. </EPISODES>`

### E04 - episodic

`EPISODE: Hay chon huong dan code retry payment phu hop voi preference ca nhan cua Minh.`

### E05 - episodic

`EPISODE: Hay chon huong dan code retry payment phu hop voi preference ca nhan cua Minh.`

### E07 - mixed

`<LONG_TERM> <USER_SUMMARY> user with the id of minh-lab17, name of Minh Nguyen and email . </USER_SUMMARY> </LONG_TERM>  <SEMANTIC> EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-`

### E11 - semantic

``

### E08 - long_term

`<USER_SUMMARY> user with the id of minh-lab17, name of Minh Nguyen and email . </USER_SUMMARY>`
