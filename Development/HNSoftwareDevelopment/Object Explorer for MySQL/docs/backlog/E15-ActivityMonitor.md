# E15 Activity monitor

See what runs on a server and stop a statement or session that blocks others. From the comparison with SSMS; picked up from P-06 as the last item of release 0.4 (decision D-23).

## US-1501 Activity monitor

**Status:** Done (accepted 2026-11-03)

As a developer, I want to see the sessions of a server with what they run, and stop a statement or session, so that I can find and end a query that hangs or holds a lock.

**Acceptance criteria**

- [x] *Activity Monitor* on a connected server opens a window in the document well, one per connection.
- [x] A list of sessions: id, user, host, database, command, time, state and statement. Active sessions first, the longest running on top.
- [x] Refresh by hand, and automatically every 5 seconds (on by default, can be switched off).
- [x] *Hide idle sessions* leaves out sessions in Sleep.
- [x] *Kill Query* stops the statement of the selected session; *Kill Connection* closes the whole session. Both ask first; *No* is the default.
- [x] The connection of the monitor itself is not in the list.
- [x] Source: `performance_schema.processlist`, with `SHOW FULL PROCESSLIST` as fallback (MariaDB, MySQL before 8.0.22).

**Tasks**

- [x] T-1501-01 `MySqlActivitySource` (read with fallback, KILL) and `ActivityMonitorViewModel` (order, filter, refresh, kill, errors) + tests
- [x] T-1501-02 Tool window with toolbar, grid, context menu, timer; command on the server node

**Implementation notes**

- *Activity Monitor* is in the context menu of a server, below *New Query*, enabled when the server is connected. A second *Activity Monitor* on the same server shows the same window. The window is transient, so Visual Studio does not reopen it at startup and never queries a server or asks a password by itself.
- Every refresh opens a pooled connection and reads `SELECT ID, USER, HOST, DB, COMMAND, TIME, STATE, INFO FROM performance_schema.processlist`. When that fails (table missing on MariaDB and MySQL before 8.0.22, or not readable), it reads `SHOW FULL PROCESSLIST` and keeps doing that for this connection. The id of the reading connection is filtered out.
- Order: sessions that run something first, then those in Sleep (grey); within each, the longest time first. Clicking a column header sorts by that column instead. The selected session stays selected after a refresh while it exists.
- Auto refresh runs every 5 seconds while the window is visible; a hidden tab does not query the server. A refresh that fails shows the error above the grid and switches Auto refresh off, so the error does not come back every 5 seconds. Cancelling the password prompt also switches it off.
- The statement column shows the statement on one line; the tooltip and *Copy Statement* give the full text.
- *Kill Query* runs `KILL QUERY <id>` (disabled for a session in Sleep, which runs nothing); *Kill Connection* runs `KILL CONNECTION <id>`, which also rolls back the open transaction of that session. The question names the session, the user, the connection and the start of the statement. After a kill the list refreshes. Errors (for example *You are not owner of thread*) appear above the grid. Kills are written to the Output window.
- Without the PROCESS privilege MySQL only shows the sessions of the own account; killing sessions of other accounts needs CONNECTION_ADMIN (or SUPER).
- Not in this story: lock waits (who blocks whom) and server statistics; possible follow-ups.

**Manual test**

Use a server where you can open a second session, for example a second query document.

1. Right-click a connected server: *Activity Monitor* below *New Query*. Disabled on a disconnected server; not on databases or other nodes.
2. Open it: a tab *<connection> [Activity]* with the sessions; the line above the grid shows the count, the active count and the refresh time. The monitor's own connection is not listed.
3. In a query document run `SELECT SLEEP(120);`. Within 5 seconds the monitor shows that session at the top, command *Query*, time counting up, the statement in the last column. Hover: the full statement as tooltip.
4. Select it and press *Kill Query*. The question names the session; *No* (default) does nothing. *Yes*: the query document reports the interrupted query, the session goes to Sleep in the list.
5. Run `SELECT SLEEP(120);` again and use *Kill Connection* from the context menu: the query document reports a lost connection; the next run in that document opens a new session.
6. *Hide idle sessions*: sessions in Sleep disappear; uncheck: they are back (grey).
7. Switch *Auto refresh* off: the refresh time stays; *Refresh* updates it. Switch it on again.
8. Put the tab in the background, then bring it back: it refreshes again (check the time).
9. Lock wait: in document A run `START TRANSACTION; UPDATE sakila.actor SET first_name = first_name WHERE actor_id = 1;` and in document B `UPDATE sakila.actor SET last_name = last_name WHERE actor_id = 1;`. B is shown with state such as *updating* or *waiting for row lock*; *Kill Connection* on A releases B.
10. Kill a system session (for example *event_scheduler*, if running) or a session of another account without the privilege: an error above the grid; Visual Studio keeps running.
11. Copy Statement on a running query: the clipboard has the full text.
12. Open *Activity Monitor* on a second connection: a separate tab. Close a tab and open it again: fresh data.
13. On MariaDB (if available): the list works through SHOW FULL PROCESSLIST.
14. Theme (Dark, Light, Blue): toolbar, grid and grey idle rows are readable.
