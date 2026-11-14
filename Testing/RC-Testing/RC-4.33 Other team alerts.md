---
rc: "4.33"
branch: RC-4.33.0
rc_commit: ed77b6064c4
rc_commit_date: 2026-10-01
baseline: 4.32.17
analysed: 2026-10-02
team: BT1
tags: [rc-testing, rc-4-33, other-team-alerts]
---

# RC-4.33 Other team alerts

Related: [[RC-4.33 Analysis]] · [[RC-4.33 Testplan]] · [[RC-4.33 Test cases]]

BT1 (Beam Team 1) changes in RC-4.33.0 that can change behaviour on machines outside your test set. Use this note to warn the testers or product owners of those machines.

## Summary

- 22 BT1 tickets have code in `4.32.17..RC-4.33.0`. One more commit uses the key `BT1-11254`, which does not exist (it belongs to SWMS-11254).
- Most BT1 work in this RC is V912 outfeed gripper, movable conveyor and material control. 17 tickets touch V912 files, 15 of them are V912 feature work.
- 7 tickets touch files of other machine types directly: V623, V807/V808, plate machines with a moveable scanner, and transverse transport.
- 18 tickets, plus the BT1-11254 commit, also change shared code that every machine type runs: transport groups, the measuring unit and measure roll unit, machine zone safety, the object registry and the config migration script.
- 4 tickets with code in the RC are not finished in Jira: BT1-2325 (In Progress), BT1-2326 (Analysis Review), BT1-2232 (Ready to Develop), and the invalid BT1-11254.

> [!danger] Highest alerts
> 1. **Transport groups** (BT1-2304, BT1-2305, BT1-2243): new axis and roller types in `FB_TransportGroup`, `TG_Update` and `TG_SynchronizeConveyorsX`. Every line with a transport group (V623, V912, VCT lines) should retest conveyor synchronisation and transport group stop.
> 2. **Measuring unit and measure roll unit** (BT1-2241, BT1-2305, BT1-2306, BT1-2340, BT1-2392): `MU_Update`, `FB_MeasureUnit`, `MU_MoveVelocityX`, `E_MU_State`, `MU_CorrectionMeasureWheel`, `MU_CalculateClampPressure` and both collision models changed. Every beam line with a measuring unit is affected.
> 3. **Config migration** (BT1-2208, BT1-2241, BT1-2244, BT1-2305): `MC_BranchScript.sql` runs on every machine at upgrade. BT1-2305 added a script that disabled MovableConveyor and V912Gripper. BT2-3827 removed it on 2026-09-14. Every upgrade test should confirm no object ends up disabled.

## Direct impact on other machines

