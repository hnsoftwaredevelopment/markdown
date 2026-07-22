# My Document

**Dashboard:** Dashboard Name
**Owner:** Your Name
**Date:** YYYY-MM-DD

---

## Purpose

What business question does this dashboard answer?

## Metrics

| # | Metric | Type | Source | Refresh |
|---|--------|------|--------|---------|
| 1 | DAU | Counter | Events DB | Hourly |
| 2 | Conversion Rate | Percentage | Analytics | Daily |
| 3 | Revenue | Currency | Billing API | Real-time |
| 4 | Churn Rate | Percentage | CRM | Weekly |

## Layout

| Position | Widget | Metric | Chart Type |
|----------|--------|--------|------------|
| Top Row L | KPI Card | DAU | Number |
| Top Row C | KPI Card | Conversion | Number + trend |
| Top Row R | KPI Card | Revenue | Number + sparkline |
| Middle | Time series | DAU over time | Line chart |
| Bottom L | Breakdown | Revenue by plan | Pie chart |
| Bottom R | Table | Top users | Data table |

## Filters

- Date range (default: last 30 days)
- Plan type
- Region

## Access

| Role | Access Level |
|------|-------------|
| Exec | View |
| PM | View + Filter |
| Data | Edit |
