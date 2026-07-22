# My Document

**Version:** 1.0
**Last Updated:** YYYY-MM-DD

---

## Design Tokens

### Colors

| Token | Value | Usage |
|-------|-------|-------|
| `--color-primary` | `#2563EB` | CTAs, links, focus rings |
| `--color-secondary` | `#7C3AED` | Accents, tags |
| `--color-surface` | `#FFFFFF` | Card backgrounds |
| `--color-text` | `#1F2937` | Body text |
| `--color-muted` | `#6B7280` | Secondary text |

### Spacing

| Token | Value | Usage |
|-------|-------|-------|
| `--space-xs` | 4px | Inline gaps |
| `--space-sm` | 8px | Component padding |
| `--space-md` | 16px | Section padding |
| `--space-lg` | 32px | Layout margins |

## Components

### Button

- **Primary:** Filled, high contrast
- **Secondary:** Outlined, subtle
- **Ghost:** Text only, minimal
- **States:** Default, Hover, Active, Disabled, Loading

### Card

- Background: `--color-surface`
- Border radius: 12px
- Shadow: `0 1px 3px rgba(0,0,0,0.1)`

## Patterns

- Forms: Label above, error below, inline validation
- Navigation: Sidebar + top bar hybrid
- Loading: Skeleton screens, not spinners
