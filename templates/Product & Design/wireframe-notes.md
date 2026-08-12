# My Document

**Screen:** Screen Name
**Author:** Your Name
**Date:** YYYY-MM-DD
**Status:** Draft | Review | Approved

---

## Screen Overview

Describe what this screen does and when users encounter it.

## Layout Notes

### Header

- Logo left, navigation center, profile right
- Sticky on scroll

### Main Content

- Two-column layout on desktop
- Single column on mobile
- Primary action above the fold

### Sidebar

- Collapsible on mobile
- Contains filters / navigation

## Component Specifications

| Component | Behavior | Notes |
|-----------|----------|-------|
| Search bar | Auto-complete after 2 chars | Debounce 300ms |
| Card list | Infinite scroll | 20 items per page |
| CTA button | Primary style | Fixed bottom on mobile |

## Interactions

- Clicking a card → opens detail view
- Long press → context menu
- Swipe left → delete (with confirmation)

## Open Questions

- [ ] Should filters persist across sessions?
- [ ] What happens with zero results?
