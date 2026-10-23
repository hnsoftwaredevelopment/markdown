# E09 Object management

Make small changes directly from the tree. Full visual table design is parked (see Parked).

## US-0901 Delete objects

**Status:** Todo

**Acceptance criteria**

- [ ] Context menu "Delete" (Del key) on database, table, view, procedure, function, trigger, event, index and column.
- [ ] Confirmation dialog shows the exact SQL that will run.
- [ ] Deleting a database requires typing the database name.
- [ ] Tree refreshes the parent node after success.

**Tasks**

- T-0901-01 DROP statement builder per type + tests
- T-0901-02 Confirmation dialog and command

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
