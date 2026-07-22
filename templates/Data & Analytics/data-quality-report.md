# My Document - Month YYYY

**Analyst:** Your Name
**Database:** Production

---

## Quality Dimensions

| Dimension | Score | Target | Status |
|-----------|-------|--------|--------|
| Completeness | 94% | >95% | 🟡 |
| Accuracy | 99% | >99% | ✅ |
| Consistency | 97% | >95% | ✅ |
| Timeliness | 100% | >99% | ✅ |
| Uniqueness | 99.8% | >99% | ✅ |

## Issues Found

| # | Table | Column | Issue | Severity | Records |
|---|-------|--------|-------|----------|---------|
| 1 | users | email | 6% have NULL email | High | 1,200 |
| 2 | events | timestamp | 12 records with future dates | Medium | 12 |
| 3 | orders | amount | 3 negative values | Low | 3 |

## Remediation

| Issue | Action | Owner | ETA | Status |
|-------|--------|-------|-----|--------|
| NULL emails | Backfill from CRM | Data Eng | This week | 🔵 |
| Future dates | Fix ingestion pipeline | Backend | Next sprint | ⬜ |

## Trends

Overall data quality score trend: 94% → target 97% by end of quarter.
