# My Document

**Date:** YYYY-MM-DD

---

## Metric: Monthly Active Users (MAU)

| Property | Value |
|----------|-------|
| **What it measures** | Unique users with ≥1 event in 30 days |
| **Formula** | `COUNT(DISTINCT user_id) WHERE timestamp >= NOW() - 30d` |
| **Data Source** | Events table |
| **Owner** | Product team |
| **Update Frequency** | Daily |
| **Current Value** | |
| **Target** | |

## Caveats

- Bots and test accounts are excluded (`WHERE is_bot = false`)
- Users with only `page_view` events are counted (intentional)
- Timezone: UTC

## Segments

| Segment | Current | Target |
|---------|---------|--------|
| Free | | |
| Pro | | |
| Enterprise | | |

## Related Metrics

- **DAU** - daily version
- **WAU** - weekly version
- **DAU/MAU Ratio** - stickiness indicator (benchmark: >20%)
