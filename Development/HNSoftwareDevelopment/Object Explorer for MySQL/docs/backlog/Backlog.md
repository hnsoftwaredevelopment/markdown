# Backlog

Status values and Definition of Done: see [Workflow](../Workflow.md).

## Release plan

| Release | Content |
|---|---|
| 0.1 (first usable) | E01, E02, E03, E04, E05 |
| 0.2 | E06, E07 |
| 0.3 | E08, E09, E10 |
| 1.0 | E11, fixes from use |

## Epics

| ID | Epic | Release | Status |
|---|---|---|---|
| E01 | [Foundation](E01-Foundation.md) | 0.1 | In progress |
| E02 | [Connection management](E02-ConnectionManagement.md) | 0.1 | Todo |
| E03 | [Object tree](E03-ObjectTree.md) | 0.1 | Todo |
| E04 | [Properties window](E04-PropertiesWindow.md) | 0.1 | Todo |
| E05 | [Drag & drop to the editor](E05-DragAndDrop.md) | 0.1 | Todo |
| E06 | [Script and view code](E06-ScriptAndCode.md) | 0.2 | Todo |
| E07 | [Query editor](E07-QueryEditor.md) | 0.2 | Todo |
| E08 | [View data](E08-ViewData.md) | 0.3 | Todo |
| E09 | [Object management](E09-ObjectManagement.md) | 0.3 | Todo |
| E10 | [Security](E10-Security.md) | 0.3 | Todo |
| E11 | [Packaging and release](E11-Release.md) | 1.0 | Todo |
| - | [Parked](Parked.md) | - | Parked |

## User stories

| ID | Story | Status |
|---|---|---|
| US-0101 | Solution and empty extension | Ready for test |
| US-0102 | Logging to the Output window | Todo |
| US-0103 | Localization infrastructure | Todo |
| US-0104 | Build pipeline | Todo |
| US-0201 | Add a server connection | Todo |
| US-0202 | Persist connections securely | Todo |
| US-0203 | Edit, remove and reorder connections | Todo |
| US-0204 | Connection state | Todo |
| US-0301 | Databases and system databases | Todo |
| US-0302 | Tables and columns | Todo |
| US-0303 | Keys, constraints, indexes and triggers | Todo |
| US-0304 | Views | Todo |
| US-0305 | Stored procedures, functions and parameters | Todo |
| US-0306 | Events | Todo |
| US-0307 | Refresh | Todo |
| US-0308 | Toolbar and filter | Todo |
| US-0401 | Column properties | Todo |
| US-0402 | Properties for other objects | Todo |
| US-0501 | Drag a single object name | Todo |
| US-0502 | Drag multiple columns | Todo |
| US-0503 | Drag a stored procedure or function as a call | Todo |
| US-0504 | Drop format options | Todo |
| US-0601 | View Code | Todo |
| US-0602 | Script As | Todo |
| US-0603 | Script database | Todo |
| US-0701 | New Query | Todo |
| US-0702 | MySQL syntax coloring | Todo |
| US-0703 | Execute and show results | Todo |
| US-0801 | View data (read-only) | Todo |
| US-0802 | Edit data | Todo |
| US-0901 | Delete objects | Todo |
| US-0902 | Rename objects | Todo |
| US-0903 | Create database | Todo |
| US-1001 | Privilege detection | Todo |
| US-1002 | Security node with users and roles | Todo |
| US-1003 | Manage users | Todo |
| US-1101 | Visual identity | Todo |
| US-1102 | Marketplace listing | Todo |
| US-1103 | Release workflow | Todo |

## Decisions

| # | Question | Decision | Date |
|---|---|---|---|
| D-1 | Localization | English + Dutch, following the VS language (ADR-005) | 2026-10-23 |
| D-2 | License | MIT (ADR-009) | 2026-10-23 |
| D-3 | Minimum MySQL version | 8.0 (ADR-008) | 2026-10-23 |
| D-4 | Documentation language | English | 2026-10-23 |
