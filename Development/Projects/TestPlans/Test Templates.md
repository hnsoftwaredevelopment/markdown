---
type: index
created: 2026-10-06
tags: [testplan, templates]
---

# Test templates

| Template | Use for | Output per item |
|---|---|---|
| [[TPL User Story Testplan]] | One Jira story (BT1, BT2) | Test cases per behaviour, machine modules, AC coverage |
| [[TPL Epic Testplan]] | One Jira epic | Story overview, coverage matrix, end-to-end scenarios, cycle time, upgrade, release advice |
| [[TPL SWMS Support Issue Testplan]] | One SWMS support ticket | Reproduction, fix verification, regression, backport check |
| RC test plan | A full release candidate | Use the `rc-risk-testplan` skill, not these templates |

## Setup in Obsidian

1. Settings > Core plugins > Templates: on. Set "Template folder location" to this folder.
2. Create a new note named after the ticket, e.g. `BT2-3857 Tool clamp check`. Run "Templates: Insert template" and pick the template. `{{title}}` and `{{date}}` fill in.
3. The epic table and progress queries need the Dataview community plugin.

## Conventions

- Test case ID: `TC-<ticket number>-01`, e.g. `TC-3857-01`. SWMS: `TC-SWMS-11520-01`.
- Status per test case as inline field `result:: open | pass | fail | blocked`.
- Frontmatter `status`: `draft` > `ready` > `in-test` > `done`.
- Story plans set `epic:` to the epic's Jira key. The epic plan lists them automatically.
- Risk score: impact x likelihood, same scale as the RC analysis (6+ High, 3-5 Medium, below 3 Low).

## Machine notes

| Machine | Code signals | Notes |
|---|---|---|
| V630 | `MachineType_V630`, `Main Objects/Drill/`, `DrillChangerType_Cylinder` | Old drill object |
| V631 | `MachineType_V631`, `Drill_V2`, `ToolClamp`, `DrillChangerType_AirCylinder8Pos` | Weiss spindle |
| V633 | `MachineType_V633`, `Drill_V2`, `Suhner`, `DrillChangerType_CarouselCylinder` | |
| VB Standard / VB 1040 | `SawFixedRotatableTable`, `Saw/OldStyle`, `SawType_VB1x50`, `SawType_VBS1x50`, `SawType_VBS1x50b` | No "1040" type in the code; it runs as the VB1050/1250 family |
| V912 | `MachineType_V912`, `V912Integration`, `LaserHead`, `LaserSafetyHandler`, `MZ_GetV912Gripper`, MeasureUnit `IsV912` | Laser head without nozzle handler, X axis with asynchronous drive |

## Open progress

```dataview
TABLE type, jira, status, risk
FROM #testplan
WHERE status != "done" AND type != "index" AND !startswith(file.name, "TPL ")
SORT created DESC
```
