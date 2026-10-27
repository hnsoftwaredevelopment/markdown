# E02 Connection management

Add, edit, remove and connect to one or more MySQL servers.

## US-0201 Add a server connection

**Status:** Done (accepted 2026-10-26)

As a developer, I want to add a MySQL server with host, port, user and password, so that it appears in the explorer.

**Acceptance criteria**

- [x] Toolbar button "Add MySQL Server" opens a dialog.
- [x] Fields: connection name (optional), host, port (default 3306), user, password, "save password" checkbox, default database (optional).
- [x] Advanced: SSL mode (None, Preferred, Required, VerifyCA, VerifyFull), connection timeout, allow public key retrieval.
- [x] Button "Test connection" shows server version on success or the error message on failure. *(logic unit tested; dialog is a manual test)*
- [x] After OK the server appears as a node in the tree, with the connection name, or `host:port (user)` / `host:port/database (user)` when no name is given.
- [x] Dialog and tree colors fit the selected Visual Studio theme. *(added after test round 1)*

**Tasks**

- [x] T-0201-01 `ConnectionDefinition` model and connection string builder in Core + tests
- [x] T-0201-02 Connection dialog (WPF, themed)
- [x] T-0201-03 Test-connection logic (async, cancellable) + `ConnectionEditorViewModel` and `ExplorerViewModel` in Core + tests
- [x] T-0201-04 Toolbar command in tool window (VSCT, ADR-011)

**Implementation notes**

- `MySqlConnector` 2.6.2 is now referenced by Core. Connection strings set the application name "Object Explorer for MySQL"; test connections do not use pooling.
- Test round 1 (Herbert, Dark theme): functionally OK, but the dialog mixed a light window with dark input fields and buttons, and the selected tree row was hard to read. Changes:
  - The dialog now uses standard Windows dialog colors, like Visual Studio's own *Add Connection* dialog, with the same layout idea: connection name, server and port, a group *Log on to the server*, default database, *Advanced*, a separator line and the buttons.
  - The tree uses Visual Studio's tree colors (`TreeViewColors`) for background, text, expand glyph and the selected row, in an active and an inactive window.
  - The field *Display name* is now called *Connection name (optional, shown in the explorer)* and is the first field, for example to have one connection per database on the same server. Without a name the tree shows `host:port/database (user)` when a default database is set.
- Validation messages and the test result appear below the fields with a status icon.
- A server version below MySQL 8.0 or MariaDB 10.6 still connects, but the result shows a warning (ADR-008).
- Errors from the driver are masked before they are shown or logged. Every test is logged in the Output pane; the connection string only at Debug level, with the password masked.
- Closing the dialog during a test cancels the test.
- **Not in this story:** connections are kept in memory only and are gone after a restart; "Save password" has no effect yet. Both come with US-0202. The tree shows server nodes only; expanding them comes with US-0301. Selection colors of the tree are not themed yet (US-0301).
- 34 new unit tests (88 in total), including a real connection attempt to a closed local port that must fail within 15 seconds without showing the password.

**Manual test**

You need a reachable MySQL 8.x server, for example your local server.

