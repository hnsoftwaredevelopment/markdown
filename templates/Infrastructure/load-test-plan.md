# My Document

**Service:** Service Name
**Date:** YYYY-MM-DD
**Tool:** k6 / Locust / JMeter

---

## Test Scenarios

| Scenario | Endpoint | Method | Payload | Think Time |
|----------|----------|--------|---------|------------|
| Homepage | `/` | GET | - | 2s |
| Login | `/api/auth` | POST | Credentials | 3s |
| Dashboard | `/api/dashboard` | GET | - | 5s |
| File Upload | `/api/upload` | POST | 5MB file | 10s |

## Load Profile

| Phase | Duration | Virtual Users | Ramp |
|-------|----------|---------------|------|
| Warm-up | 2 min | 10 | Linear |
| Ramp-up | 5 min | 10 → 200 | Linear |
| Steady state | 10 min | 200 | Flat |
| Spike | 2 min | 500 | Immediate |
| Cool-down | 3 min | 500 → 0 | Linear |

## Acceptance Criteria

| Metric | Threshold |
|--------|-----------|
| p95 Response Time | < 500ms |
| p99 Response Time | < 2s |
| Error Rate | < 1% |
| Throughput | > 1000 req/s |

## Results

*(Fill after test)*

| Metric | Result | Pass? |
|--------|--------|-------|
| p95 | | |
| p99 | | |
| Error Rate | | |
| Throughput | | |
