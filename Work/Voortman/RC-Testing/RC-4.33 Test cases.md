---
rc: "4.33"
branch: RC-4.33.0
rc_commit: ed77b6064c4
rc_commit_date: 2026-10-01
baseline: 4.32.17
analysed: 2026-10-02
machines: [V630, V631, V633, VB Standard, WB Standard + Probe Truck, VB 1040]
tags: [rc-testing, rc-4-33, test-cases]
---

# RC-4.33 Test cases

Related: [[RC-4.33 Analysis]] · [[RC-4.33 Testplan]] · [[RC-4.33 Other team alerts]]

27 cases. Numbered in plan order. Tick one box per machine and add findings under **Notes**. Change `status::` to `pass`, `fail` or `blocked` when done.

## Upgrade and configuration

### TC-433-001 Upgrade 4.32.17 to RC-4.33 on a drill line
status:: open
- **Risk:** High, area Configuration / upgrade, tickets [BT2-3879](https://voortman.atlassian.net/browse/BT2-3879), [BT2-3834](https://voortman.atlassian.net/browse/BT2-3834), [BT1-2305](https://voortman.atlassian.net/browse/BT1-2305), [BT2-3827](https://voortman.atlassian.net/browse/BT2-3827)
- **Why:** the migration script removes MachineZone values from Drill and DeburUnit and PicoScan instances. A script that was added and removed again (BT1-2305/BT2-3827) disabled MovableConveyor and V912Gripper. A wrong migration leaves a drill unit unconfigured or an object disabled.
- **Machines:** V631 (minimum), V630, V633
- **Type:** Scripted
- **Precondition:** machine runs 4.32.17. Export the machine configuration and take screenshots of drill unit, drill changer, clamp pressure and transport settings.

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Install RC-4.33 over 4.32.17 | Installer finishes without errors |
| 2 | Start VACAM and VASIM | VACAM finishes the startup migration, no config error, VASIM starts after VACAM |
| 3 | Compare drill unit, drill changer and tool settings with the screenshots | All values equal |
| 4 | Check machine objects list | No object is disabled that was enabled before |
| 5 | Reference all axes, run one standard job | Job completes, no unexpected message |

- **Result:** - [ ] V631 pass - [ ] V631 fail - [ ] V630 pass - [ ] V630 fail - [ ] V633 pass - [ ] V633 fail
- **Notes:**

### TC-433-002 Upgrade 4.32.17 to RC-4.33 on a saw line
status:: open
- **Risk:** High, area Configuration / upgrade, tickets [SWMS-11589](https://voortman.atlassian.net/browse/SWMS-11589), [BT2-3827](https://voortman.atlassian.net/browse/BT2-3827)
- **Why:** the position correction setting moved from MeasureUnit to Saw in the migration script. If it is not carried over, the operator no longer gets the correction prompt.
- **Machines:** VB Standard (minimum), WB Standard + Probe Truck, VB 1040
- **Type:** Scripted
- **Precondition:** saw runs 4.32.17. Note the position correction setting and saw parameters.

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Install RC-4.33 over 4.32.17 and start VACAM | Migration finishes, no error |
| 2 | Open saw settings | Position correction setting has the same value as before, now under Saw |
| 3 | Check saw, probe truck and measuring objects | All enabled as before |
| 4 | Reference all axes, saw one standard bar | Cut length within tolerance |

- **Result:** - [ ] VB Standard pass - [ ] VB Standard fail - [ ] WB+PT pass - [ ] WB+PT fail - [ ] VB 1040 pass - [ ] VB 1040 fail
- **Notes:**

### TC-433-003 Clamp pressure settings validation and clamping
status:: open
- **Risk:** High, area Configuration / clamping, tickets [BT1-2271](https://voortman.atlassian.net/browse/BT1-2271), [BT2-3882](https://voortman.atlassian.net/browse/BT2-3882), [SWMS-11137](https://voortman.atlassian.net/browse/SWMS-11137)
- **Why:** the clamp pressure screen now blocks invalid and negative min/max values. Clamp pressure calculation moved inside the MeasureUnit refactor. Horizontal clamps 1 and 2 got a fix from 4.0.
- **Machines:** one drill line, one saw line
- **Type:** Scripted
- **Precondition:** RC installed, machine referenced.

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Open clamp pressure settings, enter min greater than max | Error shown, OK disabled, cannot save |
| 2 | Enter a negative value | Error shown, cannot save |
| 3 | Change several values in a row, then fix them | Errors clear, OK enabled, values saved |
| 4 | Clamp a light and a heavy profile in manual and automatic | Horizontal clamps 1 and 2 close, pressure matches the setting |

- **Result:** - [ ] Drill line pass - [ ] Drill line fail - [ ] Saw line pass - [ ] Saw line fail
- **Notes:**

## Safety and collision

### TC-433-004 Measuring unit front-side detection
status:: open
- **Risk:** High, area Safety / transport, ticket [BT2-3694](https://voortman.atlassian.net/browse/BT2-3694)
- **Why:** the conveyor halt on front-side detection now only applies outside automatic mode, and the warning only appears when the conveyor moves towards the measuring unit. A wrong condition can let material run into the unit or block manual moves.
- **Machines:** one drill line, one saw line
- **Type:** Scripted
- **Precondition:** front-side sensor of the measuring unit accessible, door of measuring unit closed.

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Manual mode, cover the front-side sensor, move infeed conveyor forward | Conveyor halts, warning "blocked by front-side detection" |
| 2 | Same, move infeed conveyor backward | Conveyor moves, no warning |
| 3 | Open the measuring unit door, repeat step 1 | Behaviour as specified for open door (no halt from this check) |
| 4 | Automatic mode with material passing the sensor | Production continues, no halt |

- **Result:** - [ ] Drill line pass - [ ] Drill line fail - [ ] Saw line pass - [ ] Saw line fail
- **Notes:**

### TC-433-005 Short material on infeed (1,400 mm)
status:: open
- **Risk:** High, area Transport / safety, ticket [SWMS-11394](https://voortman.atlassian.net/browse/SWMS-11394) (Critical)
- **Why:** X target and the safe position for the next material now depend on the gripper selection. Wrong values give a collision with the next bar or a stop.
- **Machines:** one drill line, one saw line
- **Type:** Scripted
- **Precondition:** job with bars of 1,400 mm and one longer bar.

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Run the job in automatic | Each bar is picked up and positioned without stop |
| 2 | Watch the next bar on the infeed | It waits at a safe position, no contact with the bar in process |
| 3 | Check material end detection | Material end found at the right X, no index error |

- **Result:** - [ ] Drill line pass - [ ] Drill line fail - [ ] Saw line pass - [ ] Saw line fail
- **Notes:**

### TC-433-006 V631 Z3/Y4 minimum distance
status:: open
- **Risk:** High, area Drill V2, ticket [SWMS-10961](https://voortman.atlassian.net/browse/SWMS-10961)
- **Why:** `cDR2_V631_AbsoluteMinDistanceZ3Y4` went from 185 to 164 mm. Units 3 and 4 can now come 21 mm closer.
- **Machines:** V631
- **Type:** Scripted
- **Precondition:** job with holes for unit 3 and 4 close together on a small profile, Y3 below the limit position.

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Run the job, watch Z3 and Y4 | No contact, no collision error |
| 2 | Measure the closest distance (VASIM or by hand) | Not less than 164 mm without tool |
| 3 | Repeat with the job that gave "target position blocked by Z4" | Target reached, no block |

- **Result:** - [ ] V631 pass - [ ] V631 fail
- **Notes:**

### TC-433-007 V633 rat hole milling and unit 3 near side bearings
status:: open
- **Risk:** High, area Drill V633, ticket [SWMS-11577](https://voortman.atlassian.net/browse/SWMS-11577) (Blocker)
- **Why:** rat hole milling damaged tools. The fix adds a collision-free range for unit 3 with large tools near the side bearings (Xd range 300 mm, bearing at Xd 241 mm, radius 36 mm).
- **Machines:** V633
- **Type:** Scripted
- **Precondition:** job with rat holes and a large-diameter tool in unit 3.

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Run the rat hole job | Contour correct, no tool damage |
| 2 | Run unit 3 with the largest tool near the side bearings | Path stays out of the bearing area, no collision |
| 3 | Check the cycle list | Step details show the right drill unit and tool |

- **Result:** - [ ] V633 pass - [ ] V633 fail
- **Notes:**

### TC-433-008 V633 X-axis external brake check
status:: open
- **Risk:** High, area Configuration, ticket [BT1-2332](https://voortman.atlassian.net/browse/BT1-2332)
- **Why:** `CheckExternalBrakeXAxis` is now only set when the measure unit is a gripper truck (V633T). On a V633 with roller measuring the check is now off.
- **Machines:** V633 (both variants if available)
- **Type:** Scripted
- **Precondition:** know which measure unit type your V633 has.

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Start the machine and reference X | No brake error |
| 2 | Gripper truck variant: simulate brake feedback fault | Error raised |
| 3 | Roller variant: same fault | No brake check (agree with BT1 that this is intended) |

- **Result:** - [ ] V633 pass - [ ] V633 fail
- **Notes:**

## Drilling

### TC-433-009 Drill 3 waits during milling
status:: open
- **Risk:** Medium, area Drill V2, ticket [SWMS-10977](https://voortman.atlassian.net/browse/SWMS-10977)
- **Why:** the prepare position now uses `LimitedPosition` instead of `LIMIT`. Drill 3 should prepare next to a milling unit without waiting.
- **Machines:** V631, V633
- **Type:** Scripted
- **Precondition:** job with milling on one unit and holes for unit 3.

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Run the job | Unit 3 prepares while milling runs, no idle wait |
| 2 | Compare cycle time with 4.32.17 | Equal or shorter |

- **Result:** - [ ] V631 pass - [ ] V631 fail - [ ] V633 pass - [ ] V633 fail
- **Notes:**

### TC-433-010 Web support to rest
status:: open
- **Risk:** Medium, area Drill V2, tickets [SWMS-10787](https://voortman.atlassian.net/browse/SWMS-10787), [SWMS-11147](https://voortman.atlassian.net/browse/SWMS-11147)
- **Why:** the web support goes to rest when its target is not reachable, and the rest check now runs for every drill type.
- **Machines:** V631, V633, V630
- **Type:** Scripted
- **Precondition:** job where the web support target is outside its range.

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Run the job | Web support moves to rest, drill continues, no stop |
| 2 | Normal job with reachable target | Web support supports as before |

- **Result:** - [ ] V631 pass - [ ] V631 fail - [ ] V633 pass - [ ] V633 fail - [ ] V630 pass - [ ] V630 fail
- **Notes:**

### TC-433-011 Tool length measuring in automatic
status:: open
- **Risk:** High (late change 2026-09-30), area Drill V2, ticket [SWMS-11501](https://voortman.atlassian.net/browse/SWMS-11501)
- **Why:** tool length measuring now uses the actual position motion task. A wrong length gives wrong hole depth or a crash into the material.
- **Machines:** V631, V633
- **Type:** Scripted
- **Precondition:** tool with known length, tool length measuring enabled.

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Trigger tool length measuring in automatic | Measurement completes |
| 2 | Compare measured length with the known length | Within 0.1 mm |
| 3 | Drill a hole with known depth | Depth correct |

- **Result:** - [ ] V631 pass - [ ] V631 fail - [ ] V633 pass - [ ] V633 fail
- **Notes:**

### TC-433-012 Tool screen: tool change, F6 menu, tool restriction per unit
status:: open
- **Risk:** Medium, area Drill shared, tickets [SWMS-11554](https://voortman.atlassian.net/browse/SWMS-11554), [SWMS-11499](https://voortman.atlassian.net/browse/SWMS-11499), [SWMS-11363](https://voortman.atlassian.net/browse/SWMS-11363)
- **Why:** crash fix for tool change on layout marking units, tools disappearing from F6, and any tool type can now be restricted to specific units.
- **Machines:** V630, V631, V633
- **Type:** Scripted

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Change a tool on a layout marking unit | No crash, tool saved |
| 2 | Open F6, change a tool, reopen F6 | All tools visible |
| 3 | Restrict a tap or countersink to unit 1, run a job that needs it | Only unit 1 uses the tool |

- **Result:** - [ ] V630 pass - [ ] V630 fail - [ ] V631 pass - [ ] V631 fail - [ ] V633 pass - [ ] V633 fail
- **Notes:**

### TC-433-013 Marking and imprints
status:: open
- **Risk:** Medium, area Drill V2 / VACAM, tickets [SWMS-10680](https://voortman.atlassian.net/browse/SWMS-10680), [BT2-3874](https://voortman.atlassian.net/browse/BT2-3874)
- **Why:** imprints were missing on V631 and V633. Slave marking for Drill V2 was refactored.
- **Machines:** V631, V633
- **Type:** Scripted

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Run a job with imprints and scribing on several sides | All marks present and at the right position |

- **Result:** - [ ] V631 pass - [ ] V631 fail - [ ] V633 pass - [ ] V633 fail
- **Notes:**

### TC-433-014 Drill changer cycle after refactor
status:: open
- **Risk:** High, area Drill shared, ticket [BT2-3891](https://voortman.atlassian.net/browse/BT2-3891)
- **Why:** drill changer code was decoupled from the machine. A broken link shows as a tool change that hangs or picks the wrong position.
- **Machines:** V630, V631, V633
- **Type:** Scripted

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Manual tool change for every position of every unit | Correct tool in spindle, no timeout |
| 2 | Job with at least 5 tool changes in automatic | All changes complete, cycle time as on 4.32.17 |
| 3 | Emergency stop during a tool change, recover | Changer recovers to a safe state, no tool lost |

- **Result:** - [ ] V630 pass - [ ] V630 fail - [ ] V631 pass - [ ] V631 fail - [ ] V633 pass - [ ] V633 fail
- **Notes:**

### TC-433-015 Exploratory: drilling regression after the PLC refactor
status:: open
- **Risk:** High, area PLC refactoring, tickets [BT2-3871](https://voortman.atlassian.net/browse/BT2-3871), [BT2-3879](https://voortman.atlassian.net/browse/BT2-3879), [BT2-3883](https://voortman.atlassian.net/browse/BT2-3883), [BT2-3892](https://voortman.atlassian.net/browse/BT2-3892), MCPL-3147
- **Machines:** V630, V631, V633
- **Type:** Exploratory (timebox 90 min per machine)
- **Charter:** explore drilling, milling and measuring on a mix of profiles with your usual customer jobs to find behaviour that differs from 4.32.17.
- **Focus points:**
  - Prepare drill and collision checks between units (warnings that no longer appear, or appear too often)
  - Profile measurement by the measuring unit before drilling
  - Data logging files (`DZ_WriteMatAndDrillUnitDimToDisk`) still written
  - Go to rest and reference run of every unit
  - Messages and warnings shown with the right object name
- **Result:** - [ ] V630 pass - [ ] V630 fail - [ ] V631 pass - [ ] V631 fail - [ ] V633 pass - [ ] V633 fail
- **Notes:**

## Sawing

### TC-433-016 Cut position accuracy with measured material
status:: open
- **Risk:** High, area Saw shared / VACAM, tickets [BT2-3525](https://voortman.atlassian.net/browse/BT2-3525), [BT2-3566](https://voortman.atlassian.net/browse/BT2-3566), [BT2-3569](https://voortman.atlassian.net/browse/BT2-3569)
- **Why:** cut positions are now corrected with the most relevant material measurement, and alternative reference planes are allowed. A wrong choice shifts every cut.
- **Machines:** VB Standard, WB Standard + Probe Truck, VB 1040
- **Type:** Scripted
- **Precondition:** bar with a known actual length that differs from nominal by 5 to 10 mm.

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Saw 3 pieces with straight cuts | Lengths within tolerance of the drawing |
| 2 | Saw 2 pieces with mitre cuts | Lengths and angles within tolerance |
| 3 | Check the remnant length | Matches the calculated remnant |

- **Result:** - [ ] VB Standard pass - [ ] VB Standard fail - [ ] WB+PT pass - [ ] WB+PT fail - [ ] VB 1040 pass - [ ] VB 1040 fail
- **Notes:**

### TC-433-017 Position correction prompt
status:: open
- **Risk:** Medium, area Saw fixed rotatable table, ticket [SWMS-11589](https://voortman.atlassian.net/browse/SWMS-11589)
- **Why:** the position correction moved from MeasureUnit to Saw and was renamed to RecheckEnteredPositionCorrection.
- **Machines:** VB Standard, WB Standard + Probe Truck
- **Type:** Scripted

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Enable position correction, start a job | Operator gets the correction prompt |
| 2 | Enter a correction of +2 mm | Next cut shifts 2 mm |
| 3 | Disable position correction | No prompt |

- **Result:** - [ ] VB Standard pass - [ ] VB Standard fail - [ ] WB+PT pass - [ ] WB+PT fail
- **Notes:**

### TC-433-018 Saw angle with moveable rollers
status:: open
- **Risk:** Medium, area Saw shared, ticket [SWMS-11596](https://voortman.atlassian.net/browse/SWMS-11596)
- **Why:** the W-axis is limited to the moveable roller range while the roller input is active, and restored afterwards.
- **Machines:** saws with moveable rollers (VB Standard, VB 1040 if fitted)
- **Type:** Scripted

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Activate the moveable roller, request maximum mitre angle | W stops at the roller limit, no overshoot |
| 2 | Deactivate the roller | Full W range available again |

- **Result:** - [ ] VB Standard pass - [ ] VB Standard fail - [ ] VB 1040 pass - [ ] VB 1040 fail
- **Notes:**

### TC-433-019 Clear cut 0
status:: open
- **Risk:** Medium, area Saw / VACAM, ticket [SWMS-11678](https://voortman.atlassian.net/browse/SWMS-11678)
- **Why:** a redundant clear cut assignment in the batch editor was removed. Clear cut 0 must be kept.
- **Machines:** VB Standard, VB 1040
- **Type:** Scripted

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Set clear cut to 0 in the batch editor, save, reopen | Value stays 0 |
| 2 | Run the batch | No clear cut performed |

- **Result:** - [ ] VB Standard pass - [ ] VB Standard fail - [ ] VB 1040 pass - [ ] VB 1040 fail
- **Notes:**

### TC-433-020 Probe truck search and push
status:: open
- **Risk:** High, area Probe truck, tickets [BT2-3907](https://voortman.atlassian.net/browse/BT2-3907), MCPL-3149
- **Why:** `FB_ProbeTruck` used infeed and outfeed pointers before they were set. A message converter was injected. The saw table must block its rollers while the truck pushes.
- **Machines:** WB Standard + Probe Truck
- **Type:** Scripted

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Cold start PLC, start production | No pointer or null-object error |
| 2 | Probe truck searches material start | Material found, position correct |
| 3 | Probe truck pushes material to the saw | Saw table rollers blocked during push, position within tolerance |
| 4 | Trigger a probe truck error | Message shown with readable text |

- **Result:** - [ ] WB+PT pass - [ ] WB+PT fail
- **Notes:**

### TC-433-021 Exploratory: VB1050/1250 saw after refactor
status:: open
- **Risk:** Medium, area Saw old style, tickets MCPL-3154, MCPL-3147
- **Machines:** VB 1040
- **Type:** Exploratory (timebox 60 min)
- **Charter:** explore the old-style saw in manual and automatic to find interlocks or positions that changed after the saw stopped reading global machine data.
- **Focus points:**
  - Walk-in control and door open: saw must stop
  - Saw feed, clear cut cycle and saw above material detection
  - Reference point valid after restart
  - Halt and object stop during a cut
- **Result:** - [ ] VB 1040 pass - [ ] VB 1040 fail
- **Notes:**

## Shared: measuring, transport, process

### TC-433-022 Measured material width
status:: open
- **Risk:** High, area Measuring, tickets [SWMS-11254](https://voortman.atlassian.net/browse/SWMS-11254) (commit tagged BT1-11254), [SWMS-11319](https://voortman.atlassian.net/browse/SWMS-11319)
- **Why:** measured width now comes from the measure roll unit. Angle iron height and width are calculated inverted in behind orientation.
- **Machines:** one drill line, one saw line
- **Type:** Scripted

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Measure an HEA, a UNP and an angle iron | Width within 1 mm of the real width |
| 2 | Angle iron in behind orientation on transverse transport | No "wide material" detection |

- **Result:** - [ ] Drill line pass - [ ] Drill line fail - [ ] Saw line pass - [ ] Saw line fail
- **Notes:**

### TC-433-023 Conveyor synchronisation and transport groups
status:: open
- **Risk:** Medium, area Transport, tickets [SWMS-11010](https://voortman.atlassian.net/browse/SWMS-11010), [BT1-2304](https://voortman.atlassian.net/browse/BT1-2304), [BT1-2305](https://voortman.atlassian.net/browse/BT1-2305)
- **Why:** conveyor synchronisation was fixed and transport groups can now drive more axis types.
- **Machines:** one drill line, one saw line
- **Type:** Scripted

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Move long material over infeed and outfeed conveyors together | Conveyors run in sync, no slip or stop |
| 2 | Stop the transport group during a move | All conveyors stop together |

- **Result:** - [ ] Drill line pass - [ ] Drill line fail - [ ] Saw line pass - [ ] Saw line fail
- **Notes:**

### TC-433-024 Exploratory: automatic start, stop and long run
status:: open
- **Risk:** High, area Cycle list, tickets [SWMS-11536](https://voortman.atlassian.net/browse/SWMS-11536), [SWMS-11130](https://voortman.atlassian.net/browse/SWMS-11130), [BT2-3781](https://voortman.atlassian.net/browse/BT2-3781)
- **Machines:** one drill line, one saw line
- **Type:** Exploratory (timebox 2 h per machine, mostly unattended run)
- **Charter:** run a full shift job list with stops and restarts to find hangs, deadlocks or a machine that does not start automatic.
- **Focus points:**
  - Start, pause, stop and restart automatic 10 times
  - Change a property in VACAM while the PLC sends commands
  - Long run of at least 1 hour without operator action
  - Cycle list scrolling during production
- **Result:** - [ ] Drill line pass - [ ] Drill line fail - [ ] Saw line pass - [ ] Saw line fail
- **Notes:**

### TC-433-025 VACAM UI checks
status:: open
- **Risk:** Low, area VACAM application, tickets [SWMS-10779](https://voortman.atlassian.net/browse/SWMS-10779), [SWMS-11020](https://voortman.atlassian.net/browse/SWMS-11020), [SWMS-11482](https://voortman.atlassian.net/browse/SWMS-11482), [SWMS-11494](https://voortman.atlassian.net/browse/SWMS-11494), [SWMS-11371](https://voortman.atlassian.net/browse/SWMS-11371), [SWMS-11576](https://voortman.atlassian.net/browse/SWMS-11576)
- **Machines:** one machine
- **Type:** Scripted checklist

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Line with two machines: check master indicator | Master machine shown |
| 2 | Product with radius in product viewer | Radius shown |
| 3 | Try to set free length material end to 10 | Value refused or limited as specified |
| 4 | Change buffer stack positions and reopen | Positions kept |
| 5 | Product with angle cut | Angle cut shown visually |

- **Result:** - [ ] pass - [ ] fail
- **Notes:**

### TC-433-026 Messages and translations
status:: open
- **Risk:** Low, area Translations / UI text, ticket [BT2-3907](https://voortman.atlassian.net/browse/BT2-3907)
- **Why:** the message converter is now injected in many objects. A null-object default shows nothing.
- **Machines:** one drill line, one saw line
- **Type:** Scripted

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Trigger 5 common warnings (door open, emergency stop, clamp, material not found, axis error) | Each shows a readable text with the right object name |

- **Result:** - [ ] Drill line pass - [ ] Drill line fail - [ ] Saw line pass - [ ] Saw line fail
- **Notes:**

## Final

### TC-433-027 Smoke test per machine
status:: open
- **Risk:** all areas
- **Machines:** all six
- **Type:** Scripted

| # | Step | Expected result |
|---|------|-----------------|
| 1 | Cold start PLC and VACAM | No errors |
| 2 | Reference all axes | All axes referenced |
| 3 | Load and run one standard job | Job completes, parts correct |
| 4 | Emergency stop during production, recover | Machine recovers, job can continue |
| 5 | Open a door or fence during production | Machine stops safely |
| 6 | Shut down and restart | Settings kept |

- **Result:** - [ ] V630 pass - [ ] V631 pass - [ ] V633 pass - [ ] VB Standard pass - [ ] WB+PT pass - [ ] VB 1040 pass
- **Notes:**

## Status overview

Each case has an inline `status::` field, so a Dataview query on this note can count open and finished cases. Update the table below by hand if you do not use Dataview.

| Status | Count |
|---|---|
| open | 27 |
| pass | 0 |
| fail | 0 |
| blocked | 0 |
