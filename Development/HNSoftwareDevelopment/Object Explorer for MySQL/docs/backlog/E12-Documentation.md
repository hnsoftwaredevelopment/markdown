# E12 Database documentation

Generate a document of a database: tables, columns, keys, indexes, views, routines, triggers and events with their comments. Picked up from P-02.

## US-1201 Documentation as Markdown

**Status:** Ready for test

As a developer, I want to generate a document of a database, so that I can keep it in a repository or Obsidian and share it.

**Acceptance criteria**

- [x] Context menu *Generate Documentation...* on a user database: choose the file (default `<database>.md`) and what to include.
- [x] Per table: comment, engine, columns (name, type, nullable, default, key, comment), primary key, foreign keys (with the referenced table), indexes, check constraints, triggers.
- [x] Views (columns and comment), procedures and functions (parameters, return type, comment), events (schedule, status).
- [x] A table of contents with links; objects sorted by name; the generation time and server version at the top.
- [x] Runs in the background with progress and Cancel, like Script Database (US-0603).

**Tasks**

- [x] T-1201-01 `DatabaseDocumenter` (reads a `DatabaseDocument`, independent of the format, so US-1202 reuses it) + tests
- [x] T-1201-02 `MarkdownDocumentWriter` with table of contents and anchors + tests
- [x] T-1201-03 Dialog, command on a user database, wait dialog with progress and Cancel, open the file afterwards

**Implementation notes**

- *Generate Documentation...* is below *Script Database...* on a user database (not on system databases), enabled when connected. The dialog chooses the parts: tables (with keys, indexes, check constraints and triggers), views, procedures and functions, events; at least one. Then the save dialog, default `<database>.md`.
- Reading and writing run in the background behind the Visual Studio wait dialog with progress (*Tables: film (3 of 40)*) and Cancel; a cancelled or failed run leaves no file. Afterwards a message asks to open the file in Visual Studio.
- The content is read once into a `DatabaseDocument`; the Markdown writer only formats it. US-1202 adds a PDF writer on the same model.
- Document layout:
  - `# Database <name>`, then the connection and server version, the character set and collation, the generation time;
  - *Contents*: per part a link with the count, and a link per object;
  - per table: comment, engine and collation, a column table (Column, Type, Null, Default, Key = PK/FK/extra, Comment), the primary key, unique keys, foreign keys (columns, referenced table and columns, on update, on delete), indexes (columns, unique, type, invisible), check constraints, triggers (timing, event);
  - per view: comment and columns; per procedure or function: comment, return type, deterministic, data access, security, parameters (with mode for procedures);
  - events in one table: schedule, status, on completion, comment.
- The text of the document is English, like the scripts of Script Database. Line breaks in comments become `<br>`, a `|` in a cell is escaped; underscores are not escaped, so names stay readable in the file.
- Links use the heading anchors as GitHub and the Visual Studio Markdown preview make them (lower case, spaces to `-`, punctuation removed, a repeated heading gets `-1`). Obsidian resolves links to headings by their text; for names of lower case letters, digits and `_` that is the same. Names with capitals or spaces may not jump in Obsidian; check in the test.
- Check constraints are only read on servers that have them (MySQL 8.0.16+, MariaDB 10.2+).

**Manual test**

Use *sakila*.

1. Right-click *sakila*: *Generate Documentation...* is below *Script Database...*. Not on a system database; disabled when the server is not connected.
2. The dialog shows the four parts, all checked. Uncheck all: *Generate* is disabled.
3. Generate with all parts; the save dialog proposes `sakila.md`. The wait dialog shows the progress per object; the message asks to open the file.
4. Open it: the header shows the connection, server version, character set and time; *Contents* lists Tables (16), Views (7), Procedures (3), Functions (3), Events.
5. Table *film*: columns with types, NULL, defaults, PK/FK and comments; primary key; foreign keys to *language* with on update/on delete; indexes; triggers *ins_film*, *upd_film*, *del_film*.
6. Procedure *film_in_stock*: parameters with IN/OUT; function *inventory_in_stock*: return type.
7. Click links in *Contents* in the Visual Studio Markdown preview and on GitHub (or another viewer): they jump to the object.
8. Open the file in Obsidian: the tables render and the links of names such as *film_actor* jump.
9. Generate again with only *Views*: only the Views part.
10. Start on a large database and press Cancel: no file is left.
11. Theme (Dark, Light, Blue): the dialog is readable.

## US-1202 Documentation as PDF

**Status:** Todo

**Acceptance criteria**

- [ ] The same content as US-1201 as a PDF file, with page numbers and the table of contents.
- [ ] Library: MigraDoc with PDFsharp (MIT license, .NET Framework, made for documents with tables, headings and a table of contents). Syncfusion (free license of Herbert, non-commercial) is the fallback; check first whether its license allows distribution through the Marketplace and how the license key is kept out of the public repository (decision D-20).
