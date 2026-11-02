# E09 Object management

Make small changes directly from the tree. Full visual table design is parked (see Parked).

## US-0901 Delete objects

**Status:** Done (accepted 2026-11-02)

**Acceptance criteria**

- [x] Context menu "Delete" (Del key) on database, table, view, procedure, function, trigger, event, index and column.
- [x] Confirmation dialog shows the exact SQL that will run.
- [x] Deleting a database requires typing the database name.
- [x] Tree refreshes the parent node after success.

**Tasks**

- [x] T-0901-01 DROP statement builder per type + tests (`DropTarget`, `ObjectDeleter`, `DeleteConfirmation`)
- [x] T-0901-02 Confirmation dialog and command (`DeleteObjectDialog`, *Delete* in the node menu, Del in the explorer)

**Implementation notes**

- One object at a time: the selected node (decision D-14).
- Statements, every name quoted with backticks:

  | Object | SQL |
  |---|---|
  | Database | `` DROP DATABASE `shop`; `` |
  | Table, view, procedure, function, trigger, event | `` DROP TABLE `shop`.`orders`; `` (keyword per kind) |
  | Index | `` ALTER TABLE `shop`.`orders` DROP INDEX `ix_date`; `` |
  | Index PRIMARY | `` ALTER TABLE `shop`.`orders` DROP PRIMARY KEY; `` |
  | Column | `` ALTER TABLE `shop`.`orders` DROP COLUMN `note`; `` |

- *Delete* is not shown on servers, folders, keys, check constraints, parameters, view columns and anything in a system database (mysql, information_schema, performance_schema, sys). A foreign key or unique key is removed through its index or with a query.
- The dialog (own window, follows the theme) shows the SQL read-only in Consolas with *Copy SQL*. Cancel is the default button: Enter or Escape never deletes. For a database the *Delete* button is only enabled when the exact name is typed (case-sensitive).
- The statement runs on its own connection. After success the parent folder is refreshed; for an index or column the whole table node, because keys and indexes change with it. Expanded nodes stay expanded; the folder gets the selection.
- A server error (for example a table referenced by a foreign key) is shown in a message box; the tree stays as it was. The Output window logs every delete (Info) and the SQL (Debug).
- Del is bound in the explorer scope only and is disabled while a text box has focus, so Del in the search box still deletes text.
- Not handled: an open View Data window or query document of a deleted object stays open; it gives a server error on the next action.

**Manual test**

Use a test database, for example `CREATE DATABASE oe_delete_test;` with a table `t (id INT PRIMARY KEY, note VARCHAR(20), INDEX ix_note (note))`, a view, a procedure, a function, a trigger and an event.

1. Right-click table *t*: *Delete* is in the menu with a red cross. The dialog shows *Delete table oe_delete_test.t?* and `` DROP TABLE `oe_delete_test`.`t`; ``. *Copy SQL* puts the SQL on the clipboard. Cancel: nothing happens.
2. Select the table and press Del: the same dialog. Press Enter: the dialog closes without deleting (Cancel is the default).
3. Delete the column *note*: `` ALTER TABLE ... DROP COLUMN `note`; ``. Expected: the column is gone, and *ix_note* is gone from Indexes; expanded folders stay expanded.
4. Delete index PRIMARY: `` ALTER TABLE ... DROP PRIMARY KEY; ``. The key icon disappears from *id*.
5. Delete the view, procedure, function, trigger and event, one by one: each disappears from its folder.
6. Delete a table that another table references with a foreign key: the server error appears in a message box and the table stays in the tree.
7. Delete database *oe_delete_test*: the *Delete* button stays disabled until you type `oe_delete_test` exactly (try `OE_delete_test` first). After Delete the database is gone from the tree and the Databases folder is selected.
8. *Delete* is not in the menu of a server, a folder, a key, a check constraint, a parameter, a column of a view and objects in *System Databases*.
9. Type in the explorer search box and press Del: the text is deleted, nothing else happens.
10. Disconnect the server: *Delete* is disabled.
11. Theme (Dark, Light, Blue): the dialog follows the theme and the SQL is readable.

## US-0902 Rename objects

**Status:** Done (accepted 2026-11-02)

**Acceptance criteria**

- [x] Context menu "Rename" (F2) on table, view and column.
- [x] Table: `RENAME TABLE`; column: `ALTER TABLE ... RENAME COLUMN` (MySQL 8.0+).
- [x] Inline edit in the tree, Escape cancels.

**Tasks**

- [x] T-0902-01 `RenameTarget` (statement and name check), `ObjectRenamer` (run, refresh, select again), `SupportsRenameColumn` + tests
- [x] T-0902-02 Inline edit box in the tree, *Rename* in the node menu, F2 in the explorer

**Implementation notes**

- Statements, every name quoted with backticks:
  - Table and view: `` RENAME TABLE `shop`.`orders` TO `shop`.`sales`; `` (RENAME TABLE also renames a view in the same database).
  - Column: `` ALTER TABLE `shop`.`orders` RENAME COLUMN `note` TO `remark`; ``
