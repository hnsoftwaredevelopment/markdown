# E05 Drag & drop to the editor

Drag object names from the tree into any editor so they are used without typing errors.

## US-0501 Drag a single object name

**Status:** Ready for test

As a developer, I want to drag a column, table, view, procedure or function into the editor, so that its exact name is inserted.

**Acceptance criteria**

- [x] Drag starts after the standard system drag distance, not on a simple click.
- [x] Dropped text is inserted at the drop position in the editor.
- [x] In `.sql` files identifiers are quoted with backticks when needed (reserved word, special characters); embedded backticks are doubled.
- [x] In other files (C#, VB, etc.) the plain name is inserted.
- [x] Also works with *Copy* (Ctrl+C) on the selected node.

**Tasks**

- [x] T-0501-01 `DropTextBuilder` in Core with quoting rules + tests (reserved word list for MySQL 8)
- [x] T-0501-02 Drag source behavior on the TreeView (`DataObject` with `Text` and `UnicodeText`)
- [x] T-0501-03 Copy command

**Implementation notes**

- Draggable: databases, tables, views, columns, stored procedures and functions. Servers, folders, keys, indexes, triggers, parameters and events are not draggable (yet).
- A drag carries two texts: the plain name in the standard text formats, and the SQL text in a private format. An editor drop handler (MEF, `IDropHandlerProvider`, ordered before the standard text drop handlers) inserts the SQL text when the file has the extension `.sql` or a SQL content type, and the plain name in every other editor. Other applications (Notepad, Word) receive the plain name.
- Quoting "when needed": empty name, a reserved word of MySQL 8.0/8.4 (list from the reference manual, *Keywords and Reserved Words*), a character other than letters, digits, `_` and `$`, or a name that starts with a digit (`1e3` would read as a number). Non-ASCII letters (for example `ä`) are allowed unquoted, as in MySQL.
- *Copy* (Ctrl+C, and in the node context menu) puts the plain name on the clipboard. Paste does not know the target file, so a reserved word pasted into a `.sql` file is not quoted; drag & drop is. US-0504 adds an option for this.
- The drop places the caret after the inserted text; Undo (Ctrl+Z) removes it.
- Procedures and functions insert only the name; the full call follows in US-0503.

**Manual test**

Use sakila and a test table with awkward names:

```sql
CREATE TABLE sakila.oefm_drag (`order` int, `first name` varchar(20), customer_id int);
```

1. Refresh *sakila > Tables*, expand *oefm_drag > Columns*.
2. Click a column and release without moving. Expected: the node is selected, no text appears anywhere.
3. Drag `customer_id` into a `.cs` file. Expected: `customer_id` at the drop position, caret after it.
4. Drag `order` into a `.cs` file. Expected: `order` (plain).
5. Open or create a `.sql` file (for example *File > New > File > SQL File*, saved as `test.sql`). Drag `order`: expected `` `order` ``. Drag `first name`: expected `` `first name` ``. Drag `customer_id`: expected `customer_id`.
6. Drag table `film`, view `actor_info`, procedure `film_in_stock` and database `sakila` into the `.sql` file. Expected: the plain names (no quoting needed).
7. Drag `oefm_drag` into Notepad. Expected: `oefm_drag`.
8. Select `first name`, press Ctrl+C, paste in the `.cs` file. Expected: `first name`.
9. Right-click a column. Expected: menu with *Copy*, *Refresh* and *Properties Window*. Right-click a folder (for example *Columns*): *Copy* is disabled.
10. Click the expand arrow of a table and move the mouse a bit while holding the button. Expected: no drag starts.
11. Press Ctrl+Z in the editor after a drop. Expected: the inserted text is removed.
12. Clean up: `DROP TABLE sakila.oefm_drag;`

## US-0502 Drag multiple columns

**Status:** Todo

As a developer, I want to drag several selected columns at once, so that I get a column list.

**Acceptance criteria**

- [ ] Tree supports multi-select with Ctrl and Shift within the same table.
- [ ] Dragging the "Columns" folder drops all columns.
- [ ] Result: comma-separated list in ordinal order, for example `` `id`, `name`, `created_at` ``.

**Tasks**

- T-0502-01 Multi-select support in tree
- T-0502-02 Column list format + tests

## US-0503 Drag a stored procedure or function as a call

**Status:** Todo

As a developer, I want to drag a procedure and get a complete call with the correct parameter names.

**Acceptance criteria**

- [ ] Procedure in `.sql`: `` CALL `db`.`sp_name`(@p_id, @p_name); ``
- [ ] Function in `.sql`: `` SELECT `db`.`fn_name`(@p1); ``
- [ ] Holding Alt while dropping inserts only the name.

**Tasks**

- T-0503-01 Call format builder + tests
- T-0503-02 Modifier key handling

## US-0504 Drop format options

**Status:** Todo

As a developer, I want to configure how names are inserted.

**Acceptance criteria**

- [ ] Options page *Tools > Options > Object Explorer for MySQL > Drag & Drop*.
- [ ] Settings: quote identifiers (Always / When needed / Never), include database prefix (yes/no), column list separator (comma + space / comma + newline).
- [ ] Settings stored with the VisualStudio.Extensibility settings API.

**Tasks**

- T-0504-01 Settings definitions
- T-0504-02 Apply settings in `DropTextBuilder` + tests
