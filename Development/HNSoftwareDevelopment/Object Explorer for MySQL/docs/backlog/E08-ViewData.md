# E08 View data

Show and edit the content of a table or view.

## US-0801 View data (read-only)

**Status:** Done (accepted 2026-10-30)

As a developer, I want to see the rows of a table without writing a query.

**Acceptance criteria**

- [x] Context menu "View Data" on a table or view opens a document with a grid.
- [x] Paging: 1000 rows per page, page navigation, total row count (estimated for large tables).
- [x] Sort by clicking a column header (server-side `ORDER BY`).
- [x] Simple filter per column (server-side `WHERE`, parameterized).

**Tasks**

- [x] T-0801-01 `TableDataQuery` (page, count, sort, filters), `MySqlTableDataSource` and `TableDataViewModel` in Core + tests
- [x] T-0801-02 View Data window (tool window in the document well), toolbar, grid with sort and filter row; command *View Data*

**Implementation notes**

- *View Data* is in the context menu of tables and views, above *View Code*, and needs a connected server. It opens a tab in the document well with the caption `sakila.actor [Data]` (decision D-12). One tab per connection, database and table: a second *View Data* on the same table shows the open tab. The tab is not reopened when Visual Studio starts, so it never asks for a password by itself.
- Toolbar: Refresh, Clear filters, first / previous / next / last page (previous and next use the left and right arrows of Navigate Backward / Forward, changed after the test round), `Page 2 of 17`, the row count and *Loading...*. Each page has 1000 rows.
- Row count: a page that is not full gives the exact count right away. Otherwise `COUNT(*)` runs after the page is shown (*counting rows...*). A table without filters that the storage engine estimates at 1,000,000 rows or more shows the estimate (`about 3,000,000 rows (estimate)`) instead of counting; the last page is then based on the estimate.
- Sort: click a column header. The first click sorts ascending, the next descending, on the server over all rows, and goes back to page 1. Without a sort the rows are ordered by the primary key, so pages do not overlap; views and tables without a primary key have no fixed order.
- Filter row below the column headers (decision D-12): text columns filter on *contains* (`LIKE '%text%'`, `%` and `_` in the text are searched as characters), `=text` means equal; numbers, dates and times filter on *equal*; `NULL` and `NOT NULL` test for NULL. Press Enter to apply. Filters of several columns are combined with AND. Values are always parameters. A filter always gives an exact count.
- Values are shown as in the query results (US-0703): NULL, invariant numbers, ISO dates, binary data as hex. Copy and *Copy with Headers* are in the context menu of the grid; Ctrl+C copies the selected cells.
- Read-only. Editing is US-0802.

**Manual test**

Use sakila.

1. Right-click table *actor* > *View Data*. Expected: tab `sakila.actor [Data]` in the document well with 200 rows, `Page 1 of 1`, `200 rows`, rows in actor_id order.
2. *View Data* on *actor* again. Expected: the same tab is activated, no second tab.
3. *View Data* on *rental*. Expected: 1000 rows, *counting rows...*, then `16,044 rows` and `Page 1 of 17`. Next page: rows 1001-2000 (`OFFSET 1000`). Last page: `Page 17 of 17` with 44 rows; next and last are disabled; first and previous work.
4. Sort: click the header *return_date*. Expected: page 1, ascending (NULL values first), sort arrow up. Click again: descending, arrow down.
5. Filter on *customer_id* of *rental*: type `130`, Enter. Expected: page 1, only rows of customer 130, the row count matches `SELECT COUNT(*) FROM rental WHERE customer_id = 130`. Add `2005-05` in *rental_date*: no rows (dates filter on equal). Replace it by a full date-time from the grid: only that row. Clear filters button: all 16,044 rows again.
6. Text filter on *actor*: *last_name* `berg`. Expected: every last name that contains BERG, in any case. `=` plus a full last name from the grid: only actors with exactly that name. `a_b`: no rows (the underscore is searched as a character).
7. NULL filter on *rental*: *return_date* `NULL`, then `NOT NULL`. Expected: the two counts add up to 16,044.
8. View: *View Data* on *actor_info*. Expected: rows of the view; the caption is `sakila.actor_info [Data]`.
9. Copy: select a few cells, Ctrl+C, paste in Notepad. Right-click > *Copy with Headers*: column names and values.
10. Close the tab and *View Data* again: fresh data, filters and sort reset.
11. Disconnect the server: *View Data* is disabled. A server with a password that is not saved: connect via the tree first.
12. Theme (Dark, Light, Blue): toolbar, headers, filter boxes and selection follow the theme.

## US-0802 Edit data

**Status:** Ready for test

As a developer, I want to change, add or delete rows in the grid.

**Acceptance criteria**

- [x] Editing is only possible for tables with a primary key; otherwise the grid is read-only with a notice.
- [x] Changes are applied per row with parameterized UPDATE/INSERT/DELETE on the primary key.
- [x] Errors from the server are shown on the row; the row keeps its edited values.
- [x] Delete asks for confirmation.

**Tasks**

