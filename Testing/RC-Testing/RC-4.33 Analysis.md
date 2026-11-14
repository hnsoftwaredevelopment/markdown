---
rc: "4.33"
branch: RC-4.33.0
rc_commit: ed77b6064c4
rc_commit_date: 2026-10-01
baseline: 4.32.17
baseline_commit: 89b963e2aed
analysed: 2026-10-02
machines: [V630, V631, V633, VB Standard, WB Standard + Probe Truck, VB 1040]
tags: [rc-testing, rc-4-33]
---

# RC-4.33 Analysis

Related: [[RC-4.33 Testplan]] · [[RC-4.33 Test cases]] · [[RC-4.33 Other team alerts]]

## Summary

- RC-4.33.0 holds 2,937 commits that are not in 4.32.17. 1,132 of them touch code that runs on your machines.
- Those 1,132 commits name 111 tickets: 20 BT1, 32 BT2, 45 SWMS, 13 MCPL, 1 FAB. 491 relevant commits have no ticket key.
- Of the 16 code areas, 11 score High, 3 Medium and 2 Low. On top of that, the PLC refactoring is listed as one cross-cutting risk.
- Biggest risk 1: a large PLC refactoring (MCPL layer violations, BT2 decoupling of Drill, MeasureUnit, Saw and MaterialClamping). No new behaviour is intended, but it rewires how saw, drill, measuring unit and transport read machine data. Regressions will show up as wrong positions, missing interlocks or objects that do not initialise.
- Biggest risk 2: upgrade. The config migration script `MC_BranchScript.sql` is changed by 20 tickets, 10 of them from BT1, BT2 or SWMS. One of them removes MachineZone data from Drill and DeburUnit (BT2-3879).
- Biggest risk 3: safety and positioning. The measuring unit front-side detection, the V631 Z3/Y4 minimum distance (185 to 164 mm), the V633 unit 3 collision range and infeed handling of short material all change.
- There is no `RC-4.32 Analysis` yet, so no comparison with the previous RC.

## Scope

| Item | Value |
|---|---|
| Baseline | tag `4.32.17` (89b963e2aed, 2026-10-01) |
| RC state analysed | `origin/RC-4.33.0` at ed77b6064c4 (2026-10-01) |
| Range | `4.32.17..origin/RC-4.33.0`, merges excluded |
| Machines | V630, V631, V633, VB Standard, WB Standard + Probe Truck, VB 1040 (VB1050/1250 family in code) |
| Excluded | Fabricator, V912, V353/V35X laser, V807/V808 coping, V623, plate machines, robotics. Unit tests, docs and GitHub workflows. MCPL and FAB commits count only when they touch drill or saw files |
| Not included | V631MK2 and V633MK2 (your choice) |

> [!info] BT1 changes that can affect machines outside this list are in [[RC-4.33 Other team alerts]].

## Risk matrix

