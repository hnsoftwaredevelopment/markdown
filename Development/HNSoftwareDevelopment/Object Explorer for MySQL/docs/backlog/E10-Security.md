# E10 Security

Show users and privileges, but only when the connected account is allowed to read them (ADR-006).

## US-1001 Privilege detection

**Status:** Ready for test

As a developer, I want the extension to check what my account may see, so that I do not get errors on folders I cannot open.

**Acceptance criteria**

- [x] After connect: run `SHOW GRANTS FOR CURRENT_USER()` and parse the result.
- [x] Result stored per connection: can read users (`SELECT` on `mysql.*` ~~or global `CREATE USER`~~, see D-16), can manage users.
- [x] Parsing covers global, database-level and role-based grants (unit tested with `SHOW GRANTS` outputs in the formats of MySQL 5.7, 8.0, 8.4 and MariaDB 10.11).
- [x] When the check fails or is inconclusive, fall back to a test query `SELECT 1 FROM mysql.user LIMIT 0`.

**Tasks**

- [x] T-1001-01 `GrantParser` (`GrantEntry`, `GrantLevel`) + tests
- [x] T-1001-02 `PrivilegeChecker` on connect, `AccountPrivileges` on the server node, two rows in the Properties window

**Implementation notes**

- The parser reads GRANT and REVOKE lines: global (`*.*`), database (`` `db`.* ``), table (also with column lists such as `` SELECT (`id`, `name`) ``), routine (`ON PROCEDURE`/`ON FUNCTION`), proxy and role grants (`` GRANT `r1`@`%`,`r2`@`%` TO ... ``, MariaDB `` GRANT `role` TO ... ``). Names quoted with backticks, single or double quotes; lists with or without spaces (MySQL 8 writes its dynamic privileges without spaces). `ALL PRIVILEGES` counts as every privilege. MariaDB authentication parts (`IDENTIFIED VIA ... USING '...'`) are skipped; grant lines are never written to the log, so password hashes in them do not leak.
- **Can read users** (decision D-16): SELECT (or ALL) on `*.*`, on `mysql.*` or on the table `mysql.user`. A partial revoke `REVOKE SELECT ON mysql.* FROM ...` (MySQL 8 with `partial_revokes`) cancels the global SELECT. The story text also named global CREATE USER, but that privilege does not allow `SELECT` on `mysql.user`, so the Security folder of US-1002 would fail; CREATE USER only counts for managing.
- **Can manage users**: CREATE USER (or ALL) on `*.*`.
- **Roles**: the grants of the roles of the account are read too (MySQL: `SHOW GRANTS FOR CURRENT_USER() USING ...`; MariaDB: `SHOW GRANTS FOR role` per role), so a role with CREATE USER counts for managing (also when the role is not active; a user action of US-1003 then gets the server error). Role grants do not count for reading: when the account's own grants do not allow reading users, the test query `SELECT 1 FROM mysql.user LIMIT 0` decides; that query runs in a new session and therefore only sees the roles that are active by default, which is what the Security folder will use. MySQL roles are asked with host `%`; a role with another host is not expanded (logged at Debug) and only the test query counts for it.
- The check never fails the connect: when SHOW GRANTS fails, the test query decides; when that fails too, nothing is allowed.
- Result per connection on the server node; forgotten on Disconnect. The Properties window of a server shows *Can Read Users* and *Can Manage Users* (empty when not connected). The Output window logs one Info line per connect: `Account app@% on 'Local': read users no, manage users no (decided by Grants).`, with the details at Debug level.
- Nothing visible in the tree changes yet; US-1002 uses the result for the Security folder.

**Manual test**

Create test accounts as root (and drop them afterwards):

```sql
CREATE USER 'oe_plain'@'%' IDENTIFIED BY 'Test123!';
GRANT SELECT ON sakila.* TO 'oe_plain'@'%';
CREATE USER 'oe_reader'@'%' IDENTIFIED BY 'Test123!';
GRANT SELECT ON mysql.user TO 'oe_reader'@'%';
CREATE USER 'oe_admin'@'%' IDENTIFIED BY 'Test123!';
GRANT CREATE USER ON *.* TO 'oe_admin'@'%';
CREATE ROLE 'oe_role';
GRANT SELECT ON mysql.* TO 'oe_role';
CREATE USER 'oe_roleuser'@'%' IDENTIFIED BY 'Test123!';
GRANT 'oe_role' TO 'oe_roleuser'@'%';
SET DEFAULT ROLE 'oe_role' TO 'oe_roleuser'@'%';
```

1. Connect with root, select the server, open the Properties window (F4): *Can Read Users* and *Can Manage Users* are True. The Output window shows the Info line with `decided by Grants`.
2. Add a server for each test account and connect:
   - *oe_plain*: False / False.
   - *oe_reader*: True / False.
   - *oe_admin*: False / True.
   - *oe_roleuser*: True / False, `decided by TestQuery` (the role gives the access).
3. `SET DEFAULT ROLE NONE TO 'oe_roleuser'@'%';`, disconnect and connect again: False / False (the role is no longer active in a new session).
4. Disconnect a server: both properties are empty.
5. Connect works as before on every server, also when SHOW GRANTS is not allowed; no extra error messages.
6. Set the log level to Debug: the Output window shows the number of grants, roles and lines not understood. Please send me the *lines not understood* count when it is not 0, with the SHOW GRANTS output of that account (without password hashes), so I can add it to the tests.

Clean up: `DROP USER 'oe_plain'@'%', 'oe_reader'@'%', 'oe_admin'@'%', 'oe_roleuser'@'%'; DROP ROLE 'oe_role';`

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
