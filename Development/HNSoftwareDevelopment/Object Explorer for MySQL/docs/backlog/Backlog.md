# Backlog

Status values and Definition of Done: see [Workflow](../Workflow.md).

## Release plan

| Release | Content |
|---|---|
| 0.1 (first usable) | E01, E02, E03, E04, E05 |
| 0.2 | E06, E07 |
| 0.3 | E08, E09, E10, US-0505 |
| 0.4 | E13, E14, E12, US-0705, P-06 (last) |
| 1.0 | E11, fixes from use |

## Epics

| ID | Epic | Release | Status |
|---|---|---|---|
| E01 | [Foundation](E01-Foundation.md) | 0.1 | Done |
| E02 | [Connection management](E02-ConnectionManagement.md) | 0.1 | Done |
| E03 | [Object tree](E03-ObjectTree.md) | 0.1 | Done |
| E04 | [Properties window](E04-PropertiesWindow.md) | 0.1 | Done |
| E05 | [Drag & drop to the editor](E05-DragAndDrop.md) | 0.1, 0.3 | Done |
| E06 | [Script and view code](E06-ScriptAndCode.md) | 0.2 | Done |
| E07 | [Query editor](E07-QueryEditor.md) | 0.2, 0.4 | In progress |
| E08 | [View data](E08-ViewData.md) | 0.3 | Done |
| E09 | [Object management](E09-ObjectManagement.md) | 0.3 | Done |
| E10 | [Security](E10-Security.md) | 0.3 | Done |
| E11 | [Packaging and release](E11-Release.md) | 1.0 | Todo |
| E12 | [Database documentation](E12-Documentation.md) | 0.4 | Todo |
| E13 | [Query insight](E13-QueryInsight.md) | 0.4 | Done |
| E14 | [IntelliSense](E14-IntelliSense.md) | 0.4 | Done |
| - | [Parked](Parked.md) | - | Parked |

## User stories

| ID | Story | Status |
|---|---|---|
| US-0101 | Solution and empty extension | Done |
| US-0102 | Logging to the Output window | Done |
| US-0103 | Localization-ready resources | Done |
| US-0104 | Build pipeline | Done |
| US-0201 | Add a server connection | Done |
| US-0202 | Persist connections securely | Done |
| US-0203 | Edit, remove and reorder connections | Done |
| US-0204 | Connection state | Done |
| US-0301 | Databases and system databases | Done |
| US-0302 | Tables and columns | Done |
| US-0303 | Keys, constraints, indexes and triggers | Done |
| US-0304 | Views | Done |
| US-0305 | Stored procedures, functions and parameters | Done |
| US-0306 | Events | Done |
| US-0307 | Refresh | Done |
| US-0308 | Toolbar and filter | Done |
| US-0401 | Column properties | Done |
| US-0402 | Properties for other objects | Done |
| US-0501 | Drag a single object name | Done |
| US-0502 | Drag multiple columns | Done |
| US-0503 | Drag a stored procedure or function as a call | Done |
| US-0504 | Drop format options | Done |
| US-0505 | Drag a connection string | Done |
| US-0601 | View Code | Done |
| US-0602 | Script As | Done |
| US-0603 | Script database | Done |
| US-0701 | New Query | Done |
| US-0702 | MySQL syntax coloring | Done |
| US-0703 | Execute and show results | Done |
| US-0704 | Export results | Done |
| US-0705 | Export the full result | Todo |
| US-0801 | View data (read-only) | Done |
| US-0802 | Edit data | Done |
| US-0901 | Delete objects | Done |
| US-0902 | Rename objects | Done |
| US-0903 | Create database | Done |
| US-0904 | New object from template | Done |
| US-1001 | Privilege detection | Done |
| US-1002 | Security node with users and roles | Done |
| US-1003 | Manage users | Done |
| US-1004 | New role | Done |
| US-1005 | Grant a role to a user | Done |
| US-1101 | Visual identity | Todo |
| US-1102 | Marketplace listing | Todo |
| US-1103 | Release workflow | Todo |
| US-1201 | Documentation as Markdown | Done |
| US-1202 | Documentation as PDF | Todo |
| US-1301 | Explain plan | Done |
| US-1302 | Explain analyze | Done |
| US-1303 | View dependencies | Done |
| US-1401 | Completion of names | Done |
| US-1402 | Parameter info and quick info | Done |

