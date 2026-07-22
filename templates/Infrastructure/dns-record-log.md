# My Document

**Last Updated:** YYYY-MM-DD
**Primary Registrar:** Registrar Name

---

## DNS Records

| Domain | Type | Name | Value | TTL | Provider | Modified |
|--------|------|------|-------|-----|----------|----------|
| example.com | A | @ | 93.184.216.34 | 300 | CloudFlare | YYYY-MM-DD |
| example.com | CNAME | www | example.com | 300 | CloudFlare | YYYY-MM-DD |
| example.com | MX | @ | mail.example.com | 3600 | CloudFlare | |
| example.com | TXT | @ | v=spf1 include:... | 3600 | CloudFlare | |
| example.com | CNAME | api | api-lb.elb.amazonaws.com | 300 | CloudFlare | |
| example.com | CNAME | docs | hosted.gitbook.com | 300 | CloudFlare | |

## Subdomains

| Subdomain | Purpose | Target | Active |
|-----------|---------|--------|--------|
| api | API gateway | AWS ALB | ✅ |
| docs | Documentation | GitBook | ✅ |
| staging | Staging env | AWS ALB | ✅ |
| mail | Email | Google | ✅ |

## Notes

- Nameservers: `ns1.cloudflare.com`, `ns2.cloudflare.com`
- Proxy status: All web traffic through CloudFlare (orange cloud)
