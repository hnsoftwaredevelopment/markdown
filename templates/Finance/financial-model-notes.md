# My Document

**Model:** Model Name
**Date:** YYYY-MM-DD
**Author:** Your Name

---

## Assumptions

| Assumption | Value | Source | Sensitivity |
|-----------|-------|--------|-------------|
| Growth rate | 15% MoM | Historical | High |
| Churn rate | 5% monthly | Industry avg | Medium |
| ARPU | $49 | Current pricing | Low |
| CAC | $120 | Blended | High |
| Gross margin | 80% | Current | Low |

## Revenue Forecast

| Month | Users | New | Churned | Revenue |
|-------|-------|-----|---------|---------|
| M1 | 1,000 | 150 | 50 | $49K |
| M2 | 1,100 | 165 | 55 | $54K |
| M3 | 1,210 | 182 | 61 | $59K |
| M6 | 1,611 | | | $79K |
| M12 | 2,596 | | | $127K |

## Unit Economics

$$
LTV = \frac{ARPU \\times Gross\\;Margin}{Churn\\;Rate} = \frac{49 \\times 0.80}{0.05} = \\$784
$$

$$
LTV:CAC = \frac{784}{120} = 6.5x
$$

## Key Scenarios

| Scenario | Growth | Churn | M12 Revenue |
|----------|--------|-------|-------------|
| Base | 15% | 5% | $127K |
| Bull | 20% | 3% | $185K |
| Bear | 10% | 8% | $78K |
