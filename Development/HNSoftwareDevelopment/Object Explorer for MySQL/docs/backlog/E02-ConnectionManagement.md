# E02 Connection management

Add, edit, remove and connect to one or more MySQL servers.

## US-0201 Add a server connection

**Status:** Todo

As a developer, I want to add a MySQL server with host, port, user and password, so that it appears in the explorer.

**Acceptance criteria**

- [ ] Toolbar button "Add MySQL Server" opens a dialog.
- [ ] Fields: display name (optional), host, port (default 3306), user, password, "save password" checkbox, default database (optional).
- [ ] Advanced: SSL mode (None, Preferred, Required, VerifyCA, VerifyFull), connection timeout, allow public key retrieval.
- [ ] Button "Test connection" shows server version on success or the error message on failure.
- [ ] After OK the server appears as a node in the tree, with display name or `host:port (user)`.

**Tasks**

- T-0201-01 `ConnectionDefinition` model and connection string builder in Core + tests
- T-0201-02 Connection dialog (WPF, themed)
- T-0201-03 Test-connection logic (async, cancellable)
- T-0201-04 Toolbar command in tool window

**Manual test**

1. Click "Add MySQL Server", enter a local MySQL 8 server, click Test connection.
2. Expected: message with server version.
3. Enter a wrong password and test. Expected: readable error "Access denied for user ...".

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
