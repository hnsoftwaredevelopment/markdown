# Parked

Ideas that are postponed. They get an epic number when they are picked up.

## P-01 Table designer

Create and alter tables visually (columns, types, keys, indexes) with a preview of the generated `ALTER TABLE`. Useful for small changes from Visual Studio; not required because management happens elsewhere.

## P-02 Database documentation as PDF

Generate a PDF for a selected database with all tables, columns, data types, keys, indexes, routines and their comments. Possibly also Markdown output for use in a repository or Obsidian.

## P-03 Schema compare and data compare

Compare two databases (or a database and a script) and generate a migration script. Large effort; first find out whether users need it.

## P-04 Export query results

Picked up on 2026-10-30 as US-0704 in E07: CSV and JSON export of the rows shown in a result grid.

## P-05 Full result beyond the row limit

The results pane keeps at most 1000 rows per result set (US-0703), and the export saves those rows (US-0704). Ideas:

- *Show all rows* in the grid on request, with a warning for very large results (memory of Visual Studio).
- *Export full result*: run the statement again and stream all rows straight to the CSV or JSON file, without keeping them in memory, with progress and Cancel. Needs care: the statement runs a second time, so only for statements without side effects (SELECT, SHOW).
- A setting for the row limit.
