# E06 Script and view code

Open the source of objects and generate standard SQL scripts.

## US-0601 View Code

**Status:** Ready for test

As a developer, I want to open the definition of a table, view, procedure, function, trigger or event.

**Acceptance criteria**

- [x] Context menu "View Code" opens a new `.sql` document with the output of `SHOW CREATE ...`.
- [x] Document title: `<database>.<object>.sql`.
- [ ] The document is linked to the connection (see E07), so it can be executed directly. *Partly: the link is stored now; executing follows in E07.*

**Tasks**

- [x] T-0601-01 `SHOW CREATE` per object type in Core + tests
- [x] T-0601-02 Open temporary document via VS shell API

**Implementation notes**

- *View Code* appears in the context menu of tables, views, stored procedures, functions, triggers and events, above *Refresh*.
- Statements: `SHOW CREATE TABLE|VIEW|PROCEDURE|FUNCTION|TRIGGER|EVENT` with quoted names. The system views of `information_schema` have no view definition; for them *View Code* uses `SHOW CREATE TABLE`.
- Document layout: a comment line with type, object and connection (`-- Table sakila.film on Local`), an empty line, then the statement. Tables and views end with `;`. Procedures, functions, triggers and events are wrapped in `DELIMITER $$ ... $$ DELIMITER ;`, as MySQL Workbench does, so the script runs in a MySQL client.
- The file is written to `%TEMP%\ObjectExplorerForMySql\<connection id>\<database>.<object>.sql`; one folder per connection, so equal names on two servers do not clash. The document is a normal file: you can edit it and use *Save As* to keep it.
- When the document is already open, *View Code* shows it and does not overwrite it, so unsaved edits are kept. Close it first to load the current definition again.
- The link between document and connection/database is stored in memory (`DocumentConnections`); the query editor (E07) uses it to run the document on the right server.
- When the server returns no source (for a routine the account did not define and without the `SHOW_ROUTINE` privilege), a message explains why. Errors (for example missing privileges) show the server message.
- Visual Studio opens `.sql` files in its SQL Server (T-SQL) editor. That editor may underline MySQL syntax such as backticks or `DELIMITER` as errors; MySQL-aware coloring and checking are planned in US-0702.

**Manual test**

Use sakila.

1. Right-click table *film*, choose *View Code*. Expected: a document `sakila.film.sql` opens with `-- Table sakila.film on <your connection>` and the full `CREATE TABLE` statement with columns, keys, foreign keys and table options, ending with `;`.
2. View Code on view *actor_info*. Expected: `sakila.actor_info.sql` with `CREATE ALGORITHM=... SQL SECURITY INVOKER VIEW ...;`.
3. View Code on procedure *film_in_stock*. Expected: `DELIMITER $$`, the `CREATE DEFINER=... PROCEDURE ...` with its body, ending with `END$$`, then `DELIMITER ;`.
4. View Code on function *get_customer_balance*, trigger *film > Triggers > ins_film* and (if present) an event. Expected: the same layout with DELIMITER.
5. View Code on *information_schema > Views > TABLES*. Expected: a `CREATE TEMPORARY TABLE ...` statement.
6. Change something in `sakila.film.sql` without saving, then View Code on *film* again. Expected: the open document is shown, your change is still there.
7. Close it without saving and run View Code again. Expected: the definition from the server.
8. Right-click a column, key, index or folder. Expected: no *View Code* in the menu.
9. Optional: copy the procedure document into a MySQL client and run it on a test database. Expected: it runs because of the DELIMITER lines.

## US-0602 Script As

**Status:** Todo

As a developer, I want ready-made SQL for common statements on a table.

**Acceptance criteria**

- [ ] Context menu *Script Table As*: CREATE, DROP, SELECT, INSERT, UPDATE, DELETE.
- [ ] Target: new query window, or clipboard.
- [ ] INSERT and UPDATE use placeholders for values, skip generated and auto-increment columns in INSERT.
- [ ] *Script Procedure As*: CREATE, DROP, CALL.

**Tasks**

- T-0602-01 `ScriptGenerator` in Core + tests per statement
- T-0602-02 Context menus

## US-0603 Script database

**Status:** Todo

As a developer, I want a full DDL script of a database (replacement for the SQL Server "Extract Data-tier Application").

**Acceptance criteria**

- [ ] Context menu on database "Script Database" generates CREATE statements for tables (in foreign-key order), views, routines, triggers and events.
- [ ] Optional: include data as INSERT statements, with a row limit per table.
- [ ] Result opens in a new `.sql` document or is saved to a file.
