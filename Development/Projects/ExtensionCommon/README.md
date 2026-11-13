# ExtensionCommon

Source code shared by the Visual Studio extensions of HN Software Development, such as [Extension Overlap](https://github.com/hnsoftwaredevelopment/ExtensionOverlap) and [Shortcut Cheatsheet](https://github.com/hnsoftwaredevelopment/VisualStudioShortcutCheatsheet).

It is a Shared Project: it has no output of its own. Each extension compiles the files into its own assembly, so two extensions in the same Visual Studio process never load two versions of one shared DLL. All types are `internal` for the same reason.

## Contents

| File | What it does |
|---|---|
| `VisualStudio/InstalledExtensions.cs` | Finds the folders of Visual Studio and of the enabled extensions, through the Extension Manager of Visual Studio, with a fallback to reading the extension folders |
| `VisualStudio/ExtensionSource.cs` | One such folder, with its owner |

## Use in an extension

Add the repository as a submodule:

```
git submodule add https://github.com/hnsoftwaredevelopment/ExtensionCommon.git external/ExtensionCommon
```

Import the shared items in the `.csproj` of the extension, before `Microsoft.CSharp.targets`:

```xml
<Import Project="..\..\external\ExtensionCommon\ExtensionCommon.projitems" Label="Shared" />
```

In GitHub Actions, check out with submodules:

```yaml
- uses: actions/checkout@v7
  with:
    submodules: true
```

The code needs the `Microsoft.VisualStudio.SDK` package and targets .NET Framework 4.8, like the extensions.

## License

MIT
