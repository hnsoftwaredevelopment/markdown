# E11 Packaging and release

## US-1101 Visual identity

**Status:** Done (accepted 2026-11-04)

**Acceptance criteria**

- [x] Own extension icon (128x128) and tree icons. Use the Visual Studio Image Catalog (`KnownMonikers`) for standard objects so icons follow the theme.
- [x] No Oracle or MySQL logo (trademark).

**Input (2026-10-26):** Herbert added `docs/AppIcon.svg`, `docs/AppIcon.ico` (32x32) and `docs/AppIcon.png` (128x128): a blue database cylinder with three colored `</>` code tags, without the word "MySQL", so it does not suggest that the extension comes from Oracle.

**Implementation notes**

- Found after the first release build (Herbert, 2026-11-04): *Manage Extensions* showed the default icon and a very short description.
- `Assets/AppIcon.png` in the VSIX project is a copy of `docs/AppIcon.png`; the VSIX manifest uses it as `Icon` and `PreviewImage`. Replace both files together when the icon changes.
- The tree, menus and toolbars use `KnownMonikers`, so they follow the theme; Explain and Explain Analyze have own icons (US-1301, US-1302).
- The manifest got a full description (what the extension does, MySQL 8.0+ and MariaDB, the Oracle notice), more tags and a link to the changelog as release notes. The version in the repository is now 0.5.0, the first release.

**Manual test**

1. Build a release (or install the Debug VSIX). *Extensions > Manage Extensions > Installed*: *Object Explorer for MySQL* shows the cylinder icon and the full description, version 0.5.0 or the release version.
2. Click *Release notes* or *More info* in the details: the changelog and the repository open.

## US-1102 Marketplace listing

**Status:** Done (accepted 2026-11-04)

**Acceptance criteria**

- [x] Overview for the Marketplace with the "not affiliated with Oracle" notice: `README.md`, which is also the GitHub page.
- [x] Screenshots in the overview.
- [x] License file chosen and added (MIT, ADR-009).
- [x] `CHANGELOG.md` following Keep a Changelog.
- [x] Publisher account `hnsoftwaredevelopment` on the Visual Studio Marketplace (exists, Herbert 2026-11-03).
- [x] `publishManifest.json` for `VsixPublisher.exe` (used by the release workflow, US-1103).

**Implementation notes**

- `README.md` describes every feature, getting started, keyboard shortcuts, options, where data is stored, requirements and limitations. Links to other files use absolute GitHub URLs, because the Marketplace shows the overview outside the repository. The icon and the screenshots use relative paths: the repository is private, so raw.githubusercontent.com URLs give 404 for everyone else. GitHub shows relative images in a private repository, and `VsixPublisher` uploads them to the Marketplace through `assetFiles` in `publishManifest.json`.
- `publishManifest.json`: internal name `ObjectExplorerForMySQL`, categories *data* and *coding*, free, Q&A on, overview `README.md`, the icon and screenshots as asset files.
- While the repository is private, the links to GitHub (More info, Release notes, the changelog and docs in the overview, the Q&A repository link) only work for Herbert. Make the repository public before publishing to the Marketplace, as XAML Resource Preview is.
- Screenshots (Herbert, 2026-11-04) in `docs/images/`: `explorer.png`, `query-editor.png`, `explain-plan.png`, `view-data.png`, `pdf-documentation.png`, `activity-monitor.png`, each below the feature it shows. They are linked with relative paths and listed in `assetFiles` of `publishManifest.json`.

**Manual test**

