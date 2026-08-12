# My Document

**Database:** PostgreSQL / MySQL
**Last Updated:** YYYY-MM-DD

---

## Daily Active Users

```sql
SELECT
    DATE(timestamp) AS day,
    COUNT(DISTINCT user_id) AS dau
FROM events
WHERE timestamp >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY DATE(timestamp)
ORDER BY day;
```

## Retention by Cohort (Week 1)

```sql
WITH cohorts AS (
    SELECT
        user_id,
        DATE_TRUNC('week', MIN(created_at)) AS cohort_week
    FROM users
    GROUP BY user_id
)
SELECT
    c.cohort_week,
    COUNT(DISTINCT c.user_id) AS cohort_size,
    COUNT(DISTINCT e.user_id) AS returned,
    ROUND(COUNT(DISTINCT e.user_id)::numeric / COUNT(DISTINCT c.user_id) * 100, 1) AS retention_pct
FROM cohorts c
LEFT JOIN events e ON c.user_id = e.user_id
    AND e.timestamp BETWEEN c.cohort_week + INTERVAL '7 days'
                        AND c.cohort_week + INTERVAL '14 days'
GROUP BY c.cohort_week
ORDER BY c.cohort_week;
```

## Revenue by Plan

```sql
SELECT
    plan,
    COUNT(*) AS subscribers,
    SUM(amount) AS mrr
FROM subscriptions
WHERE status = 'active'
GROUP BY plan
ORDER BY mrr DESC;
```

## Funnel Conversion

```sql
SELECT
    COUNT(DISTINCT CASE WHEN event_name = 'signup' THEN user_id END) AS signups,
    COUNT(DISTINCT CASE WHEN event_name = 'onboarding_complete' THEN user_id END) AS onboarded,
    COUNT(DISTINCT CASE WHEN event_name = 'purchase' THEN user_id END) AS purchased
FROM events
WHERE timestamp >= CURRENT_DATE - INTERVAL '30 days';
```

## Tips

- Use `EXPLAIN ANALYZE` to check query performance
- Add indexes on frequently filtered columns
- Use CTEs for readability over subqueries
