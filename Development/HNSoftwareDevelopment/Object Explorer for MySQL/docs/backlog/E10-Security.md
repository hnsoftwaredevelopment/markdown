# E10 Security

Show users and privileges, but only when the connected account is allowed to read them (ADR-006).

## US-1001 Privilege detection

**Status:** Todo

As a developer, I want the extension to check what my account may see, so that I do not get errors on folders I cannot open.

**Acceptance criteria**

- [ ] After connect: run `SHOW GRANTS FOR CURRENT_USER()` and parse the result.
- [ ] Result stored per connection: can read users (`SELECT` on `mysql.*` or global `CREATE USER`), can manage users.
- [ ] Parsing covers global, database-level and role-based grants (unit tested with real `SHOW GRANTS` outputs from MySQL 8.0, 8.4 and MariaDB 10.11).
- [ ] When the check fails or is inconclusive, fall back to a test query `SELECT 1 FROM mysql.user LIMIT 0`.

**Tasks**

- T-1001-01 `GrantParser` + tests
- T-1001-02 Privilege check on connect

## US-1002 Security node with users and roles

**Status:** Todo

**Acceptance criteria**

- [ ] "Security" folder under the server, only visible when US-1001 says users can be read.
- [ ] Subfolders: Users (`user@host`), Roles (MySQL 8+).
- [ ] Per user: grants shown as child nodes; Properties window shows account locked, password expired, authentication plugin.
- [ ] Read-only in this story.

## US-1003 Manage users

**Status:** Todo (only when the account can manage users)

**Acceptance criteria**

- [ ] Create user, drop user, change password, grant/revoke on a database. Every action shows the SQL before it runs.
