# My Document

**Set:** Icon Set Name
**Version:** 1.0
**Date:** YYYY-MM-DD

---

## Inventory

| Name | Category | Sizes | Format |
|------|----------|-------|--------|
| home | Navigation | 16, 20, 24 | SVG |
| search | Navigation | 16, 20, 24 | SVG |
| settings | Navigation | 16, 20, 24 | SVG |
| user | People | 16, 20, 24 | SVG |
| bell | Notification | 16, 20, 24 | SVG |
| check | Status | 16, 20, 24 | SVG |
| warning | Status | 16, 20, 24 | SVG |
| plus | Action | 16, 20, 24 | SVG |
| trash | Action | 16, 20, 24 | SVG |

## Design Rules

- **Grid:** 24×24 with 2px padding
- **Stroke:** 1.5px, round caps and joins
- **Style:** Outlined (default), Filled (active states)
- **Color:** Inherits from `currentColor`

## Naming Convention

`[category]-[name]-[variant]`

Examples: `nav-home`, `action-plus-circle`, `status-check-filled`

## Export Specs

| Format | Use Case |
|--------|----------|
| SVG | Web, responsive |
| PNG @1x, @2x | Legacy fallback |
| PDF | iOS assets |
