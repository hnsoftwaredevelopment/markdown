# E06 Script and view code

Open the source of objects and generate standard SQL scripts.

## US-0601 View Code

**Status:** Done (accepted 2026-10-29)

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
9. Optional: copy the procedure document into a MySQL client and run it on a test database. Expected: it runs because of the DELIMITER lines. *(Checked 2026-10-29 in DBeaver.)*

## US-0602 Script As

**Status:** Ready for test

As a developer, I want ready-made SQL for common statements on a table.

**Acceptance criteria**

- [x] Context menu *Script Table As*: CREATE, DROP, SELECT, INSERT, UPDATE, DELETE.
- [x] Target: new query window, or clipboard.
- [x] INSERT and UPDATE use placeholders for values, skip generated and auto-increment columns in INSERT.
- [x] *Script Procedure As*: CREATE, DROP, CALL.
- [x] Added (decision 2026-10-29): views (CREATE, DROP, SELECT) and functions (CREATE, DROP, SELECT of a call).

**Tasks**

- [x] T-0602-01 `ScriptGenerator` in Core + tests per statement
- [x] T-0602-02 Context menus

**Implementation notes**

- Menu: *Script As > CREATE To / DROP To / SELECT To / INSERT To / UPDATE To / DELETE To / CALL To > New Query Window / Clipboard*, like SQL Server Object Explorer. Only the statements of the selected object type are shown.

| Object | CREATE | DROP | SELECT | INSERT | UPDATE | DELETE | CALL |
|---|---|---|---|---|---|---|---|
| Table | yes | yes | yes | yes | yes | yes | |
| View | yes | yes | yes | | | | |
| Procedure | yes | yes | | | | | yes |
| Function | yes | yes | yes (`SELECT fn(...)`) | | | | |

- Placeholders are user variables named after the column or parameter (decision 2026-10-29): `VALUES (@title, @description)`, `SET title = @title`, `CALL sakila.film_in_stock(@p_film_id, ...)`. The script runs after `SET @title = ...;`.
- SELECT lists every column in table order. INSERT skips auto-increment and generated columns. UPDATE sets every column except the primary key, auto-increment and generated columns. UPDATE and DELETE filter on the primary key (`WHERE actor_id = @actor_id AND film_id = @film_id` for a composite key).
- Without a primary key, UPDATE and DELETE get `WHERE 1 = 0` and a comment, so a script that is run by accident changes no rows.
- Scripts always name the database (`sakila.film`), so they run whatever database is active. Backticks follow the option *Backticks in .sql files* (US-0504); user variables get backticks only when needed.
- CREATE uses `SHOW CREATE` as in View Code, with DELIMITER for procedures and functions. DROP is a plain `DROP TABLE|VIEW|PROCEDURE|FUNCTION db.name;` (no `IF EXISTS`, so a typo gives an error).
- *New Query Window* opens `<database>.<object>.<STATEMENT>.sql` (for example `sakila.film.INSERT.sql`) with a comment line, linked to the connection like View Code; an open document is shown, not overwritten. *Clipboard* copies only the statement.
- Columns and parameters are read from the server at the moment of scripting, so the script matches the current definition, also when the tree was not refreshed.
- Fix found while testing the scripts (since US-0302): columns with an expression default such as `last_update ... DEFAULT CURRENT_TIMESTAMP` (EXTRA `DEFAULT_GENERATED`) counted as generated columns: computed-column icon in the tree, *Is Generated* True in the Properties window. Now only `VIRTUAL GENERATED`, `STORED GENERATED` and `PERSISTENT GENERATED` count.

**Manual test**

Use sakila and the New Query Window target unless stated otherwise.

1. Right-click table *actor*, open *Script As*. Expected: CREATE To, DROP To, SELECT To, INSERT To, UPDATE To, DELETE To; no CALL To.
2. SELECT To > New Query Window. Expected: `sakila.actor.SELECT.sql` with `SELECT actor_id, first_name, last_name, last_update FROM sakila.actor;` (one column per line).
3. INSERT To. Expected: `INSERT INTO sakila.actor (first_name, last_name, last_update) VALUES (@first_name, @last_name, @last_update);` (no `actor_id`, which is auto-increment).
4. UPDATE To. Expected: `SET first_name = @first_name, last_name = @last_name, last_update = @last_update` and `WHERE actor_id = @actor_id;`.
5. DELETE To on *film_actor*. Expected: `WHERE actor_id = @actor_id AND film_id = @film_id;`.
6. CREATE To and DROP To on *actor*. Expected: the CREATE TABLE statement as in View Code; `DROP TABLE sakila.actor;`.
7. Script As on view *actor_info*. Expected: only CREATE, DROP and SELECT.
8. Procedure *film_in_stock*: CALL To > Clipboard, paste. Expected: `CALL sakila.film_in_stock(@p_film_id, @p_store_id, @p_film_count);` without comment line.
9. Function *get_customer_balance*: SELECT To. Expected: `SELECT sakila.get_customer_balance(@p_customer_id, @p_effective_date);`.
10. Right-click a column, a trigger or a folder. Expected: no *Script As*.
11. Set *Backticks in .sql files* to *Always* and script INSERT for *actor*. Expected: `` `sakila`.`actor` `` and backticked column names; the `@` variables stay as they are. Reset the option.
12. Check the fix: expand *actor > Columns*. Expected: `last_update` has the normal column icon; Properties shows *Is Generated* False.
13. Optional: run the INSERT in DBeaver after `SET @first_name = 'TEST', @last_name = 'USER', @last_update = NOW();`, then the DELETE with `SET @actor_id = LAST_INSERT_ID();`.

## US-0603 Script database

**Status:** Todo

As a developer, I want a full DDL script of a database (replacement for the SQL Server "Extract Data-tier Application").

**Acceptance criteria**

- [ ] Context menu on database "Script Database" generates CREATE statements for tables (in foreign-key order), views, routines, triggers and events.
- [ ] Optional: include data as INSERT statements, with a row limit per table.
- [ ] Result opens in a new `.sql` document or is saved to a file.
