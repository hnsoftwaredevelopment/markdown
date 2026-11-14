# E04 Properties window

Show object details in the standard Visual Studio Properties window (F4), like SQL Server Object Explorer does.

## US-0401 Column properties

**Status:** Done (accepted 2026-10-28)

As a developer, I want to select a column and see its properties in the Properties window.

**Acceptance criteria**

- [x] Selecting a node updates the Properties window via `ITrackSelection`.
- [x] Categories and properties for a column:
  - General: Nullable, Primary Key, Foreign Key, Default, Auto Increment, Is Generated, Generation Expression
  - Data Type: Data Type, Length, Precision, Scale, Unsigned, Character Set, Collation
  - Description: Name, Parent, Parent Type, Database, Comment, Ordinal Position
  - Connection: Connection Name, Server, Port, User
- [x] All properties are read-only.
- [x] Category and property names are localized (resource file; English only for now, ADR-010).

**Tasks**

- [x] T-0401-01 Property object base class with localized `CategoryAttribute`/`DisplayNameAttribute`
- [x] T-0401-02 `ITrackSelection` integration in tool window
- [x] T-0401-03 Column property object + tests on mapping

**Implementation notes**

- The `COLUMNS` query now also reads `DATA_TYPE`, `COLUMN_DEFAULT`, `CHARACTER_MAXIMUM_LENGTH`, `NUMERIC_PRECISION`, `NUMERIC_SCALE`, `CHARACTER_SET_NAME`, `COLLATION_NAME`, `COLUMN_COMMENT`, `ORDINAL_POSITION` and `GENERATION_EXPRESSION`. No extra query per selection: the values come with the column list.
- The values are a snapshot of the last load; Refresh (F5) on the Columns folder updates them.
- Changes to the original criteria: *Foreign Key* and *Parent Type* (Table or View) added. The Connection category shows *Connection Name*, *Server* (host), *Port* and *User*; the database is already under Description.
- The header of the Properties window shows the column name and the type "Column".
- *Data Type* shows the full MySQL type, for example `decimal(10,2) unsigned` or `enum('G','PG')`.
- *Default* shows the value as MySQL reports it; empty means no default (or `DEFAULT NULL`).
- The Visual Studio Properties window sorts the categories and the properties within a category alphabetically.
- The node context menu now has *Properties Window* (F4) below *Refresh*.
- Property object classes and texts are in Core (`ObjectProperties/`, `Resources/PropertyTexts.resx`), so US-0402 only adds a class per object type. A unit test checks that every category and property name has a resource.
- Other nodes show an empty Properties window until US-0402.

**Manual test**

Use sakila.

1. Open the Properties window (*View > Properties Window* or F4) and dock it next to the explorer.
2. Expand *sakila > Tables > film > Columns* and select `film_id`. Expected: header `film_id  Column`; General: Primary Key True, Auto Increment True, Nullable False; Data Type: `smallint unsigned`, Unsigned True, Precision 5, Scale 0; Description: Parent `film`, Parent Type Table, Database `sakila`, Ordinal Position 1; Connection: your connection name, host, port and user.
3. Select `title`. Expected: Data Type `varchar(128)`, Length 128, Character Set and Collation filled (for example `utf8mb4` / `utf8mb4_0900_ai_ci`), Precision and Scale empty.
4. Select `rental_rate`. Expected: `decimal(4,2)`, Precision 4, Scale 2, Default `4.99`.
5. Select `rating`. Expected: Data Type `enum('G','PG','PG-13','R','NC-17')`, Default `G`.
6. Select `language_id`. Expected: Foreign Key True.
7. Expand *sakila > Views > customer_list > Columns*, select `name`. Expected: Parent `customer_list`, Parent Type View.
8. Try to edit a value in the Properties window. Expected: all values are read-only (grey).
9. Select a folder or a table. Expected: the Properties window is empty (US-0402 follows).
10. Right-click a column. Expected: the menu shows *Refresh* and *Properties Window*; *Properties Window* opens or activates the Properties window.
11. With the focus in the explorer, select a column and press F4. Expected: the Properties window opens with the column properties.

## US-0402 Properties for other objects

**Status:** Done (accepted 2026-10-28)

As a developer, I want to see the properties of every object in the Properties window, not only of columns.

**Acceptance criteria**

- [x] Server: version, host, port, user, SSL in use, character set, time zone.
- [x] Database: default character set, collation, number of tables (when loaded).
- [x] Table: engine, row format, estimated rows, data length, index length, auto increment value, created, updated, collation, comment.
- [x] View: is updatable, security type, definer, check option.
- [x] Index: unique, type (BTREE/HASH/FULLTEXT/SPATIAL), visible, columns.
- [x] Key/constraint: type, columns, referenced table/columns, on update, on delete.
- [x] Procedure/function: definer, security type, deterministic, SQL data access, created, modified, comment.
- [x] Trigger: timing, event, table, definer, created.
- [x] Event: status, schedule, starts, ends, on completion.

