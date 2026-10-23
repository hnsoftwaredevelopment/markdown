# E04 Properties window

Show object details in the standard Visual Studio Properties window (F4), like SQL Server Object Explorer does.

## US-0401 Column properties

**Status:** Todo

As a developer, I want to select a column and see its properties in the Properties window.

**Acceptance criteria**

- [ ] Selecting a node updates the Properties window via `ITrackSelection`.
- [ ] Categories and properties for a column:
  - General: Nullable, Primary Key, Default, Auto Increment, Is Generated, Generation Expression
  - Data Type: Data Type, Length, Precision, Scale, Unsigned, Character Set, Collation
  - Description: Name, Parent, Database, Comment, Ordinal Position
  - Connection: Server, Port, User, Database
- [ ] All properties are read-only.
- [ ] Category and property names are localized.

**Tasks**

- T-0401-01 Property object base class with localized `CategoryAttribute`/`DisplayNameAttribute`
- T-0401-02 `ITrackSelection` integration in tool window
- T-0401-03 Column property object + tests on mapping

**Manual test**

1. Select a column, press F4.
2. Expected: Properties window shows the categories above with correct values.

## US-0402 Properties for other objects

**Status:** Todo

**Acceptance criteria**

- [ ] Server: version, host, port, user, SSL in use, character set, time zone.
- [ ] Database: default character set, collation, number of tables (when loaded).
- [ ] Table: engine, row format, estimated rows, data length, index length, auto increment value, created, updated, collation, comment.
- [ ] View: is updatable, security type, definer, check option.
- [ ] Index: unique, type (BTREE/HASH/FULLTEXT/SPATIAL), visible, columns.
- [ ] Key/constraint: type, columns, referenced table/columns, on update, on delete.
- [ ] Procedure/function: definer, security type, deterministic, SQL data access, created, modified, comment.
- [ ] Trigger: timing, event, table, definer, created.
- [ ] Event: status, schedule, starts, ends, on completion.