| Area | Risk | Machines | Commits | Key tickets | What can change on the machine |
|---|---|---|---|---|---|
| PLC refactoring (layers, data ports) | High | All | 185 tagged, plus untagged review fixes | MCPL-3147, MCPL-3154, MCPL-3149, MCPL-3151, MCPL-3152, BT2-3871, BT2-3879, BT2-3891, BT2-3857, BT2-3881/3882/3883, BT2-3907 | Saw, drill, measuring unit, transport and clamping now get machine data through injected interfaces instead of globals. A wrong or missing link gives a null object: an axis that does not move, a check that always passes, or a message that does not appear |
| Configuration / upgrade | High | All | 233 | BT2-3879, BT2-3834, BT1-2305, BT2-3827, SWMS-11589, SWMS-11520, BT2-3694, BT1-2332, BT1-2271 | Migration script removes MachineZone values from Drill and DeburUnit, removes PicoScan instances, moves position correction from MeasureUnit to Saw. Clamp pressure min/max is now validated in the settings screen. V633: X-axis external brake check is only set when the measure unit is a gripper truck |
| Safety / collision | High | All | 155 | BT2-3694, BT2-3882, SWMS-11394, SWMS-10961, SWMS-11577, SWMS-11137 | Front-side detection of the measuring unit now halts conveyors only outside automatic mode. MeasureUnit collision model, clamp pressure and safety rectangles moved. V631 Z3/Y4 minimum distance 185 to 164 mm. V633 unit 3 gets a collision-free range for large tools near the side bearings |
| Cycle list / process control | High | All | 102 | SWMS-11536, SWMS-11130, BT2-3781, SWMS-11371 | Two reentrant deadlocks in the PLC command/property pipeline fixed. Event buffer handling for automatic start changed. Early validation code is in although the ticket is still Ready to Develop |
| Material transport / measuring | High | All | 289 | SWMS-11394, BT1-11254, SWMS-11254, SWMS-11010, SWMS-11319, BT1-2304, BT1-2305 | Infeed safe position for the next material and X target based on gripper selection (short rollers, 1,400 mm material). Measured width now comes from the measure roll unit. Conveyor synchronisation fix. Angle iron height and width calculated inverted in behind orientation. Transport groups can also drive position-controlled axes and synchronised rollers |
| Drill shared (V630, V631, V633) | High | V630, V631, V633 | 139 | BT2-3871, BT2-3879, BT2-3891, SWMS-11363, SWMS-11554, SWMS-11499, SWMS-11600 | Drill changer and drilling cross-cutting refactor. Any drill tool type can be restricted to specific drill units. Crash fix when changing a tool on layout marking units. Tools disappearing from the F6 menu fixed |
| Drill V2 (V631, V633) | High | V631, V633 | 96 | SWMS-10961, SWMS-10977, SWMS-10787, SWMS-11147, SWMS-11501, BT2-3892, BT2-3874 | Z3/Y4 margin, drill 3 waiting during milling (LimitedPosition), web support goes to rest if the target is not reachable and is checked in rest for every drill type, tool length measuring uses the actual position motion task (commit 2026-09-30) |
| Saw shared | High | VB Standard, WB + Probe Truck, VB 1040 | 113 | SWMS-11596, SWMS-11057, BT2-3525, BT2-3566, BT2-3569, SWMS-11678 | W-axis limited to the moveable roller range while the roller is active. Cut positions corrected with the most relevant material measurement. Alternative reference planes. Clear cut can be 0 |
| Saw fixed rotatable table | High | VB Standard, WB + Probe Truck | 24 | SWMS-11589, BT2-3907 | Position correction moved from MeasureUnit to Saw, renamed to RecheckEnteredPositionCorrection. Message converter injected into saw objects |
| VACAM application | High | All | 302 | BT2-3535, BT2-3522, BT2-3529, SWMS-10779, SWMS-11020, SWMS-11482, SWMS-11494 | Hole operation machine view refactor, material translation, default reference data, master machine indicator, radius in product viewer, free length material end limit, buffer stack positions. Also NLog, gRPC and .NET package updates |
| Translations / UI text | High (score), treat as Medium | All | 56 | various | New and changed message texts. Check that new warnings show readable text |
| Saw old style (VB1050/1250) | Medium | VB 1040 | 31 | MCPL-3154, MCPL-3147 | Saw free functions no longer read the global saw. Walk-in control and the remaining saw reads go through `I_SawData`. `SW_Safety` and `SW_Update` touched |
| Drill V633 | Medium | V633 | 23 | SWMS-11577, BT1-2332 | Rat hole milling fix (Blocker, tool damage), new V633 machine definition and drill zone in .NET, unit 3 side bearing collision range |
| Probe truck / standalone saw | Medium | WB + Probe Truck | 22 | BT2-3907, MCPL-3149 | Fix: infeed and outfeed pointers were used in `FB_ProbeTruck` before they were set. Message converter injected |
| Drill V631 | Low | V631 | 7 | refactor only | No functional V631-only change apart from the Drill V2 items above |
| Drill V630 | Low | V630 | 6 | refactor only | No V630-only change. V630 gets the shared drill and transport changes |

