# E11 Packaging and release

## US-1101 Visual identity

**Status:** Todo

**Acceptance criteria**

- [ ] Own extension icon (128x128) and tree icons. Use the Visual Studio Image Catalog (`KnownMonikers`) for standard objects so icons follow the theme.
- [ ] No Oracle or MySQL logo (trademark).

**Input (2026-10-26):** Herbert added `docs/AppIcon.svg` and `docs/AppIcon.ico` (32x32) as candidate extension icon: a blue database cylinder with three colored `</>` code tags and the word "MySQL" in plain text. Points to check in this story:

- The plain word "MySQL" is not the MySQL dolphin logo, but on a Marketplace icon it can still suggest that the extension comes from Oracle. Decide whether to keep the word or replace it.
- At 16x16 (tool window tab, menu) the code tags and the text are not readable; a simplified small variant may be needed.
- The Marketplace needs a 128x128 PNG, which can be exported from the SVG.

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