1. On GitHub, the README shows the icon, the badges and the six screenshots.
2. Publish a release with *publish* on (needs the secret `VS_MARKETPLACE_TOKEN`). The Marketplace page shows the same overview with the screenshots, the icon, the categories *Data* and *Coding*, and Q&A.
- First manual upload (Herbert, 2026-11-04) was refused: the Marketplace does not accept 18.0 as the lower bound of the installation target ("experimental API version"), and the Publisher in the manifest must equal the publisher display name. Fixed: installation target and prerequisite `[17.14,)`, Publisher `Herbert Nijkamp`. Visual Studio 2026 only looks at the lower bound, so the extension still installs there; it now also installs in Visual Studio 2022 17.14, which is not tested.
- The Marketplace refused the README as overview: "Overview cannot contain a link to an svg file". The badges at the top of the README are SVG images. `overview.md` is now the Marketplace text, made from README.md by `tools/New-MarketplaceOverview.ps1`: without badges, with absolute image URLs (the repository is public now) and without the sections for contributors. `publishManifest.json` uses overview.md. Run the script again after every README change.

## US-1103 Release workflow

**Status:** Done (accepted 2026-11-04)

As the maintainer, I want to build a release VSIX on GitHub with one action, so that every release is built the same way from a clean checkout.

**Acceptance criteria**

- [x] Git tag `v*` triggers a GitHub Actions release build that attaches the VSIX to a GitHub Release.
- [x] Added (Herbert, 2026-11-03): the release can also be started by hand in GitHub (*Run workflow*) with a version number; the workflow then creates the tag.
- [x] Optional: publish to the Marketplace with `VsixPublisher.exe` and a stored token. The step is in the workflow; it uses `publishManifest.json` from US-1102.

**Tasks**

- [x] T-1103-01 `.github/workflows/release.yml`
- [x] T-1103-02 The same workflow for XAML Resource Preview (separate repository, at Herbert's request)

**Implementation notes**

- Two ways to start: *Actions > Release > Run workflow* with a version such as `0.4.0` (options *pre-release* and *publish*), or pushing a tag `v0.4.0`.
- The version must be numeric (`1.2.3` or `1.2.3.4`), because a VSIX version cannot have a suffix such as `-beta`; use the pre-release option for that. A version whose tag already exists is refused.
- The workflow writes the version into the VSIX manifest of the build only; `source.extension.vsixmanifest` in the repository keeps its value. Update it in the repository too when the version in Visual Studio's debug builds matters.
- Steps: checkout, version, .NET SDK from `global.json`, MSBuild of Visual Studio 2026 (`windows-2025` runner), build Release with warnings as errors, unit tests, VSIX renamed to `ObjectExplorerForMySql-<version>.vsix` and attached to a GitHub Release with generated release notes (the commits and pull requests since the previous release).
- Marketplace (only with *publish*): `VsixPublisher.exe publish` with `publishManifest.json` and the repository secret `VS_MARKETPLACE_TOKEN`: an Azure DevOps personal access token, organization *All accessible organizations*, scope *Marketplace > Manage*. The publisher in the publish manifest must be `hnsoftwaredevelopment`.
- After the first run (Herbert, 2026-11-04): the build artifact step is removed. GitHub always offers an artifact as a zip, which was confusing; the plain VSIX is on the Releases page.
- XAML Resource Preview got the same workflow, adapted to its classic VSSDK project (no `global.json`, MSBuild 17.14 or newer, tests with `vstest.console`, output in `Builds\`). It already has `publishManifest.json`, so publishing works there once the secret is set.

**Manual test**

1. In GitHub: *Actions > Release > Run workflow*, version `0.4.0`, *pre-release* on, *publish* off. Expected: a green run; under *Releases* a pre-release *ObjectExplorerForMySql 0.4.0* with tag `v0.4.0`, the file `ObjectExplorerForMySql-0.4.0.vsix` and release notes.
2. Download the VSIX and install it in Visual Studio. *Extensions > Manage Extensions > Installed* shows version 0.4.0.
3. Run the workflow again with `0.4.0`: it stops at *Determine the version* with *Tag v0.4.0 already exists*.
4. Run it with `0.4-beta`: it stops with the message about the version format.
5. Tag push: `git tag v0.4.1` and `git push origin v0.4.1` start the same workflow; the release has no pre-release mark.
6. Delete test releases and tags you do not want to keep (*Releases > Delete*, and `git push origin :refs/tags/v0.4.1`).
7. XAML Resource Preview: the same steps 1 to 4 in that repository (version for example `1.1.0`).