The "VACAM application" and "Translations" scores come from volume. Most of those commits are UI or refactoring. Testing them is covered by the smoke test and the upgrade test.

## Per machine

### V630
- Areas: Drill shared, PLC refactoring, configuration migration, transport and measuring, safety.
- Tickets: BT2-3871, BT2-3879, BT2-3891, SWMS-11363, SWMS-11554, SWMS-11499, BT2-3694, SWMS-11394.
- Verdict: full drill regression after upgrade. Focus on drill changer, tool restriction per unit and the front-side detection.

### V631
- Areas: Drill V2, Drill shared, PLC refactoring, configuration, safety.
- Tickets: SWMS-10961, SWMS-10977, SWMS-10787, SWMS-11147, SWMS-11501, SWMS-11554, SWMS-10680, BT2-3892.
- Verdict: full regression. Z3/Y4 margin changed by 21 mm: run collision-sensitive jobs on unit 3 and 4. Check tool length measuring in automatic.

### V633
- Areas: Drill V633, Drill V2, Drill shared, configuration, safety.
- Tickets: SWMS-11577, BT1-2332, SWMS-10977, SWMS-11501, SWMS-11147, SWMS-10680.
- Verdict: full regression. Rat hole milling and unit 3 with large tools first. Check X-axis brake behaviour on a V633 with roller measuring (V633M).

### VB Standard
- Areas: Saw fixed rotatable table, Saw shared, PLC refactoring, transport and measuring.
- Tickets: SWMS-11589, SWMS-11596, SWMS-11678, BT2-3525, BT2-3907, BT2-3694.
- Verdict: focus on cut position accuracy, position correction dialog and W-axis limits with moveable rollers.

### WB Standard + Probe Truck
- Areas: Probe truck, Saw fixed rotatable table, Saw shared, measuring.
- Tickets: BT2-3907, MCPL-3149, SWMS-11589, BT1-11254.
- Verdict: focus on probe truck search and push, roller blocking on the saw table while the truck pushes, measured width.

### VB 1040 (VB1050/1250 family)
- Areas: Saw old style, Saw shared, PLC refactoring.
- Tickets: MCPL-3154, MCPL-3147, SWMS-11596, SWMS-11678, BT2-3525.
- Verdict: saw safety and walk-in control regression after the refactor. No functional ticket targets this saw directly.

## Ticket list

Tickets with a commit in a relevant area. MCPL refactoring tickets are listed together at the end.

