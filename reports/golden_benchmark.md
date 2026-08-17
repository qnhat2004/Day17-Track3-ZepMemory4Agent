# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **18/20**
- Evidence hit rate: **90.0%**
- Average retrieval latency: **850.3 ms**
- Average token reduction vs full source context: **16.3%**
- Golden bonus: **0/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| G08 | long_term | FAIL | 2495.5 | 0 | 100.0% | BadRequestError: headers: {'date': 'Mon, 17 Aug 2026 16:51:55 GMT', 'content-type': 'application/json; charset=utf-8', 'content-length': '128', 'connection': 'keep-alive', 'vary': 'Origin', 'x-content-type-options': 'nosniff', 'x-ratelimit-increment': '1', 'x-ratelimit-limit': '300', 'x-ratelimit-remaining': '297', 'x-ratelimit-reset': '1786985520', 'strict-transport-security': 'max-age=2592000', 'cf-cache-status': 'DYNAMIC', 'server': 'cloudflare', 'cf-ray': 'a2ca2fae189c4b09-HKG'}, status_code: 400, body: {'message': 'bad request: session already exists with session_id: eval-g08', 'request_id': 'e1aa79b8-f085-4e1c-8a3d-e3b6baedfdaf'} |
| G09 | long_term | FAIL | 375.8 | 0 | 100.0% | BadRequestError: headers: {'date': 'Mon, 17 Aug 2026 16:51:55 GMT', 'content-type': 'application/json; charset=utf-8', 'content-length': '128', 'connection': 'keep-alive', 'vary': 'Origin', 'x-content-type-options': 'nosniff', 'x-ratelimit-increment': '1', 'x-ratelimit-limit': '300', 'x-ratelimit-remaining': '295', 'x-ratelimit-reset': '1786985520', 'strict-transport-security': 'max-age=2592000', 'cf-cache-status': 'DYNAMIC', 'server': 'cloudflare', 'cf-ray': 'a2ca2fb07ea44b09-HKG'}, status_code: 400, body: {'message': 'bad request: session already exists with session_id: eval-g09', 'request_id': '7eaa9a31-ff59-4452-920e-b0566173c016'} |
| G12 | semantic | PASS | 478.7 | 418 | 8.9% |  |
| G14 | semantic | PASS | 217.5 | 270 | 30.2% |  |
| G15 | semantic | PASS | 222.2 | 270 | 41.2% |  |
| G19 | mixed | PASS | 1470.3 | 581 | 0.0% |  |
| G03 | long_term | PASS | 1171.9 | 1545 | 0.0% |  |
| G04 | long_term | PASS | 1157.4 | 1517 | 0.0% |  |
| G05 | long_term | PASS | 1138.8 | 1534 | 0.0% |  |
| G10 | episodic | PASS | 225.0 | 557 | 0.0% |  |
| G11 | episodic | PASS | 222.9 | 555 | 0.0% |  |
| G13 | semantic | PASS | 225.9 | 416 | 26.4% |  |
| G16 | mixed | PASS | 1371.8 | 581 | 0.0% |  |
| G18 | mixed | PASS | 450.5 | 500 | 11.5% |  |
| G20 | mixed | PASS | 1659.4 | 831 | 0.0% |  |
| G06 | long_term | PASS | 1379.3 | 1539 | 0.0% |  |
| G07 | long_term | PASS | 1235.2 | 1525 | 0.0% |  |
| G17 | mixed | PASS | 1508.6 | 581 | 8.1% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G08 - long_term

``

### G09 - long_term

``

### G12 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped m`

### G14 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G15 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python for this purpose. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 05:16:15     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Lan uu tien stack backend nao cho LOTUS-88?   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples.   - Created At: 2026-08-01 11:00:00     Source: me`

### G03 - long_term

`<USER_SUMMARY> The user's main pursuit is to complete a benchmark report named LAB-REPORT-1600 by Friday at 16:00. The current task involves debugging async HTTP requests. The user has learned that increasing the timeout was ineffective and that reusing the aiohttp ClientSession with a concurrency of 20 resolves connection churn. This approach is considered efficient for the ASYNC-FIX-20 incident. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project's backend. Python is still preferred for the personal demo project ORCHID-27.  The user prefers Python and dislikes Java. When explaining code, the user wants short exampl`

### G04 - long_term

