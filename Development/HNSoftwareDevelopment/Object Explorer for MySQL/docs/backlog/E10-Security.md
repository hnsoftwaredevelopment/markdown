# E10 Security

Show users and privileges, but only when the connected account is allowed to read them (ADR-006).

## US-1001 Privilege detection

**Status:** Done (accepted 2026-11-02)

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

**Status:** Done (accepted 2026-11-02)

**Acceptance criteria**

- [x] "Security" folder under the server, only visible when US-1001 says users can be read.
- [x] Subfolders: Users (`user@host`), Roles (MySQL 8+).
- [x] Per user: grants shown as child nodes; Properties window shows account locked, password expired, authentication plugin.
- [x] Read-only in this story.

**Tasks**

- [x] T-1002-01 `MySqlAccountReader` (accounts, roles, grants), `GrantText`, `AccountInfo` + tests
- [x] T-1002-02 `SecurityFolder`, `AccountNodeViewModel`, `AccountProperties`, icons and texts

**Implementation notes**

- *Security* comes after *Databases*, as in SQL Server Object Explorer, and only when *Can Read Users* (US-1001) is true. It contains *Users* and, on MySQL 8.0+ and MariaDB 10.0.5+, *Roles*. Both lists are read when the folder is expanded and are sorted by user, then host. The name filter of the search box also filters users and roles.
- Accounts come from `mysql.user`. Only the columns the server has are read (they differ between MySQL 5.7, 8.x and MariaDB); a password hash is never read.
- Roles: MariaDB marks them with `is_role = 'Y'`. MySQL stores a role as a normal account; it counts as a role when it appears in `mysql.role_edges` (when the account may read that table) or when it is locked with an expired, empty password, which is how CREATE ROLE creates it. A MariaDB role is shown without host.
- Icons: user, locked user (lock), role, grant.
- Expanding a user or role runs `SHOW GRANTS FOR` the account. Each line becomes a node with the part between GRANT and TO, for example ``ALL PRIVILEGES ON `shop`.* (with grant option)``; granted roles get the role icon. The account and everything after it are left out, so a MariaDB password hash never shows. MySQL needs SELECT on the `mysql` schema for SHOW GRANTS of another account: with only SELECT on `mysql.user` the user node shows the server error as a child.
- Properties window: user name, host, authentication plugin, account locked, password expired, password last changed (MySQL) and password lifetime (empty means the server default). Values the server does not have stay empty.
- Read-only: Delete, Rename and New are not on these nodes.

**Manual test**

Reuse the test accounts of US-1001 (create them again when they were dropped).

1. Connect as root: *Security* is under *Databases*. Expand it: *Users* and *Roles*.
2. *Users*: all accounts as `user@host`, sorted; *oe_role* is not here but under *Roles* with a role icon. The MySQL system accounts (mysql.sys, mysql.session, mysql.infoschema) are locked and show the lock icon.
3. Expand *oe_plain@%*: `USAGE ON *.*` and ``SELECT ON `sakila`.*``. Expand *root@localhost*: the global privileges with *(with grant option)*. Expand *oe_roleuser@%*: the role ``` `oe_role`@`%` ``` with the role icon.
4. Expand *oe_role* under *Roles*: ``SELECT ON `mysql`.*``.
5. Select *oe_plain@%* and press F4: user name, host, plugin (*caching_sha2_password*), account locked *False*, password expired *False*, password last changed. Select *oe_role*: type *Role*, account locked *True*.
6. Connect as *oe_plain*: no *Security* folder. Connect as *oe_reader* (only SELECT on mysql.user): *Security* is there; expanding a user shows the server error (no SELECT on the mysql schema) as a child node.
7. MySQL 5.7 or MariaDB (if available): on 5.7 no *Roles* folder; on MariaDB a role shows without host.
8. Type `oe` in the search box: *Users* and *Roles* show only the oe accounts, with *(filtered)*.
9. The context menu of a user, role or grant has no Delete, Rename or New items. Refresh (F5) on *Users* reloads the list.
10. Theme (Dark, Light, Blue): the icons are readable.

## US-1003 Manage users

**Status:** Done (accepted 2026-11-02)

**Acceptance criteria**

- [x] Create user, drop user, change password, grant/revoke on a database. Every action shows the SQL before it runs.

**Tasks**

- [x] T-1003-01 `UserStatements` (CREATE/ALTER USER with the password as parameter, GRANT on a database, REVOKE from a grant line), `UserDialogViewModel`, `GrantDialogViewModel`, `UserManager`, DROP USER/ROLE in `DropTarget` + tests
- [x] T-1003-02 `UserDialog`, `GrantDialog`, `ConfirmSqlDialog`, four commands and Delete on accounts

**Implementation notes**