## Decisions

| # | Question | Decision | Date |
|---|---|---|---|
| D-1 | Localization | Follow the VS language; version 1 English only, because Visual Studio has no Dutch UI (ADR-005, ADR-010) | 2026-10-26 |
| D-2 | License | MIT (ADR-009) | 2026-10-23 |
| D-3 | Minimum MySQL version | 8.0 (ADR-008) | 2026-10-23 |
| D-4 | Documentation language | English | 2026-10-23 |
| D-5 | Quoting of dragged names in .sql files | Only when needed (default); Always / Never as option in US-0504 | 2026-10-28 |
| D-6 | Drag & Drop options | Separate quoting for .sql and other files; separate database prefix for tables/views and for calls (US-0504) | 2026-10-29 |
| D-7 | Data in Script Database | With or without data only: all rows of every table, no row limit and no selection per table, because partial data breaks foreign keys (US-0603) | 2026-10-29 |
| D-8 | Re-running Script Database | The script targets an empty database. Views use CREATE OR REPLACE and the settings restore has an IFNULL fallback; no DROP or IF NOT EXISTS for other objects, because the extension is an object explorer, not a full database management tool (US-0603) | 2026-10-29 |
| D-9 | Editor for query documents | Own *MySQL Query Editor* (code editor with content type `MySql`), not the T-SQL editor of SSDT and no own file extension (ADR-012, US-0701) | 2026-10-30 |
| D-10 | Syntax coloring | Own classifier with a tokenizer in Core, not a TextMate grammar: a grammar is bound to the .sql extension, which already has one, and cannot target the `MySql` content type (US-0702) | 2026-10-30 |
| D-11 | Server session of a query document | One session per document that stays open between runs (variables, temporary tables, USE and transactions carry over), closed with the document. An exception to "connections per operation" in the workflow checklist (US-0703) | 2026-10-30 |
| D-12 | View Data window and filter | A tab in the document well per table (multi-instance tool window, not reopened at startup); a filter box below each column header: contains for text, equal for numbers and dates, NULL / NOT NULL (US-0801) | 2026-10-30 |
| D-13 | Saving edited rows | Per row when the grid leaves it, no Save button; text NULL sets NULL; binary, generated and spatial columns are read-only (US-0802) | 2026-11-02 |
| D-14 | Deleting objects | Own themed dialog with the exact SQL and Copy SQL, Cancel as default button; one selected object at a time; a database needs its exact name typed; nothing in system databases (US-0901) | 2026-11-02 |
| D-15 | Creating objects | Not a designer: New Table, View, Procedure, Function, Event, Column, Trigger and Index open a query document with a template that the user completes and runs (US-0904); Create Database is a dialog, as in SSMS (US-0903) | 2026-11-02 |
| D-16 | Reading users | Users can be read with SELECT on mysql.user (via *.*, mysql.* or the table), not with CREATE USER alone; roles count through the test query on mysql.user, which reflects the roles active in a new session (US-1001) | 2026-11-02 |
| D-17 | Managing users | Only with Can Manage Users; every action shows its SQL first; passwords are parameters and shown as '********'; grants on a database only, revoke from any grant line; Delete on accounts, not on the own account or mysql.* system accounts (US-1003) | 2026-11-02 |
| D-18 | Follow-up after E10 | Roles can be created and granted to users (US-1004, US-1005), granting sets a default role by default; a dragged connection string follows the file type and has a password placeholder, never the password (US-0505) | 2026-11-02 |
| D-19 | Scope after 0.3 | P-01 table designer and P-03 schema compare dropped; P-02 becomes E12; from SSMS: execution plan and dependencies (E13) and IntelliSense (E14); activity monitor parked as P-06 | 2026-11-02 |
| D-20 | Full result and PDF | Export runs a read-only statement again and streams all rows to the file, with progress and Cancel (US-0705; paging the results pane would not make the export complete); PDF with MigraDoc/PDFsharp (MIT), Syncfusion as fallback (US-1202); P-06 activity monitor as the last item of 0.4 | 2026-11-03 |
| D-21 | Completion list | No commit with the space bar (an alias after a table would be replaced); commit with Tab, Enter and `.` `,` `(` `)` `;`. Not a copy of SSMS. The list never asks for a password and typing never waits for the server (US-1401) | 2026-11-03 |
