# E14 IntelliSense in the query editor

**Status:** Done (accepted 2026-11-03)

Completion of names in the MySQL Query Editor from the metadata of the linked connection. From the comparison with SSMS.

## US-1401 Completion of names

**Status:** Done (accepted 2026-11-03)

As a developer, I want the editor to suggest databases, tables, views, columns and routines while I type, so that I type less and make fewer mistakes.

**Acceptance criteria**

- [x] Completion list (Ctrl+Space and while typing) with keywords, databases, tables, views, procedures and functions of the linked connection and database.
- [x] After `table.` or `alias.`: the columns of that table; aliases from the FROM and JOIN parts of the statement.
- [x] Names are quoted when needed (setting of US-0504).
- [x] The metadata is read once per connection and database and cached; Refresh in the explorer clears the cache. Typing never waits for the server.

**Tasks**

- [x] T-1401-01 `SqlCompletionAnalyzer`: word at the caret, qualifier before the dot, tables and aliases of the statement + tests
- [x] T-1401-02 `SchemaCache` and `CompletionBuilder` + tests
- [x] T-1401-03 Async completion source and commit manager in the MySQL Query Editor, cache cleared by Refresh

**Implementation notes**

- Visual Studio async completion (`IAsyncCompletionSource`), only for the content type of the MySQL Query Editor. The list opens on Ctrl+Space and when a letter, `_`, `` ` `` or `.` is typed; never in a string, a comment, a number or after `@`.
- Without a dot: keywords, the databases of the connection, the tables, views, procedures and functions of the database of the query bar, and the columns of the tables in the statement (the tooltip names the table and type).
- After a dot: `alias.` and `table.` give the columns in table order; `database.` gives the tables, views and routines of that database; `database.table.` gives its columns.
- Tables and aliases come from the FROM (with commas), JOIN, UPDATE and INTO parts of the statement at the caret. `AS` is optional; a keyword after the table is no alias. A statement ends at `;` (a procedure body with `;` inside counts as several statements, so aliases do not reach across them).
- Quoting follows the Drag & Drop option *Quote SQL names* (US-0504). After a typed backtick the name is always quoted.
- The chosen name is committed with Tab, Enter, or by typing `.`, `,`, `(`, `)` or `;`. Not with a space: when you type an alias such as `f` after `film`, a space would replace it with a name from the list. Kept on purpose after the test (decision D-21).
- `SchemaCache`: per connection the list of databases, per database its tables, views and routines, per table its columns. Read once on a background thread and kept; a failed read is not kept, so the next keystroke tries again. *Refresh* on any node of a server clears the cache of that server.
- The list never asks for a password: when the password of the connection is not known yet (not saved and not connected), only keywords are offered. Waiting for metadata only delays the list; typing goes on.

**Manual test**

Use *sakila* on a connected server, in a New Query on *sakila*.

1. Type `SEL`: the list opens with *SELECT* and other keywords. Tab inserts `SELECT`.
2. Type `SELECT * FROM f`: the list shows *film*, *film_actor*, *film_category*, *film_list* (view), and functions and procedures starting with *f* (each with its icon). Enter inserts the name.
3. Type `SELECT f.` in `SELECT f. FROM film f`: after the dot the columns of *film* in table order; the tooltip shows the type. Also with `JOIN film_actor fa ON fa.`: the columns of *film_actor*.
4. `sakila.` gives the tables of sakila; `sakila.film.` gives its columns. `mysql.` gives the tables of the *mysql* database.
5. Ctrl+Space in an empty spot: the full list. In a string `'fi` or after `--`: no list. After `@`: no list.
6. Quoting: a database or table with a space or a reserved word (for example a table `order`) is inserted as ``` `order` ```. Set *Quote SQL names* to *Always*: every name gets backticks.
7. Type `FROM film f` and a space after `f`: the alias stays `f`.
8. Create a table in another query window, then type its name: not in the list (cached). *Refresh* in the explorer, type again: now it is.
9. A connection whose password is not saved, before connecting: only keywords, no password dialog.
10. Type quickly with a slow or unreachable server: the editor never freezes.

## US-1402 Parameter info and quick info

**Status:** Done (accepted 2026-11-03)

As a developer, I want to see the parameters of a routine while I type the call, and the details of a table or column when I hover over it.

**Acceptance criteria**

- [x] Parameter info for procedures and functions after `(`.
- [x] Quick info on hover over a table or column: type, nullable, key, comment.

**Tasks**

- [x] T-1402-01 `SqlCompletionAnalyzer.SignatureAt` and `SymbolAt`, `IntelliSenseInfoBuilder` (signature, quick info), parameters and details in `SchemaCache` + tests
- [x] T-1402-02 Quick info source, signature help source and the command filter that opens and follows parameter info

**Implementation notes**

- Parameter info opens after `(` and `,`, and with Ctrl+Shift+Space (Edit.ParameterInfo), when the name before the parenthesis is a procedure or function of the database (or `db.routine`). Built-in functions such as `COUNT(` get no tip; a keyword before `(` (`IN (`, `VALUES (`) is no call.
- Procedures show the mode of each parameter: `film_in_stock(IN p_film_id int, IN p_store_id int, OUT p_film_count int)`. Functions show the return type: `inventory_in_stock(p_inventory_id int) RETURNS tinyint(1)`. The routine comment is the description.
- The parameter at the caret is in bold; it follows the caret and the commas (commas inside strings and nested parentheses do not count). The tip closes when the caret leaves the call, after `)`, and with Esc.
- Quick info on a name:
  - column (`f.title`, `title` of a table in the statement, `db.table.column`): `film.title (column)`, then the type, NULL or NOT NULL, primary key, foreign key, extra (`auto_increment`), and the comment;
  - table or view: `sakila.film (table)`, the engine and the comment;
  - procedure or function: its signature and comment;
  - database: `sakila (database)`.
  Keywords and unknown names show nothing.
- Same rules as the completion list (US-1401, D-21): data from `SchemaCache` (parameters are cached per routine too), never a password dialog, and the tip only appears when the data is there; typing never waits.

**Manual test**

Use *sakila* on a connected server, in a New Query on *sakila*.

1. Type `CALL film_in_stock(`: the tip shows `film_in_stock(IN p_film_id int, IN p_store_id int, OUT p_film_count int)` with *p_film_id* in bold.
2. Type `1, `: *p_store_id* is bold. Move the caret back into the first argument: *p_film_id* is bold again.
3. Type `)`: the tip closes. Esc also closes it.
4. `SELECT inventory_in_stock(`: the tip ends with `RETURNS tinyint(1)`.
5. Ctrl+Shift+Space inside the parentheses of an existing call: the tip opens.
6. `SELECT COUNT(` and `WHERE id IN (`: no tip.
7. Hover over `film` in `SELECT * FROM film`: `sakila.film (table)`, InnoDB and the comment.
8. Hover over `title` in `SELECT f.title FROM film f` and in `SELECT title FROM film`: `film.title (column)`, `varchar(128) NOT NULL` and so on. Hover over `film_id`: also *primary key* and *auto_increment*.
9. Hover over a procedure name and over `sakila` in `USE sakila`: the signature, and `sakila (database)`.
10. Hover over `SELECT`: nothing.
11. A connection whose password is not known yet: no tips, no password dialog.
