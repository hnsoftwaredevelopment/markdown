# E07 Query editor

Write and execute SQL against a selected server and database inside Visual Studio.

## US-0701 New Query

**Status:** Todo

As a developer, I want to open a query window for a selected database.

**Acceptance criteria**

- [ ] Context menu "New Query" on server and database nodes opens a new `.sql` document.
- [ ] The document shows the active connection and database in a bar above the editor, with a dropdown to switch database.
- [ ] Existing `.sql` files in a project can be linked to a connection through the same bar.

**Tasks**

- T-0701-01 Connection binding per document (document properties or `IVsTextBuffer` property bag)
- T-0701-02 Editor margin with connection/database selector

## US-0702 MySQL syntax coloring

**Status:** Todo

**Acceptance criteria**

- [ ] `.sql` documents linked to a MySQL connection use MySQL keywords for coloring (TextMate grammar).
- [ ] Coloring follows the Visual Studio theme.

## US-0703 Execute and show results

**Status:** Todo

As a developer, I want to execute the query and see the results in a grid.

**Acceptance criteria**

- [ ] Ctrl+Shift+E executes the selection, or the full document when nothing is selected.
- [ ] Results pane below the editor with tabs *Results* (one grid per result set) and *Messages* (rows affected, warnings, duration).
- [ ] Cancel button stops a running query (`KILL QUERY`).
- [ ] Large result sets: grid virtualization, default limit 1000 rows with a notice.
- [ ] Copy cells, copy with headers.

**Tasks**

- T-0703-01 Query executor in Core (multiple result sets, cancel) + integration tests
- T-0703-02 Results pane UI with virtualized grid
- T-0703-03 Execute and cancel commands

## US-0704 Export results

**Status:** Parked candidate

**Acceptance criteria**

- [ ] Save a result set as CSV or JSON.
