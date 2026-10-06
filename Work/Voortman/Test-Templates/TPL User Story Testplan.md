---
type: story-testplan
jira: BT2-0000
title: "{{title}}"
epic: BT2-0000
fix_version: 4.xx.0
rc_branch: RC-4.xx.0
vacam_version:
plc_commit:
machines: [V630, V631, V633, VB Standard / VB 1040, V912]
risk: Medium
tester: Herbert Nijkamp
created: {{date}}
status: draft
tags: [testplan, story]
---

# Test plan {{title}}

> [!info] How to use
> 1. Fill the frontmatter. Remove machines from `machines` that the story does not touch.
> 2. Fill section 2 first. It decides which machine modules in section 7 you keep.
> 3. Delete every machine module that is "No" in the matrix. Keep the shared smoke test.
> 4. One test case per behaviour change, not per acceptance criterion. Group criteria that test the same behaviour.

## 1. Story

- **Jira:** [BT2-0000](https://voortman.atlassian.net/browse/BT2-0000)
- **Epic:** [BT2-0000](https://voortman.atlassian.net/browse/BT2-0000) / [[<Epic test plan name>]]
- **What changes on the machine:** one sentence in operator terms. Example: "When the drill unit changes tool, the PLC now checks the tool clamp feedback before the spindle starts."
- **What can go wrong:** one sentence. Example: "A missing clamp signal stops the job with no clear message, or the spindle starts with an unclamped tool."

## 2. Machine scope

| Machine | Affected | Reason (code signal or ticket) | Test on |
|---|---|---|---|
| V630 | Yes / No / Shared | e.g. `Main Objects/Drill/`, `DrillChangerType_Cylinder` | Real machine / Simulation |
| V631 | Yes / No / Shared | e.g. `Drill_V2`, `ToolClamp`, `DrillChangerType_AirCylinder8Pos` | |
| V633 | Yes / No / Shared | e.g. `Drill_V2`, `Suhner`, `DrillChangerType_CarouselCylinder` | |
| VB Standard / VB 1040 | Yes / No / Shared | e.g. `SawFixedRotatableTable`, `Saw/OldStyle`, `SawType_VB1x50` | |
| V912 | Yes / No / Shared | e.g. `MachineType_V912`, `LaserHead`, `LaserSafetyHandler`, `V912Integration` | |

> [!tip] Scope rules
> - Machine-specific code (Drill, Drill_V2, Saw, LaserHead): test only on the machines that use it.
> - Drill shared (`DrillZone`, `DrillChanger`, `FB_DrillingAdapter`): test on at least 2 of V630, V631, V633.
> - Shared core (`Machine`, `MachineZone`, `Transport`, `MeasureUnit`, safety, configuration, `vacam/`): test on at least one drill line and one saw line. Add V912 when `MeasureUnit` or `MachineZone` changes, because V912 has its own branches there.
> - UI or VACAM-only change with no PLC impact: one machine is enough, note which one.

**Out of scope:** list what you deliberately do not test, and why.

## 3. Risk

| Factor | Score | Reason |
|---|---|---|
| Impact (3 = safety, collision, configuration/upgrade, cycle list; 2 = other behaviour; 1 = UI text or one machine only) | | |
| Likelihood (1 = small change; 2 = 4+ commits or 300+ changed lines; 3 = 15+ commits or 1500+ lines) | | |
| **Risk = impact x likelihood** (6+ High, 3-5 Medium, <3 Low) | | |

Risk sets the depth: High = scripted cases on every affected machine plus exploratory session. Medium = scripted cases on one machine per type plus smoke test. Low = smoke test and one check of the change.

## 4. Acceptance criteria coverage

| # | Acceptance criterion (from Jira) | Test case | Machines | Result |
|---|---|---|---|---|
| AC1 | | TC-xxxx-01 | | open |
| AC2 | | TC-xxxx-02 | | open |

Every AC needs at least one test case. An AC you cannot test on a machine: write how you verify it instead (code review, log, simulation).

## 5. Test environment and data

- **VACAM version:** 4.xx.x (build ...)
- **PLC commit:** short hash from `git log -1 --format="%h" origin/RC-4.xx.0`
- **Machine configuration:** backup name and date, taken before the test
- **Parameters changed for this test:** name, old value, new value. Restore after the test.
- **Test material and NC files:** profile, length and operations. Example: "HEA 200, L = 6000 mm, 6 holes Ø 22 on flange, 2 holes Ø 18 on web, file `TEST_HEA200_6H.nc1`".
- **Simulation:** what you cannot test in simulation (real I/O, timing, band tension, laser power).

## 6. Test cases

### TC-xxxx-01 <behaviour> (<machines>)
- **AC:** AC1
- **Type:** Scripted
- **Machines:** 
- **Precondition:** machine homed, automatic mode, test material on infeed

| # | Step | Expected result |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

- **Result:** - [ ] V630 pass - [ ] V631 pass - [ ] V633 pass - [ ] VB pass - [ ] V912 pass
- result:: open
- **Notes:**

### TC-xxxx-02 <negative or edge case> (<machines>)
- **AC:** AC1
- **Type:** Scripted, negative
- **Ideas:** missing sensor signal, value at minimum and maximum, empty or wrong parameter, operator stop or E-stop halfway, restart after power loss, material shorter or longer than expected.

| # | Step | Expected result |
|---|---|---|
| 1 | | |
| 2 | | |

- **Result:** - [ ] pass - [ ] fail
- result:: open
- **Notes:**

### TC-xxxx-03 Exploratory <area> (<machines>)
- **Type:** Exploratory, timebox 60 min
- **Charter:** Explore <area> with <material, settings, operator actions> to find <risk>.
- **Focus points:**
  - [ ] 
  - [ ] 
  - [ ] 
- **Session notes:** what you tried, what you saw, open questions
- result:: open

## 7. Machine modules

Delete every module for a machine that is "No" in section 2.

> [!example]- Drill lines shared (infeed, cross transport, drilling process; V630, V631, V633)
> Full check list with requirement numbers: [[Testplan 631]].
> - [ ] Infeed: system asks to rotate material when the start view in the buffer is wrong.
> - [ ] Search material: drag dog goes up within 1 cm of the material and never closer than 1 cm. Test small flange, wide flange and closed profile.
> - [ ] Datum line: material pushed at reduced speed, touches at least 2 datum rollers, drag dogs slow down between the rollers (automatic and manual).
> - [ ] Wrong profile: message when actual differs from theoretical (e.g. theoretical UNP180 or UNP220, actual UNP200).
> - [ ] Feed and RPM: suggested and actual values match the tool (HSS and HM) and the material grade.
> - [ ] Special holes when touched by the story: blind hole depth, threaded hole (standard 20 mm, custom 21 mm), dual layer hole in a tube.
> - [ ] Reference points when touched by the story: all units, top, bottom, symmetry and absolute.

> [!example]- V630 drill line (old drill object, cylinder tool changer)
> - [ ] Home all drill units and axes. Reference OK, no warnings in VACAM log.
> - [ ] Tool change on each drill unit through the cylinder changer. Tool in spindle matches the tool table.
> - [ ] Run the test NC file. Measure 3 hole positions, record deviation per unit.
> - [ ] Material clamped before drilling starts, released before transport.
> - [ ] Drill units retract before material moves (watch the first transport move after drilling).
> - [ ] Force a fault on the changed function (e.g. remove a sensor signal). Correct message, job stops, recovery without restart.
> - [ ] Story-specific check: 

> [!example]- V631 drill line (Drill_V2, Weiss spindle, ToolClamp, 8-position air cylinder changer)
> Existing detailed plan: [[Testplan 631]].
> - [ ] Home all drill units and axes.
> - [ ] Tool change on all 8 changer positions. ToolClamp clamp and unclamp feedback correct each time.
> - [ ] Spindle start, speed ramp and stop. No spindle start with unclamped tool.
> - [ ] Run the test NC file. Measure 3 hole positions.
> - [ ] Material clamping and release around the drill cycle.
> - [ ] Force a fault on the changed function. Correct message and recovery.
> - [ ] Story-specific check: 

> [!example]- V633 drill line (Drill_V2, Suhner spindles, carousel changer)
> - [ ] Home all drill units and axes.
> - [ ] Tool change on every carousel position used in the test file. Carousel position feedback matches the requested tool.
> - [ ] Suhner spindle start, speed and stop on each unit.
> - [ ] Run the test NC file. Measure 3 hole positions.
> - [ ] Material clamping and release around the drill cycle.
> - [ ] Force a fault on the changed function. Correct message and recovery.
> - [ ] Story-specific check: 

> [!example]- VB Standard / VB 1040 saw (SawFixedRotatableTable, or Saw/OldStyle VB1x50 family)
> Code note: VB Standard runs `SawFixedRotatableTable`. The VB 1040 has no own type in the code; it runs as the VB1050/1250 family (`SawType_VB1x50` hydraulic feed, `SawType_VBS1x50` servo feed, `SawType_VBS1x50b`). Write down which saw type the test machine is configured as.
> - [ ] Home saw, table and transport.
> - [ ] Straight cut 90°. Check cut length against the NC file.
> - [ ] Miter cuts at the angles in the test file (e.g. +45° and -45°). Table rotates to the right angle and locks.
> - [ ] Saw feed: hydraulic or servo, correct feed speed for the material, cut-through detected.
> - [ ] Band tension and band speed reach their set values before the cut starts.
> - [ ] Short piece handling and material clamping before and after the cut.
> - [ ] Band break or band slip fault: saw stops, correct message, recovery.
> - [ ] Story-specific check: 

> [!example]- V912 (laser head, LaserSafetyHandler, MeasureUnit with asynchronous X drive)
> Code note: `ConfigureMachineTypeV912` sets `IsV912`, `XAxisHasAsynchronousDrive` on the MeasureUnit and `HasNoNozzleHandler` on the LaserHead. V912 also uses its own gripper in `MachineZone` (`MZ_GetV912Gripper`).
> - [ ] Start-up: LaserSafetyHandler configuration check passes, no configuration errors.
> - [ ] Laser safety: open door or enclosure during a job. Laser switches off, job stops, correct message.
> - [ ] Material front and end detection with the vertical photocells. Measured length matches the real length.
> - [ ] X positioning with the asynchronous drive: move to 3 positions, check actual against target.
> - [ ] Gripper takes and releases the material at the right moments.
> - [ ] Run the test job. Check the result on the material (position and quality of laser output).
> - [ ] Story-specific check: 

## 8. Regression and smoke test

Run on every machine marked Yes or Shared.

- [ ] Home all axes after a cold start.
- [ ] Load and run one standard job from start to finish.
- [ ] Emergency stop during the job, reset, continue or restart the job.
- [ ] Door or fence interlock stops motion.
- [ ] Shut down VACAM and the PLC, restart, machine comes back in the same state.
- [ ] VACAM log and TwinCAT event log: no new errors or warnings compared with the previous version.

## 9. Upgrade and configuration

Skip when the story adds no parameter, configuration item or data migration.

- [ ] Upgrade from the current field version (4.xx.x) to the test version.
- [ ] New parameters exist after the upgrade and have a sane default. List them: 
- [ ] Existing customer values are kept.
- [ ] Machine runs the standard job after the upgrade without changing any setting.

## 10. Findings

| # | Finding | Machine | Jira bug | Severity | Status |
|---|---|---|---|---|---|
| 1 | | | | | |

## 11. Exit and sign-off

- [ ] All ACs covered and passed, or accepted by the PO with a reason.
- [ ] No open safety or collision findings.
- [ ] Findings logged in Jira and linked to the story.
- [ ] Test result added to the Jira story (comment with link to this note).

**Verdict:** Pass / Pass with remarks / Fail
**Signed off by:** 
**Date:** 
