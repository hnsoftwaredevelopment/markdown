# Changelog

## Unreleased

- Read extension manifests (2010 and 2011 schema) and find their MEF assemblies.
- Read MEF exports and their attributes from an assembly without loading it, on types, fields and properties.
- Sort editor exports into features (inline adornments, text colors, squiggles, highlights, outlining, Quick Info, completion, signature help, light bulbs, margins) and find features that two or more owners provide for the same content type, following the content type hierarchy.
- Extension Overlap window (View > Other Windows): extensions with overlap, filtered to the file types in the open solution, with the setting that turns a built-in Visual Studio feature off.
- Per-extension report: with whom each extension overlaps, in which feature and in which of the content types you use.
