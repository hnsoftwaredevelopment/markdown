# Shortcut Cheatsheet

A Visual Studio 2026 extension that shows every keyboard shortcut of your own Visual Studio as a cheat sheet: your settings, your changes and the shortcuts your extensions add. Print it, or export it to PDF, PNG, HTML, Markdown, CSV, JSON or XML.

Open it with **View > Other Windows > Shortcut Cheatsheet**.

![The Shortcut Cheatsheet window](docs/images/window.png)

## What it shows

- **Every shortcut that works in your Visual Studio**, read from Visual Studio itself, so it includes the shortcuts you changed in Tools > Options > Environment > Keyboard.
- **Grouped by where it works** (Global, Text Editor, Solution Explorer, ...) and by category, by extension, or as one list sorted by keys.
- **Keys drawn as keys**, with the arrow keys and Enter as symbols.
- Commands get a readable name: "Edit.CommentSelection" becomes "Comment Selection" in the category Edit.

## Search

Search by name, command, category or keys. Keys work with or without spaces: `ctrl+e,v` finds Ctrl+E, V. Every word must match, so `debug f10` finds Step Over in the Debug category.

![Searching for "debug"](docs/images/search.png)

## Which extension adds a shortcut

Shortcuts from an extension carry its name; shortcuts of Visual Studio itself have no label. Group by Extension, or tick **Only extensions**, to see what each extension brings.

![Shortcuts grouped by extension](docs/images/extensions.png)

The extension is found in the compiled command table of each installed extension, the same data Visual Studio loads its menus from. Nothing of the extension is loaded or run.

## Your own shortcuts

Shortcuts you added yourself are marked **yours**. **Only added by you** lists them; the filter only appears when you have any.

![Shortcuts you added](docs/images/yours.png)

## Shortcuts that were not applied

An extension can bring a default shortcut whose keys another command already uses. Visual Studio then skips it without a message. Shortcut Cheatsheet shows such a shortcut dimmed, with a warning icon and the command that has the keys, for example: *Bookmark Studio wants these keys, but they are used by Build Solution.* To use the command, give it other keys in Tools > Options > Environment > Keyboard. **Only not applied** lists them; the filter only appears when there are any.

## Export

**Export...** saves what the window shows, with the same search, filters and grouping.

| Format | For |
|---|---|
| PDF | printing; pages of A4 or Letter, landscape, keys drawn as keys |
| PNG | one image per page |
| HTML | one page with search, a dark mode and a print layout; nothing loaded from the internet |
| Markdown | wikis and repositories; keys in `<kbd>` |
| CSV | Excel, with the list separator of your Windows region |
| JSON, XML | scripts and other tools |

![A PDF page](docs/images/export-pdf.png)

![The HTML export](docs/images/export-html.png)

Shortcuts that were not applied are left out of PDF and PNG, and marked in the other formats.

## Settings

Tools > Options > Shortcut Cheatsheet, in the new and in the legacy Options dialog.

| Setting | Default |
|---|---|
| Language: English, Chinese (simplified and traditional), Czech, Dutch, French, German, Italian, Japanese, Korean, Polish, Portuguese (Brazil), Russian, Spanish or Turkish | the language of Visual Studio |
| Group by: how the window groups the shortcuts when it opens | Where it works |
| Paper size for PDF and PNG | Letter in North America, A4 elsewhere |
| Colors for PDF and PNG: light or dark | Light |
| Columns per page, 1 to 4 | 3 |

![The settings](docs/images/options.png)

The window, the settings, and the PDF, PNG, HTML and Markdown exports follow the language. JSON, XML and CSV stay English, so scripts and formulas always see the same names. Command and scope names come from Visual Studio and keep its language.

## Requirements

Visual Studio 2026 (Community, Professional or Enterprise), x64 or Arm64.

## Building

The shared code is a git submodule. Clone with:

```
git clone --recurse-submodules https://github.com/hnsoftwaredevelopment/VisualStudioShortcutCheatsheet.git
```

Build and run the unit tests without the IDE:

```
powershell -File tools\build-and-test.ps1
```

`tools\readme-shots.ps1` makes the screenshots of this README in the Experimental Instance.

## License

MIT
