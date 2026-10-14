---
type: epic-testplan
jira: BT1-0000
title: "{{title}}"
fix_version: 4.xx.0
rc_branch: RC-4.xx.0
machines: [V630, V631, V633, VB Standard/VB1040/VB1250, V912]
risk: [Low, Moderate, High]
tester: Herbert Nijkamp
created: {{date}}
test_start:
test_end:
status: [draft, final]
tags: [testplan, epic]
---

# Epic test plan {{title}}

## 1. Goal

- **Jira:** [BT1-0000](https://voortman.atlassian.net/browse/BT1-0000)
- **What the customer can do after this epic:** one or two sentences. Example: "The operator can run a V631 job with mixed tool sets without manual tool changes."
- **Definition of done for testing:** which end-to-end scenario must run on which machine.

## 2. Scope

| Machine               | In scope | Why | Main risk on this machine |
| --------------------- | -------- | --- | ------------------------- |
| V630                  | Yes / No |     |                           |
| V631                  | Yes / No |     |                           |
| V633                  | Yes / No |     |                           |
| VB Standard / VB 1040 | Yes / No |     |                           |
| V912                  | Yes / No |     |                           |

**Out of scope:** what is not tested in this epic, and who covers it (other team, later epic, customer acceptance).

## 3. User Stories
User stories are linked to the Epic and have a specific test plan, except when noted that testing is not done by software tester.

## 4. Risks

| #   | Risk | Impact (1-3) | Likelihood (1-3) | Score | Covered by |
| --- | ---- | ------------ | ---------------- | ----- | ---------- |
| R1  |      |              |                  |       | BT1-0000   |
| R2  |      |              |                  |       |            |

Typical epic-level risks: two stories change the same object (`MachineZone`, `MeasureUnit`, `DrillChanger`), a new parameter has no default after upgrade, the workflow works per story but not in sequence, cycle time goes up.

## 5. End-to-end scenarios

### E2E-01 full workflow
- **Covers stories:** 
- **Type:** Scripted
- **Precondition:** VACAM version, machine configuration backup, test material

| #   | Step                            | Expected result                          |
| --- | ------------------------------- | ---------------------------------------- |
| 1   | Import the NC file in VACAM     | Part appears with the right operations   |
| 2   | Start the job in automatic mode |                                          |
| 3   |                                 |                                          |
| 4   | Job finished                    | Part matches the drawing, report correct |
- result:: open
### E2E-02 Exploratory, combined stories
- **Type:** Exploratory, timebox 90 min
- **Charter:** Explore workflow with mixed jobs, operator interruptions, restarts, act like a new user to find problems
- **Focus points:**
  - [ ] Order of operations when features from different stories run in one job
  - [ ] Stop, E-stop and restart in the middle of the new workflow
  - [ ] Switching between old and new behavior (parameter on/off)
- result:: open

## 6. Non-functional checks

- [ ] **Cycle time:** run the reference job on the old and new version. Old: ___ s, new: ___ s. Limit agreed with PO: ___ % (e.g. max +5 %).
- [ ] **Stability:** run ___ jobs or ___ hours in automatic mode without operator action. Errors: ___
- [ ] **Operator UI:** new screens and messages in English and at least one other language. No missing translations.
- [ ] **Logging:** new errors and warnings have a clear text and a cause the operator can act on.

## 7. Findings

| #   | Finding | Machine | Story | Jira bug | Severity | Status |
| --- | ------- | ------- | ----- | -------- | -------- | ------ |
| 1   |         |         |       |          |          |        |

## 8. Exit and sign-off

- [ ] Every story in section 3 has status Done/Closed or an accepted remark.
- [ ] Every in-scope machine has at least one passed E2E scenario.
- [ ] No open safety, collision or data-loss findings.

**Release advice:** [Go, Go with remarks, No go]
**Remarks:** 
**Signed off by:** Herbert
**Date:** 
