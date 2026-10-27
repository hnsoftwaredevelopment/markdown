# E03 Object tree

Show the structure of each server in a tree, comparable to SQL Server Object Explorer.

Target tree:

```
Server (host:port, MySQL 8.4.x)
  Databases
    System Databases            (mysql, information_schema, performance_schema, sys)
    <database>
      Tables
        <table>
          Columns               name (type, null/not null, PK/FK)
          Keys                  primary key, foreign keys, unique keys
          Constraints           check constraints
          Indexes
          Triggers
      Views
        <view>
          Columns
      Stored Procedures
        <procedure>
          Parameters
      Functions
        <function>
          Parameters
      Events
  Security                      (only when permitted, see E10)
```

## US-0301 Databases and system databases

**Status:** Done (accepted 2026-10-27, built and tested together with US-0204)

As a developer, I want to see all databases on a server, with system databases grouped separately.

**Acceptance criteria**

- [x] Expanding a server shows folder "Databases"; below it "System Databases" and the user databases, sorted by name.
- [x] Children load only on expand (lazy loading) and off the UI thread.
- [x] A loading placeholder "Loading..." is shown while querying.
- [x] Errors show as a red child node with the message. *(error icon; message in the node and its tooltip)*
- [x] When a connection has no password (not saved, or not decryptable), a password prompt appears on first expand; Cancel leaves the node collapsed. *(moved from US-0202)*

**Tasks**

- [x] T-0301-01 Tree node view model base (lazy children, loading, error state)
- [x] T-0301-02 `IMetadataProvider` + database query in Core + tests
- [x] T-0301-03 Server and database nodes in the tree
- [ ] T-0301-04 Integration test against MySQL 8 container: **not done.** It needs Docker on the build machine and in GitHub Actions. Proposal: a separate technical story once more queries exist (tables, columns), so one test setup covers them all.
- [x] T-0301-05 Password prompt dialog (moved from T-0202-03)

**Implementation notes**

- `TreeNodeViewModel` (Core) is the base of every node: a node that can have children starts with a hidden "Loading..." placeholder, so the tree shows an expand arrow. The first expand loads the children; the placeholder is visible meanwhile. A failed load shows an error node; collapsing and expanding again retries.
- Queries run in `MySqlMetadataProvider` with `ConfigureAwait(false)`, so the network work never blocks the UI thread. Every metadata call opens and closes its own pooled connection (ADR-003). Databases come from `INFORMATION_SCHEMA.SCHEMATA`, so the tree only shows what the account may see.
- System databases are `mysql`, `information_schema`, `performance_schema` and `sys` (any case). The "System Databases" folder is always first, then the user databases, both sorted case-insensitive.
- Password prompt: shows the connection name and user name, a password field and "Save password" (preset from the connection). With "Save password" checked the password is stored encrypted directly (US-0202). An account without a password can be used by leaving the field empty and clicking *Connect*.
- When the server answers "Access denied", the password is forgotten for this session, so the next expand asks for it again (also for a saved password that is no longer valid).
- The tree now uses the implicit item style for every level, with expand and selection state bound to the view models.
- With *Debug logging* on, every metadata query and its duration and row count appear in the Output pane.
- 20 new unit tests (138 in total). The `AccessDenied` handling is not unit tested, because MySqlConnector does not allow creating that exception in a test; it is part of the manual test.

**Manual test**

You need a reachable MySQL 8.x server. Turn on *Debug logging* to see the queries.

1. Rebuild and press F5. Open the explorer. Expected: servers with a dimmed server icon (not connected). Hover a server: tooltip with server:port, user, state "Not connected", version "-".
2. Expand a server with a saved password. Expected: for a moment the sync icon and "Loading...", then the normal server icon and one child "Databases". Tooltip: state "Connected" and the server version. Output pane: "Connected to ... Server version ...".
3. Expand "Databases". Expected: "System Databases" first, then your databases alphabetically. Output pane (Debug): the `INFORMATION_SCHEMA.SCHEMATA` query with row count.
4. Expand "System Databases". Expected: `information_schema`, `mysql`, `performance_schema`, `sys` with database icons.
5. Right-click the server: *Refresh* and *Disconnect* are now enabled. Choose *Refresh*. Expected: the server reloads and is collapsed to its "Databases" folder.
6. Choose *Disconnect*. Expected: the node collapses, the icon is dimmed again, tooltip "Not connected". Expanding connects again.
7. Use *Properties* to set a wrong password, OK, expand. Expected: error icon on the server, a child node with the MySQL error ("Access denied ..."), tooltip with the last error. Collapse and expand again: the password prompt appears. Enter the correct password, check "Save password", *Connect*. Expected: connected; after a restart of the Experimental Instance the server connects without a prompt.
8. Add a server with "Save password" unchecked, restart the Experimental Instance and expand it. Expected: the password prompt. *Cancel*: the node stays collapsed, no error. Expand again and enter the password: connected.
9. Add a server with an unreachable host and timeout 3 seconds, expand it. Expected: after about 3 seconds an error node, error icon and the error in the tooltip; Visual Studio stays responsive meanwhile.
10. Switch between Dark and Light theme. Expected: icons and the error node stay readable.

