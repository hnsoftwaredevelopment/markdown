---
type: swms-testplan
jira: SWMS-11157
title: "Preventable case where tools can fall out the tool changer"
customer: "11890 Hall & Pickles 1812 Limited"
machine: [V631]
machine_config: "DrillChangerType_AirCylinder8Pos (8 position air cylinder tool changer)"
reported_version: 4.11.x (V631), also seen on V630-MK2 with 4.11.33.16
fixed_version: 4.11.36
reproducible: yes
Tester: Herbert Nijkamp
created: 2026-10-08
status: draft
tags:
  - testplan
  - swms
---

# SWMS test plan: Preventable case where tools can fall out the tool changer

## 1. Ticket

- **Jira:** [SWMS-11157](https://voortman.atlassian.net/browse/SWMS-11157) (CIM 52265, SLA 2026-10-01, sprint BT1 231)
- **Customer and site:** 11890 Hall & Pickles 1812 Limited, machine 20250149, normal production
- **Machine and configuration:** V631, tool changer type `DrillChangerType_AirCylinder8Pos`
- **Version at the customer:** VACAM 4.11.x. Bruce Lubberdink saw the same on a V630-MK2 with 4.11.33.16.
- **Problem as reported:** after opening and closing the doors, or after a startup, the operator presses "Get tool" before Start. The drill unit (DU) moves to the tool change position, but the tool changer stays in. After a few seconds a timeout "tool changer not out" follows. If the operator presses Start between the request and the timeout, the tool changer shoots out and tools fall out.
- **Impact for the customer:** tools fall out of the changer (tool damage, possible damage to holders and machine, risk for the operator during recovery). Workaround: always press Start before a manual tool change.

### Root cause (code, `origin/Develop-4.11`)

`AC_Update` (FB_AirCylinder). For cylinders with `bEnableSwitchOffBySafety` the PLC stores the desired position in `eDesiredPositionSafety` when TwinSAFE drops power (`AC_Halted` = `VA_PowerDownRequest`). After the safety is back, the cylinder stays in `bDisabledBySafety` and `AC_Reset` runs every scan, until Start is pressed or automatic is active. A manual "Get tool" in that state is reset every scan, so the changer does not move. A Start press during the wait releases the cylinder while the DU already waits at the changer.

### The fix

Commit `402d33e2d58` "SWMS-11157 Allow restoring desired position of air cylinder with reset button" + `c19344b1598`, merged in PR #22098 on 2026-10-05 into `Develop-4.11` only. Author: Andre Holtschlag.

New release condition in `AC_Update`:

```
ELSIF AirCylinder.bDisabledBySafety THEN
  IF MA_StartButtonPressed() OR_ELSE MA_AutomaticActive()
  OR_ELSE (MA_ResetButtonPressed() AND_THEN AirCylinder.eDesiredPositionSafety = AirCylinder.eActualPosition) THEN
    bDisabledBySafety := FALSE; eDesiredPosition := eDesiredPositionSafety; ...
  ELSE
    AC_Reset(...)
```

So Reset now releases the cylinder when its actual position equals the stored safety position. Start still releases it in every case.

Not in the fix: the reporter's proposal (direct message "drill not ready" and do not move the DU to the changer when the changer cannot move). The DU still moves to position when the cylinder is not released.

### Scope of the change

`AC_Update` is generic. It changes behaviour for every air cylinder that calls `AC_SetEnableSwitchOffBySafety(TRUE)`:

| Caller | Cylinder | Machines (from enum comments) |
| --- | --- | --- |
| `DRC_Update` action `Cylinder` | tool changer | V6xx (V630), V550, V320, V330 |
| `DRC_Update` action `AirCylinder8Pos` | tool changer | V631 |
| `DRC_Update` action `CarouselCylinder` | tool changer | V633, V310_V2 |
| `DR2_Update` (2x) | material clamp `pClampAirCylinder` | V310 (VSS-3735) |

Not affected: `AirCylinder10Pos` (V310), `Carousel` (V630 V2), `Auxiliary20Pos` (V325). These do not enable switch off by safety.

`origin/develop` (twincat/src, 4.3x line) has no `bDisabledBySafety` logic and does not contain this fix.

## 2. Risks of the solution

Scale: impact (I) and likelihood (L) 1 to 3, score = I x L. Test depth follows the score.

| # | Risk | I | L | Score | How to test |
| --- | --- | --- | --- | --- | --- |
| R1 | **Reset edge comes too early.** `MA_ResetButtonPressed` is a rising edge, high for 1 scan. `AC_Halted` reads the TwinSAFE status (`SafetyStatus = Run` / `TS_PowerAvailable`). If TwinSAFE reports Run a few scans after the reset edge (TwinSAFE often acknowledges on the falling edge), the cylinder is still halted in the scan with the edge and the new branch is never reached. Then the fix does nothing after one Reset press, and the original race with Start is still there. | 3 | 2 | 6 | TC-02, TC-05. Only on a real machine: in Vasim `TS_PowerAvailable_Vasim` is used and timing differs. Watch `bDisabledBySafety` online. |
| R2 | **Race still open when positions do not match.** When the actual position differs from the stored one (door opened while the changer moved, sensor flicker, air loss moved the cylinder), Reset does not release. The DU can still move to the changer and a Start during the wait gives the same shoot-out. | 3 | 1 | 3 | TC-07, TC-08 |
| R3 | **Movement on Reset.** EN 60204-1 / ISO 13849: a reset may not start a movement. The fix only releases when the position matches, so the valve should hold the cylinder where it is. Edge case: desired `Position_None` and cylinder between sensors gives `None = None`, release on Reset; a later "Get tool" then moves the cylinder from mid stroke with vented air. | 3 | 1 | 3 | TC-04, TC-09 |
| R4 | **Other machines change behaviour.** V630/V550/V320/V330 (Cylinder), V633/V310_V2 (CarouselCylinder) and the V310 material clamp now also release on Reset. For the clamp this means clamping pressure is back on Reset instead of on Start. | 2 | 2 | 4 | Section 6 regression |
| R5 | **Fix only in 4.11.** Not in `develop`. 4.3x machines are not covered and the ticket question "how does this work with other drills" is open for that line. | 2 | 2 | 4 | Check 4.3x behaviour separately, create follow-up ticket if needed |
| R6 | **Same area changed in the same release.** SWMS-11376 (toolchange position S, `Develop-4.11`, merged 2026-10-07) touches tool change too. | 2 | 1 | 2 | Run TC-03 on a build with both changes |
| R7 | Small structure change: in the release scan `AC_Reset` is no longer called before restoring. | 1 | 1 | 1 | Covered by TC-02/TC-10 |

## 3. Customer data

- [x] Machine backup: `20250149_V631_260603_094231.zip` (attached to Jira)
- [ ] NC file or job that shows the problem: not needed, manual "Get tool"
- [ ] VACAM log, time window around the problem: in backup, check
- [ ] TwinCAT event log or error code: timeout "tool changer not out" (look up exact code in backup)
- [x] Screenshots or video from the operator: `Video1.mp4`, `Video2.mp4`
- [ ] Material details: not relevant

## 4. Reproduction and fix verification

**Safety for all tests:** do the first runs with an empty tool changer or dummy holders. Keep hands out of the changer area. The shoot-out in TC-01 is the defect itself.

**Test machine:** V631 with 8 position air cylinder changer (VEC). Build A = 4.11.35.x (before fix), build B = 4.11.36 or Develop-4.11 build that contains `2904764f366`.

**Online watch list** (TwinCAT, tool holder cylinder of the drill changer): `bDisabledBySafety`, `eDesiredPosition`, `eDesiredPositionSafety`, `eActualPosition`, valve outputs, `SafetyStatus` of the valve.

### TC-SWMS-11157-01 Reproduce on build A

| # | Step | Expected (correct) | Seen at customer |
| --- | --- | --- | --- |
| 1 | Machine in manual, changer IN, open and close the doors | Safety drops, `bDisabledBySafety` = TRUE | |
| 2 | Press Reset once | Safety back to Run | |
| 3 | Press "Get tool" | DU moves to changer | DU moves, changer stays in |
| 4 | Wait | | Timeout "tool changer not out" |
| 5 | Repeat 1-3, press Start before the timeout | | Changer shoots out, tools fall out |

- [ ] Reproduced on machine in VEC
- result:: open

### TC-SWMS-11157-02 Fix: doors open and close, one Reset press (build B)

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Changer IN, open and close the doors | `bDisabledBySafety` = TRUE, `eDesiredPositionSafety` = In | |
| 2 | Press Reset **once**, short press | `bDisabledBySafety` = FALSE right after this press | |
| 3 | Press "Get tool" without Start | Changer moves out at normal speed, tool change completes, no timeout | |
| 4 | Repeat 10 times with short and long Reset presses | Same result every time | |

Fail on step 2 means R1 is real: report back to Andre with the online trace.
- result:: open

### TC-SWMS-11157-03 Fix: after startup

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Cold start of the PLC (power off/on), changer IN | Cylinder disabled by safety | |
| 2 | Reset once, then "Get tool" | Tool change completes without Start and without timeout | |
| 3 | Same after VACAM restart only (PLC keeps running) | Same | |

- result:: open

### TC-SWMS-11157-04 Fix: after E-stop

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Changer IN, press E-stop, release, Reset once | Released on Reset, no movement of the changer at Reset | |
| 2 | "Get tool" | Tool change completes | |
| 3 | Changer OUT (manual tool change position), E-stop, release, Reset | Changer stays OUT, no movement at Reset | |

- result:: open

### TC-SWMS-11157-05 Reset sources and timing

| # | Variation | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Reset on the operator panel | Released | |
| 2 | Reset via TransportManager (`TM_ResetButtonPressed`) | Released | |
| 3 | Reset via direct control / VACAM | Released | |
| 4 | Reset pressed while doors still open | No release, cylinder stays disabled | |
| 5 | Press Reset, close door after it | No release until next Reset or Start | |

- result:: open

## 5. Negative and edge cases

### TC-SWMS-11157-07 Position does not match (R2)

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Start a manual tool change, open the door while the changer moves (between sensors) | Safety stops it, stored position = desired | |
| 2 | Close door, Reset | No release (actual <> stored) | |
| 3 | "Get tool" | Note what happens: does the DU move to the changer? Message? | |
| 4 | Press Start during the wait (empty changer!) | Document behaviour. Shoot-out here means R2 is still open: create follow-up ticket | |

- result:: open

### TC-SWMS-11157-08 Sensor fault

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Changer IN, disconnect IN sensor, open/close doors, Reset | No release on Reset | |
| 2 | Start | Released, error for missing sensor as before the fix | |

- result:: open

### TC-SWMS-11157-09 No motion on Reset (R3)

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | For changer IN and changer OUT: doors open/close, Reset | No visible or audible movement of the cylinder at Reset | |
| 2 | Changer between sensors with desired None (if possible to create) | Note behaviour at Reset and at next "Get tool" | |

- result:: open

### TC-SWMS-11157-10 Automatic mode unchanged

| # | Step | Expected result | Result |
| --- | --- | --- | --- |
| 1 | Run a job with several tool changes | All tool changes OK | |
| 2 | Stop and open door during the job, close, Reset, Start | Job continues, tool changes OK | |

- result:: open

### Exploratory charter (30 min)

Explore door, E-stop, Reset, Start and "Get tool" in fast and unusual order on the V631 changer, to find a sequence where the changer moves while the DU waits at the changer, or where Reset causes a movement.

- result:: open

## 6. Regression around the fix

| Function/methods changed code | Affected machine | Result |
| --- | --- | --- |
| `AC_Update`, tool changer `Cylinder` | V630 (V6xx), V550, V320, V330: run TC-02 and TC-10 on one V630 | |
| `AC_Update`, tool changer `CarouselCylinder` | V633, V310_V2: run TC-02 and TC-10 on V633 | |
| `AC_Update`, material clamp `DR2_Update` | V310: clamp closed, doors open/close, Reset: clamp pressure back, no clamp movement; Start job | |
| Not affected (smoke only) | V310 `AirCylinder10Pos`, V325 `Auxiliary20Pos`, V630 V2 `Carousel` | |

- [ ] Fix also merged to develop, or a written decision why not (4.3x line has other code, see R5).
- [ ] Combined test with SWMS-11376 on the same 4.11 build.

Machine reminders:
- **V631:** tool change on all 8 positions, ToolClamp feedback, Weiss spindle start and stop.
- **V630:** tool change via cylinder changer, hole positions, clamp before drilling, unit retract before transport.
- **V633:** carousel positions, Suhner spindle start and stop, hole positions.
- **All machines:** home, standard job, E-stop and recovery, restart, no new errors in VACAM log.

## 7. Findings

| # | Finding | Machine | Jira | Severity | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Reporter's proposal (message and block DU move when changer is not ready) is not part of the fix | all drills with air cylinder changer | follow-up? | Medium | open |
| 2 | Fix not in `develop` (4.3x) | 4.3x drills | follow-up? | Medium | open |

## 8. Close

- [ ] Problem reproduced on build A, or a written reason why not.
- [ ] Fix verified on V631 with one Reset press (TC-02 to TC-05).
- [ ] Negative cases documented (TC-07 to TC-09).
- [ ] Regression around the fix passed (V630, V633, V310 clamp).
- [ ] Decision on develop / 4.3x recorded.
- [ ] Short answer for service in the SWMS ticket: fixed in 4.11.36; after doors or E-stop one Reset is enough for a manual tool change; customer action = update to 4.11.36.

**Verdict:** Fixed / Fixed with remarks / Not fixed / Cannot reproduce
**Signed off by:** Herbert
**Date:** 
