# E12 Database documentation

Generate a document of a database: tables, columns, keys, indexes, views, routines, triggers and events with their comments. Picked up from P-02.

## US-1201 Documentation as Markdown

**Status:** Todo

As a developer, I want to generate a document of a database, so that I can keep it in a repository or Obsidian and share it.

**Acceptance criteria**

- [ ] Context menu *Generate Documentation...* on a user database: choose the file (default `<database>.md`) and what to include.
- [ ] Per table: comment, engine, columns (name, type, nullable, default, key, comment), primary key, foreign keys (with the referenced table), indexes, check constraints, triggers.
- [ ] Views (columns and comment), procedures and functions (parameters, return type, comment), events (schedule, status).
- [ ] A table of contents with links; objects sorted by name; the generation time and server version at the top.
- [ ] Runs in the background with progress and Cancel, like Script Database (US-0603).

## US-1202 Documentation as PDF

**Status:** Todo

**Acceptance criteria**

- [ ] The same content as US-1201 as a PDF file, with page numbers and the table of contents.
- [ ] Library: MigraDoc with PDFsharp (MIT license, .NET Framework, made for documents with tables, headings and a table of contents). Syncfusion (free license of Herbert, non-commercial) is the fallback; check first whether its license allows distribution through the Marketplace and how the license key is kept out of the public repository (decision D-20).