1. Rebuild and press F5. Open *View > Object Explorer for MySQL*. Expected: a toolbar with one button (plug icon, tooltip "Add MySQL Server") and the hint text.
2. Click the button. Expected: dialog "Add MySQL Server" in standard Windows dialog colors (light, white input fields, normal buttons) in every theme; port 3306, timeout 15, SSL mode "Preferred", "Save password" checked, cursor in "Connection name".
3. Click *Test Connection* with empty fields. Expected: error icon with "Enter a server host." and "Enter a user name."
4. Enter host, user and a wrong password, click *Test Connection*. Expected: "Connection failed: Access denied for user ..." and a WARN entry in the Output pane without the password.
5. Enter the correct password and test again. Expected: green icon with "Connected. Server version: 8.x.y." and an INFO entry in the Output pane.
6. Enter port `abc` and click OK. Expected: the dialog stays open with "The port must be a number between 1 and 65535."
7. Fix the port, leave the connection name empty, click OK. Expected: a node `host:3306 (user)` with a database icon; the hint text disappears; Output pane: "Server '...' added."
7a. Add the same server again with default database `mysql` and no name. Expected: a node `host:3306/mysql (user)`.
8. Add a server with connection name "A test". Expected: it is listed above the others (alphabetical).
8a. Click a node, then click in the code editor. Expected (Dark and Light theme): the selected row uses the Visual Studio selection color with readable text, and a lighter inactive selection color when the explorer does not have focus.
9. Open *Advanced*, set an unknown host and timeout 3, test. Expected: an error within about 3 seconds.
10. Start a test against an unreachable host with timeout 30 and close the dialog with Cancel while it runs. Expected: the dialog closes at once; the Output pane shows "Connection test cancelled."

**Test result**

2026-10-26, Herbert: accepted after test round 2. All manual tests passed; dialog and tree colors are correct, also in the tree view; the connection name as first field is more logical.
## US-0202 Persist connections securely

**Status:** Done (accepted 2026-10-27)

As a developer, I want my connections kept after restarting Visual Studio, with passwords stored encrypted.

**Acceptance criteria**

- [x] Connections saved in `%LOCALAPPDATA%\ObjectExplorerForMySql\connections.json`.
- [x] Password encrypted with DPAPI CurrentUser; plain text never in the file (unit test).
- [ ] ~~Without saved password, the user gets a password prompt on first expand.~~ Moved to US-0301: servers cannot be expanded yet, so there is no moment to ask. Until then a connection without a saved password is loaded without password.
- [x] Corrupt or missing file does not crash the extension; a warning is logged.

**Tasks**

- [x] T-0202-01 `ConnectionStore` with JSON serialization + tests
- [x] T-0202-02 `ISecretProtector` with DPAPI implementation + tests
- [ ] T-0202-03 Password prompt dialog: moved to US-0301

**Implementation notes**

- File format: indented JSON with `"version": 1` and one entry per connection. The password is only written as `protectedPassword` (DPAPI, scope CurrentUser, with extra entropy) and only when "Save password" is checked. Example:

  ```json
  {
    "version": 1,
    "connections": [
      {
        "id": "4b0d...",
        "displayName": "Production",
        "host": "db.local",
        "port": 3306,
        "userName": "app",
        "savePassword": true,
        "protectedPassword": "AQAAANCMnd8BFdERjHoAwE...",
        "sslMode": "Preferred",
        "connectionTimeoutSeconds": 15,
        "allowPublicKeyRetrieval": false
      }
    ]
  }
  ```

- Saving writes to `connections.json.tmp` first and then replaces the file, so a crash never leaves half a file.
- An unreadable file is renamed to `connections.json.corrupt-<date>-<time>` before anything else happens, so the next save cannot overwrite the user's data. The Output pane shows a warning with the new name.
- Invalid entries (for example an empty host after a manual edit) are skipped with a warning; missing values get their defaults; an unknown SSL mode becomes "Preferred". A file saved by Notepad with a byte order mark is read correctly.
- A password that cannot be decrypted (file copied to another Windows user or computer) is loaded as empty, with a warning.
- Connections are loaded when the package loads (opening the explorer) and saved after every change. If saving fails, a message says the list will be lost when Visual Studio closes.
- The JSON is written with the .NET Framework's own `DataContractJsonSerializer`, so no extra JSON library ends up in the VSIX next to the one Visual Studio already loads.
- 17 new unit tests (106 in total), including DPAPI round trips on Windows.

**Manual test**

