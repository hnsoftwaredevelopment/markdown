# E06 Script and view code

Open the source of objects and generate standard SQL scripts.

## US-0601 View Code

**Status:** Todo

As a developer, I want to open the definition of a table, view, procedure, function, trigger or event.

**Acceptance criteria**

- [ ] Context menu "View Code" opens a new `.sql` document with the output of `SHOW CREATE ...`.
- [ ] Document title: `<database>.<object>.sql`.
- [ ] The document is linked to the connection (see E07), so it can be executed directly.

**Tasks**

- T-0601-01 `SHOW CREATE` per object type in Core + tests
- T-0601-02 Open temporary document via VS shell API

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
