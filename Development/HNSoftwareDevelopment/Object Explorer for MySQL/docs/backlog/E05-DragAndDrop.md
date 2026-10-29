# E05 Drag & drop to the editor

Drag object names from the tree into any editor so they are used without typing errors.

## US-0501 Drag a single object name

**Status:** Done (accepted 2026-10-28)

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

**Status:** Done (accepted 2026-10-29)

As a developer, I want to drag several selected columns at once, so that I get a column list.

**Acceptance criteria**

- [x] Tree supports multi-select with Ctrl and Shift within the same table.
- [x] Dragging the "Columns" folder drops all columns.
- [x] Result: comma-separated list in ordinal order, for example `` `id`, `name`, `created_at` `` (quoting follows D-5: only when needed, so `id, name, created_at`).

**Tasks**

- [x] T-0502-01 Multi-select support in tree
- [x] T-0502-02 Column list format + tests

**Implementation notes**

- Multi-select works only for columns of the same table or view, starting from the selected column:
  - Ctrl+click adds a column or removes it again.
  - Shift+click selects the range from the selected column to the clicked one (both directions).
  - Ctrl or Shift+click on a node that is not a column of the same table selects that node as usual and ends the multi-selection.
- The extra columns get the same highlight as the selected node. The Properties window shows the column that was selected first.
- Pressing the mouse on one of the selected columns keeps the selection, so you can drag all of them. Releasing without dragging selects only that column, like Windows Explorer.
- Dragging a column outside the selection drags only that column.
- The list is always in ordinal (table) order, whatever the click order.
- Dragging or copying the Columns folder gives all columns of the table or view. When the folder was never expanded, it is loaded first (one short query).
- Ctrl+C copies the same list as a drag. The separator is `, ` for now; US-0504 adds comma + newline as option.

**Manual test**

Use sakila, table *film*.

1. Expand *film > Columns*, click `film_id`.
2. Ctrl+click `title` and `release_year`. Expected: three columns highlighted.
3. Drag `title` into a `.cs` file. Expected: `film_id, title, release_year`.
4. Click `rating`, Shift+click `description`. Expected: `description` up to `rating` highlighted (`description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating`).
5. Drag the selection into a `.sql` file. Expected: the same list; no backticks needed for these names.
6. Ctrl+click `release_year` again. Expected: it is no longer highlighted. Press Ctrl+C, paste. Expected: the list without `release_year`.
7. With several columns selected, click one of them and release without moving. Expected: only that column is selected.
8. With several columns selected, Ctrl+click a column of another table (for example *actor > Columns > first_name*). Expected: only `first_name` is selected.
9. Collapse *actor*, then drag *actor > Columns* (the folder) into the editor without expanding it. Expected: `actor_id, first_name, last_name, last_update`.
10. With the test table from US-0501 (`CREATE TABLE sakila.oefm_drag (`order` int, `first name` varchar(20), customer_id int);`): drag its Columns folder into the `.sql` file. Expected: `` `order`, `first name`, customer_id ``. Clean up with `DROP TABLE sakila.oefm_drag;`.

## US-0503 Drag a stored procedure or function as a call

**Status:** Done (accepted 2026-10-29)

As a developer, I want to drag a procedure and get a complete call with the correct parameter names.

**Acceptance criteria**

- [x] Procedure in `.sql`: `` CALL `db`.`sp_name`(@p_id, @p_name); `` (quoting only when needed, D-5: `CALL db.sp_name(@p_id, @p_name);`)
- [x] Function in `.sql`: `` SELECT `db`.`fn_name`(@p1); `` (likewise `SELECT db.fn_name(@p1);`)
- [x] Holding Alt while dropping inserts only the name.

**Tasks**

- [x] T-0503-01 Call format builder + tests
- [x] T-0503-02 Modifier key handling

**Implementation notes**

- Every parameter becomes a user variable with the parameter name: `@p_film_id`. A name with characters a user variable cannot have unquoted gets backticks: `` @`p id` ``.
- The call always includes the database, so it works whatever database is active in the query window. US-0504 adds an option for the prefix.
- When the routine was never expanded, the parameters are loaded at the start of the drag (one short query). If that fails, the drag drops only the name and the Output window logs a warning.
- In C#, VB and other files, and in other applications, the drag drops only the name (as in US-0501). Ctrl+C also copies only the name.
- Alt is read at the moment of dropping: hold Alt while you release the mouse button.

**Manual test**

Use sakila and a `.sql` file.