- Everything is only shown when *Can Manage Users* (US-1001) is true for the connection (decision D-17).
- **New User...** (first item on *Users*): user name, host (default `%`), password and confirmation. The SQL below the fields shows `` CREATE USER `app`@`%` IDENTIFIED BY '********'; ``. The password goes to the server as a parameter, so it is never in a SQL text, the Output window or a message. The dialog says when the account exists (user name exact, host without case) or the passwords differ. After *Create* the Users folder is refreshed and the new user is selected.
- **Change Password...** (on a user, not a role): password and confirmation, `` ALTER USER ... IDENTIFIED BY '********'; ``.
- **Grant on Database...** (on a user or role): database, *All privileges* or a choice of 18 database privileges, *With grant option*. The SQL updates while you choose: `` GRANT SELECT, INSERT ON `shop`.* TO `app`@`%`; ``. Afterwards the account is refreshed and expanded, so the new grant shows.
- **Revoke...** (on a grant node): the REVOKE is built from the grant line, so it also works for table, column, routine and role grants: `` REVOKE SELECT ON `shop`.* FROM `app`@`%`; ``. A grant with *with grant option* also revokes the grant option. Not on `USAGE ON *.*` (nothing to revoke), proxy grants and partial revokes. The dialog has Cancel as default button, like Delete.
- **Delete** (Del) on a user or role: the Delete dialog of US-0901 with `` DROP USER `app`@`%`; `` or `` DROP ROLE ...; ``. Not on the own account (the connection would lock itself out) and not on the MySQL system accounts `mysql.sys`, `mysql.session` and `mysql.infoschema`.
- Server errors (no GRANT OPTION, weak password with validate_password, ...) are shown in a message box; the Output window logs every statement with the password masked.
- Not in this story: New Role, granting roles to users, global and table-level grants, authentication plugins other than the server default. Those can be done with a query.

**Manual test**

Connect as root (*Can Manage Users* True).

1. Right-click *Users*: *New User...* is the first item. Type `oe_new`, keep host `%`, type a password twice. The SQL shows `'********'`, never the password. Make the confirmation different: *The passwords are not the same.*, *Create* disabled. Type `root` with host `localhost`: *An account with this user name and host already exists.*
2. Create `oe_new@%`: it appears in *Users* and is selected. The Output window shows the statement with `'********'`. Connect a new server entry as *oe_new* with that password: it works.
3. *Change Password...* on `oe_new@%`: change it, connect again with the new password. *Change Password...* is not on a role.
4. *Grant on Database...* on `oe_new@%`: choose *sakila*, check SELECT and INSERT: the SQL follows each click. *All privileges* disables the separate boxes. Grant SELECT, INSERT: the user expands and shows ``SELECT, INSERT ON `sakila`.*``.
5. Grant on a role (*oe_role* of US-1001): works the same.
6. Select the grant ``SELECT, INSERT ON `sakila`.*`` and choose *Revoke...*: the dialog shows the REVOKE; Enter cancels. *Revoke*: the grant is gone. *Revoke...* is not on `USAGE ON *.*`.
7. Grant with *With grant option*, then revoke it: the REVOKE contains `, GRANT OPTION`.
8. Delete (Del) on `oe_new@%`: the Delete dialog with `` DROP USER `oe_new`@`%`; ``; after *Delete* the user is gone. Delete is not on `root@localhost` (the own account) and not on `mysql.sys@localhost`.
9. Connect as *oe_reader* (can read, cannot manage): *Security* is there, but none of New User, Change Password, Grant, Revoke and Delete.
10. With `validate_password` active (if installed): a weak password gives the server error in a message box.
11. Theme (Dark, Light, Blue): the three dialogs are readable.

Clean up: drop the test accounts of US-1001 with *Delete*.

## US-1004 New role

**Status:** Done (accepted 2026-11-02)

As a developer, I want to create a role from the tree, so that I can give the same privileges to several users.

**Acceptance criteria**

- [x] Context menu *New Role...* on the Roles folder: a dialog with the name (MySQL: host, default `%`) and the SQL ``CREATE ROLE `...`;``.
- [x] After creating, the Roles folder is refreshed and the role is selected. Privileges are given with *Grant on Database...* (US-1003); *Delete* drops it.

**Tasks**

- [x] T-1004-01 `UserStatements.CreateRole`, `RoleDialogViewModel`, `UserManager.CreateRoleAsync` + tests
- [x] T-1004-02 `RoleDialog` and the command on the Roles folder

**Implementation notes**

- *New Role...* is the first item on *Roles*, only with *Can Manage Users*. The Roles folder only exists on MySQL 8.0+ and MariaDB 10.0.5+ (US-1002).
- MySQL: name and host (default `%`); ``CREATE ROLE `app_read`@`%`;``. MySQL keeps roles and users in one list of accounts, so the dialog also says *A user or role with this name already exists.* for a user with the same name and host. For that check the dialog reads all accounts first.
- MariaDB: only the name (roles have no host there); ``CREATE ROLE `app_read`;``; only roles count for the check.
- After *Create* the Roles folder is refreshed (expanded when it was collapsed) and the new role is selected. The Output window logs the statement.
- A server error (for example no CREATE ROLE privilege) is shown in a message box.