**Test result**

2026-10-27, Herbert: accepted. Password prompt, save / not save, System Databases first and collapsed, Access denied on a wrong password: all as described. Finding: *Refresh* collapses the server to its "Databases" folder; Herbert expects Refresh to keep the expanded folders and only update their content (for example a new or deleted database). Moved to US-0307.
## US-0302 Tables and columns

**Status:** Done (accepted 2026-10-27)

As a developer, I want to see the tables of a database and their columns with data type and nullability.

**Acceptance criteria**

- [x] Column label format: `name (type, null)` or `name (PK, type, not null)`, same style as SSOX (for example `optname (varchar(128), null)`).
- [x] Icons differ for normal column, primary key column and foreign key column.
- [x] Columns in ordinal position order.

**Tasks**

- [x] T-0302-01 Table and column queries + label formatter + tests
- [x] T-0302-02 Table and column nodes with icons

**Implementation notes**

- A database node now expands to a "Tables" folder; a table expands to a "Columns" folder. Views, routines and events get their own folders in US-0304 to US-0306; keys, constraints, indexes and triggers below a table in US-0303.
- Tables: `INFORMATION_SCHEMA.TABLES` with `TABLE_TYPE = 'BASE TABLE'`, sorted by name. `information_schema` itself has no base tables (its tables are system views), so its "Tables" folder is empty; they appear under Views in US-0304. The table comment is shown as tooltip.
- Columns: `INFORMATION_SCHEMA.COLUMNS` in `ORDINAL_POSITION` order, with a foreign key flag from `KEY_COLUMN_USAGE`. One query per table, only when its "Columns" folder is expanded. Database and table names are passed as query parameters, never pasted into the SQL.
- Label: `name (PK, FK, type, null|not null)`. The type is the full MySQL type (`int unsigned`, `decimal(10,2)`, `varchar(128)`); ENUM and SET lists longer than 60 characters are shortened with "...". The full type will be in the Properties window (US-0401).
- Icons: primary key column = key column icon, foreign key column = foreign key icon, generated (virtual or stored) column = computed column icon, other columns = column icon. A column that is both PK and FK shows the key icon.
- With *Debug logging* on, each query appears with its parameters, duration and row count.
- 12 new unit tests (152 in total).

**Manual test**

1. Rebuild and press F5. Expand a server, "Databases", one of your databases. Expected: a folder "Tables".
2. Expand "Tables". Expected: the base tables of that database, sorted by name, with a table icon. Hover a table that has a comment: the comment as tooltip.
3. Expand a table and its "Columns" folder. Expected: the columns in the order of the table definition, for example `id (PK, int unsigned, not null)`, `name (varchar(100), null)`.
4. Check a table with a foreign key. Expected: the FK column shows `(FK, ...)` and the foreign key icon.
5. Check a table with a generated column, if you have one. Expected: the computed column icon.
6. Expand `mysql` under "System Databases" > "Tables" > `user` > "Columns". Expected: many columns, ENUM columns shown as `enum('N','Y')`.
7. With *Debug logging* on: the Output pane shows the TABLES and COLUMNS queries with `@schema` and `@table` values.

**Test result**

2026-10-27, Herbert: accepted. Expanding tables and columns works and looks good.
## US-0303 Keys, constraints, indexes and triggers

**Status:** Ready for test

As a developer, I want to see the keys, check constraints, indexes and triggers of a table.

**Acceptance criteria**

- [x] Keys: primary key, unique keys, foreign keys (with referenced table in label).
- [x] Constraints: check constraints (MySQL 8.0.16+); folder hidden on older versions.
- [x] Indexes: name, unique/non-unique, columns in order.
- [x] Triggers: name, timing and event (for example `BEFORE INSERT`).

**Tasks**

- [x] T-0303-01 Queries + models + tests
- [x] T-0303-02 Folder and child nodes

