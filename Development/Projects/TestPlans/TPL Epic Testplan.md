---
type: epic-testplan
jira: BT2-0000
title: "{{title}}"
fix_version: 4.xx.0
rc_branch: RC-4.xx.0
machines: [V630, V631, V633, VB Standard / VB 1040, V912]
risk: High
tester: Herbert Nijkamp
created: {{date}}
test_start:
test_end:
status: draft
tags: [testplan, epic]
---

# Epic test plan {{title}}

> [!info] How to use
> The epic plan covers what single stories cannot: the full workflow, the combination of stories, cycle time, upgrade and release readiness. Story details stay in the story test plans ([[TPL User Story Testplan]]). Set `epic:` in each story plan to this epic's Jira key, so the table in section 3 fills itself.

## 1. Goal

- **Jira:** [BT2-0000](https://voortman.atlassian.net/browse/BT2-0000)
- **What the customer can do after this epic:** one or two sentences. Example: "The operator can run a V631 job with mixed tool sets without manual tool changes."
- **Definition of done for testing:** which end-to-end scenario must run on which machine.

## 2. Scope

| Machine | In scope | Why | Main risk on this machine |
|---|---|---|---|
| V630 | Yes / No | | |
| V631 | Yes / No | | |
| V633 | Yes / No | | |
| VB Standard / VB 1040 | Yes / No | | |
| V912 | Yes / No | | |

**Out of scope:** what is not tested in this epic, and who covers it (other team, later epic, customer acceptance).

## 3. Stories

```dataview
TABLE jira AS "Story", status, risk, machines
FROM #story
WHERE epic = this.jira
SORT jira ASC
```

Stories without a test plan (fill in by hand, check in Jira with `"Epic Link" = BT2-0000` or `parent = BT2-0000`):

| Story | Summary | Status in Jira | Test plan needed? |
|---|---|---|---|
| | | | Yes / No, reason |

## 4. Coverage matrix

Mark each cell: `T` = tested in the story plan, `E` = tested in this epic plan, `-` = not applicable.

| Story / scenario | V630 | V631 | V633 | VB | V912 |
|---|---|---|---|---|---|
| BT2-0000 | | | | | |
| E2E-01 | | | | | |

A column with only `-` while the machine is in scope means a gap. Fix it before the test period starts.

## 5. Risks

| # | Risk | Impact (1-3) | Likelihood (1-3) | Score | Covered by |
|---|---|---|---|---|---|
| R1 | | | | | E2E-01, BT2-0000 |
| R2 | | | | | |

Typical epic-level risks: two stories change the same object (`MachineZone`, `MeasureUnit`, `DrillChanger`), a new parameter has no default after upgrade, the workflow works per story but not in sequence, cycle time goes up.

## 6. End-to-end scenarios

### E2E-01 <full workflow> (<machines>)
- **Covers stories:** 
- **Type:** Scripted
- **Precondition:** VACAM version, machine configuration backup, test material

| # | Step | Expected result |
|---|---|---|
| 1 | Import the NC file in VACAM | Part appears with the right operations |
| 2 | Start the job in automatic mode | |
| 3 | | |
| 4 | Job finished | Part matches the drawing, report correct |

- **Result:** - [ ] V630 - [ ] V631 - [ ] V633 - [ ] VB - [ ] V912
- result:: open

### E2E-02 Exploratory, combined stories (<machines>)
- **Type:** Exploratory, timebox 90 min
- **Charter:** Explore <workflow> with <mixed jobs, operator interruptions, restarts> to find problems that only show when the stories work together.
- **Focus points:**
  - [ ] Order of operations when features from different stories run in one job
  - [ ] Stop, E-stop and restart in the middle of the new workflow
  - [ ] Switching between old and new behaviour (parameter on/off)
- result:: open

## 7. Non-functional checks

- [ ] **Cycle time:** run the reference job on the old and new version. Old: ___ s, new: ___ s. Limit agreed with PO: ___ % (e.g. max +5 %).
- [ ] **Stability:** run ___ jobs or ___ hours in automatic mode without operator action. Errors: ___
- [ ] **Operator UI:** new screens and messages in English and at least one other language. No missing translations.
- [ ] **Logging:** new errors and warnings have a clear text and a cause the operator can act on.

## 8. Upgrade and release readiness

- [ ] Upgrade from the current field version (4.xx.x) on one drill line and one saw line (plus V912 when in scope).
- [ ] All new parameters and configuration items listed with default value:

| Parameter / config item | Default after upgrade | Checked on |
|---|---|---|
| | | |

- [ ] Rollback to the previous version works and the machine runs the reference job.
- [ ] Manual, release notes and service documentation updated (link): 

## 9. Schedule

| Week | Machine | Focus | Stories / scenarios |
|---|---|---|---|
| 1 | | High risks, safety, configuration | |
| 2 | | | |
| 3 | | | |
| 4 | | Retest of fixes, E2E on all machines in scope | |

## 10. Findings

| # | Finding | Machine | Story | Jira bug | Severity | Status |
|---|---|---|---|---|---|---|
| 1 | | | | | | |

## 11. Exit and sign-off

- [ ] Every story in section 3 has status Pass or an accepted remark.
- [ ] Every in-scope machine has at least one passed E2E scenario.
- [ ] No open safety, collision or data-loss findings.
- [ ] Cycle time within the agreed limit.
- [ ] Upgrade test passed.

**Release advice:** Go / Go with remarks / No go
**Remarks:** 
**Signed off by:** 
**Date:** 