- [x] T-0802-01 `RowChangeBuilder` (UPDATE, INSERT, DELETE, read back), `EditableRow` and save/delete logic in `TableDataViewModel` + tests
- [x] T-0802-02 Grid editing, row markers, Add row / Delete rows / Undo Changes, paging glyphs

**Implementation notes**

- Editing works in the View Data window of a table with a primary key. A view or a table without primary key stays read-only, with a notice in the toolbar (*Read-only: ...*).
- Not editable columns (read-only in the grid): generated columns, binary and BLOB columns (shown as hex) and spatial columns.
- Edit a cell with a double-click or by typing. A row is saved when the grid leaves it (another row, Enter on the last cell); there is no separate Save button (decision D-13). The save is `UPDATE ... SET <changed columns> WHERE <primary key> = <old values>`, all values as parameters; afterwards the row is read back, so the grid shows what the server stored (for example a trimmed value or a default).
- Text `NULL` (any case) sets NULL, as in SSMS. An empty cell is an empty string.
- Row header: `*` unsaved changes, `+` new row, `!` error. The tooltip of `!` shows the server message; the row keeps its edited values. Fix the value and leave the row again, or *Undo Changes* in the context menu.
- A row with an error gets a red background and a red `!` (after the first test round: the `!` alone was easy to miss). When the server message names a column (`Data too long for column 'name'`, `Column 'name' cannot be null`, `Field 'name' doesn't have a default value`, `... for column `db`.`t`.`name``), that cell is marked stronger, with a red border and the message as tooltip. A message without column (for example a duplicate key) marks only the row.
- An UPDATE that finds no row (someone else changed the key or deleted the row) gives the error *The row was not found...* on the row.
- *Add row* (toolbar) adds an empty row at the end of the page and starts editing the first editable cell. Empty columns get their default; an empty AUTO_INCREMENT key gets the next value, which the grid shows after the save.
- *Delete selected rows* (toolbar and context menu) deletes the rows with a selected cell, after a confirmation with the number of rows. A new row that was never saved is only removed.
- Paging, sorting, filtering and Refresh ask first when rows have unsaved changes.
- The paging buttons are now one drawn set (|◀ ◀ ▶ ▶|) in the text color of the theme, after the remark on US-0801.

**Manual test**

Use sakila. Create a test table first, so sakila stays intact:

```sql
CREATE TABLE sakila.edit_test (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20) NOT NULL, note VARCHAR(50) NULL, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
INSERT INTO sakila.edit_test (name, note) VALUES ('one', 'first'), ('two', NULL), ('three', 'third');
CREATE TABLE sakila.no_key_test (a INT, b VARCHAR(10));
```

1. Refresh the explorer, *View Data* on *edit_test*. Expected: the Add row and Delete buttons in the toolbar; no read-only notice. The paging buttons look like one set.
2. Double-click *name* of row 1, change it to `uno`, press Enter and click another row. Expected: no marker; `SELECT * FROM edit_test` in a query window shows `uno`.
3. Change *note* of row 2 to `null` (lower case) and leave the row. Expected: the cell shows `NULL`; in the database the value is NULL. Change *note* of row 1 to an empty text: an empty string, not NULL.
4. Error: change *name* of row 3 to a text of 25 characters and leave the row. Expected: the row turns red with a red `!`; the *name* cell is darker red with a red border; hovering the cell or the `!` shows *Data too long for column 'name'*; the cell keeps the 25 characters. Shorten it and leave the row: the red marking and the `!` disappear.
5. *Undo Changes*: change *note* of row 1, then right-click > *Undo Changes* before leaving the row. Expected: the old value is back, no marker.
6. *Add row*: a new row with `+`, the cursor in *name*. Type `four`, leave the row. Expected: *id* shows the next number, *created* the current time; the row count goes up by 1.
7. Add a row and leave it empty with *name* empty: the server error about *name* (no default) appears on the row. Delete that row with *Delete selected rows*: removed without a question (it was never saved).
8. Select cells in rows 1 and 2, *Delete selected rows*. Expected: *Delete 2 row(s) from sakila.edit_test?*; *No* keeps them, *Yes* deletes them and the row count goes down by 2.
9. Unsaved rows: make a change that gives an error (step 4), then click Next page or Refresh. Expected: the question to discard the changes; *No* keeps them.
10. *View Data* on *no_key_test*: read-only notice about the primary key; cells cannot be edited; no Add/Delete buttons. *View Data* on view *actor_info*: read-only notice for a view.
11. *View Data* on *staff*: *picture* (BLOB) cannot be edited; the other columns can.
12. Theme (Dark, Light, Blue): the edit box of a cell, the row markers and the drawn paging buttons follow the theme.
13. Error without column: add a row and type the *id* of an existing row (for example `1`) and a *name*. Expected: *Duplicate entry '1' for key ...*; the row is red, no cell has the red border. Type `abc` in *id* of a new row: *Incorrect integer value ... for column ... id*: the *id* cell is marked. Check the red is readable in Dark, Light and Blue.

Clean up afterwards: `DROP TABLE sakila.edit_test, sakila.no_key_test;`
