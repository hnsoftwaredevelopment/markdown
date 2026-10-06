---
type: swms-testplan
jira: SWMS-00000
title: "{{title}}"
customer:
site:
machine: V630 / V631 / V633 / VB Standard / VB 1040 / V912
machine_serial:
reported_version: 4.xx.x
fixed_version: 4.xx.x
backport_versions: []
priority: Normal
reproduced: unknown
tester: Herbert Nijkamp
created: {{date}}
status: draft
tags: [testplan, swms]
---

# SWMS test plan {{title}}

> [!info] How to use
> A support test answers three questions: can we reproduce the problem, does the fix solve it, and does the fix break anything around it. Fill section 2 before you touch a machine. Keep the customer's own data (backup, NC file, logs) as the main test input.

## 1. Ticket

- **Jira:** [SWMS-00000](https://voortman.atlassian.net/browse/SWMS-00000)
- **Linked development ticket:** [BT2-0000](https://voortman.atlassian.net/browse/BT2-0000)
- **Customer and site:** 
- **Machine and serial number:** 
- **Version at the customer:** VACAM 4.xx.x, PLC commit 
- **Problem as reported:** quote the customer or service engineer in one or two sentences.
- **Problem in test terms:** "When <condition>, the machine <wrong behaviour> instead of <expected behaviour>."
- **Impact for the customer:** machine stops / wrong part / scrap / safety / workaround available (which one).

## 2. Customer data

- [ ] Machine backup (configuration and parameters), date: 
- [ ] NC file or job that shows the problem: 
- [ ] VACAM log, time window around the problem: 
- [ ] TwinCAT event log or error code: 
- [ ] Screenshots or video from the operator: 
- [ ] Material details: profile, dimensions, grade

Missing data: ask the service engineer before testing. A guess at the configuration often leads to "cannot reproduce".

## 3. Reproduction

**Test machine:** ___ configured as ___ (same machine type and option set as the customer)
**Version:** same as the customer, 4.xx.x

| # | Step | Expected (correct) | Seen at customer |
|---|---|---|---|
| 1 | Load the customer backup | | |
| 2 | Load the customer NC file | | |
| 3 | | | |

- [ ] Reproduced on the test machine
- [ ] Reproduced in simulation only
- [ ] Not reproduced. Tried: 

**Root cause (from development):** 
**Affected code:** objects or files from the fix commit, e.g. `Main Objects/Drill_V2/...`

## 4. Fix verification

**Version with fix:** 4.xx.x, PLC commit 

### TC-SWMS-00000-01 Problem is gone
Repeat the steps from section 3 on the fixed version, same data.

| # | Step | Expected result |
|---|---|---|
| 1 | | |
| 2 | | |

- **Result:** - [ ] pass - [ ] fail
- result:: open

### TC-SWMS-00000-02 Variations of the same problem
Change one input at a time: other profile size, other tool or angle, other speed, operator stop halfway, restart after E-stop.

| # | Variation | Expected result | Result |
|---|---|---|---|
| 1 | | | |
| 2 | | | |

- result:: open

## 5. Regression around the fix

List the functions that use the changed code and test each once.

| Function that shares the changed code | Machine | Result |
|---|---|---|
| | | |

Machine reminders (keep the line for the customer's machine, delete the rest):

- **V630:** tool change via cylinder changer, hole positions, clamp before drilling, unit retract before transport.
- **V631:** tool change on all 8 positions, ToolClamp feedback, Weiss spindle start and stop.
- **V633:** carousel positions, Suhner spindle start and stop, hole positions.
- **VB Standard / VB 1040:** straight and miter cuts, table rotation, saw feed, band tension and speed, cut-through detection. Note the configured saw type (`SawFixedRotatableTable` or `SawType_VB1x50` / `VBS1x50` / `VBS1x50b`).
- **V912:** LaserSafetyHandler config check, door interlock stops the laser, photocell front and end detection, X positioning with asynchronous drive, gripper.
- **All machines:** home, standard job, E-stop and recovery, restart, no new errors in VACAM log.

## 6. Versions and backport

| Version | Fix present (commit) | Verified on | Result |
|---|---|---|---|
| 4.xx.x (customer version line) | | | |
| 4.xx.x (current release) | | | |
| RC-4.xx.0 / develop | | | |

- [ ] Fix also merged to develop, so it does not come back in the next RC.
- [ ] Upgrade path for the customer checked: from 4.xx.x to 4.xx.x, settings kept.

## 7. Findings

| # | Finding | Machine | Jira | Severity | Status |
|---|---|---|---|---|---|
| 1 | | | | | |

## 8. Close

- [ ] Problem reproduced, or a written reason why not.
- [ ] Fix verified with the customer's data.
- [ ] Regression around the fix passed.
- [ ] Fix present in all versions in section 6.
- [ ] Short answer for service written in the SWMS ticket: what was wrong, which version fixes it, any action at the customer (parameter, update, restart).

**Verdict:** Fixed / Fixed with remarks / Not fixed / Cannot reproduce
**Signed off by:** 
**Date:** 