- *Rename* is shown on tables, views and columns of a table. Not on a view column, not in a system database, and not on a column when the server has no RENAME COLUMN (MySQL before 8.0, MariaDB before 10.5.2); older servers need `CHANGE COLUMN` with the full column definition, which belongs in a query.
- The edit box shows the bare name (for a column without the type part of the label), with all text selected. Enter or clicking elsewhere renames; Escape cancels. Up and Down do not move the selection while editing.
- No confirmation dialog: a rename does not lose data, and SSMS does not ask either. The statement is written to the Output window (Info).
- An unchanged or empty name does nothing. A name longer than 64 characters or ending with a space gives a message before anything runs. A server error (for example *Table 'sales' already exists*) is shown in a message box; the tree keeps the old name.
- After success the folder is refreshed (for a column the whole table node, so keys and indexes show the new name), the object is selected under its new name, and a table or view that was expanded is expanded again.
- While a text box in the explorer has focus, F2, Del and Ctrl+C (copy object name) are disabled, so the keys work on the text.
- Not handled: an open View Data window of a renamed table keeps the old name and gives a server error on the next action; close it and open View Data again.

**Manual test**

Use a test database with table `t (id INT PRIMARY KEY, note VARCHAR(20), INDEX ix_note (note))` and a view `v` on it.

1. Select table *t* and press F2: the name becomes an edit box with *t* selected. Type `t2` and press Enter. Expected: the table is renamed, selected and, when it was expanded, expanded again. The Output window shows the RENAME TABLE statement.
2. Right-click the table: *Rename* is in the menu above *Delete*. Start a rename and press Escape: nothing changes.
3. Start a rename, type a new name and click another node: the rename runs.
4. Rename column *note* to `remark`. Expected: the edit box shows only `note` (no type); after Enter the column is called *remark*, is selected, and the index *ix_note* still exists on *remark*.
5. Rename view *v*: it is renamed in the Views folder.
6. Rename a table to the name of another existing table: the server error appears; the tree keeps the old name.
7. Rename to an empty name or the same name: nothing happens. Paste a name of 65 characters: message about the maximum length, nothing runs.
8. In the edit box: Ctrl+A, Ctrl+C, Ctrl+V, Del, Home and End work on the text; Up and Down do nothing.
9. *Rename* is not in the menu of a server, database, folder, key, index, routine, a column of a view and objects in *System Databases*.
10. If you have a MySQL 5.7 or MariaDB < 10.5 server: *Rename* is not on columns there, but is on tables.
11. Theme (Dark, Light, Blue): the edit box is readable.

## US-0903 Create database

**Status:** Done (accepted 2026-11-02)

**Acceptance criteria**

- [x] Context menu "Create Database" on the Databases folder: name, character set, collation.

**Note:** a dialog, as in SSMS (*New Database...* opens a dialog there). Decision D-15. The menu item is called *New Database...*, as in SSMS and in line with the *New ...* items of US-0904.

**Tasks**

- [x] T-0903-01 `CharacterSetCatalog` and its MySQL source, `NewDatabaseViewModel` (name check, collations per character set, SQL), `DatabaseCreator` + tests
- [x] T-0903-02 `NewDatabaseDialog` and the command on the Databases folder

**Implementation notes**

- The dialog reads the character sets and collations from `INFORMATION_SCHEMA` (works on MySQL and MariaDB), the server defaults (`@@character_set_server`, `@@collation_server`) and the existing database names, in one round trip. With a password that is not saved, the password prompt comes first.
- Character set and collation start at the server defaults. Choosing another character set shows only its collations and selects its default collation.
- The name is checked while you type: empty disables *Create*; an existing name (without case, as on Windows), more than 64 characters or a trailing space disable it with a message under the name. Leading spaces are allowed.
- Below the fields the exact SQL is shown, as in the Delete dialog: `` CREATE DATABASE `sales` CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci; ``. Enter creates (Create is the default button; nothing is lost by creating).
- After success the Databases folder is refreshed and, when it was collapsed, expanded; the new database is selected. A folder collapsed in the tree keeps its old list, so it is always refreshed first (found in the first test round: a collapsed folder opened with the old list). On Windows the server stores the name in lower case (`lower_case_table_names=1`); the node is found without case.
- A server error (for example no CREATE privilege) is shown in a message box. The Output window logs the statement (Info).

**Manual test**