1. Rebuild and press F5. Open the explorer and add two servers: A with "Save password" checked, B with "Save password" unchecked.
2. Open `%LOCALAPPDATA%\ObjectExplorerForMySql\connections.json` in an editor. Expected: both connections; A has a long `protectedPassword` value, B has none; your password appears nowhere in the file.
3. Close the Experimental Instance, start it again with F5 and open the explorer. Expected: both servers are back, sorted as before; the Output pane shows "Loaded 2 connection(s) from ...".
4. Close the Experimental Instance. Replace the content of `connections.json` with `this is not json` and save. Start again and open the explorer. Expected: no error dialog, an empty explorer, a WARN line in the Output pane, and a file `connections.json.corrupt-...` next to it with your text.
5. Add a server again. Expected: a new `connections.json` is written; the corrupt copy stays.
6. Optional: make the folder read-only (or open `connections.json` exclusively in another program) and add a server. Expected: a message that the list could not be saved, and an ERROR line in the Output pane.

**Test result**

2026-10-27, Herbert: accepted. All manual tests passed as expected.
## US-0203 Edit, remove and reorder connections

**Status:** Ready for test

As a developer, I want to change or delete a server connection.

**Acceptance criteria**

- [x] Context menu on server node: Properties (edit dialog), Remove (with confirmation), Disconnect, Refresh. *(Disconnect and Refresh are shown but disabled until US-0204 and US-0301)*
- [x] Removing deletes the stored password as well.
- [x] Servers sorted alphabetically by display name, also after a change of name.

**Tasks**

- [x] T-0203-01 Context menu on server node (VSCT, ADR-011)
- [x] T-0203-02 Edit and remove logic in `ExplorerViewModel` and `ConnectionEditorViewModel` + tests

**Implementation notes**

- The context menu is a Visual Studio menu from the VSCT file, so it has the Visual Studio look, icons and access keys. It opens with a right-click (which selects the node first, like Solution Explorer), Shift+F10 or the context menu key.
- **Delete** on a selected server runs *Remove*. Remove asks for confirmation with *No* as default button and says that the server itself is not changed.
- **Properties** opens the connection dialog with the title *Connection Properties* and the current values. The password field starts empty; when a password is saved, the hint "Leave empty to keep the current password." is shown. Typing a password replaces it. The connection keeps its ID, so later features (open queries, settings per connection) stay linked.
- After a change of name the node moves to its new alphabetical position.
- Every change is saved directly to `connections.json` (US-0202).
- 12 new unit tests (118 in total).

**Manual test**

1. Rebuild and press F5. Open the explorer with at least two saved servers, A (with saved password) and B.
2. Right-click server B. Expected: B is selected and a menu shows *Refresh* and *Disconnect* (disabled), *Remove*, and *Properties*, with icons and separator lines.
3. Select A and press Shift+F10. Expected: the same menu at the node.
4. Choose *Properties* on A. Expected: title "Connection Properties", all fields filled except the password, with the hint below the password field.
5. Change only the connection name to "Z test", click OK. Expected: the node is renamed and moves to the bottom; the Output pane shows "changed and renamed".
6. Open *Properties* again and click *Test Connection* without typing a password. Expected: the test succeeds (the saved password is used).
7. Restart the Experimental Instance. Expected: "Z test" is still there with its new name and still connects with the saved password (step 6 again).
8. Select B and press Delete. Expected: a question with *No* as default. Press Enter: nothing changes.
9. Press Delete again and choose *Yes*. Expected: B disappears; `connections.json` no longer contains B or its `protectedPassword`.
10. Remove the last server. Expected: the hint text "No MySQL servers yet ..." is back.

**Test result**

_To be filled in by Herbert._
## US-0204 Connection state

**Status:** Todo

As a developer, I want to see whether a server is connected, connecting or in error.

**Acceptance criteria**

- [ ] Server icon shows state: not connected, connecting (animated or overlay), connected, error.
- [ ] Tooltip shows server version, user and the last error.
- [ ] Disconnect clears loaded children; expand reconnects.