| Machine | Ticket | Status | What changed | Files |
|---|---|---|---|---|
| V623 | [BT1-2244](https://voortman.atlassian.net/browse/BT1-2244) Release material with outfeed gripper | Done | Motor drive reset logic and a migration script step | `FB_ResetMotorDrive.TcPOU`, `MC_BranchScript.sql` |
| V623 | [BT1-2325](https://voortman.atlassian.net/browse/BT1-2325) V912 material-mover machine definition | **In Progress** | V623 machine state and schedule request factory adapted for the new material mover | `V623MachineState.cs`, `V623ScheduleRequestFactory.cs` |
| V807 / V808 | [BT1-2326](https://voortman.atlassian.net/browse/BT1-2326) Positioning post-processor SCENARIO_CUT | **Analysis Review** | Profile cutter command generation and V807 3D view changed, plus the shared post-processor | `ProfileCutterCommandGenerator.cs`, `V807ViewModel3D.cs`, `PostProcessor.cs` |
| V807 / V808, V912 | [BT1-2293](https://voortman.atlassian.net/browse/BT1-2293) Start from safe position for profile scan | Done | Manipulator moves to a safe position before a profile scan restart | `SafeManipulatorMotionWhenRestarting.cs` |
| Plate machines with moveable scanner | [BT1-2229](https://voortman.atlassian.net/browse/BT1-2229) V912 safety: person detection (Vasim) | Done | Moveable scanner function block changed for person detection | `FB_MoveableScanner.TcPOU` |
| Lines with transverse transport (VCT) | [BT1-2232](https://voortman.atlassian.net/browse/BT1-2232) V912 safety: deactivate modules | **Ready to Develop** | Transverse transport update and configuration check changed | `TT_Update.TcPOU`, `TT_ConfigurationOK.TcPOU` |
| Lines with transverse transport, V633 | [BT1-2332](https://voortman.atlassian.net/browse/BT1-2332) V633M config problems | Done | Transverse transport config check, and `CheckExternalBrakeXAxis` only for gripper truck measuring units | `TT_ConfigurationOK.TcPOU`, `FB_MachineHardCodedConfigurations.TcPOU` |

### V912 (BT1's own machine)

Listed for completeness. BT1 tests these on the V912.

| Ticket | Status | Summary |
|---|---|---|
| [BT1-2207](https://voortman.atlassian.net/browse/BT1-2207) | Done | State machines for go-to-rest and reference run of the outfeed gripper |
| [BT1-2208](https://voortman.atlassian.net/browse/BT1-2208) | Done | Manual operation of outfeed gripper and conveyor (TwinCAT) |
| [BT1-2209](https://voortman.atlassian.net/browse/BT1-2209) | Done | Manual operation of outfeed gripper and conveyor (.NET) |
| [BT1-2241](https://voortman.atlassian.net/browse/BT1-2241) | Done | Take over with outfeed gripper |
| [BT1-2243](https://voortman.atlassian.net/browse/BT1-2243) | Done | Move material with outfeed gripper |
| [BT1-2303](https://voortman.atlassian.net/browse/BT1-2303) | Done | Z-axis goes out of positive limit during ScanProfile (Critical) |
| [BT1-2304](https://voortman.atlassian.net/browse/BT1-2304) | Done | Transport groups control I_PositionControl axes |
| [BT1-2305](https://voortman.atlassian.net/browse/BT1-2305) | Done | Transport groups control synchronised rollers |
| [BT1-2306](https://voortman.atlassian.net/browse/BT1-2306) | Done | Synchronise measure roll unit drive wheel with outfeed gripper X |
| [BT1-2307](https://voortman.atlassian.net/browse/BT1-2307) | Done | Synchronise movable conveyor rollers with its X-axis |
| [BT1-2340](https://voortman.atlassian.net/browse/BT1-2340) | Done | Outfeed gripper clamp pressure per profile type |
| [BT1-2392](https://voortman.atlassian.net/browse/BT1-2392) | Done | Clone of BT1-2306 |
| [BT1-2395](https://voortman.atlassian.net/browse/BT1-2395) | Done | Missing state machine for fbZeroLineClamp |
| [BT1-2398](https://voortman.atlassian.net/browse/BT1-2398) | Done | Move movable conveyor via V912MaterialControl |
| [BT1-2325](https://voortman.atlassian.net/browse/BT1-2325) | In Progress | Material-mover machine definition (.NET) |

## Shared code changed by BT1

These files run on every machine type, including the ones you do not test.

| Shared area | Tickets | Files | Who should look at it |
|---|---|---|---|
| Transport groups | BT1-2243, BT1-2304, BT1-2305 | `FB_TransportGroup`, `TG_Update`, `TG_SynchronizeConveyorsX`, `FB_XAxisPositioner`, `TransportGroup.TcGVL` | V623, V912 and VCT line testers |
| Measuring unit / measure roll unit | BT1-2241, BT1-2305, BT1-2306, BT1-2340, BT1-2392 | `MU_Update`, `FB_MeasureUnit`, `MU_MoveVelocityX`, `E_MU_State`, `MU_CorrectionMeasureWheel`, `MU_CalculateClampPressure`, `MU_GetPressureHorizontalClampOnMaterial`, `I_MeasureRollUnitData` | All beam line testers |
| Measuring collision models | BT1-2306, BT1-2340, BT1-2392 | `FB_MeasureUnitCollisionModel`, `FB_MeasureRollUnitCollisionModel` | All beam line testers |
| Machine zone and safety | BT1-2207, BT1-2208 | `MZ_Safety`, `FB_MachineZone`, `MZ_Update`, `FB_Machine` | All testers |
| Object registry and configurators | BT1-2241, BT1-2305, BT1-2306, BT1-2307, BT1-2398 | `E_ObjectType`, `ObjectID_TO_ADR`, `MachineObjectsArray`, `FB_LibraryConfigurator`, `FB_ModuleConfigurator`, `FB_MaterialHandlingAdapter`, `FB_MachineZoneGroupAdapter` | All testers (startup and object initialisation) |
| Command execution | BT1-2207, BT1-2241 | `CMD_Execute` | All testers |
| Config migration | BT1-2208, BT1-2241, BT1-2244, BT1-2305 | `MC_BranchScript.sql` | All testers doing an upgrade test |
| Clamp pressure settings screen | BT1-2271 | `ClampPressureSettingsView.xaml` and view models | All testers |
| Measured width | commit 3d876de4a0e tagged BT1-11254 | `MR_GetMeasuredWidth`, `MU_Update` | All beam line testers |
| .NET command generation and post-processor | BT1-2325, BT1-2326 (both unfinished) | `ProductionCommandsGenerator`, `AutomaticListBuilder`, `PostProcessor`, `ExecutionFrameworkAdapter` | All testers on machines that use the execution framework |

## Impact on your own machines

BT1 changes that also hit your test set. They are covered in [[RC-4.33 Test cases]]:

- BT1-2332 V633 X-axis brake check: TC-433-008
- BT1-2271 clamp pressure validation: TC-433-003
- BT1-2304 and BT1-2305 transport groups: TC-433-023
- BT1-2305 migration script (removed again by BT2-3827): TC-433-001 and 002
- measuring unit changes and measured width: TC-433-005, 022

## Suggested messages

- **V623 testers:** BT1-2244 and BT1-2325 touch V623 files. BT1-2325 is still In Progress. Retest material release, motor drive reset and scheduling.
- **V807/V808 testers:** BT1-2326 changes profile cutter command generation and is in Analysis Review, so the code may change again. BT1-2293 changes the restart motion before a profile scan.
- **Plate machine testers:** BT1-2229 changes `FB_MoveableScanner`. Retest person detection and scanner moves.
- **VCT and transverse transport testers:** BT1-2232 (Ready to Develop) and BT1-2332 change transverse transport configuration checks.
- **All testers:** run the upgrade test and confirm no machine object is disabled after the migration.

## Method

All commits in the range with a BT1 key in the subject were taken. Each changed file was mapped to a machine type with path rules, for example `V623`, `V807`, `MoveableScanner` or `TranverseTransport` in the path. Files in shared PLC or VACAM code count as "shared". Unit tests, docs and workflows were skipped. Raw data: `_data/RC-4.33/analysis.json`, key `bt1_alerts`.