**Manual test**

1. Connect as root. Right-click *Roles*: *New Role...* is the first item. It is not on *Users*, a role or a user.
2. Type `oe_app_read`: the SQL shows ``CREATE ROLE `oe_app_read`@`%`;``; *Create* is enabled.
3. Type `oe_role` (exists from US-1001) or `root` with host `localhost`: *A user or role with this name already exists.*, *Create* disabled.
4. Create `oe_app_read`: it appears under *Roles* with the role icon and is selected.
5. *Grant on Database...* on the new role: SELECT on *sakila*; expand the role: the grant shows.
6. *Delete* on the role: ``DROP ROLE `oe_app_read`@`%`;``; the role is gone.
7. Collapse *Roles* and create another role: the folder expands with the new role selected.
8. MariaDB (if available): no host field; ``CREATE ROLE `name`;``.
9. Connect as *oe_reader* (cannot manage users): no *New Role...*.
10. Theme (Dark, Light, Blue): the dialog is readable.

## US-1005 Grant a role to a user

**Status:** Done (accepted 2026-11-02)

As a developer, I want to give a user a role from the tree, so that the user gets the privileges of that role.

**Acceptance criteria**

- [x] Context menu *Grant Role...* on a user: a dialog with the roles of the server and a check box *Make it a default role*, on by default (decision 2026-11-02; without a default role the role is not active in a new session, see US-1001).
- [x] SQL shown before it runs: ``GRANT `role` TO `user`@`host`;`` and, with the check box, ``SET DEFAULT ROLE `role` TO ...;`` (MySQL) or ``SET DEFAULT ROLE `role` FOR ...;`` (MariaDB).
- [x] Roles the user already has are not offered. Afterwards the user is refreshed and shows the role grant; *Revoke...* (US-1003) already removes it.

**Tasks**

- [x] T-1005-01 `GrantRoleDialogViewModel` (statements, available roles), `IAccountReader.GetDefaultRolesAsync`, `UserManager.ChangeGrantsAsync` with several statements + tests
- [x] T-1005-02 `GrantRoleDialog` and the command on a user

**Implementation notes**

- *Grant Role...* is on a user (not on a role), only with *Can Manage Users* and on servers with roles (MySQL 8.0+, MariaDB 10.0.5+). It is below *Grant on Database...*.
- The dialog reads the roles of the server and the grants of the user; roles the user already has are left out (compared by name). When none are left: the message *... already has every role of this server.*
- **MySQL**: `SET DEFAULT ROLE` replaces the whole list of default roles of a user. So the dialog first reads the current default roles from `mysql.default_roles` and keeps them in the statement: ``SET DEFAULT ROLE `oe_role`@`%`, `oe_app_read`@`%` TO `oe_new`@`%`;``. When that table cannot be read, the check box starts off and a note says a default role set here replaces the current ones.
- **MariaDB**: a user has one default role; ``SET DEFAULT ROLE `role` FOR `user`@`host`;``.
- The SQL box shows both statements, one per line. They run in that order; when the GRANT fails, the SET DEFAULT ROLE does not run. Afterwards the user is refreshed and expanded and shows the role grant with the role icon.
- Taking a role away: *Revoke...* on the role grant (US-1003). A revoked role is also removed from the default roles by the server.

**Manual test**

Use *oe_new* (New User, US-1003) and the roles *oe_role* (US-1001) and *oe_app_read* (New Role, US-1004).

1. Right-click *oe_new@%*: *Grant Role...* is below *Grant on Database...*. It is not on a role, *Users* or *Roles*.
2. *Grant Role...*: the list shows the roles; *Make it a default role* is on; the SQL shows the GRANT and ``SET DEFAULT ROLE `oe_role`@`%` TO `oe_new`@`%`;``. Clear the check box: only the GRANT remains.
3. Grant *oe_role* with the check box on: *oe_new@%* expands and shows ``` `oe_role`@`%` ``` with the role icon.
4. *Grant Role...* again: *oe_role* is not offered. Grant *oe_app_read* as default role: the SET DEFAULT ROLE contains both roles.
5. Check the default roles: ``SELECT * FROM mysql.default_roles WHERE USER = 'oe_new';`` shows both. Connect as *oe_new* and run ``SELECT CURRENT_ROLE();``: both roles are active.
6. When *oe_new* has every role: the message *oe_new@% already has every role of this server.*
7. *Revoke...* on the role grant ``` `oe_role`@`%` ```: the REVOKE runs, the role is gone from the user.
8. MariaDB (if available): ``SET DEFAULT ROLE `role` FOR `user`@`host`;``.
9. Connect as *oe_reader* (cannot manage users): no *Grant Role...*.
10. Theme (Dark, Light, Blue): the dialog is readable.

Clean up: drop *oe_new*, *oe_app_read* and the US-1001 accounts with *Delete*.
