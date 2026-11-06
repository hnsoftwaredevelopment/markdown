# Parked

Ideas that are postponed. They get an epic number when they are picked up.

## P-01 Table designer

**Dropped** (2026-11-02): this is an object explorer, not a management tool; the templates of US-0904 cover small changes.

Create and alter tables visually (columns, types, keys, indexes) with a preview of the generated `ALTER TABLE`. Useful for small changes from Visual Studio; not required because management happens elsewhere.

## P-02 Database documentation as PDF

**Picked up** on 2026-11-02 as E12 (Markdown, then PDF).

Generate a PDF for a selected database with all tables, columns, data types, keys, indexes, routines and their comments. Possibly also Markdown output for use in a repository or Obsidian.

## P-03 Schema compare and data compare

**Dropped** (2026-11-02): large effort, little use for most users.

Compare two databases (or a database and a script) and generate a migration script. Large effort; first find out whether users need it.

## P-04 Export query results

Picked up on 2026-10-30 as US-0704 in E07: CSV and JSON export of the rows shown in a result grid.

## P-05 Full result beyond the row limit

**Picked up** on 2026-11-03 as US-0705: export runs a read-only statement again and streams all rows to the file. Paging buttons in the results pane do not help: the pane only holds the first 1000 rows, and paging an arbitrary query would mean running it again per page.

The results pane keeps at most 1000 rows per result set (US-0703), and the export saves those rows (US-0704). Ideas:

- *Show all rows* in the grid on request, with a warning for very large results (memory of Visual Studio).
- *Export full result*: run the statement again and stream all rows straight to the CSV or JSON file, without keeping them in memory, with progress and Cancel. Needs care: the statement runs a second time, so only for statements without side effects (SELECT, SHOW).
- A setting for the row limit.

## P-06 Activity monitor

**Picked up** on 2026-11-03 as E15 / US-1501 (decision D-23), the last item of release 0.4.

From the comparison with SSMS: running statements of the server (`SHOW PROCESSLIST` or `performance_schema`) with *Kill Query*. Useful when a statement waits on a lock. Parked on 2026-11-02.
