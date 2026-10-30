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