1. Drag procedure `film_in_stock` (without expanding it first) into the `.sql` file. Expected: `CALL sakila.film_in_stock(@p_film_id, @p_store_id, @p_film_count);`
2. Drag procedure `rewards_report`. Expected: `CALL sakila.rewards_report(@min_monthly_purchases, @min_dollar_amount_purchased, @count_rewardees);`
3. Drag function `get_customer_balance`. Expected: `SELECT sakila.get_customer_balance(@p_customer_id, @p_effective_date);`
4. Expand `inventory_in_stock > Parameters`, then drag the function. Expected: `SELECT sakila.inventory_in_stock(@p_inventory_id);`
5. Drag `film_in_stock` again and hold Alt while releasing. Expected: `film_in_stock`.
6. Drag `film_in_stock` into a `.cs` file. Expected: `film_in_stock`.
7. Select `get_customer_balance`, press Ctrl+C, paste. Expected: `get_customer_balance`.
8. Optional: run the dropped CALL in a MySQL client after `SET @p_film_id = 1, @p_store_id = 1;` and check `SELECT @p_film_count;`.

## US-0504 Drop format options

**Status:** Done (accepted 2026-10-29)

As a developer, I want to configure how names are inserted.

**Acceptance criteria**

- [x] Options page *Tools > Options > Object Explorer for MySQL > Drag & Drop*.
- [x] Settings (changed 2026-10-29, see notes):
  - Backticks in .sql files: Only when needed (default, D-5) / Always
  - Backticks in other files: Never (default) / Only when needed / Always
  - Database prefix for tables and views: off (default) / on
  - Database prefix in procedure and function calls: on (default) / off
  - Column list separator: comma and space (default) / comma and new line
- [x] Settings stored with the VisualStudio.Extensibility settings API.
- [x] The setting for other files also applies to Copy (Ctrl+C).

**Tasks**

- [x] T-0504-01 Settings definitions
- [x] T-0504-02 Apply settings in `DropTextBuilder` + tests

**Implementation notes**

- Decision 2026-10-29 (Herbert): two quoting settings instead of one, so you can have backticks in SQL and plain names in C# (where you add your own quotes). Two prefix settings instead of one: a call usually needs the database, a table name usually not.
- "Never" is not offered for .sql files: a reserved word such as `order` without backticks is invalid SQL.
- Ctrl+C follows the setting for other files, because the clipboard does not know where you paste.
- The table prefix applies in all files (`sakila.actor`); columns, databases and the name-only drop of a routine (Alt) get no prefix. The call prefix applies to the CALL/SELECT in .sql files.
- Parameter variables (`@p_film_id`) are not affected by the quoting settings; they get backticks only when the name needs them.
- Changes apply to the next drag without restarting Visual Studio. The options are read when you open the explorer from the View menu or when the first editor opens; before that, the defaults apply.
- The "Debug logging" option is now also read when the first editor opens, so it works when Visual Studio restores the explorer window at startup.

**Manual test**

Use sakila and a `.sql` and a `.cs` file.

1. Open *Tools > Options > Object Explorer for MySQL > Drag & Drop*. Expected: the five settings with the defaults above and their descriptions.
2. Without changing anything, drag table `actor` into the `.sql` and the `.cs` file. Expected: `actor` in both.
3. Set *Backticks in .sql files* to *Always*. Drag `actor` into the `.sql` file: `` `actor` ``. Into the `.cs` file: `actor`. Drag `film_in_stock` into the `.sql` file: `` CALL `sakila`.`film_in_stock`(@p_film_id, @p_store_id, @p_film_count); ``.
4. Set *Backticks in other files* to *Always*. Drag `actor` into the `.cs` file: `` `actor` ``. Select `actor`, press Ctrl+C, paste: `` `actor` ``. Set it to *Only when needed*: column `order` of the test table (`CREATE TABLE sakila.oefm_drag (`order` int, customer_id int);`) gives `` `order` ``, `customer_id` stays plain.
5. Turn on *Database prefix for tables and views*. Drag `actor`: `.sql` gives `sakila.actor` (or `` `sakila`.`actor` `` with Always); `.cs` gives `sakila.actor`. Drag a column: no prefix.
6. Turn off *Database prefix in procedure and function calls*. Drag `get_customer_balance` into the `.sql` file: `SELECT get_customer_balance(@p_customer_id, @p_effective_date);`
7. Set *Column list separator* to *Comma and new line*. Drag the Columns folder of `actor` into the `.sql` file. Expected: one column per line, each line except the last ending with a comma.
8. Restart Visual Studio (the explorer window opens again by itself), open the `.sql` file and drag `actor`. Expected: the changed settings still apply.
9. Reset the settings to their defaults. Clean up: `DROP TABLE sakila.oefm_drag;`