`<USER_SUMMARY> The user's main pursuit is to complete a benchmark report named LAB-REPORT-1600 by Friday at 16:00. The current task involves debugging async HTTP requests. The user has learned that increasing the timeout was ineffective and that reusing the aiohttp ClientSession with a concurrency of 20 resolves connection churn. This approach is considered efficient for the ASYNC-FIX-20 incident. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project's backend. Python is still preferred for the personal demo project ORCHID-27.  The user prefers Python and dislikes Java. When explaining code, the user wants short exampl`

### G05 - long_term

`<USER_SUMMARY> The user's main pursuit is to complete a benchmark report named LAB-REPORT-1600 by Friday at 16:00. The current task involves debugging async HTTP requests. The user has learned that increasing the timeout was ineffective and that reusing the aiohttp ClientSession with a concurrency of 20 resolves connection churn. This approach is considered efficient for the ASYNC-FIX-20 incident. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project's backend. Python is still preferred for the personal demo project ORCHID-27.  The user prefers Python and dislikes Java. When explaining code, the user wants short exampl`

### G10 - episodic

`EPISODE: Tuan nay minh phai them chuc nang retry payment vao dung cai backend cua du an ben cong ty chu khong phai project ca nhan, nen minh can lam theo dung chuan cong nghe ma cong ty bat EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. E`

### G11 - episodic

`EPISODE: Tuan nay minh phai them chuc nang retry payment vao dung cai backend cua du an ben cong ty chu khong phai project ca nhan, nen minh can lam theo dung chuan cong nghe ma cong ty bat EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurr`

### G13 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and `

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's main pursuit is to complete a benchmark report named LAB-REPORT-1600 by Friday at 16:00. The current task involves debugging async HTTP requests. The user has learned that increasing the timeout was ineffective and that reusing the aiohttp ClientSession with a concurrency of 20 resolves connection churn. This approach is considered efficient for the ASYNC-FIX-20 incident. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project's backend. Python is still preferred for the personal demo project ORCHID-27.  The user prefers Python and dislikes Java. When explaining code, the user wants `

### G18 - mixed

`<EPISODIC> EPISODE: Tuan nay minh phai them chuc nang retry payment vao dung cai backend cua du an ben cong ty chu khong phai project ca nhan, nen minh can lam theo dung chuan cong nghe ma cong ty bat EPISODE: Sang mai minh phai hop review tien do voi mentor nen toi nay minh muon don dep lai het may thu con dang do. Minh biet minh con vai viec chua chot xong nhung dau oc dang roi qua kho EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Toi se uu tien timeline khi giai thich coroutin`

### G20 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's main pursuit is to complete a benchmark report named LAB-REPORT-1600 by Friday at 16:00. The current task involves debugging async HTTP requests. The user has learned that increasing the timeout was ineffective and that reusing the aiohttp ClientSession with a concurrency of 20 resolves connection churn. This approach is considered efficient for the ASYNC-FIX-20 incident. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project's backend. Python is still preferred for the personal demo project ORCHID-27.  The user prefers Python and dislikes Java. When explaining code, the user wants `

### G06 - long_term

`<USER_SUMMARY> The user's main pursuit is to complete a benchmark report named LAB-REPORT-1600 by Friday at 16:00. The current task involves debugging async HTTP requests. The user has learned that increasing the timeout was ineffective and that reusing the aiohttp ClientSession with a concurrency of 20 resolves connection churn. This approach is considered efficient for the ASYNC-FIX-20 incident. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project's backend. Python is still preferred for the personal demo project ORCHID-27.  The user prefers Python and dislikes Java. When explaining code, the user wants short exampl`

### G07 - long_term

`<USER_SUMMARY> The user's main pursuit is to complete a benchmark report named LAB-REPORT-1600 by Friday at 16:00. The current task involves debugging async HTTP requests. The user has learned that increasing the timeout was ineffective and that reusing the aiohttp ClientSession with a concurrency of 20 resolves connection churn. This approach is considered efficient for the ASYNC-FIX-20 incident. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project's backend. Python is still preferred for the personal demo project ORCHID-27.  The user prefers Python and dislikes Java. When explaining code, the user wants short exampl`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's main pursuit is to complete a benchmark report named LAB-REPORT-1600 by Friday at 16:00. The current task involves debugging async HTTP requests. The user has learned that increasing the timeout was ineffective and that reusing the aiohttp ClientSession with a concurrency of 20 resolves connection churn. This approach is considered efficient for the ASYNC-FIX-20 incident. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project's backend. Python is still preferred for the personal demo project ORCHID-27.  The user prefers Python and dislikes Java. When explaining code, the user wants `
