# E07 Query editor

Write and execute SQL against a selected server and database inside Visual Studio.

## US-0701 New Query

**Status:** Done (accepted 2026-10-30)

As a developer, I want to open a query window for a selected database.

**Acceptance criteria**

- [x] Context menu "New Query" on server and database nodes opens a new `.sql` document.
- [x] The document shows the active connection and database in a bar above the editor, with a dropdown to switch database.
- [x] Existing `.sql` files in a project can be linked to a connection through the same bar.

**Tasks**

- [x] T-0701-01 Document links in Core: `DocumentLink`, `Changed` event and rename in `DocumentConnections`, `DocumentLinkStore` (JSON), `QueryConnectionBarViewModel`, `ServerNodeViewModel.EnsurePasswordAsync` + tests
- [x] T-0701-02 MySQL Query Editor (editor factory, content type `MySql`), connection bar as editor margin, command *New Query*

**Implementation notes**

- Own editor, see ADR-012. *MySQL Query Editor* is the Visual Studio code editor with the content type `MySql`. It is registered for `.sql` in *Open With* with priority 0, so a `.sql` file keeps its default editor (for example the T-SQL editor of SSDT) unless the user chooses *MySQL Query Editor* there, optionally with *Set as Default*.
- Documents from the explorer always open in the MySQL Query Editor: *New Query*, *View Code*, *Script As* and *Script Database*. A file that is already open in another editor gives the Visual Studio question to close it first.
- *New Query* is on server nodes and database nodes. It creates an empty `Query<n>.sql` (first free number) in `%TEMP%\ObjectExplorerForMySql\<connection id>`, linked to the server and to the database of the node; on a server node to the default database of the connection, if set.
- The bar above the editor: *Connection* (all servers of the explorer) and *Database*. Picking a server links the document with the default database of that connection and loads the database list; a password that is not saved is asked then. The database list loads when it is opened. Opening a document never asks for a password by itself, also not when Visual Studio restores open documents at startup.
- A choice in the bar is saved right away in `%LOCALAPPDATA%\ObjectExplorerForMySql\documents.json` (path, connection id, database). Links of files that no longer exist are dropped when Visual Studio starts. Save As and a rename move the link to the new path.
- A server that is removed from the explorer empties the bar; adding a server with the same connection id (not possible from the UI today) would show it again. The link itself stays in the file.
- Not in this story: syntax coloring (US-0702) and execution (US-0703). The editor shows plain text until then.

**Manual test**

Use the connection with sakila. SSDT is installed, so a `.sql` file normally opens in the T-SQL editor.

1. Right-click the server node. Expected: *New Query* at the top of the menu, with the New Query icon. Click it. Expected: `Query1.sql` opens; the bar shows the connection and the default database of the connection (empty when none is set). No T-SQL error squiggles when you type `` SELECT `actor_id` FROM actor LIMIT 5; ``.
2. Right-click *sakila* under Databases > *New Query*. Expected: `Query2.sql` with *sakila* in the Database list.
3. Open the Database list. Expected: all databases of the server, *sakila* still selected. Pick *world*. Close and reopen the list: *world* stays.
4. Pick another connection in the Connection list. Expected: its default database is selected and its database list loads. For a connection without a saved password: the password prompt appears; Cancel keeps the connection without a database list.
5. Disconnect a connection with a password that is not saved, then open a query document of that connection and open the Database list. Expected: the password prompt appears only now.
6. Close Visual Studio with `Query2.sql` open and start it again. Expected: the document opens in the MySQL Query Editor with the bar, the same connection and *world*, without a password prompt.
7. *File > Save Query2.sql As...* to a project folder, for example `C:\Temp\report.sql`. Expected: the bar keeps the connection and database. Close and reopen the file with *Open With > MySQL Query Editor*: same connection and database.
8. A `.sql` file in a project: right-click > *Open With...*. Expected: *MySQL Query Editor* in the list. Open it. Expected: empty bar with the hint *Choose a connection to run this query.* Pick a connection and database. Double-click the file in Solution Explorer later: it opens in the T-SQL editor again (default editor unchanged), unless *Set as Default* was used.
9. *View Code* on table *actor* and *Script As > SELECT To > New Query Window*. Expected: both open in the MySQL Query Editor with *sakila* in the bar.
10. Switch the Visual Studio theme (Dark, Light, Blue). Expected: the bar follows the theme; the lists are readable.
11. Split the editor window (*Window > Split*). Expected: both halves show the bar; a change in one is shown in the other.

## US-0702 MySQL syntax coloring

