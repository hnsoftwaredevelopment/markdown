# E08 View data

Show and edit the content of a table or view.

## US-0801 View data (read-only)

**Status:** Todo

As a developer, I want to see the rows of a table without writing a query.

**Acceptance criteria**

- [ ] Context menu "View Data" on a table or view opens a document with a grid.
- [ ] Paging: 1000 rows per page, page navigation, total row count (estimated for large tables).
- [ ] Sort by clicking a column header (server-side `ORDER BY`).
- [ ] Simple filter per column (server-side `WHERE`, parameterized).

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
