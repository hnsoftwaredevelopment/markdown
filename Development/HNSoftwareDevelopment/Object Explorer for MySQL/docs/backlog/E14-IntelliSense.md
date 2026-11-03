# E14 IntelliSense in the query editor

Completion of names in the MySQL Query Editor from the metadata of the linked connection. From the comparison with SSMS.

## US-1401 Completion of names

**Status:** Todo

As a developer, I want the editor to suggest databases, tables, views, columns and routines while I type, so that I type less and make fewer mistakes.

**Acceptance criteria**

- [ ] Completion list (Ctrl+Space and while typing) with keywords, databases, tables, views, procedures and functions of the linked connection and database.
- [ ] After `table.` or `alias.`: the columns of that table; aliases from the FROM and JOIN parts of the statement.
- [ ] Names are quoted when needed (setting of US-0504).
- [ ] The metadata is read once per connection and database and cached; Refresh in the explorer clears the cache. Typing never waits for the server.

## US-1402 Parameter info and quick info

**Status:** Todo

**Acceptance criteria**

- [ ] Parameter info for procedures and functions after `(`.
- [ ] Quick info on hover over a table or column: type, nullable, key, comment.