**Status:** Done (accepted 2026-10-30)

**Acceptance criteria**

- [x] Documents in the MySQL Query Editor use MySQL keywords for coloring (own classifier instead of a TextMate grammar, decision D-10).
- [x] Coloring follows the Visual Studio theme.

**Tasks**

- [x] T-0702-01 `MySqlTokenizer`, `MySqlKeywords` and `MySqlLineStates` in Core + tests
- [x] T-0702-02 `MySqlClassifier` (MEF) for the content type `MySql`

**Implementation notes**

- Colors come from the standard Visual Studio classifications, so they follow the theme and *Tools > Options > Environment > Fonts and Colors*: *Keyword*, *Comment*, *String*, *Number*, and *Identifier* for backtick names and variables.
- Keywords: the reserved words of MySQL 8.0/8.4, frequent non-reserved keywords (data types, ENGINE, DEFINER, BEGIN/END, ...) and `DELIMITER`. Built-in functions (COUNT, NOW, CONCAT) keep the text color. A word after a dot (`t.status`) is never a keyword.
- Comments: `-- ` (only with a space or at the line end, as in MySQL, so `5--3` stays a calculation), `#` and `/* */`, also over several lines. `/*!40101 ... */` is colored as a comment, although MySQL runs it.
- Strings in single and double quotes with `''` and backslash escapes; backtick identifiers with ` `` `; strings and backticks can continue on the next line.
- Variables: `@name`, `@@sql_mode`, `@@global.max_connections`, `` @`my var` ``.
- Only the changed lines are read again after an edit, plus the lines after them when a comment or string opens or closes, so large scripts (Script Database with data) stay fast.
- Only documents in the MySQL Query Editor are colored; .sql files in the T-SQL editor are not affected.

**Manual test**

1. *New Query* and type:

   ```sql
   -- line comment
   # hash comment
   SELECT a.actor_id, `first name`, 'it''s', "dq", 12, 1.5, 0x1F, @total, @@sql_mode
   FROM sakila.actor a /* block
   comment */ WHERE a.last_name LIKE 'A%' AND 5--3 = 8
   LIMIT 10;
   ```

   Expected: comments green (Dark theme default), keywords blue, strings red/brown, numbers in the number color, `` `first name` ``, `@total` and `@@sql_mode` in the identifier color. `actor_id`, `last_name` and `a` keep the text color. `5--3` is not a comment.
2. Type `/*` at the start of the first line. Expected: the whole document turns into a comment color. Type `*/` at the end of line 2: the rest gets its colors back.
3. Start a string with `'` on a line and do not close it. Expected: the following lines show the string color until the next `'`.
4. *View Code* on a procedure (for example *film_in_stock*). Expected: `DELIMITER`, `CREATE`, `PROCEDURE`, `BEGIN`, `END`, `IN`, `OUT`, `INT` are keywords.
5. *Script Database...* on modelbuilder with data to a new query window. Expected: the document opens without a noticeable delay; scrolling and typing in the INSERT lines stays smooth.
6. Switch the theme (Dark, Light, Blue). Expected: the colors follow the theme. Change *Keyword* in *Fonts and Colors*: the query editor uses the new color.
7. Open a `.sql` file in the T-SQL editor (double-click in Solution Explorer). Expected: unchanged T-SQL coloring.

## US-0703 Execute and show results

**Status:** Done (accepted 2026-10-30)

As a developer, I want to execute the query and see the results in a grid.

**Acceptance criteria**

- [x] Ctrl+Shift+E executes the selection, or the full document when nothing is selected.
- [x] Results pane below the editor with tabs *Results* (one grid per result set) and *Messages* (rows affected, warnings, duration).
- [x] Cancel button stops a running query (`KILL QUERY`).
- [x] Large result sets: grid virtualization, default limit 1000 rows with a notice.
- [x] Copy cells, copy with headers.

**Tasks**

- [x] T-0703-01 Query executor in Core: `SqlScriptSplitter` (with DELIMITER), `MySqlQuerySession`, `QueryRunner`, `QueryValueFormatter` + unit tests. Integration tests against a real server are not added; the runner is tested with a fake session.
- [x] T-0703-02 Results pane UI with virtualized grid (editor margin below the main view)
- [x] T-0703-03 Execute and cancel commands: key binding scope *MySQL Query Editor* (ADR-013), context menu, buttons in the bar

**Implementation notes**

