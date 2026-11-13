# Shortcut Cheatsheet

A Visual Studio 2026 extension that shows every keyboard shortcut in your own Visual Studio as a cheat sheet: grouped by where it works, with the extension that adds it, the shortcuts you changed yourself, and conflicts. Export it to PNG, PDF, HTML, Markdown, CSV, JSON or XML.

Work in progress. The first version is being built on the branch `feature/v1`.

## Building

The shared code is a git submodule. Clone with:

```
git clone --recurse-submodules https://github.com/hnsoftwaredevelopment/VisualStudioShortcutCheatsheet.git
```

Build and run the unit tests without the IDE:

```
powershell -File tools\build-and-test.ps1
```

## License

MIT
