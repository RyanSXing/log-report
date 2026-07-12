Analyze the Apache-style access log at `/app/access.log` and write the summary to
`/app/report.json`.

Success criteria:

1. `/app/report.json` is a valid JSON object containing exactly the keys
   `total_requests`, `unique_ips`, and `top_path`.
2. `total_requests` is the number of non-empty request lines in the log.
3. `unique_ips` is the number of distinct client IP addresses in the log.
4. `top_path` is the request path that occurs most often.
