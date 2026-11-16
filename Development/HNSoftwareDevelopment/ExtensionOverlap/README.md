# Extension Overlap

<img src="https://raw.githubusercontent.com/hnsoftwaredevelopment/ExtensionOverlap/main/art/icon-128.png" alt="Extension Overlap icon" width="96" align="right" />

Over time you install extensions that do the same thing as each other, or as Visual Studio itself: two color swatches in front of every color, two tooltips on hover, two light bulbs. Every extension also costs startup time and makes Visual Studio updates slower.

Extension Overlap shows which installed extensions and built-in Visual Studio features register the same kind of editor feature for the same file type, and where you turn each one off. It also finds leftover extension folders that Visual Studio no longer uses.

Works in Visual Studio 2026.

> Work in progress. The first version is not released yet.

## How it works

The extension reads the metadata of each extension's MEF assemblies, the same information Visual Studio reads at startup, without loading or running any code from them. It groups what it finds by file type (content type) and feature, such as inline adornments, Quick Info, completion, light bulbs and margins.

## License

[MIT](LICENSE)