| Ticket | Type | Status | Summary | Area | Machines |
|---|---|---|---|---|---|
| [SWMS-11577](https://voortman.atlassian.net/browse/SWMS-11577) | CIM issue | Done | Rat hole milling not working properly, damaging tool (Blocker) | Drill V633 | V633 |
| [SWMS-11394](https://voortman.atlassian.net/browse/SWMS-11394) | CIM issue | Done | Short rollers on infeed for 1,400 mm material (Critical) | Transport / safety | All |
| [SWMS-11554](https://voortman.atlassian.net/browse/SWMS-11554) | CIM issue | Done | Error during tool selection in tool screen (Critical) | Drill shared | V630, V631, V633 |
| [SWMS-11536](https://voortman.atlassian.net/browse/SWMS-11536) | Story | Done | Fix two reentrant deadlocks in the PLC command/property pipeline | Cycle list | All |
| [SWMS-11501](https://voortman.atlassian.net/browse/SWMS-11501) | CIM issue | Done | Tool measurements in automatic mode | Drill V2 | V631, V633 |
| [SWMS-11147](https://voortman.atlassian.net/browse/SWMS-11147) | Salesforce | Done | Check web support in rest regardless of drill type | Drill V2 | V630, V631, V633 |
| [SWMS-11137](https://voortman.atlassian.net/browse/SWMS-11137) | Salesforce | Done | Horizontal clamp 1 and 2 not closing (release clamp cylinders of shear zone, from 4.0) | Safety | All |
| [SWMS-11130](https://voortman.atlassian.net/browse/SWMS-11130) | Salesforce | Done | Machine won't start automatic (PLC event cancel handling) | Cycle list | All |
| [SWMS-11010](https://voortman.atlassian.net/browse/SWMS-11010) | Salesforce | Done | Conveyor system malfunction (synchronising conveyors) | Transport | All |
| [SWMS-10977](https://voortman.atlassian.net/browse/SWMS-10977) | Salesforce | Done | Drill 3 prepares and waits during milling | Drill V2 | V631, V633 |
| [SWMS-10961](https://voortman.atlassian.net/browse/SWMS-10961) | Salesforce | Done | Target position blocked by Z4 axis (Z3/Y4 margin 185 to 164 mm) | Drill V2 | V631 |
| [SWMS-10787](https://voortman.atlassian.net/browse/SWMS-10787) | Salesforce | Done | Web support to rest if target position not reachable | Drill V2 | V631, V633 |
| [SWMS-10680](https://voortman.atlassian.net/browse/SWMS-10680) | CIM issue | Done | No imprints on a V633 and V631 | VACAM | V631, V633 |
| [SWMS-11363](https://voortman.atlassian.net/browse/SWMS-11363) | Salesforce | Done | Restrict any drill tool type to specific drill units | Drill shared | V630, V631, V633 |
| [SWMS-11499](https://voortman.atlassian.net/browse/SWMS-11499) | CIM issue | Done | Tools disappear from the F6 menu | Drill shared | V630, V631, V633 |
| [SWMS-11596](https://voortman.atlassian.net/browse/SWMS-11596) | CIM issue | Done | Saw overshoots maximum angle with moveable rollers | Saw shared | Saws |
| [SWMS-11589](https://voortman.atlassian.net/browse/SWMS-11589) | Story | Done | Position correction moved from MeasureUnit to Saw | Saw table / config | Saws |
| [SWMS-11678](https://voortman.atlassian.net/browse/SWMS-11678) | CIM issue | Done | Clear cut to 0 | Saw / VACAM | Saws |
| [SWMS-11057](https://voortman.atlassian.net/browse/SWMS-11057) | Salesforce | Done | SPRS handling limits and automated detection | Saw shared | Saws |
| [SWMS-11254](https://voortman.atlassian.net/browse/SWMS-11254) | Salesforce | Done | Material width incorrect | Measuring | All |
| [SWMS-11319](https://voortman.atlassian.net/browse/SWMS-11319) | CIM issue | Done | Angle in behind orientation, transverse transport detects wide material | Measuring | All |
| [SWMS-11482](https://voortman.atlassian.net/browse/SWMS-11482) | CIM issue | Done | Free length material end can be set to 10 | VACAM | All |
| [SWMS-11494](https://voortman.atlassian.net/browse/SWMS-11494) | CIM issue | Done | Stack positions disappear in buffer settings | VACAM | All |
| [SWMS-11371](https://voortman.atlassian.net/browse/SWMS-11371) | Story | Done | Scrolling through cycle list during production | VACAM | All |
| [SWMS-10779](https://voortman.atlassian.net/browse/SWMS-10779) | Story | Done | Show in VACAM which machine is the master | VACAM | All |
| [SWMS-11020](https://voortman.atlassian.net/browse/SWMS-11020) | Story | Done | Show radius in product viewer | VACAM | All |
| [SWMS-11576](https://voortman.atlassian.net/browse/SWMS-11576) | Salesforce | Done | Visual for angle cut versus straight cut | VACAM | Saws |
| [SWMS-11585](https://voortman.atlassian.net/browse/SWMS-11585) | Salesforce | Done | VACAM Office will not start up | VACAM | All |
| [SWMS-11302](https://voortman.atlassian.net/browse/SWMS-11302) | Salesforce | Done | Linearisation out of tolerance (temporary solution) | PLC core | All |
| [BT2-3694](https://voortman.atlassian.net/browse/BT2-3694) | Story | Done | Manual roller conveyor movement blocked by front-side detection | Safety / transport | All |
| [BT2-3857](https://voortman.atlassian.net/browse/BT2-3857) | Story | Done | Decouple FB_MaterialClamping from machine | Refactor / clamping | All |
| [BT2-3871](https://voortman.atlassian.net/browse/BT2-3871) | Task | Done | Cross-cutting: Drilling | Refactor | Drill lines |
| [BT2-3879](https://voortman.atlassian.net/browse/BT2-3879) | Task | Done | Remaining: Drill (incl. migration script removing MachineZone from Drill) | Refactor / config | Drill lines |
| [BT2-3891](https://voortman.atlassian.net/browse/BT2-3891) | Task | Done | DrillChanger | Refactor | Drill lines |
| [BT2-3892](https://voortman.atlassian.net/browse/BT2-3892) | Task | Done | FunctionPrepareDrillV2 + CollisionChecks | Refactor / collision | V631, V633 |
| [BT2-3874](https://voortman.atlassian.net/browse/BT2-3874) | Task | Done | SlaveMarkingDrillV2 | Refactor | V631, V633 |
| [BT2-3875](https://voortman.atlassian.net/browse/BT2-3875) | Task | Done | DataLogging | Refactor | Drill lines |
| [BT2-3876](https://voortman.atlassian.net/browse/BT2-3876) | Task | Done | GVL constant relocation | Refactor | Drill lines |
| [BT2-3872](https://voortman.atlassian.net/browse/BT2-3872) | Task | Done | Cross-cutting: Material Handling | Refactor | All |
| [BT2-3881](https://voortman.atlassian.net/browse/BT2-3881) | Task | Done | MeasureUnit (1/3): saw interface and status | Refactor | Saws |
| [BT2-3882](https://voortman.atlassian.net/browse/BT2-3882) | Task | Done | MeasureUnit (2/3): collision model, clamp pressure, safety rectangles | Refactor / safety | All |
| [BT2-3883](https://voortman.atlassian.net/browse/BT2-3883) | Task | Done | MeasureUnit (3/3): drill interface and profile measurement | Refactor | Drill lines |
| [BT2-3907](https://voortman.atlassian.net/browse/BT2-3907) | Story | Done | Solve layer violations with fbMessagesConverter | Refactor | All |
| [BT2-3834](https://voortman.atlassian.net/browse/BT2-3834) | Task | Done | PLCC implementation for MoveableScanner and PicoScan (removes PicoScan instances in DB) | Config | All |
| [BT2-3827](https://voortman.atlassian.net/browse/BT2-3827) | Bug | Done | VASIM reads machine config DB before VACAM finishes startup migration | Config | All |
| [BT2-3525](https://voortman.atlassian.net/browse/BT2-3525) | Story | Done | Correct cut positions using most relevant material measurements | VACAM / saw | Saws |
| [BT2-3566](https://voortman.atlassian.net/browse/BT2-3566) | Story | Done | Correct for actual measurement data | VACAM | All |
| [BT2-3522](https://voortman.atlassian.net/browse/BT2-3522) | Story | Done | Correct for hardcoded material translation | VACAM | All |
| [BT2-3529](https://voortman.atlassian.net/browse/BT2-3529) | Story | Done | Set default reference data | VACAM | All |
| [BT2-3569](https://voortman.atlassian.net/browse/BT2-3569) | Story | Done | Allow alternative reference planes | VACAM / saw | Saws |
| [BT2-3535](https://voortman.atlassian.net/browse/BT2-3535) | Task | Done | Refactor usage of HoleOperation.MachineView | VACAM | Drill lines |
| [BT2-3781](https://voortman.atlassian.net/browse/BT2-3781) | Story | Ready to Develop | Perform early validation | Cycle list | All |
| [BT1-2332](https://voortman.atlassian.net/browse/BT1-2332) | Bug | Done | V633M config problems with develop (external brake X only for gripper truck) | Config | V633 |
| [BT1-2271](https://voortman.atlassian.net/browse/BT1-2271) | Bug | Done | Prevent invalid min/max clamp pressure configuration in VACAM | Config / clamping | All |
| [BT1-2304](https://voortman.atlassian.net/browse/BT1-2304) | Story | Done | Transport groups can also control I_PositionControl axes | Transport | All |
| [BT1-2305](https://voortman.atlassian.net/browse/BT1-2305) | Story | Done | Transport groups can also control synchronised rollers | Transport / config | All |
| MCPL-3056, 3122, 3136, 3147, 3149, 3151, 3152, 3154, 3184, 3228, 3229, 3230, 3275 | Story/Epic | Done | Layer violation and decoupling work across Machine, MeasureUnit, MachineZone, Transport, TransportGroup, Saw and Shear | Refactor | All |

Other BT1 tickets are V912 work that touches shared files. See [[RC-4.33 Other team alerts]].

## Findings

> [!warning] Code in the RC for tickets that are not finished
> - [BT2-3781](https://voortman.atlassian.net/browse/BT2-3781) Perform early validation: Ready to Develop, 1 commit in cycle list code.
> - [BT1-2325](https://voortman.atlassian.net/browse/BT1-2325) V912 material-mover definition: In Progress, touches production command generation.
> - [BT1-2326](https://voortman.atlassian.net/browse/BT1-2326) Positioning post-processor SCENARIO_CUT: Analysis Review, 9 commits in command generators and post-processor.
> - [BT1-2232](https://voortman.atlassian.net/browse/BT1-2232) V912 safety deactivate modules: Ready to Develop, touches transverse transport.
> - [SWMS-11337](https://voortman.atlassian.net/browse/SWMS-11337): To Do, 2 commits in collision code.
> - [SWMS-11360](https://voortman.atlassian.net/browse/SWMS-11360): Canceled, but a circle measurement tool was added to the slice viewer on 2026-09-21.

- **Wrong ticket key:** commit 3d876de4a0e (2026-09-18) is tagged `BT1-11254`, which does not exist. It moves the measured width calculation to the measure roll unit and belongs to [SWMS-11254](https://voortman.atlassian.net/browse/SWMS-11254) Material width incorrect.
- **Jira cross-check not possible:** no BT1, BT2 or SWMS ticket has fixVersion `4.33.0`, so there is no Jira list to compare with the code.
- **No ticket key:** 491 of the 1,132 relevant commits have no ticket in the subject (formatting, STweep, review fixes, dependency updates).
- **Config migration added and removed:** BT1-2305 added SQL that disables MovableConveyor and V912Gripper for every machine. BT2-3827 removed it again on 2026-09-14. The net effect should be zero, but the upgrade test must confirm no object is disabled.
- **Late changes** (2026-09-17 or later, 43 commits): SWMS-11501 tool length measuring (2026-09-30), SWMS-11678 clear cut (2026-09-23), radius contour angle margin set to 0 without a ticket (2026-09-23), SWMS-11254 width (2026-09-18), MCPL-3147 machine object getters (2026-09-18), BT2-3883 MeasureUnit drill interface (2026-09-17), .NET, NLog, gRPC and Xaml.Behaviors package updates.
- **New or changed parameters:** `cDR2_V631_AbsoluteMinDistanceZ3Y4` 185 to 164 mm. V633 unit 3 collision-free range uses Xd range 300 mm, side bearing X offset 241 mm, radius 36 mm. `CheckExternalBrakeXAxis` now only TRUE when the measure unit category is GripperTruck. Clamp pressure min/max fields now block saving on invalid or negative values.

## Method

The git range was split per changed file. Each file was mapped to an area and to the machines it can affect, using path and name rules (see `_tools/rc_classify.py`). Areas got a score: impact (3 for safety, configuration and cycle list, 2 for the rest, minus 1 when only one machine is affected) times likelihood (1 to 3 by commit count and changed lines). 6 or more is High. The scores were then checked against Jira status and priority and against the diffs of the most important commits. Raw data: `_data/RC-4.33/analysis.json`.
