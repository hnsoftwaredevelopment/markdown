# My Document

**Module:** `module-name`
**Version:** 1.0.0
**Last Updated:** YYYY-MM-DD

---

## Description

What this module provisions and when to use it.

## Usage

```hcl
module "example" {
  source  = "git::https://github.com/org/module.git?ref=v1.0.0"
  name    = "my-resource"
  region  = "us-east-1"
  tags    = var.default_tags
}
```

## Inputs

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| `name` | string | - | Yes | Resource name |
| `region` | string | `us-east-1` | No | AWS region |
| `tags` | map(string) | `{}` | No | Resource tags |
| `instance_type` | string | `t3.medium` | No | EC2 instance type |

## Outputs

| Name | Description |
|------|-------------|
| `id` | Resource ID |
| `arn` | Resource ARN |
| `endpoint` | Service endpoint URL |

## Resources Created

- `aws_instance.main`
- `aws_security_group.main`
- `aws_iam_role.main`

## Notes

- Requires AWS provider >= 5.0
- State is stored in S3 backend
