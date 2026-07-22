# My Document

**Service:** Service Name
**Date:** YYYY-MM-DD

---

## Current Usage

| Resource | Current | Capacity | Utilization |
|----------|---------|----------|-------------|
| CPU | 45% | 8 cores | 45% |
| Memory | 6 GB | 16 GB | 37.5% |
| Disk I/O | 5K IOPS | 16K IOPS | 31% |
| Network | 200 Mbps | 1 Gbps | 20% |
| DB connections | 80 | 200 | 40% |

## Growth Projections

| Metric | Current | +3 Mo | +6 Mo | +12 Mo |
|--------|---------|-------|-------|--------|
| Users | 10K | 15K | 25K | 50K |
| Requests/sec | 500 | 750 | 1,250 | 2,500 |
| Storage (GB) | 100 | 150 | 250 | 500 |

## Scaling Triggers

| Resource | Warning (70%) | Critical (85%) | Action |
|----------|--------------|----------------|--------|
| CPU | Alert | Scale out +1 | Auto-scaling group |
| Memory | Alert | Upgrade instance | Manual |
| Disk | Alert | Expand volume | Automated |

## Cost Forecast

| Timeline | Infra Cost | Delta |
|----------|-----------|-------|
| Today | $X/mo | - |
| +3 months | $Y/mo | +$Z |
| +12 months | $A/mo | +$B |