- *Execute*: Ctrl+Shift+E, the Run button in the bar above the editor, or *Execute* in the context menu of the editor. Runs the selection, or the whole document when nothing is selected. *Cancel Query*: Alt+Break, the Stop button, or the context menu.
- The shortcuts belong to the key binding scope *MySQL Query Editor* (*Tools > Options > Environment > Keyboard*, commands `MySQL.Execute` and `MySQL.CancelQuery`). The editor window inherits the Text Editor shortcuts, so normal editing keys keep working. Ctrl+Shift+E outside this editor keeps its own meaning (ADR-013).
- The script is split into statements as the mysql client does: on `;` outside strings, backtick names and comments; `DELIMITER $$` changes the delimiter, so procedures and triggers from *View Code* and *Script Database* run as they are. Comments before a statement are left out; `/*! ... */` and `/*+ ... */` are code.
- Statements run one by one, in the database of the bar. Execution stops at the first error; the Messages tab shows the MySQL error number, the line in the editor and the message.
- One server session per document (decision D-11): user variables, temporary tables, `USE` and an open transaction carry over to the next run, as in MySQL Workbench and SSMS. The session closes with the document, and is replaced when another connection is chosen or the connection was lost. A `USE` in the script updates the Database list in the bar.
- *Results* tab: one grid per result set; several result sets are stacked, each with its own scroll bar. At most 1000 rows per result set are shown; the rest is read and counted, so the Messages tab gives the real total (`16044 row(s) returned; the first 1000 are shown.`). Cancel stops reading a large result.
- Values: `NULL` for NULL, numbers and dates in invariant format (`2026-10-30 14:05:00`, DATE as `2026-10-30`), TIME as `838:59:59`, binary data as hex (first 64 bytes), zero dates as `0000-00-00`. TINYINT(1) shows 0/1 and CHAR(36) the text, as the server stores them.
- *Messages* tab: rows returned or affected per statement, warnings and notes of the server, and the total duration. After a run the pane shows *Results* when there are result sets and no error, otherwise *Messages*.
- Copy: Ctrl+C or *Copy* in the context menu of a grid copies the selected cells (all cells when nothing is selected), tab-separated; *Copy with Headers* adds the column names.
- The pane appears at the first run, can be resized by dragging its top edge and closed with the ✕ button; the next run shows it again.
- The editor keeps the keyboard focus during and after a run; the Run and Stop buttons take no focus. Only when the user clicked into the results pane during the run, the focus stays there.
- Not in this story: sorting the grid, export (US-0704), a setting for the row limit (P-05).

**Manual test**

Use sakila.

1. *New Query* on *sakila*. Type `SELECT * FROM actor;` and press Ctrl+Shift+E. Expected: the results pane opens below the editor with 200 rows in a grid; Messages: `200 row(s) returned.` and `1 statement(s) completed in ... ms.`
2. Check the editor still works normally: arrow keys, Ctrl+Z, Ctrl+L (cut line), Alt+Up (move line), Ctrl+F. Press Ctrl+Shift+E in a C# file: Visual Studio's own command (or nothing), no MySQL execution.
3. Type a second statement `SELECT * FROM film_text LIMIT 5;`, select only that line and click the Run button in the bar. Expected: only that statement runs (5 rows).
4. Run `SELECT * FROM rental;` Expected: 1000 rows in the grid; Messages: `16044 row(s) returned; the first 1000 are shown.`
5. Run without selection:
   ```sql
   SELECT COUNT(*) FROM actor;
   SELECT * FROM category;
   UPDATE actor SET first_name = first_name WHERE actor_id = 1;
   ```
   Expected: two grids stacked; Messages has `1 row(s) returned.`, `16 row(s) returned.`, `0 row(s) affected.`
