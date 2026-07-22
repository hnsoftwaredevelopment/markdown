# My Document

**Date:** YYYY-MM-DD

---

## Configuration Parity

| Config | Dev | Staging | Production | Parity? |
|--------|-----|---------|------------|---------|
| Node version | 20.x | 20.x | 20.x | ✅ |
| DB engine | Postgres 16 | Postgres 16 | Postgres 16 | ✅ |
| Redis version | 7.0 | 7.0 | 7.0 | ✅ |
| Instance type | t3.small | t3.medium | t3.large | ⚠️ Expected |
| Feature flags | All on | Matches prod | Controlled | ✅ |
| HTTPS | ❌ | ✅ | ✅ | ⚠️ Dev uses HTTP |
| Log level | DEBUG | INFO | WARN | ✅ Expected |

## Env Variables

| Variable | Dev | Staging | Production | Notes |
|----------|-----|---------|------------|-------|
| `API_URL` | localhost | staging.api.com | api.com | |
| `DB_POOL` | 5 | 20 | 50 | Scaled by env |
| `SENTRY_DSN` | - | ✅ | ✅ | Not in dev |

## Known Discrepancies

| # | Discrepancy | Risk | Action |
|---|-------------|------|--------|
| 1 | Dev uses HTTP | Low | Accept (local dev) |
| 2 | Dev DB pool is smaller | Medium | Could hide connection issues |
