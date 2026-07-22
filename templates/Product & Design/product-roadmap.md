# My Document

**Product:** Product Name
**Last Updated:** YYYY-MM-DD

---

## Roadmap Timeline

```mermaid
gantt
    title Product Roadmap
    dateFormat YYYY-MM-DD
    section Now
    Feature A           :active, a1, 2026-01-01, 30d
    Feature B           :a2, after a1, 21d
    section Next
    Feature C           :a3, after a2, 30d
    Feature D           :a4, after a2, 45d
    section Later
    Feature E           :a5, after a4, 30d
    Feature F           :a6, after a5, 30d
```

## Now (This Quarter)

| Feature | Owner | Status | Target |
|---------|-------|--------|--------|
| Feature A | @name | 🔵 In Progress | Jan 30 |
| Feature B | @name | ⬜ Not Started | Feb 21 |

## Next (Next Quarter)

| Feature | Owner | Status | Dependencies |
|---------|-------|--------|-------------|
| Feature C | TBD | 💡 Planned | Feature A |
| Feature D | TBD | 💡 Planned | None |

## Later (Backlog)

- Feature E - brief description
- Feature F - brief description

## Themes

| Theme | Goal | Features |
|-------|------|----------|
| Growth | Increase activation | A, B |
| Retention | Reduce churn | C, D |
| Platform | Technical foundation | E, F |
