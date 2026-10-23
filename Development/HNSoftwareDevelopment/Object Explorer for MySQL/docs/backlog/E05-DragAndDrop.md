# E05 Drag & drop to the editor

Drag object names from the tree into any editor so they are used without typing errors.

## US-0501 Drag a single object name

**Status:** Todo

As a developer, I want to drag a column, table, view, procedure or function into the editor, so that its exact name is inserted.

**Acceptance criteria**

- [ ] Drag starts after the standard system drag distance, not on a simple click.
- [ ] Dropped text is inserted at the drop position in the editor.
- [ ] In `.sql` files identifiers are quoted with backticks when needed (reserved word, special characters); embedded backticks are doubled.
- [ ] In other files (C#, VB, etc.) the plain name is inserted.
- [ ] Also works with *Copy* (Ctrl+C) on the selected node.

**Tasks**

- T-0501-01 `DropTextBuilder` in Core with quoting rules + tests (reserved word list for MySQL 8)
- T-0501-02 Drag source behavior on the TreeView (`DataObject` with `Text` and `UnicodeText`)
- T-0501-03 Copy command

**Manual test**

1. Drag column `customer_id` into a `.cs` file. Expected: `customer_id`.
2. Drag column `order` into a `.sql` file. Expected: `` `order` ``.

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
