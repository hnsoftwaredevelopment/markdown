# E08 View data

Show and edit the content of a table or view.

## US-0801 View data (read-only)

**Status:** Ready for test

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
- Toolbar: Refresh, Clear filters, first / previous / next / last page, `Page 2 of 17`, the row count and *Loading...*. Each page has 1000 rows.
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

**Status:** Todo

As a developer, I want to change, add or delete rows in the grid.

**Acceptance criteria**

- [ ] Editing is only possible for tables with a primary key; otherwise the grid is read-only with a notice.
- [ ] Changes are applied per row with parameterized UPDATE/INSERT/DELETE on the primary key.
- [ ] Errors from the server are shown on the row; the row keeps its edited values.
- [ ] Delete asks for confirmation.

**Tasks**

- T-0802-01 Row change statement builder in Core + tests
- T-0802-02 Grid editing and save logic
