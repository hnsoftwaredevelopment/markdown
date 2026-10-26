---
type: story-testplan
jira: BT1-2308
title: "Manual operation of I_SynchronizedRollerConveyor rollers with TransportManager (TC)"
epic: BT2-3028
machine: [V912]
regression_machines: [V6xx, V3x0C, BeamlinesV2, V320]
version: develop (PR #22305, merge 1cb4ffaa6c3, 2026-10-22) + Voortman.TcLib.MaterialHandling PR #27
environment: VASIM
Tester: Herbert Nijkamp
created: 2026-10-23
updated: 2026-10-26
status: draft
tags:
  - testplan
  - story
  - v912
  - transportmanager
---

# Story test plan: Manual operation of I_SynchronizedRollerConveyor rollers with TransportManager

## 1. Ticket and context

- **Jira:** [BT1-2308](https://voortman.atlassian.net/browse/BT1-2308), epic [BT2-3028](https://voortman.atlassian.net/browse/BT2-3028) "V912 - Position material for cutting". Status In Test, assigned to Herbert.
- **Design:** [V912 Material movement TC, section "Manual operation of rollers with TransportManager"](https://voortman.atlassian.net/wiki/spaces/~55705855f7692928c245cd8245ab1680a4578b/pages/1743060993/V912+Material+movement+TC#Manual-operation-of-rollers-with-TransportManager) (Andre Holtschlag).
- **Goal:** the operator can jog the rollers of the V912 movable conveyor (Rc1, `FB_MovableConveyor`) with the normal TransportManager conveyor buttons, the same way as the old `FB_Conveyor` roller conveyors (Rc2, Rc3).
- **The ticket itself has no acceptance criteria** (template not filled in). The criteria below are derived from the design page and the code.

### Related tickets

| Ticket | Summary | Status | Relation to this test |
| --- | --- | --- | --- |
| BT1-2304 | Transport groups can control axis of type `I_PositionControl` | Done | Same TransportGroup refactor area |
| BT1-2305 | Transport groups can control rollers that implement `I_SynchronizedRollerConveyor` | Done | Created the interface array on the machine. Floris' comment: VASIM objects are disabled on first start, enable and restart VACAM without deleting the DB |
| BT1-2307 | Synchronize rollers of movable conveyor with Xc | Done | Rollers compensate when Xc moves. Interacts with manual jog (TC-07) |
| BT1-2309 | `TransportGroupRollers` with Digitax M753 open loop | Done | Rc2/Rc3 drive type on V912 |
| BT1-2337 | Xc and Xg stop 1 mm before absolute target | open | Known VASIM/CNC issue, not a finding for this story |
| MCPL-3311, MCPL-3314 | Conveyor registration / Conveyor | Rejected (duplicate) | None |

Comments on BT1-2308: Maurice asked Floris to test; Floris: "see if all pointers in the TransportManager can be converted to interfaces". That is what was built.

### What changed (code, `origin/develop`, PR #22305)

**PLC (TransportManager)**

- The 20 pointers `pConveyorInfeed1..10` and `pConveyorOutfeed1..10` (`POINTER TO FB_Conveyor`) are replaced by two arrays `arrRollerConveyorInfeed[1..10]` and `arrRollerConveyorOutfeed[1..10]` of `I_SynchronizedRollerConveyor`. Empty slots hold `fbNullSynchronizedRollerConveyor`. New constant `GVL_TransportManager.cMaxRollerConveyors = 10`.
- `TM_MoveInfeedRC` / `TM_MoveOutfeedRC` now use the interface: `Yoffset`, `XoffsetFirstRoller`, `XoffsetLastRoller`, `MaxSpeed`, `IgnoreXAxisHalt`, `MoveVelocity(...)`. "Not configured" checks use `IsNull()` instead of `F_PointerDefined`.
- **Behaviour change in stop logic** (commit "Only stop conveyors that are not selected for moving"). Before: every scan all 20 conveyors got `CV_StopMoveVelocity`, then the selected ones got `CV_MoveVelocity`. Now: both move functions return a bit word of the conveyors they moved. Main TM request and the separate operator panel requests are OR-ed. Only conveyors whose bit is not set get `StopMoveVelocity`.
- The second (older) TM update path still stops infeed 1-3 and outfeed 1-6 first and then moves, now via the interface.
- The X+/X- button path (`TM_GetButtonXPositiveActive`) jogs `arrRollerConveyorInfeed[1]` via the interface.
- `TM_TestMoveRequestPermitted`: section 1 fallback (only conveyor 1 configured) now checks `IsNull()` of slot 2 and 3.

**VACAM (.NET)**

- `TransportManagerContainer.cs`: properties renamed to `RollerConveyorInfeed1..10` / `RollerConveyorOutfeed1..10`, type is now a reference to `I_SynchronizedRollerConveyor`. Display names "Roller conveyor infeed section 01..10" and "Roller conveyor outfeed 01..10" (leading zero for sorting). Availability per machine type unchanged: section 1 for V6xx, V3x0C, BeamlinesV2 (+ V320 for infeed 1); others mostly V6xx and BeamlinesV2.
- `ConveyorContainer` now declares `I_RollerConveyor`; `MovableConveyorContainer` declares `I_SynchronizedRollerConveyor`. New extends relation: `I_RollerConveyor` extends `I_SynchronizedRollerConveyor`, which extends `I_Nullable`.
- `PlcPointerControl.GetInterfaceOffsets` now uses `GetImplementedInterfaces()`. **This is generic code**: it resolves interface offsets for every object with interface references, on every machine.
- DB migration in `MC_BranchScript.sql` (ClassID 39 TransportManager): rename `ConveyorInfeedN`/`ConveyorOutfeedN` to `RollerConveyorInfeedN`/`RollerConveyorOutfeedN`. If the new name already exists, the old value is deleted. The stored ObjectID stays the same.

**Not changed:** the TcUnit/UnitTest `.tsproj` files still list the old `pConveyorInfeed*` symbols (stale mappings, outside manual test scope; mention to Andre).

### What changed in the library (Voortman.TcLib.MaterialHandling PR #27)

[PR #27 "BT1-2308 Handle move velocity via I_SynchronizedRollerConveyor"](https://github.com/voortman-steel-machinery/Voortman.TcLib.MaterialHandling/pull/27), Andre Holtschlag. Checked on 2026-10-26: the commits are only on branch `BT1-2308_Manual_operation_TM_AH`, not yet on the library main. vacam-twincat develop already calls the new methods.

- `I_SynchronizedRollerConveyor` gets `MoveVelocity(inCallerId, inTargetVelocityPercentage, inRequestFromTransportManager)`, `StopMoveVelocity(inCallerID, inRequestFromTransportManager)` and property `IgnoreXAxisHalt`.
- `FB_Conveyor`: three wrappers only. `MoveVelocity` calls `CV_MoveVelocity`, `StopMoveVelocity` calls `CV_StopMoveVelocity`, `IgnoreXAxisHalt` calls `CV_GetIgnoreXAxisHalt`. No change to conveyor logic.
- `FB_MovableConveyor`:
  - `MoveVelocity`: if the rollers steering is already active for another caller, the call is ignored. Velocity = `inTargetVelocityPercentage / 100 * fMaximumVelocityRollers`. Calls `JogRollers`.
  - `StopMoveVelocity`: only acts when caller ID matches **and** the request source (TM or not) matches the one that started the jog. Calls `JogRollers` with `inCancel := TRUE`.
  - `JogRollers`: new early return "do not start new movement if `inCancel`", and stores `CallerId` when the steering starts. `JogRollers` is also the VACAM proxy command for manual roller jog.
  - `Update`: `CallerId` is cleared when **any** state machine ends with ready or error (also positioning and synchronize).
  - `IgnoreXAxisHalt` = TRUE when the Y-offset is not 0.
- Null objects get empty implementations.

### Derived acceptance criteria

- AC1: In VACAM the TransportManager can reference the movable conveyor (Rc1) as an infeed or outfeed roller conveyor section.
- AC2: With the TM conveyor buttons the operator can jog Rc1 forward and backward, at normal and fast speed, and it stops on release.
- AC3: Rc1 can be jogged together with `FB_Conveyor` sections (Rc2, Rc3), with the same speed limiting as before.
- AC4: Manual movement of Rc1 respects the same permission rules as other roller conveyors (`AllowManualMovementConveyors`, X-axis halt, safety, automatic ownership).
- AC5: Existing machines keep their conveyor configuration after update and jog exactly as before.

## 2. Machine scope

### Impact analysis: who uses `I_SynchronizedRollerConveyor`

Checked against library branch PR #27 and vacam-twincat `origin/develop` (aca89fd15f9, 2026-10-26).

| Implementation | Via | Instantiated on |
| --- | --- | --- |
| `FB_MovableConveyor` | direct | V912 only (`MachineObjectsArray.TcGVL`, `MovableConveyor : ARRAY[0..1]`) |
| `FB_Conveyor` | `I_RollerConveyor` extends `I_SynchronizedRollerConveyor` | Almost every machine (`Conveyor : ARRAY[0..cMaxConveyor]`) |
| `FB_NullRollerConveyor`, `FB_NullSynchronizedRollerConveyor` | null objects | Empty slots |

Only caller of `MoveVelocity`, `StopMoveVelocity` and `IgnoreXAxisHalt` on the interface: the TransportManager (`TM_MoveInfeedRC`, `TM_MoveOutfeedRC`, `TM_Update`). Transport groups in the library do not call them. So an `FB_Conveyor` is only affected when it is assigned to a TM slot "Roller conveyor infeed/outfeed 01..10". VACAM offers those slots only for these TM types:

| TM type | Machines | Slots |
| --- | --- | --- |
| V6xx | V630, V631, V633 | infeed + outfeed 1-10 |
| BeamlinesV2 | V807, LES, probe truck lines | infeed + outfeed 1-10 |
| V3x0C | code comment: "not used anymore, use V320" | infeed 1-2, outfeed 1 |
| V320 | V320 | infeed 1 only (also X+/X- buttons) |

Other TM types (V5xx, VCS, V550_6, V3xx, V302, V310, V325, PlateMachine) and saws cannot assign roller conveyors to the TM: no effect from PR #27.

Conclusion: the real behaviour change of PR #27 is on V912 only. Regression on V6xx/BeamlinesV2/V320 is still needed, mainly because of the TM refactor and stop logic in PR #22305. The enum `TransportManager.SubCategory` has no V912 value (see R7).

### Scope per machine

| Machine type (TM SubCategory) | In scope | Why | Where |
| --- | --- | --- | --- |
| V912 | Full | Target of the story, only machine with `FB_MovableConveyor` | VASIM |
| V6xx (V630, V631, V633) | Regression | Uses up to 10 infeed / 10 outfeed conveyor references | VASIM |
| BeamlinesV2 (V807, LES, Probe truck lines) | Regression | Uses multiple sections and the speed factor code (`TransportManagerType_BeamlineV2`) | VASIM |
| V3x0C | Regression | Infeed 1-2, outfeed 1 | VASIM |
| V320 | Regression | Infeed 1 only, older TM update path, X+/X- button jog | VASIM |
| Saws, other machines without TM conveyor references | Smoke | Only affected by `PlcPointerControl` change | VASIM, start + log check |

## 3. Risks

Scale: impact (I) and likelihood (L) 1 to 3, score = I x L. Test depth follows the score.

| # | Risk | I | L | Score | How to test |
| --- | --- | --- | --- | --- | --- |
| R1 | **Regression on all machines with TM conveyors.** 20 pointer references became interface array slots in every TM function. A wrong index, a swapped infeed/outfeed slot or a missed property (`IgnoreXAxisHalt`, `MaxSpeed`, offsets) makes the wrong conveyor move or none at all. | 3 | 2 | 6 | TC-11, TC-12, section 6 regression |
| R2 | **Stop logic changed.** Conveyors are no longer stopped every scan. A conveyor can keep running when: the selection changes during a jog, the permission drops during a jog, a second operator panel with separate control stops, or the request word goes to 0 in a path that skips the stop loop. | 3 | 2 | 6 | TC-04, TC-05, TC-06, TC-10 |
| R3 | **DB migration.** Existing configs lose their conveyor links after update, or links point to another object. Edge case: both old and new name exist (old one deleted). | 3 | 2 | 6 | TC-13 |
| R4 | **Generic `PlcPointerControl` change.** Interface offsets are resolved differently for every object with interface references. A wrong offset gives a wrong or null reference somewhere outside the TM. Two commits on 2026-10-22 went back and forth on this code ("Fix use of extended interfaces", then "Change during testing"). | 3 | 2 | 6 | TC-01 log check on every regression machine, section 6 smoke |
| R5 | **Movable conveyor roller area is dynamic.** `XoffsetFirstRoller`/`XoffsetLastRoller` depend on the actual Xc position. During a final automatic list with measure rollers, `MA_AllowManualMovementConveyors` returns `NOT MA_MaterialInRollerArea(...)`. Wrong offsets allow jogging under material that the gripper or measure unit holds, or block jogging when it should be free. | 3 | 2 | 6 | TC-08 |
| R6 | **Conflict between TM jog and Xc compensation (BT1-2307) or transport group claims (BT1-2305).** Two callers write a velocity to the same roller axis. | 2 | 2 | 4 | TC-07, TC-09 |
| R7 | **Property not visible for V912.** Availability is limited to V6xx/V3x0C/BeamlinesV2/V320. If the V912 TM uses another SubCategory, the new reference cannot be set in VACAM. Confirmed 2026-10-26: `TransportManager.SubCategory` has no V912 value. | 2 | 3 | 6 | TC-01 |
| R8 | **Speed factor with mixed conveyors** (BeamlineV2 only): all selected sections are scaled to the slowest `MaxSpeed`. If Rc1 reports `MaxSpeed` in other units or 0, the speed of the mix is wrong. | 2 | 1 | 2 | TC-03 |
| R9 | Display names changed ("01".."10", "Roller conveyor ..."). Service documentation and screenshots are outdated. | 1 | 3 | 3 | TC-01, note in findings |
| R10 | **`CallerId` handling in `FB_MovableConveyor` (PR #27).** `CallerId` is cleared when any steering ends, and `StopMoveVelocity` only stops when caller and source match. A VACAM jog and a TM jog, or a jog followed by positioning/synchronize, can leave the rollers running or block a new start. | 3 | 2 | 6 | TC-14 |

## 4. VASIM setup

1. Build: develop at or after merge `1cb4ffaa6c3` (2026-10-22). Check the MaterialHandling library version that came with "Update MaterialHandling library" (`9bc22a83df7`), and ask Andre which library build contains PR #27 (not yet on library main on 2026-10-26).
2. Load the V912 VASIM configuration. Start VACAM once. Enable `V912Gripper` and `MovableConveyor` (they start disabled, see BT1-2305). Restart VACAM **without** deleting the database.
3. In VACAM, TransportManager object: write down the current values of all "Roller conveyor infeed section 01..10" and "Roller conveyor outfeed 01..10".
4. Assign `MovableConveyor` (Rc1) to a free outfeed slot. Pick the slot that matches the physical position on the V912 and the operator panel selection button. Note which selection button belongs to that slot:

   | Slot | Request bit | Condition |
   | --- | --- | --- |
   | 1 | .10 (section 1) | also moves when slot 2 and 3 are empty |
   | 2 | .11 | |
   | 3 | .12 | |
   | 4-6 | .13-.15 | only with `bSeparateRollerConveyorSelectionFromSel4` |
   | 7-10 | .4-.7 | only with `bSeparateRollerConveyorSelectionFromSel4` |

5. **Online watch list** (TwinCAT): `TransportManager.arrRollerConveyorOutfeed[1..10]` (IsNull, MaxSpeed, XoffsetFirstRoller, XoffsetLastRoller), `nMoveOutfeedConveyor`/`nMoveInfeedConveyor` in `TM_Update`, MovableConveyor `iRollerAxis` target and actual velocity, `iMovableConveyorAxis` position, `CallerId`, `bJogRequestFromTransportManager`, Rc2/Rc3 conveyor velocity.
6. Known VASIM limits: SAI actual velocity always shows +100 or -100 (reported to Platform, see BT1-2307). Check the target velocity instead. Xc and Xg stop 1 mm before target (BT1-2337).

## 5. Test cases (V912, VASIM)

### TC-BT1-2308-01 Configuration and references (AC1, R4, R7, R9)

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Open TransportManager properties in VACAM | Properties "Roller conveyor infeed section 01..10" and "Roller conveyor outfeed 01..10" visible, sorted 01 to 10. No old "Conveyor infeed section N" properties | |
| 2 | Open the selection list of an outfeed slot | List shows the `FB_Conveyor` objects (Rc2, Rc3) and `MovableConveyor`. No unrelated object types | |
| 3 | Assign MovableConveyor, save, restart VACAM | Value is kept after restart | |
| 4 | Check VACAM log after start | No warning "declared the following interfaces, which are not used for references", no reference or offset errors | |
| 5 | Check online: `arrRollerConveyorOutfeed[slot]` | Not null, points to MovableConveyor, `MaxSpeed` and offsets have plausible values | |

If step 1 shows no roller conveyor properties for the V912: R7 is real, report to Andre (V912 TM SubCategory not in `AvailableFor`).

- result:: open

### TC-BT1-2308-02 Jog Rc1 forward and backward (AC2)

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Manual mode, no material. Select Rc1 section, hold "forward" | Rc1 rollers rotate in material direction (outfeed side), target velocity matches normal jog speed | |
| 2 | Release | Rollers stop within one scan cycle, target velocity 0 | |
| 3 | Hold "backward" | Rollers rotate in opposite direction | |
| 4 | Hold "fast" + forward / backward | Higher speed, same direction | |
| 5 | Repeat with Xc at minimum, middle and maximum position | Same behaviour at every Xc position | |

- result:: open

### TC-BT1-2308-03 Jog Rc1 together with Rc2 and Rc3 (AC3, R8)

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Select Rc1, Rc2 and Rc3, jog forward | All three move in the same direction | |
| 2 | Compare target velocities | Same linear speed for all three. On a BeamlineV2 type TM: all scaled to the slowest `MaxSpeed` | |
| 3 | Same with only Rc2 + Rc3 (Rc1 not selected) | Rc1 stays at 0 | |

- result:: open

### TC-BT1-2308-04 Release one section during a combined jog (R2)

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Jog Rc1 + Rc2 forward, deselect Rc1 while holding forward | Rc1 stops, Rc2 keeps moving | |
| 2 | Select Rc1 again while holding | Rc1 starts again without jerk or error | |
| 3 | Same with Rc2 deselected | Rc2 stops, Rc1 keeps moving | |

- result:: open

### TC-BT1-2308-05 Change selection during jog (R2)

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Jog Rc2 forward, switch selection to Rc1 while holding | Rc2 stops, Rc1 starts | |
| 2 | Switch from outfeed to infeed while holding | Outfeed conveyors stop | |
| 3 | Quickly switch forward/backward 10 times | Direction follows the button, no conveyor keeps running after release | |

- result:: open

### TC-BT1-2308-06 Stop conditions during jog (R2, AC4)

| # | Variation while Rc1 is jogging | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Stop command from VACAM | Rc1 stops, no command error message (`bJogCommandConverorStopped`) | |
| 2 | E-stop | Rc1 stops. After reset: does not restart without a new jog command | |
| 3 | Open RC door / operator door | Rc1 stops. After close + reset: no restart | |
| 4 | X-axis halt active (outfeed, `bCheckIgnoreXAxisHalt`) | Rc1 stops when its Y-offset is 0. With a Y-offset other than 0, `IgnoreXAxisHalt` is TRUE and Rc1 keeps moving | |
| 5 | Disable the MovableConveyor object | Rc1 stops, TM jog of that section does nothing, no PLC exception | |

- result:: open

### TC-BT1-2308-07 Jog Rc1 while Xc moves (R6, BT1-2307)

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Material on Rc1. Jog Xc positive (own manual control), do not jog rollers | Rollers compensate opposite to Xc (BT1-2307 scenario 3) | |
| 2 | Jog Rc1 rollers forward via TM, at the same time jog Xc in the same direction | Roller velocity lower (material speed minus Xc speed) | |
| 3 | Same with Xc in opposite direction | Roller velocity higher, limited by roller max speed | |
| 4 | Release TM jog while Xc still moves | Rollers go back to pure compensation, no stop-then-jump | |

- result:: open

### TC-BT1-2308-08 Manual jog blocked when material is in the roller area (R5, AC4)

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Start a V912 job (final list). Let the job stop with material lying on Rc1 (gripper or measure rollers hold it) | | |
| 2 | Try to jog Rc1 via TM | No movement, same refusal/message as an `FB_Conveyor` under material | |
| 3 | Move Xc so the rollers are no longer under the material (if possible within limits) | Jog of Rc1 now allowed | |
| 4 | Move Xc back under the material | Jog refused again | |
| 5 | Same check for Rc2 | Unchanged behaviour compared to before the merge | |

- result:: open

### TC-BT1-2308-09 Automatic ownership (R6)

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | During automatic transport the transport group synchronizes Rc1 (BT1-2305). Press TM jog for Rc1 | TM jog does not override the transport group, no velocity fight on the roller axis | |
| 2 | After the transport group releases Rc1 | TM jog works again | |

- result:: open

### TC-BT1-2308-10 Two control sources at the same time (R2)

Only if the V912 VASIM config has a second operator panel or a remote control with separate RC control.

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Panel A jogs Rc1, panel B (separate control) jogs Rc2 | Both move | |
| 2 | Release panel B | Rc2 stops, Rc1 keeps moving | |
| 3 | Release panel A | Rc1 stops | |

- result:: open

### TC-BT1-2308-11 Section 1 fallback and empty slots (R1)

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Put MovableConveyor in outfeed slot 1, empty slot 2 and 3. Jog with any section selection | Rc1 moves (fallback "only 1 conveyor configured") | |
| 2 | Select a section whose slot is empty | Nothing moves, no error, no PLC exception | |
| 3 | Put MovableConveyor in an infeed slot | Jog works the same way on infeed | |
| 4 | Restore the original V912 configuration | | |

- result:: open

### TC-BT1-2308-12 Same object in two slots (negative)

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Assign MovableConveyor to two outfeed slots, select only one | Note behaviour. The stop loop stops the unselected slot, which is the same object: check that Rc1 does not stutter between move and stop | |

Not a normal configuration. A stutter here is a low priority finding, but it shows how the new stop loop behaves.

- result:: open

### TC-BT1-2308-13 Upgrade of an existing database (R3, AC5)

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Take a VASIM DB from a build before 2026-10-22 with several conveyor links (V6xx config with infeed and outfeed sections) | Write down all `ConveyorInfeedN`/`ConveyorOutfeedN` values | |
| 2 | Start the new build on that DB | Branch script runs without error | |
| 3 | Check TM properties | Every link is now under `RollerConveyorInfeedN`/`RollerConveyorOutfeedN` with the same object | |
| 4 | Jog every configured section | Each selection moves the same conveyor as before the update | |
| 5 | Run the update a second time (restart) | No changes, no duplicates | |

- result:: open

### TC-BT1-2308-14 Caller ID and jog source on the movable conveyor (R10)

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Start a roller jog from VACAM (JogRollers command). While it runs, press TM jog for Rc1 | TM jog is ignored, VACAM jog continues. Watch `CallerId` | |
| 2 | Stop the VACAM jog | Rollers stop, `CallerId` is empty | |
| 3 | Start TM jog, then send a VACAM jog command for the rollers | VACAM command does not take over, TM jog continues | |
| 4 | Release the TM button | Rollers stop (TM stop with matching caller and source) | |
| 5 | Jog via TM, release, then directly position Xc (PositionMovableConveyorAxis) | Positioning works, rollers do not restart | |
| 6 | During Xc positioning press TM jog for Rc1, release after positioning ends | Rollers stop on release, no rollers left running | |

- result:: open

### Exploratory charter (45 min)

Explore TM jog of Rc1 combined with Xc jog, gripper Xg moves, VACAM roller jog, door and E-stop events and selection changes, to find a sequence where a roller conveyor keeps running after the operator released the button, or where Rc1 moves while material is in its roller area.

- result:: open

## 6. Regression on other machines (VASIM)

For each machine: open TM properties (names and values after update), check VACAM log for reference/offset warnings, jog every configured infeed and outfeed section forward/backward/fast, release, change selection during jog, E-stop during jog, run one standard job with transport.

PR #27 only adds wrappers to `FB_Conveyor`, so on these machines the risk comes from the TM refactor (PR #22305), not from the library change.

| Machine (VASIM config) | TM type | Extra focus | Result |
| --- | --- | --- | --- |
| V630 / V631 / V633 (V6xx) | V6xx | Sections 4-10 with `bSeparateRollerConveyorSelectionFromSel4`, separate operator panel control | |
| V807 / LES / Probe truck line | BeamlinesV2 | Speed factor with mixed `MaxSpeed`, outfeed `IgnoreXAxisHalt` | |
| V3x0C | V3x0C | Infeed 1-2, outfeed 1, section 1 fallback. Only if a VASIM config still exists (type marked "not used anymore") | |
| V320 | V320 | Infeed 1 only, X+/X- button jog of infeed 1, older TM update path | |
| Saw (VB Standard) and one machine without TM conveyors | - | Start, log check only (`PlcPointerControl`) | |

## 7. Findings

| # | Finding | Machine | Jira | Severity | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Ticket has no acceptance criteria or test plan filled in; criteria in this plan are derived from design + code | - | BT1-2308 | Low | open |
| 2 | UnitTest/TcUnit `.tsproj` files still map old `pConveyorInfeed*`/`pConveyorOutfeed*` symbols | - | ask Andre | Low | open |
| 3 | Property display names changed, service docs may show old names | all TM machines | - | Low | open |
| 4 | `TransportManager.SubCategory` has no V912 value; roller conveyor slots are only available for V6xx, V3x0C, BeamlinesV2, V320 | V912 | ask Andre | Medium | open |
| 5 | Library PR #27 not yet merged to library main (2026-10-26), while vacam-twincat develop already calls the new interface methods | - | ask Andre | Medium | open |

## 8. Close

- [ ] TC-01 to TC-14 executed on V912 in VASIM.
- [ ] Regression section 6 passed on V6xx, BeamlinesV2, V3x0C and V320.
- [ ] Upgrade test TC-13 passed on at least one existing database.
- [ ] Open question for Andre: is a test on the real V912 planned (open loop M753 drives, real roller inertia)?
- [ ] Open question for Andre: which library build contains PR #27, and which TM type does the V912 use?

**Verdict:** Passed / Passed with remarks / Failed
**Signed off by:** Herbert
**Date:**