**Tasks**

- [x] T-0402-01 Extend the metadata queries (tables, views, keys, indexes, triggers, routines, events) and read server settings on connect
- [x] T-0402-02 Property object per object type + tests
- [x] T-0402-03 Properties window follows a selected server that connects or disconnects

**Implementation notes**

- No extra query when you select a node: the values come with the list that fills the folder, and the server values are read once when connecting (`@@character_set_server`, `@@collation_server`, `@@time_zone`, `@@system_time_zone`, `SHOW SESSION STATUS LIKE 'Ssl_cipher'`).
- Every object shows the Connection category (Connection Name, Server, Port, User). Server, table, view, index, key and routine objects also show Name and Database under Description; objects of a table also show Table.
- Additions beyond the criteria: Server: State, Authenticated As, SSL Mode (configured), SSL Cipher, Default Database. Database: System Database. Index: Primary Key, Comment. Check constraint: Expression, Enforced. Trigger: Action Order. Routine: Returns. Event: Definer, Created, Modified, Last Executed, Comment. Parameters got properties too: Mode, Data Type, Ordinal Position, Routine.
- The header shows the object type: MySQL Server, Database, Table, View, Index, Primary Key, Unique Key, Foreign Key, Check Constraint, Trigger, Stored Procedure, Function, Parameter, Event.
- Sizes are shown as `16 KB`, `1.5 MB` (1024 per step).
- Referenced Table gets a schema prefix only when the table is in another database.
- Index visibility: MySQL reads `IS_VISIBLE`, MariaDB reads `IGNORED` (inverted). The query is chosen from the server version.
- Database *Tables* stays empty until the Tables folder was expanded. After expanding it, select the database again to see the number.
- *Estimated Rows*, *Data Size*, *Index Size* and *Last Data Change* come from `INFORMATION_SCHEMA.TABLES`. MySQL 8 caches these values (`information_schema_stats_expiry`, default 24 hours) and InnoDB estimates the row count, so they can differ from `SELECT COUNT(*)`. Run `ANALYZE TABLE` to update them.
- System views (`information_schema`) have no view definition; Is Updatable, Security Type, Definer and Check Option stay empty.
- A server that connects or disconnects while it is selected updates the Properties window directly.

**Manual test**

Use sakila. Keep the Properties window open next to the explorer.

1. Select the server while it is not connected. Expected: header `<name>  MySQL Server`; State Not connected; Version empty; Server, Port, User and SSL Mode filled.
2. Expand the server, keep it selected. Expected without reselecting: State Connected; Version, Character Set, Collation, Time Zone and Authenticated As filled; SSL In Use True with an SSL Cipher when the connection uses TLS (default for MySQL 8 with SSL Mode Preferred).
3. Select *sakila*. Expected: Character Set and Collation; Tables empty. Expand *Tables*, select *sakila* again. Expected: Tables 16 (or 17 with `oefm_check_test`).
4. Select table *film*. Expected: Engine InnoDB, Row Format Dynamic, Next Auto Increment 1001, Estimated Rows about 1000, Data Size and Index Size filled, Created filled.
5. Select view *actor_info*. Expected: Security Type INVOKER, Is Updatable False, Definer filled. Select *information_schema > Views > TABLES*. Expected: those four values empty.
6. Expand *film > Keys*, select `fk_film_language`. Expected: header Foreign Key; Columns `language_id`; Referenced Table `language`; Referenced Columns `language_id`; On Update CASCADE; On Delete RESTRICT. Select `PRIMARY`: Key Type Primary Key, On Update and On Delete empty.
7. Expand *film > Indexes*, select `idx_title`. Expected: Unique False, Index Type BTREE, Visible True, Columns `title`. Expand *film_text > Indexes*, select `idx_title_description`: Index Type FULLTEXT.
8. Expand *film > Triggers*, select `ins_film`. Expected: Timing AFTER, Event INSERT, Table `film`, Definer and Created filled.
9. Select procedure *film_in_stock*. Expected: header Stored Procedure; SQL Data Access READS SQL DATA; Returns empty. Select function *get_customer_balance*: header Function; Returns `decimal(5,2)`; Deterministic True.
10. Expand *film_in_stock > Parameters*, select `p_film_count`. Expected: Mode OUT, Data Type `int`, Ordinal Position 3, Routine `film_in_stock`.
11. Create an event: `CREATE EVENT sakila.oefm_props ON SCHEDULE EVERY 1 HOUR ON COMPLETION PRESERVE COMMENT 'Props test' DO SELECT 1;` Refresh *Events*, select it. Expected: Status ENABLED, Schedule `EVERY 1 HOUR STARTS '...'`, Starts filled, On Completion PRESERVE, Comment `Props test`. Clean up: `DROP EVENT sakila.oefm_props;`
12. If `sakila.oefm_check_test` still exists: select its check constraint. Expected: Expression and Enforced.
13. Disconnect the server while it is selected. Expected: State Not connected, Version and SSL values empty.

