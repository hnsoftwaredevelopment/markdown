---
rc: "4.33"
branch: RC-4.33.0
rc_commit: ed77b6064c4
rc_commit_date: 2026-10-01
baseline: 4.32.17
analysed: 2026-10-02
test_start: 2026-10-05
release_target: 2026-11-27
machines: [V630, V631, V633, VB Standard, WB Standard + Probe Truck, VB 1040]
tags: [rc-testing, rc-4-33, testplan]
---

# RC-4.33 Testplan

Related: [[RC-4.33 Analysis]] · [[RC-4.33 Test cases]] · [[RC-4.33 Other team alerts]]

## Goal and period

- Test RC-4.33.0 at commit ed77b6064c4 against what customers run now (4.32.17).
- Start: Monday 2026-10-05. Release target: 2026-11-27 (8 weeks).
- 27 test cases on 6 machines. Safety, upgrade and configuration go first so findings reach development before week 4.
- New commits on the RC branch during the period: ask for a re-run of the analysis. New cases get the next free number and passed cases in touched areas get a retest line.

## Priorities

1. **High, week 1 to 3:** upgrade (TC-433-001, 002), clamp pressure (003), front-side detection (004), short material (005), V631 Z3/Y4 (006), V633 rat hole and unit 3 (007), V633 brake (008), tool length measuring (011), drill changer (014), drilling regression (015).
2. **High, week 4 to 5:** cut positions (016), probe truck (020), measured width (022), long run and restarts (024).
3. **Medium:** drill 3 waiting (009), web support (010), tool screen (012), marking (013), position correction (017), saw angle with moveable rollers (018), clear cut (019), VB1050/1250 exploratory (021), conveyor sync (023).
4. **Low:** VACAM UI checks (025), messages (026). Final smoke test (027) on every machine.

## Schedule

| Week | Dates | Machine | Focus areas | Test cases |
|---|---|---|---|---|
| 1 | 05-09 Oct | V631, VB Standard | Upgrade, configuration, front-side detection, short material, clamping | TC-433-001, 002, 003, 004, 005 |
| 2 | 12-16 Oct | V631, V633 | Z3/Y4 margin, drill V2, tool length measuring, drill changer, V633 rat hole and brake | TC-433-006, 007, 008, 009, 010, 011, 012, 014 |
| 3 | 19-23 Oct | V633, V630 | V633 marking and regression, V630 upgrade and drill changer | TC-433-001 (V630, V633), 010, 012, 013, 014, 015 (V633) |
| 4 | 26-30 Oct | VB Standard, WB + Probe Truck | Cut positions, position correction, saw angle, clear cut, probe truck | TC-433-002 (WB+PT), 016, 017, 018, 019, 020 |
| 5 | 02-06 Nov | VB 1040, shared | VB1050/1250 upgrade and regression, measured width, conveyor sync | TC-433-002 (VB 1040), 016, 018, 019, 021, 022, 023 |
| 6 | 09-13 Nov | V630, V631, one saw | Exploratory drilling regression, long run, UI and messages | TC-433-015 (V630, V631), 024, 025, 026 |
| 7 | 16-20 Nov | as needed | Retest of fixes, re-run analysis for new RC commits | open and failed cases, new cases |
| 8 | 23-27 Nov | all six | Final smoke test and sign-off | TC-433-027 |

## Upgrade test

Always upgrade from 4.32.17 to the RC on at least one drill line (V631) and one saw line (VB Standard), cases TC-433-001 and 002. Before the upgrade, export the machine configuration and take screenshots of drill unit, drill changer, tool, clamp pressure, transport and saw settings. After the upgrade, compare them. Pay attention to:

- MachineZone values removed from Drill and DeburUnit (BT2-3879)
- PicoScan instances removed (BT2-3834)
- position correction moved from MeasureUnit to Saw (SWMS-11589)
- no object disabled by the BT1-2305 script that BT2-3827 removed again
- clamp pressure min/max values still valid under the new validation (BT1-2271)

## Smoke test per machine

Run on every machine at the start of its test week and again in week 8 (TC-433-027):

1. Cold start PLC and VACAM
2. Reference all axes
3. Load and run one standard job
4. Emergency stop during production and recovery
5. Door or fence interlock during production
6. Shut down and restart, settings kept

## Entry and exit criteria

- **Entry:** RC-4.33 installs cleanly over 4.32.17 and the machine references.
- **Exit:** all High cases passed or accepted by the PO, no open safety findings, smoke test passed on all six machines.

## Risks for the plan

- The PLC refactoring is wide. If week 1 to 3 show more than 3 regressions in one area, add exploratory time for that area in week 6 and tell development early.
- SWMS-11501 landed on 2026-09-30. More late fixes are likely. Check the RC branch every Monday.
- V633 brake behaviour (BT1-2332) needs confirmation from BT1 that the roller variant should skip the check.
