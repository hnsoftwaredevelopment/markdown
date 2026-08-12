# My Document

**Last Updated:** YYYY-MM-DD
**Review Cadence:** Quarterly

---

## Recovery Objectives

| Metric | Target | Current |
|--------|--------|---------|
| **RPO** (Recovery Point Objective) | 1 hour | |
| **RTO** (Recovery Time Objective) | 4 hours | |

## Disaster Scenarios

| Scenario | Likelihood | Impact | Recovery Steps |
|----------|-----------|--------|----------------|
| Region outage | Low | Critical | Failover to DR region |
| Database corruption | Medium | High | Restore from backup |
| DDoS attack | Medium | Medium | Activate CloudFlare rules |
| Key compromise | Low | Critical | Rotate all keys, audit |

## Failover Procedure

1. **Detect:** Monitoring alerts trigger
2. **Assess:** On-call determines severity (P1/P2/P3)
3. **Communicate:** Notify stakeholders via PagerDuty + Slack
4. **Execute:** Follow runbook for specific scenario
5. **Verify:** Confirm services are healthy in DR
6. **Post-mortem:** Document within 48 hours

## Backup Schedule

| System | Method | Frequency | Retention | Location |
|--------|--------|-----------|-----------|----------|
| Database | pg_dump + WAL | Hourly | 30 days | S3 Cross-Region |
| Files | S3 replication | Real-time | Indefinite | DR Region |
| Config | Git | Every commit | Indefinite | GitHub |

## Communication Plan

| Audience | Channel | Who Notifies | Within |
|----------|---------|-------------|--------|
| Engineering | Slack #incidents | On-call | 5 min |
| Leadership | Email + Slack | Engineering Manager | 30 min |
| Customers | Status page | Comms team | 1 hour |

## Test Schedule

- [ ] Quarterly DR drill
- [ ] Last drill date: ___
- [ ] Next drill date: ___
