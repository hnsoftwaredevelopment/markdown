---
type: swms-testplan
jira: SWMS-00000
title: "{{title}}"
customer:
machine: [V630, V631, V633, VB Standard/VB 1050/1250, V912]
machine_config:
reported_version: 4.xx.x
fixed_version: 4.xx.x
reproducible: [yes, no]
Tester: Herbert Nijkamp
created:
  "{ date }":
status: [draft, final]
tags:
  - testplan
  - swms
---

# SWMS test plan {{title}}
## 1. Ticket

- **Jira:** [SWMS-00000](https://voortman.atlassian.net/browse/SWMS-00000)
- **Customer and site:** 
- **Machine and configuration:** 
- **Version at the customer:** VACAM 4.xx.x
- **Problem as reported:** quote the customer or service engineer in one or two sentences.
- **Impact for the customer:** machine stops / wrong part / scrap / safety / workaround available (which one).

## 2. Customer data

- [ ] Machine backup (configuration and parameters), date: 
- [ ] NC file or job that shows the problem: 
- [ ] VACAM log, time window around the problem: 
- [ ] TwinCAT event log or error code: 
- [ ] Screenshots or video from the operator: 
- [ ] Material details: profile, dimensions, grade

## 3. Reproduction

| #   | Step                      | Expected (correct) | Seen at customer |
| --- | ------------------------- | ------------------ | ---------------- |
| 1   | Load the customer backup  |                    |                  |
| 2   | Load the customer NC file |                    |                  |
| 3   |                           |                    |                  |

- [ ] Reproduced on machine in factory/VEC/VENG
- [ ] Reproduced in simulation only
- [ ] Not reproducible

### TC-SWMS-00000-02 Variations of the same problem
Change one input at a time: other profile size, other tool or angle, other speed, operator stop halfway, restart after E-stop.

| #   | Variation | Expected result | Result |
| --- | --------- | --------------- | ------ |
| 1   |           |                 |        |
| 2   |           |                 |        |

- result:: open

## 4. Regression around the fix

When code has changed that can effect other machines note what code and machines are changed.

| Function/Methothods  changed code | Effected machine | Result |
| --------------------------------- | ---------------- | ------ |
|                                   |                  |        |

- [ ] Fix also merged to develop, so it does not come back in the next RC.

Machine reminders (keep the line for the customer's machine, delete the rest):
- **V630:** tool change via cylinder changer, hole positions, clamp before drilling, unit retract before transport.
- **V631:** tool change on all 8 positions, ToolClamp feedback, Weiss spindle start and stop.
- **V633:** carousel positions, Suhner spindle start and stop, hole positions.
- **VB Standard / VB 1040:** straight and miter cuts, table rotation, saw feed, band tension and speed, cut-through detection. Note the configured saw type (`SawFixedRotatableTable` or `SawType_VB1x50` / `VBS1x50` / `VBS1x50b`).
- **V912:** LaserSafetyHandler config check, door interlock stops the laser, photocell front and end detection, X positioning with asynchronous drive, gripper.
- **All machines:** home, standard job, E-stop and recovery, restart, no new errors in VACAM log.

## 5. Findings

| #   | Finding | Machine | Jira | Severity | Status |
| --- | ------- | ------- | ---- | -------- | ------ |
| 1   |         |         |      |          |        |

## 8. Close

- [ ] Problem reproduced, or a written reason why not.
- [ ] Fix verified with the customer's data.
- [ ] Regression around the fix passed.
- [ ] Fix merged to develop.
- [ ] Short answer for service written in the SWMS ticket: what was wrong, which version fixes it, any action at the customer (parameter, update, restart).

**Verdict:** Fixed / Fixed with remarks / Not fixed / Cannot reproduce
**Signed off by:** Herbert
**Date:** 
