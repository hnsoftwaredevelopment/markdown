# E02 Connection management

Add, edit, remove and connect to one or more MySQL servers.

## US-0201 Add a server connection

**Status:** Ready for test

As a developer, I want to add a MySQL server with host, port, user and password, so that it appears in the explorer.

**Acceptance criteria**

- [x] Toolbar button "Add MySQL Server" opens a dialog.
- [x] Fields: display name (optional), host, port (default 3306), user, password, "save password" checkbox, default database (optional).
- [x] Advanced: SSL mode (None, Preferred, Required, VerifyCA, VerifyFull), connection timeout, allow public key retrieval.
- [x] Button "Test connection" shows server version on success or the error message on failure. *(logic unit tested; dialog is a manual test)*
- [x] After OK the server appears as a node in the tree, with display name or `host:port (user)`.

**Tasks**

- [x] T-0201-01 `ConnectionDefinition` model and connection string builder in Core + tests
- [x] T-0201-02 Connection dialog (WPF, themed)
- [x] T-0201-03 Test-connection logic (async, cancellable) + `ConnectionEditorViewModel` and `ExplorerViewModel` in Core + tests
- [x] T-0201-04 Toolbar command in tool window (VSCT, ADR-011)

**Implementation notes**

- `MySqlConnector` 2.6.2 is now referenced by Core. Connection strings set the application name "Object Explorer for MySQL"; test connections do not use pooling.
- The dialog uses `DialogWindow` with Visual Studio's themed dialog styles, so it follows the Light, Dark and Blue themes. Validation messages and the test result appear below the fields with a status icon.
- A server version below MySQL 8.0 or MariaDB 10.6 still connects, but the result shows a warning (ADR-008).
- Errors from the driver are masked before they are shown or logged. Every test is logged in the Output pane; the connection string only at Debug level, with the password masked.
- Closing the dialog during a test cancels the test.
- **Not in this story:** connections are kept in memory only and are gone after a restart; "Save password" has no effect yet. Both come with US-0202. The tree shows server nodes only; expanding them comes with US-0301. Selection colors of the tree are not themed yet (US-0301).
- 34 new unit tests (88 in total), including a real connection attempt to a closed local port that must fail within 15 seconds without showing the password.

**Manual test**

You need a reachable MySQL 8.x server, for example your local server.

1. Rebuild and press F5. Open *View > Object Explorer for MySQL*. Expected: a toolbar with one button (plug icon, tooltip "Add MySQL Server") and the hint text.
2. Click the button. Expected: dialog "Add MySQL Server" in the Visual Studio theme, port 3306, timeout 15, SSL mode "Preferred", "Save password" checked, cursor in "Server host".
3. Click *Test Connection* with empty fields. Expected: error icon with "Enter a server host." and "Enter a user name."
4. Enter host, user and a wrong password, click *Test Connection*. Expected: "Connection failed: Access denied for user ..." and a WARN entry in the Output pane without the password.
5. Enter the correct password and test again. Expected: green icon with "Connected. Server version: 8.x.y." and an INFO entry in the Output pane.
6. Enter port `abc` and click OK. Expected: the dialog stays open with "The port must be a number between 1 and 65535."
7. Fix the port, leave the display name empty, click OK. Expected: a node `host:3306 (user)` with a database icon; the hint text disappears; Output pane: "Server '...' added."
8. Add a second server with display name "A test". Expected: it is listed above the first one (alphabetical).
9. Open *Advanced*, set an unknown host and timeout 3, test. Expected: an error within about 3 seconds.
10. Start a test against an unreachable host with timeout 30 and close the dialog with Cancel while it runs. Expected: the dialog closes at once; the Output pane shows "Connection test cancelled."

**Test result**

_To be filled in by Herbert._
## US-0202 Persist connections securely

**Status:** Todo

As a developer, I want my connections kept after restarting Visual Studio, with passwords stored encrypted.

**Acceptance criteria**

- [ ] Connections saved in `%LOCALAPPDATA%\ObjectExplorerForMySql\connections.json`.
- [ ] Password encrypted with DPAPI CurrentUser; plain text never in the file (unit test).
- [ ] Without saved password, the user gets a password prompt on first expand.
- [ ] Corrupt or missing file does not crash the extension; a warning is logged.

**Tasks**

- T-0202-01 `ConnectionStore` with JSON serialization + tests
- T-0202-02 `ISecretProtector` with DPAPI implementation + tests
- T-0202-03 Password prompt dialog

## US-0203 Edit, remove and reorder connections

**Status:** Todo

As a developer, I want to change or delete a server connection.

**Acceptance criteria**

- [ ] Context menu on server node: Properties (edit dialog), Remove (with confirmation), Disconnect, Refresh.
- [ ] Removing deletes the stored password as well.
- [ ] Servers sorted alphabetically by display name.

**Tasks**

- T-0203-01 Context menu on server node
- T-0203-02 Edit and remove logic in `ConnectionStore` + tests

## US-0204 Connection state

**Status:** Todo

As a developer, I want to see whether a server is connected, connecting or in error.

**Acceptance criteria**

- [ ] Server icon shows state: not connected, connecting (animated or overlay), connected, error.
- [ ] Tooltip shows server version, user and the last error.
- [ ] Disconnect clears loaded children; expand reconnects.