6. Error: `SELECT 1;` on line 1, `SELEC 2;` on line 3, `SELECT 3;` on line 4. Run all. Expected: Messages tab is shown with `Error 1064 at line 3: You have an error in your SQL syntax...`; `SELECT 3` did not run.
7. Session: run `SET @x = 42;`, then run `SELECT @x;` separately. Expected: 42. Run `USE world;` Expected: the Database list in the bar shows *world*.
8. DELIMITER: *View Code* on procedure *film_in_stock*, change `CREATE PROCEDURE` into `CREATE PROCEDURE film_in_stock_copy` (name only), run the whole document. Expected: no error; the procedure exists (Refresh in the explorer). Drop it afterwards with `DROP PROCEDURE film_in_stock_copy;`.
9. Cancel: run `SELECT SLEEP(30);` and press Alt+Break (or click Stop) after a few seconds. Expected: `Cancelled after ...`; the Run button is enabled again; `SELECT 1;` runs right after.
10. Warnings: run `SELECT CAST('12abc' AS UNSIGNED);` Expected: Messages shows `Warning 1292: Truncated incorrect INTEGER value: '12abc'`.
11. Values: `SELECT NULL, 1.50, NOW(), CURDATE(), CAST('838:59:59' AS TIME), 0x0AFF, picture FROM staff LIMIT 1;` Expected: `NULL`, `1.50`, date-time, date only, `838:59:59`, `0x0AFF`, the picture as hex ending with `...`.
12. Copy: click a cell in the grid, press Ctrl+C and paste in Notepad: the value. Select a block of cells with the mouse, right-click > *Copy with Headers*: column names and values, tab-separated. Press the arrow keys in the grid: the cell selection moves (not the editor caret).
13. Pane: drag the top edge to make it larger and smaller; close it with ✕; run again: it opens again. Switch the theme (Dark, Light, Blue): the pane, grid headers and selection follow the theme.
14. Connection: pick a connection without a saved password and run. Expected: the password prompt; Cancel runs nothing. A document without connection: Messages says *Choose a connection in the bar above the editor.*
15. Close the document after step 7 and open the server's process list (`SHOW PROCESSLIST;` in another query window). Expected: no session of the closed document left.
16. Focus (fix after the first test round): run with Ctrl+Shift+E and with the Run button. Expected: right after the run the arrow keys move the caret in the editor without clicking in it first. Click a cell in the grid during a long run (`SELECT SLEEP(5), 1;`): the focus stays in the grid.

## US-0704 Export results

**Status:** Done (accepted 2026-10-30)

As a developer, I want to save a result set as a file, so I can use it in Excel or another tool.

**Acceptance criteria**

- [x] Save a result set as CSV or JSON.

**Tasks**

- [x] T-0704-01 `QueryResultExporter` in Core (CSV and JSON) + tests; *Save Results As...* in the context menu of a result grid

**Implementation notes**

- Picked up from the parked list (P-04) on 2026-10-30.
- *Save Results As...* in the context menu of a grid saves that result set. The file type follows the choice in the save dialog: CSV or JSON.
- Only the rows shown are saved (at most 1000, US-0703). When the result had more rows, a question first says how many rows are saved. Saving the full result is parked as P-05.
- CSV: RFC 4180, comma separated, a header line with the column names, fields with a comma, quote or line break in double quotes, NULL as an empty field. UTF-8 with BOM, so Excel shows accents right. Values as in the grid (invariant numbers, ISO dates); binary data in full as hex.
- JSON: an array with one object per row; numbers stay numbers, NULL is `null`, other values are strings. A column name that occurs twice gets a suffix (`id_2`). UTF-8 without BOM.

**Manual test**

1. Run `SELECT * FROM actor;` Right-click the grid > *Save Results As...*, keep *CSV file*, save as `actor.csv`. Open it in Notepad: a header line `actor_id,first_name,last_name,last_update` and 200 lines. Open it in Excel (*Data > From Text/CSV*): 200 rows, 4 columns.
2. Save the same result as `actor.json` (choose *JSON file* in the dialog). Open it in Visual Studio: valid JSON, `"actor_id": 1` as a number, `last_update` as a string.
3. Run `SELECT NULL AS a, 'x,"y"' AS b, 1 AS a;` and save as CSV and as JSON. Expected CSV: `a,b,a` and `,"x,""y""",1`. Expected JSON: `{"a": null, "b": "x,\"y\"", "a_2": 1}`.
4. Run `SELECT * FROM rental;` and choose *Save Results As...* Expected: the question that only 1000 of 16044 rows are saved; *No* saves nothing, *Yes* opens the save dialog.
5. With two result sets (`SELECT * FROM category; SELECT * FROM language;`): *Save Results As...* on the second grid saves only the languages.
6. Save to a read-only file or a folder without write access. Expected: an error message; Visual Studio keeps running.

## US-0705 Export the full result

**Status:** Ready for test

As a developer, I want to export all rows of a query result, also beyond the 1000 rows the results pane shows, so that an export is complete. From P-05 (decision D-20).

**Acceptance criteria**

