# A/B Test: My Document

**Owner:** Your Name
**Date:** YYYY-MM-DD
**Status:** Draft | Running | Complete

---

## Hypothesis

If we [change], then [metric] will [improve/decrease] because [reason].

## Variants

| Variant | Description | Traffic Split |
|---------|-------------|---------------|
| Control (A) | Current experience | 50% |
| Treatment (B) | New experience | 50% |

## Primary Metric

**Metric:** Conversion Rate
**Current Baseline:** X%
**Minimum Detectable Effect:** Y%

## Sample Size

$$
n = \frac{(Z_{\\alpha/2} + Z_\\beta)^2 \\cdot 2p(1-p)}{\\delta^2}
$$

**Required:** ~N users per variant
**Estimated Duration:** X weeks

## Secondary Metrics

| Metric | Expected Impact |
|--------|-----------------|
| Revenue per user | +5% |
| Bounce rate | -3% |
| Session duration | Neutral |

## Guardrail Metrics

- Page load time ≤ 2s
- Error rate ≤ 0.1%
- Support tickets: no increase

## Results

*(Fill in after test completion)*

| Metric | Control | Treatment | Δ | p-value | Significant? |
|--------|---------|-----------|---|---------|-------------|
|        |         |           |   |         |             |

## Decision

☐ Ship Treatment ☐ Keep Control ☐ Iterate
