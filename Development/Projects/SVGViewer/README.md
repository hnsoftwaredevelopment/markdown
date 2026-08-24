# SVGViewer

A Windows desktop application (C# / WPF, .NET 8) to **browse a drive, find SVG
files fast, and preview them** — with folders that contain SVGs clearly marked,
adjustable preview sizes, and one double‑click to open a file in your associated
editor (e.g. Inkscape). The interface is fully multilingual (Dutch, English,
German).

## Features

- **Drive & folder navigation** — pick a drive or a chosen folder and click through a tree view.
- **SVG folder highlighting** — folders that contain `.svg` files are marked so
  you can jump straight to them.
- **Persistent scan cache** — completed scans are available immediately the next
  time you open the same drive or folder.
- **Structure filter** — show the full folder tree, or only folders that contain
  SVG files.
- **Preview sizes** — Large, Medium, Small, or Only details (list view).
- **SVG‑only** — all non‑SVG files are hidden.
- **Edit externally** — double‑click an SVG to open it in the associated app.
- **Multilingual UI** — Dutch (default), English, German, switchable at runtime.
- **In‑app help** — user guide opens in the currently selected language.
- **Simple filemanagement** - rename, copy or move files from one directory to another on the selected drive, or to another drive when you have an open explorer window with that drive.
- **Export to XAML resource** — right-click one SVG, a multi-selection, or a whole folder
  and export it straight to a WPF `ResourceDictionary` (colored `DrawingImage` or
  colorless `Geometry`/`GeometryGroup`), ready to merge into any WPF app's resources. Uses
  the same conversion engine as the standalone `SvgResourceConverter` tool, so both apps
  produce identical output. See [Export to XAML resource](#export-to-xaml-resource) below.

## Screenshots

Main window:

![SVG Viewer main window](docs/images/Screenshot01.png)

Preview window (zoom & pan):

![SVG preview window](docs/images/Screenshot02.png)

## Export to XAML resource

Right-click any SVG in the preview list (or a multi-selection of several), or a folder in
the tree, and choose **Export as XAML resource...** / **Export folder as XAML
resource...**. A dialog lets you pick:

- **Format** — `DrawingImage` (keeps the SVG's own colors; use as the `Source` of an
  `<Image>`) or `Geometry`/`GeometryGroup` (no color, one shape per icon; use as the
  `Data` of a `<Path>` with your own `Foreground`).
- **Preserve full canvas size** — keeps every icon's `Geometry.Bounds` matching its
  original SVG canvas, even when the drawn shape doesn't reach the edges (useful when
  showing several icons together at a consistent size).
- **Include subfolders** (folder export only) — recurse into subfolders before
  converting.
- **Output file** — where the combined `.xaml` resource dictionary is written.

Clicking **Export** converts every selected file, shows per-file status (including a
graceful skip - not a crash - for files that turn out to share the same resource key
after sanitizing), and writes the result once at least one file converted successfully.
The resource key is always exactly the SVG's file name (without extension).

This reuses the conversion engine originally built for the standalone
`SvgResourceConverter` app (`C:\DevOps\hnsoftwaredevelopment\SVGConverter\SvgResourceConverter\`) -
see that project's README for a fuller discussion of SVG feature coverage and known
limitations (filters, patterns/masks, and why `Geometry` mode isn't a good fit for pure
outline/line-art icon sets).

## Tech stack

| Area | Choice |
|------|--------|
| Framework | .NET 8 (`net8.0-windows`), WPF |
| Pattern | MVVM (`CommunityToolkit.Mvvm`) |
| SVG rendering | `SharpVectors.Reloaded` |
| Optional UI | Syncfusion WPF (license read from a local file) |
| Localization | `.resx` satellite assemblies (nl / en / de) |

## Documentation

- Quick reference: [`docs/user-guide/`](docs/user-guide/) — a short overview in NL / EN / DE (also opened by the in‑app Help button).
- Design & planning: [`docs/Epic.md`](docs/Epic.md) and
  [`docs/UserStories.md`](docs/UserStories.md).
- Performance measurement: [`docs/Performance.md`](docs/Performance.md) — measure
  the current scan on a real drive.

## License

© HN Software Development. All rights reserved.
