# E11 Packaging and release

## US-1101 Visual identity

**Status:** Todo

**Acceptance criteria**

- [ ] Own extension icon (128x128) and tree icons. Use the Visual Studio Image Catalog (`KnownMonikers`) for standard objects so icons follow the theme.
- [ ] No Oracle or MySQL logo (trademark).

## US-1102 Marketplace listing

**Status:** Todo

**Acceptance criteria**

- [ ] `overview.md` for the Marketplace with screenshots and the "not affiliated with Oracle" notice.
- [x] License file chosen and added (MIT, ADR-009).
- [ ] `CHANGELOG.md` following Keep a Changelog.
- [ ] Publisher account `hnsoftwaredevelopment` on the Visual Studio Marketplace.

## US-1103 Release workflow

**Status:** Todo

**Acceptance criteria**

- [ ] Git tag `v*` triggers a GitHub Actions release build that attaches the VSIX to a GitHub Release.
- [ ] Optional: publish to the Marketplace with `VsixPublisher.exe` and a stored token.