**Implementation notes**

- Folders below a table, in the same order as SQL Server Object Explorer: Columns, Keys, Constraints, Triggers, Indexes. Each folder runs its own query on first expand.
- **Keys** (`TABLE_CONSTRAINTS` + `KEY_COLUMN_USAGE`): primary key first, then unique keys, then foreign keys, each by name. Labels: `PRIMARY (order_id, line)`, `uq_number (number)`, `fk_order_customer (customer_id) → customers (id)`. A referenced table in another database gets the database name: `→ geo.countries (code)`. Composite keys list their columns in key order.
- **Constraints** (`CHECK_CONSTRAINTS`): label `chk_price ((`price` >= 0))`, with ", not enforced" for a disabled constraint (`NOT ENFORCED`). Long expressions are shortened to 60 characters; the tooltip shows the full expression. The folder only appears on MySQL 8.0.16+ and MariaDB 10.2+ (`ServerCapabilities`, read from the server version of the connection). MariaDB uses its own query, because its `CHECK_CONSTRAINTS` table has a different layout.
- **Triggers** (`TRIGGERS`): label `trg_orders_bi (BEFORE INSERT)`, ordered by timing, event and trigger order.
- **Indexes** (`STATISTICS`): PRIMARY first, then by name. Labels: `ix_name (non-unique: name(10), city)` with prefix length, `uq_email (unique: email)`, `ft_body (fulltext: body)`, `ix_func (non-unique: (expression))` for a functional index.
- Icons: key, unique key, foreign key, check constraint, trigger; PRIMARY index = clustered index icon (InnoDB stores rows in primary key order), FULLTEXT = search icon, other indexes = sort icon.
- 19 new unit tests (171 in total).

**Manual test**

1. Rebuild and press F5. Expand a server > Databases > a database > Tables > a table. Expected: folders Columns, Keys, Constraints, Triggers, Indexes (Constraints only on MySQL 8.0.16+).
2. Expand Keys on a table with a primary key and a foreign key. Expected: `PRIMARY (...)` first with a key icon, then the foreign key with `→ table (column)`.
3. Expand Indexes. Expected: `PRIMARY (unique: ...)` first with the clustered index icon, then the other indexes with their columns in order.
4. If you have a table with a CHECK constraint (for example `ALTER TABLE t ADD CONSTRAINT chk_x CHECK (x >= 0);`): Expand Constraints. Expected: `chk_x ((`x` >= 0))`; tooltip with the expression.
5. If you have a trigger: Expand Triggers. Expected: `name (BEFORE INSERT)` or similar.
6. A table without keys, constraints, triggers or indexes: the folders expand and stay empty, without an error.
7. Check `mysql` > Tables > `user` > Keys and Indexes. Expected: `PRIMARY (Host, User)`.

**Test result**

_To be filled in by Herbert._
## US-0304 Views

**Status:** Todo

**Acceptance criteria**

- [ ] Views folder per database with views and their columns.

## US-0305 Stored procedures, functions and parameters

**Status:** Todo

As a developer, I want to see procedures and functions including their parameters, so that I can drag them into code correctly.

**Acceptance criteria**

- [ ] Parameters show direction and type: `p_id (IN, int)`, `p_total (OUT, decimal(10,2))`.
- [ ] Function nodes show the return type.

**Tasks**

- T-0305-01 `ROUTINES` and `PARAMETERS` queries + tests
- T-0305-02 Routine and parameter nodes

## US-0306 Events

**Status:** Todo

**Acceptance criteria**

- [ ] Events folder per database with name, status (enabled/disabled) and schedule in tooltip.

## US-0307 Refresh

**Status:** Todo

As a developer, I want to refresh any node, so that I see changes made outside Visual Studio.

**Acceptance criteria**

- [ ] Context menu "Refresh" and F5 key on every node reload that node's children.
- [ ] Toolbar button refreshes the selected node.
- [ ] Expanded state of child nodes is kept where the objects still exist.
- [ ] Refresh does not collapse anything: expanded folders stay expanded and only their content is updated, so a database that was added or dropped elsewhere appears or disappears. *(finding from the US-0301 test, 2026-10-27; today Refresh on a server collapses it to its "Databases" folder)*

## US-0308 Toolbar and filter

**Status:** Todo

**Acceptance criteria**

- [ ] Tool window toolbar: Refresh, Add server, Collapse all.
- [ ] Filter box filters loaded tables, views and routines by name (case-insensitive).
