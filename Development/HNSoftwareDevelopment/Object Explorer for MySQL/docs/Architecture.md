# Architecture decisions

Each decision has a number, a status and a reason. Change a decision by adding a new one that supersedes it, so the history stays readable.

## ADR-001 Extension model: in-process VSSDK with VisualStudio.Extensibility where it fits

**Status:** Accepted (2026-10-23)

**Context.** The extension targets Visual Studio 2026 and later only, so we can use the newest APIs. The new VisualStudio.Extensibility model renders tool window content through Remote UI. Remote UI has these limits, according to the Microsoft documentation:

- No code-behind and no event handlers. User actions only go through bound async commands.
- No custom controls. XAML can only reference types from the Visual Studio process.
- The data context must be serializable `[DataContract]` types.
- No documented integration with the Properties window.
- Drag & drop from a tree to the code editor needs mouse events, which Remote UI does not offer.

Drag & drop and the Properties window are core requirements of this product.

**Decision.**

- One VSIX, running **in-process**, as a *VSSDK-compatible* VisualStudio.Extensibility extension.
- The **explorer tool window** is a classic `ToolWindowPane` with a WPF `TreeView`. This gives us drag & drop, context menus, keyboard handling and `ITrackSelection` for the Properties window.
- **VisualStudio.Extensibility** is used for parts where it works well: commands and menu placement, the settings API (options page), and later simple dialogs.
- All logic that does not need Visual Studio lives in `ObjectExplorerForMySql.Core`, so it can be unit tested without Visual Studio.

**Consequence.** The VSIX targets .NET Framework 4.8 (Visual Studio itself still runs on .NET Framework). The Core library targets `netstandard2.0` so it works in Visual Studio and in .NET 10 test projects.

## ADR-002 MySQL driver: MySqlConnector

**Status:** Accepted

**Decision.** Use [MySqlConnector](https://mysqlconnector.net/) (MIT license, fully async, `netstandard2.0` support).

**Reason.** Commercial use requires a license compatible with MIT/GPL open source without restrictions. Oracle's `MySql.Data` uses GPL with a FOSS exception or a commercial license, which complicates distribution.

## ADR-003 Metadata source: INFORMATION_SCHEMA plus SHOW statements

**Status:** Accepted

**Decision.** Read metadata from `INFORMATION_SCHEMA` (`SCHEMATA`, `TABLES`, `COLUMNS`, `TABLE_CONSTRAINTS`, `KEY_COLUMN_USAGE`, `REFERENTIAL_CONSTRAINTS`, `STATISTICS`, `ROUTINES`, `PARAMETERS`, `TRIGGERS`, `VIEWS`, `EVENTS`). Use `SHOW CREATE ...` for source code.

**Reason.** `INFORMATION_SCHEMA` only returns objects the current user can see, so the tree automatically respects permissions. The queries also work on MariaDB with small differences.

Each tree level loads with one query per level, only when the node is expanded (lazy loading).

## ADR-004 Credentials: Windows DPAPI, per user

**Status:** Accepted

**Decision.** Connection definitions (host, port, user, options) are stored in a JSON file under `%LOCALAPPDATA%\ObjectExplorerForMySql\connections.json`. Passwords are encrypted with DPAPI (`ProtectedData`, scope `CurrentUser`) and never written as plain text. The user can also choose "do not save password" and gets a prompt on connect.

## ADR-005 Localization: resource files, follow the Visual Studio UI language

**Status:** Accepted (2026-10-23)

**Decision.**

- All user-visible text goes into `.resx` files from the first line of code. No hardcoded strings.
- Visual Studio sets the UI culture of its process to the language chosen in *Tools > Options > Environment > International Settings*. .NET resource lookup then picks the right `.resx` automatically. No own language switch is needed.
- Menu and command texts in VisualStudio.Extensibility use `string-resources.json` per language; the VSIX manifest is localized with a `Extension.vsixlangpack` per language.
- **Version 1 ships English (neutral) and Dutch.** Other Visual Studio languages (cs, de, es, fr, it, ja, ko, pl, pt-BR, ru, tr, zh-Hans, zh-Hant) can be added later by adding resource files only, without code changes.

**Reason.** Building for localization from day one costs little. Translating into 14 languages and keeping those translations correct costs a lot, so we only do that when users ask for it.

## ADR-006 Security node only when permitted

**Status:** Accepted

**Decision.** On connect, the extension checks the privileges of the current account with `SHOW GRANTS FOR CURRENT_USER()` and a test query `SELECT 1 FROM mysql.user LIMIT 0`. The *Security* node (users and grants) is only shown when that check succeeds. Without permission the node is hidden, and a tooltip on the server node explains why.

## ADR-007 Testing split

**Status:** Accepted

- **Unit tests (xUnit, .NET 10):** Core library: SQL generation, quoting of identifiers, drag & drop text formats, parsing of metadata rows, settings serialization, privilege detection logic.
- **Integration tests (optional):** Metadata queries against a real MySQL 8 server in Docker via Testcontainers. These run when Docker is available and are skipped otherwise.
- **Manual tests (Herbert):** Everything that needs a running Visual Studio: tool window, tree behavior, drag & drop into the editor, Properties window, theming (light/dark/blue), localization.

## ADR-008 Minimum supported version: MySQL 8.0

**Status:** Accepted (2026-10-23)

**Context.** MySQL 8.0 reached end of life in April 2026, and 8.4 is the current LTS line. Many servers in production still run 8.0, and some cloud providers offer extended support for it.

**Decision.** Support MySQL 8.0 and later (including 8.4 LTS and 9.x Innovation releases). MariaDB 10.6+ is best effort.

**Reason.** The `INFORMATION_SCHEMA` tables we use are almost identical in 8.0 and 8.4, so supporting 8.0 costs little. Version-dependent features are detected at runtime instead of blocking the connection:

- Check constraints: 8.0.16 and later. The Constraints folder is hidden on older servers.
- Invisible indexes and columns: shown only when the server reports them.
- `ALTER TABLE ... RENAME COLUMN`: available in all 8.0 versions.

Integration tests run against MySQL 8.0 and 8.4.

## ADR-009 License: MIT

**Status:** Accepted (2026-10-23)

**Decision.** The source code is published under the MIT license. All dependencies must be MIT-compatible (MySqlConnector is MIT).

## Parked topics

- Table designer (visual create/alter table)
- Database documentation export as PDF
- Schema compare and data compare
