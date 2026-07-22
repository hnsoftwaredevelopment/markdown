# My Document

**Last Updated:** YYYY-MM-DD
**Cloud Provider:** AWS / GCP / Azure

---

## Compute

| Name | Type | Region | vCPU | RAM | OS | Purpose |
|------|------|--------|------|-----|-----|---------|
| web-1 | t3.large | us-east-1 | 2 | 8 GB | Ubuntu 22.04 | Web server |
| web-2 | t3.large | us-east-1 | 2 | 8 GB | Ubuntu 22.04 | Web server |
| worker-1 | c5.xlarge | us-east-1 | 4 | 8 GB | Ubuntu 22.04 | Background jobs |

## Databases

| Name | Engine | Version | Size | Region | Replicas |
|------|--------|---------|------|--------|----------|
| main-db | PostgreSQL | 16 | db.r6g.large | us-east-1 | 1 read replica |
| cache | Redis | 7.0 | cache.t3.medium | us-east-1 | - |

## Storage

| Bucket | Region | Purpose | Lifecycle |
|--------|--------|---------|-----------|
| app-assets | us-east-1 | Static files | - |
| app-backups | us-east-1 | DB backups | 90-day expiry |

## Networking

| Resource | CIDR / Value | Purpose |
|----------|-------------|---------|
| VPC | 10.0.0.0/16 | Main network |
| Public Subnet | 10.0.1.0/24 | Load balancers |
| Private Subnet | 10.0.2.0/24 | App servers |

## Monthly Cost Estimate

| Category | Monthly Cost |
|----------|-------------|
| Compute | $ |
| Database | $ |
| Storage | $ |
| Network | $ |
| **Total** | **$** |