- [x] When a result was cut off at the row limit, *Save Results As...* asks: *Save the 1000 rows shown* or *Run the statement again and save all rows*.
- [x] Running again is only offered for statements without side effects: SELECT, SHOW, DESCRIBE, EXPLAIN and WITH ... SELECT. Other statements only save the rows shown.
- [x] The rows go straight from the server to the CSV or JSON file, without keeping them in memory; same format as US-0704.
- [x] Progress with the number of rows and Cancel (the Visual Studio wait dialog, as in Script Database). A cancelled export removes the incomplete file. Changed at the build: the criterion said *Visual Studio stays usable*, but the wait dialog blocks Visual Studio while it is open, as with Script Database and Generate Documentation; the export itself runs in the background, so Visual Studio does not freeze.
- [x] The statement runs on its own connection, not in the session of the document (D-11), so temporary tables and variables of the session are not available: the message says so when the statement fails.
- [x] A result that was not cut off is saved as before, without running anything.

**Tasks**

- [x] T-0705-01 `ExportStatement.CanRunAgain` + tests
- [x] T-0705-02 `QueryRunner` keeps the statement, connection and database of a result that was cut off (`QueryResultSet.Source`) + tests
- [x] T-0705-03 `QueryResultExporter` writes rows as they come; `FullResultExporter` runs the statement on its own connection and streams the rows + tests
- [x] T-0705-04 *Save Results As...*: the question, the wait dialog with row count and Cancel, the messages

**Implementation notes**

- When a statement returns one result set that is cut off and the statement may run again, the runner keeps the statement text, the connection and the current database of the session (read with `SELECT DATABASE()` right after the statement, so a `USE` earlier in the script counts). Nothing else changes for a normal run.
- *Save Results As...* on such a result asks with Yes / No / Cancel: *Yes* runs the statement again and saves all rows, *No* saves the rows shown, *Cancel* stops. The save dialog comes after the answer.
- A result that was cut off but may not run again keeps the old question, which now also says why: only SELECT, SHOW, DESCRIBE and EXPLAIN run again.
- May run again: SELECT, TABLE, VALUES, a parenthesized SELECT with UNION, SHOW, DESCRIBE/DESC, EXPLAIN, and WITH whose main statement is not INSERT, UPDATE, DELETE or REPLACE. Not: anything with INTO at the top level (`SELECT ... INTO OUTFILE`, `INTO @var`), `EXPLAIN ANALYZE` and MariaDB `ANALYZE` (they run the statement), CALL and all other statements. Words in strings, quoted names, comments and subqueries do not count. A stored function called in a SELECT can still change data; the text does not show that.
- The export opens its own connection (no pooling, the same value settings as the results pane), switches to the database of the session and runs the statement without a time limit. Every row goes from the server to the file right away, so memory use stays flat for millions of rows. CSV and JSON are written by the same code as US-0704, so the format is identical.
- The wait dialog shows *n rows saved*, updated every 1000 rows. Cancel stops the statement on the server (KILL QUERY through MySqlConnector) and removes the file. When the export is done a message shows the row count and the file.
- When the statement fails on the new connection (for example a temporary table of the document), the message shows the server error and explains that the statement runs on its own connection.
- The rows saved can differ from the count shown in the grid when the data changed in between; the export saves what the server returns now.

**Manual test**

Use *sakila*.

1. Run `SELECT * FROM rental;` (16044 rows, 1000 shown). Right-click the grid > *Save Results As...* Expected: a question with *Yes* (run again, all rows), *No* (the 1000 rows shown) and *Cancel*.
2. Choose *Yes*, save as `rental.csv`. Expected: the wait dialog with the row count; then the message *16044 rows are saved to: ...*. Open the file: a header line and 16044 data lines; the first lines match the grid.
3. Repeat with `rental.json`: valid JSON with 16044 objects; numbers stay numbers.
4. Choose *No*: 1000 rows are saved, as in US-0704. Choose *Cancel*: nothing happens.
5. Run `SELECT 1;`: *Save Results As...* goes straight to the save dialog, no question.
6. A larger result, for example `SELECT r.*, p.* FROM rental r CROSS JOIN payment p LIMIT 3000000;`: press *Cancel* in the wait dialog. Expected: the dialog closes quickly, no file is left, Visual Studio keeps running.
7. If the *world* sample database is installed: run `USE world; SELECT * FROM city;` in a document linked to *sakila* (4079 rows): *Yes* saves the cities, so the export runs in *world*.
8. `CREATE TEMPORARY TABLE t AS SELECT * FROM rental; SELECT * FROM t;` then *Yes*. Expected: an error message that the table does not exist, with the note about the own connection; no file is left.
9. A statement that may not run again, for example `CALL` of a procedure that returns more than 1000 rows: the old question, which says only SELECT, SHOW, DESCRIBE or EXPLAIN run again.
10. `SHOW GLOBAL STATUS;` or another SHOW over the row limit (if available): *Yes* saves all rows.
11. Save to a read-only file: an error message; Visual Studio keeps running.
