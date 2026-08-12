# My Document

**Service:** Service Name
**Last Updated:** YYYY-MM-DD
**Owner:** Team Name

---

## Deployment Flow

```mermaid
graph TD
    A[Code Merged] --> B[CI Build]
    B --> C{Tests Pass?}
    C -->|Yes| D[Deploy to Staging]
    C -->|No| E[Fix & Retry]
    D --> F[QA Verification]
    F --> G{Approved?}
    G -->|Yes| H[Deploy to Production]
    G -->|No| E
    H --> I[Smoke Tests]
    I --> J{Healthy?}
    J -->|Yes| K[Done ✅]
    J -->|No| L[Rollback]
```

## Environment Configuration

| Setting         | Staging              | Production           |
|-----------------|----------------------|----------------------|
| URL             |                      |                      |
| Database        |                      |                      |
| API Key         |                      |                      |
| Feature Flags   |                      |                      |

## Pre-Deploy Checklist

- [ ] All tests passing
- [ ] Changelog updated
- [ ] Database migrations ready
- [ ] Rollback plan documented
- [ ] On-call engineer notified

## Deploy Commands

```bash
# Staging
./deploy.sh --env staging

# Production
./deploy.sh --env production
```

## Rollback Procedure

1. Identify the issue
2. Run `./rollback.sh --to <previous-version>`
3. Verify health checks
4. Notify team in #deployments
