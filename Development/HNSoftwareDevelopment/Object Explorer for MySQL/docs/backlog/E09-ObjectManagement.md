# E09 Object management

Make small changes directly from the tree. Full visual table design is parked (see Parked).

## US-0901 Delete objects

**Status:** Ready for test

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

**Status:** Todo

**Acceptance criteria**

- [ ] Context menu "Rename" (F2) on table, view and column.
- [ ] Table: `RENAME TABLE`; column: `ALTER TABLE ... RENAME COLUMN` (MySQL 8.0+).
- [ ] Inline edit in the tree, Escape cancels.

## US-0903 Create database

**Status:** Todo

**Acceptance criteria**

- [ ] Context menu "Create Database" on the Databases folder: name, character set, collation.
