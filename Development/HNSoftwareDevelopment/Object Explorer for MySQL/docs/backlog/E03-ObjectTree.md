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

**Status:** Todo

As a developer, I want to see all databases on a server, with system databases grouped separately.

**Acceptance criteria**

- [ ] Expanding a server shows folder "Databases"; below it "System Databases" and the user databases, sorted by name.
- [ ] Children load only on expand (lazy loading) and off the UI thread.
- [ ] A loading placeholder "Loading..." is shown while querying.
- [ ] Errors show as a red child node with the message.
- [ ] When a connection has no password (not saved, or not decryptable), a password prompt appears on first expand; Cancel leaves the node collapsed. *(moved from US-0202)*

**Tasks**

- T-0301-01 Tree node view model base (lazy children, loading, error state)
- T-0301-02 `IMetadataProvider` + database query in Core + tests
- T-0301-03 Server and database nodes in the tree
- T-0301-04 Integration test against MySQL 8 container
- T-0301-05 Password prompt dialog (moved from T-0202-03)

## US-0302 Tables and columns

**Status:** Todo

As a developer, I want to see the tables of a database and their columns with data type and nullability.

**Acceptance criteria**

- [ ] Column label format: `name (type, null)` or `name (PK, type, not null)`, same style as SSOX (for example `optname (varchar(128), null)`).
- [ ] Icons differ for normal column, primary key column and foreign key column.
- [ ] Columns in ordinal position order.

**Tasks**

- T-0302-01 Table and column queries + label formatter + tests
- T-0302-02 Table and column nodes with icons

## US-0303 Keys, constraints, indexes and triggers

**Status:** Todo

As a developer, I want to see the keys, check constraints, indexes and triggers of a table.

**Acceptance criteria**

- [ ] Keys: primary key, unique keys, foreign keys (with referenced table in label).
- [ ] Constraints: check constraints (MySQL 8.0.16+); folder hidden on older versions.
- [ ] Indexes: name, unique/non-unique, columns in order.
- [ ] Triggers: name, timing and event (for example `BEFORE INSERT`).

**Tasks**

- T-0303-01 Queries + models + tests
- T-0303-02 Folder and child nodes

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

## US-0308 Toolbar and filter

**Status:** Todo

**Acceptance criteria**

- [ ] Tool window toolbar: Refresh, Add server, Collapse all.
- [ ] Filter box filters loaded tables, views and routines by name (case-insensitive).