1. Right-click *Databases* of a connected server: *New Database...* is the first item. It is not on a database, a folder in a database, the server or *System Databases*.
2. Open the dialog. Expected: focus in the name box; character set and collation show the server defaults (MySQL 8: *utf8mb4* / *utf8mb4_0900_ai_ci*); *Create* is disabled; the SQL box is empty.
3. Type `oe_create_test`: the SQL shows `` CREATE DATABASE `oe_create_test` CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci; `` and *Create* is enabled.
4. Choose character set *latin1*: the collation list shows only latin1 collations and *latin1_swedish_ci* is selected; the SQL follows.
5. Type the name of an existing database in other case (for example `SAKILA`): message *A database with this name already exists.*, *Create* disabled. Try a trailing space and 65 characters too.
6. Create `oe_create_test`: the database appears in the tree and is selected. Expand it: the folders are there.
7. Collapse *Databases*, create another database: the folder expands and selects the new database.
8. Create a database with capitals, for example `OE_Case`: on Windows it appears as *oe_case* and is selected.
9. Cancel and Escape close the dialog without creating anything.
10. A user without CREATE privilege (if available): the server error appears in a message box.
11. Theme (Dark, Light, Blue): the dialog is readable. Delete the test databases afterwards with *Delete* (US-0901).

## US-0904 New object from template

**Status:** Done (accepted 2026-11-02)

As a developer, I want to start a new object from the tree with a script I complete and run myself, so I do not have to remember the syntax. This is not a designer: the explorer only opens a query document with a template (decision D-15).

**Acceptance criteria**

- [x] Context menu "New ..." on the folders: Tables (New Table), Views (New View), Stored Procedures (New Procedure), Functions (New Function), Events (New Event), and under a table: Columns (New Column), Triggers (New Trigger), Indexes (New Index).
- [x] The command opens a new query document in the MySQL Query Editor, linked to the server and database of the folder.
- [x] The template has the database (and for a column, trigger or index the table) filled in, and placeholder names to replace.
- [x] Procedures, functions, triggers and events use `DELIMITER $$`, like View Code.
- [x] Not on system databases. After running the script, F5 on the folder shows the new object.

**Templates**

| Folder | Statement |
|---|---|
| Tables | `CREATE TABLE` with an `id` AUTO_INCREMENT primary key |
| Views | `CREATE VIEW ... AS SELECT` |
| Stored Procedures | `CREATE PROCEDURE` with an IN parameter |
| Functions | `CREATE FUNCTION ... RETURNS ... DETERMINISTIC` |
| Events | `CREATE EVENT ... ON SCHEDULE EVERY 1 DAY` |
| Columns | `ALTER TABLE <table> ADD COLUMN` |
| Triggers | `CREATE TRIGGER ... BEFORE INSERT ON <table>` |
| Indexes | `CREATE INDEX ... ON <table>` |

**Tasks**

- [x] T-0904-01 Template generator per object kind (`NewObjectTemplates`, `FolderNodeViewModel.NewObjectKind`) + tests
- [x] T-0904-02 Command on the folders (one command, the text follows the folder), open as query document

**Implementation notes**

- The menu item is the first item on the folder: *New Table...*, *New View...*, *New Stored Procedure...*, *New Function...*, *New Event...*, and under a table *New Column...*, *New Trigger...*, *New Index...*. Not on the folders of a view, not in system databases.
- The document opens in the MySQL Query Editor, linked to the server and the database of the folder, named after the example object (`shop.new_table.sql`, `shop.orders.new_column.sql`). A second *New Table...* while the first is still open gets `shop.new_table (2).sql`.
- The first lines say what the template is for and what to do: replace the example names, run with Ctrl+Shift+E, refresh the folder with F5. The event template also says the event scheduler must be on.
- Names follow the quoting setting for .sql files (Tools > Options, US-0504), like Script As.
- Every template is one statement for the query editor (checked in the tests with the script splitter). Routines, triggers and events are between `DELIMITER $$` and `DELIMITER ;`. The event and trigger bodies only contain an example as a comment; an empty `BEGIN ... END` is valid in MySQL.
- No automatic refresh after running the script: the query editor does not know which folder it came from. F5 on the folder shows the new object.

**Manual test**

1. Right-click *Tables* of a user database: *New Table...* is the first item. A document *shop.new_table.sql* opens in the MySQL Query Editor; the connection bar shows the server and database.
2. Run it unchanged (Ctrl+Shift+E): it succeeds. F5 on *Tables*: *new_table* is there with columns id, name and created_at.
3. *New Table...* again while the first document is open: a second document *(2)* opens.
4. Under *new_table*: *New Column...* on Columns, *New Index...* on Indexes, *New Trigger...* on Triggers. Run each (for the index first replace `column_name` by `name`): after F5 the column, index and trigger are there.
5. *New Stored Procedure...*, *New Function...* and *New Event...*: each runs unchanged and appears after F5. Test the function with `SELECT new_function(21);` (42).
6. *New View...*: replace `table_name` by `new_table` and run; the view appears after F5.
7. The menu item is not on: Keys, Constraints, Parameters, the Columns folder of a view, a table, a database, the Databases folder and folders in *System Databases*.
8. Set the quoting setting to *Always* (Tools > Options): a new template quotes every name with backticks.
9. Theme: nothing special, the document is a normal query editor. Delete the test objects afterwards with *Delete* (US-0901).
