# A/B Experiment Report: My Document

**Experiment ID:** EXP-___
**Owner:** Your Name
**Duration:** Start - End
**Status:** Complete

---

## Hypothesis

If we [change], then [primary metric] will [improve] by [X%] because [reason].

## Setup

| Parameter | Value |
|-----------|-------|
| Variants | Control vs Treatment |
| Traffic Split | 50/50 |
| Sample Size | N per variant |
| Duration | X days |

## Results

| Metric | Control | Treatment | Δ | CI (95%) | p-value |
|--------|---------|-----------|---|----------|---------|
| Primary: CVR | X% | Y% | +Z% | [a, b] | 0.0X |
| Revenue/User | $X | $Y | +$Z | | |
| Bounce Rate | X% | Y% | -Z% | | |

## Statistical Significance

$$
z = \frac{\\hat{p}_1 - \\hat{p}_2}{\sqrt{\\hat{p}(1-\\hat{p})(\frac{1}{n_1} + \frac{1}{n_2})}}
$$

**Result:** Statistically significant at α = 0.05? **Yes / No**

## Guardrails

- [ ] Page load time: No degradation
- [ ] Error rate: Within threshold
- [ ] Revenue: No negative impact

## Decision

**Ship / No Ship / Iterate**

Rationale:
