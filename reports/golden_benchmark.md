# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1331.8 ms**
- Average token reduction vs full source context: **6.7%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| G08 | long_term | PASS | 3620.6 | 732 | 0.0% |  |
| G09 | long_term | PASS | 2099.2 | 996 | 0.0% |  |
| G12 | semantic | PASS | 208.1 | 370 | 19.4% |  |
| G14 | semantic | PASS | 414.5 | 314 | 18.9% |  |
| G15 | semantic | PASS | 419.1 | 314 | 31.6% |  |
| G19 | mixed | PASS | 1505.8 | 581 | 0.0% |  |
| G03 | long_term | PASS | 1632.6 | 996 | 0.0% |  |
| G04 | long_term | PASS | 1701.8 | 996 | 0.0% |  |
| G05 | long_term | PASS | 1665.7 | 996 | 0.0% |  |
| G10 | episodic | PASS | 802.6 | 272 | 0.0% |  |
| G11 | episodic | PASS | 773.0 | 272 | 0.0% |  |
| G13 | semantic | PASS | 463.6 | 314 | 44.4% |  |
| G16 | mixed | PASS | 2068.8 | 581 | 0.0% |  |
| G18 | mixed | PASS | 1177.2 | 500 | 11.5% |  |
| G20 | mixed | PASS | 2642.1 | 831 | 0.0% |  |
| G06 | long_term | PASS | 1688.6 | 996 | 0.0% |  |
| G07 | long_term | PASS | 1745.7 | 996 | 0.0% |  |
| G17 | mixed | PASS | 2006.1 | 581 | 8.1% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G08 - long_term

`SESSION NOTE (lan-s1): Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.  <USER_SUMMARY> Lan's project is LOTUS-88. Lan prioritizes Java and Spring Boot and does not use Python for the backend.  Lan's project is LOTUS-88. Lan prioritizes Java and Spring Boot and does not use Python for the backend.  Lan prioritizes Java and Spring Boot. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du`

### G09 - long_term

`SESSION NOTE (minh-s3): Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27.  SESSION NOTE (minh-s2): Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail.  SESSION NOTE (minh-s2): Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20.  SESSION NOTE (minh-s1): Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan.  SESSION NOTE (minh-s1): Toi dang hoc async/await va `

### G12 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata=  KNOWLEDGE (kb-payment-retry): For POST /payments, every retryable request MUST send the same Idempotency-K`

### G14 - semantic

`ENTITY: PAYMENT-RULE-3 -  ENTITY: transient 5xx errors -  ENTITY: Idempotency-Key -  ENTITY: Payment API Retry Policy - For POST /payments, every retryable request must send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. ENTITY: max-3-retries -  ENTITY: HTTP 429 -   KNOWLEDGE (kb-payment-retry): For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.  KNOWLEDGE (kb-async-http): When async HTTP calls time out, inspect connection pooling, downstre`

### G15 - semantic

`ENTITY: transient 5xx errors -  ENTITY: Idempotency-Key -  ENTITY: PAYMENT-RULE-3 -  ENTITY: Payment API Retry Policy - For POST /payments, every retryable request must send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. ENTITY: max-3-retries -  ENTITY: HTTP 429 -   KNOWLEDGE (kb-payment-retry): For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.  KNOWLEDGE (kb-async-http): When async HTTP calls time out, inspect connection pooling, downstre`

### G19 - mixed

`<LONG_TERM> SESSION NOTE (lan-s1): Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.  <USER_SUMMARY> Lan's project is LOTUS-88. Lan prioritizes Java and Spring Boot and does not use Python for the backend.  Lan's project is LOTUS-88. Lan prioritizes Java and Spring Boot and does not use Python for the backend.  Lan prioritizes Java and Spring Boot. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: To`

### G03 - long_term

`SESSION NOTE (minh-s3): Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27.  SESSION NOTE (minh-s2): Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail.  SESSION NOTE (minh-s2): Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20.  SESSION NOTE (minh-s1): Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan.  SESSION NOTE (minh-s1): Toi dang hoc async/await va `

### G04 - long_term

`SESSION NOTE (minh-s3): Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27.  SESSION NOTE (minh-s2): Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail.  SESSION NOTE (minh-s2): Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20.  SESSION NOTE (minh-s1): Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan.  SESSION NOTE (minh-s1): Toi dang hoc async/await va `

### G05 - long_term

`SESSION NOTE (minh-s3): Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27.  SESSION NOTE (minh-s2): Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail.  SESSION NOTE (minh-s2): Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20.  SESSION NOTE (minh-s1): Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan.  SESSION NOTE (minh-s1): Toi dang hoc async/await va `

### G10 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan.  EPISODE (minh-s3): Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27.  EPISODE (minh-s2): Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail.  EPISODE (minh-s2): Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20.  `

### G11 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan.  EPISODE (minh-s3): Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27.  EPISODE (minh-s2): Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail.  EPISODE (minh-s2): Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20.  `

### G13 - semantic

`ENTITY: HTTP 429 -  ENTITY: transient 5xx errors -  ENTITY: Payment API Retry Policy - For POST /payments, every retryable request must send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. ENTITY: max-3-retries -  ENTITY: Idempotency-Key -  ENTITY: PAYMENT-RULE-3 -   KNOWLEDGE (kb-payment-retry): For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.  KNOWLEDGE (kb-async-http): When async HTTP calls time out, inspect connection pooling, downstre`

### G16 - mixed

`<LONG_TERM> SESSION NOTE (minh-s3): Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27.  SESSION NOTE (minh-s2): Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail.  SESSION NOTE (minh-s2): Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20.  SESSION NOTE (minh-s1): Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan.  SESSION NOTE (minh-s1): Toi dang hoc asy`

### G18 - mixed

`<EPISODIC> EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan.  EPISODE (minh-s3): Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27.  EPISODE (minh-s2): Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail.  EPISODE (minh-s2): Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYN`

### G20 - mixed

`<LONG_TERM> SESSION NOTE (minh-s3): Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27.  SESSION NOTE (minh-s2): Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail.  SESSION NOTE (minh-s2): Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20.  SESSION NOTE (minh-s1): Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan.  SESSION NOTE (minh-s1): Toi dang hoc asy`

### G06 - long_term

`SESSION NOTE (minh-s3): Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27.  SESSION NOTE (minh-s2): Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail.  SESSION NOTE (minh-s2): Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20.  SESSION NOTE (minh-s1): Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan.  SESSION NOTE (minh-s1): Toi dang hoc async/await va `

### G07 - long_term

`SESSION NOTE (minh-s3): Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27.  SESSION NOTE (minh-s2): Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail.  SESSION NOTE (minh-s2): Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20.  SESSION NOTE (minh-s1): Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan.  SESSION NOTE (minh-s1): Toi dang hoc async/await va `

### G17 - mixed

`<LONG_TERM> SESSION NOTE (minh-s3): Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27.  SESSION NOTE (minh-s2): Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail.  SESSION NOTE (minh-s2): Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20.  SESSION NOTE (minh-s1): Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan.  SESSION NOTE (minh-s1): Toi dang hoc asy`
