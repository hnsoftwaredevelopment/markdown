---
name: rc-risk-testplan
description: Builds the RC risk analysis, test plan, test cases and BT1 other-team alerts for a VACAM Release Candidate (e.g. "Create a risk analysis and testplan for RC 4.33") for Herbert's drill and saw machines, as Obsidian notes.
---

# RC risk analysis and test plan (VACAM, drill and saw lines)

Every 8 weeks a new Release Candidate (RC) is cut from `vacam-twincat`. Herbert has 8 weeks to test it on his machines before release. This skill turns the RC's git changes plus the Jira tickets behind them into four Obsidian notes:

- `RC-4.33 Analysis.md` (what changed, per machine, with risk level)
- `RC-4.33 Testplan.md` (what to test, on which machine, in which order)
- `RC-4.33 Test cases.md` (concrete test cases with checkboxes Herbert ticks off)
- `RC-4.33 Other team alerts.md` (BT1 tickets that can change behaviour on machines outside Herbert's set, so he can warn the testers of those machines)

Use the RC number from the request in every file name. "RC 4,33", "RC-4.33", "4.33" and "rc433" all mean RC `4.33`, branch `RC-4.33.0`.

Write all notes in English, in Herbert's style: short active sentences, concrete numbers, no em dashes, no filler. Apply the `avoid-ai-writing-patterns` skill to every note before saving.

## Fixed context

| Item | Value |
|---|---|
| Local repo | `C:\Git\vacam-twincat` (Windows laptop, reach it with `mcp__remote-devices__Desktop_Commander__start_process`, PowerShell) |
| Remote | `voortman-steel-machinery/vacam-twincat` on GitHub (no direct GitHub access from the cloud; always use the local clone) |
| RC branch | `origin/RC-X.YY.0` (e.g. `origin/RC-4.33.0`) |
| Baseline | highest patch tag of the previous RC: `git tag --list "4.32.*" --sort=-v:refname`, first line (for RC 4.33 that was `4.32.17` on 2026-10-02) |
| Output folder | `C:\DevOps\hnsoftwaredevelopment\Obsidian\Work\Voortman\RC-Testing\` |
| Raw data folder | `...\RC-Testing\_data\RC-X.YY\` (git exports, `analysis.json`, `jira.tsv`) |
| Script folder | `...\RC-Testing\_tools\rc_classify.py` (copy in the appendix below) |
| Jira | cloudId `2e7a5d2f-08b7-405e-8a40-ff02b3b9f183` (voortman.atlassian.net). Relevant projects: BT1, BT2, SWMS |
| PractiTest | optional, via the `practitest-access` skill, dry run first |

The baseline is "what runs in the field now". Comparing the RC against the last patch of the previous RC shows exactly what is new for a customer who upgrades.

## Machines in scope and how they show up in the code

The code does not use sales names for every machine. This table is the mapping the classifier uses. When a run shows a mapping is wrong, fix it here and in `RULES` in the script, and tell Herbert.

| Test machine | Code signals | Notes |
|---|---|---|
| V630 | `MachineType_V630`, `V630` in path or name, `Main Objects/Drill/` (old drill object), `DrillChangerType_Cylinder` | `MachineType_V630MK2` also exists. Include it under V630 only if Herbert asks |
| V631 | `MachineType_V631`, `V631`, `Main Objects/Drill_V2`, `ToolClamp`, `DrillChangerType_AirCylinder8Pos` | Weiss spindle |
| V633 | `MachineType_V633`, `V633`, `Suhner`, `Drill_V2`, `DrillChangerType_CarouselCylinder` | Variants V633M (roller measuring) and V633T (gripper truck) exist in config code |
| Drill lines shared | `DrillZone`, `DrillChanger`, `FB_DrillingAdapter` | Affects V630, V631 and V633 |
| VB Standard | `SawFixedRotatableTable`, `VB_Standard`, `SawBandControl` | Saw with fixed, rotatable table |
| WB Standard + Probe Truck | `MachineType_V100StandAlone`, `ProbeTruck`, `V100StandAloneIntegration`, plus `SawFixedRotatableTable` | Assumed to be the standalone saw with probe truck. Confirm with Herbert |
| VB 1040 | `Saw/OldStyle`, `E_SawType` values `SawType_VB1x50`, `SawType_VBS1x50`, `SawType_VBS1x50b`, `VB1050`/`VB1250` | No "1040" exists in the code. Herbert said to use the VB1050/1250 family |
| All machines | `twincat/src` core (`Machine`, `MachineZone`, `-MAIN`, `Transport`, `Conveyor`, `MeasureUnit`, `TransportManager`, safety, collision, configuration) and `vacam/` application code | Shared code. A change here is tested on at least one drill and one saw line |

Skipped on purpose: V631MK2 and V633MK2 (Herbert's decision, they have no separate machine type).

Out of scope for the main analysis: Fabricator (`FAB-*`), robotics and material handling library (`MCPL-*`) unless the commit touches drill or saw files, laser (`V35X-*`, V353, V912), coping (V807/V808), V623, plate machines (V310, V304, V303, V210, V325), DevOps and test infrastructure. Tests, docs and GitHub workflows count as "no machine behaviour". BT1 changes to those machines go in the Other team alerts note.

## Step 0: set up

1. Parse the RC number. Set `RC=4.33`, `BRANCH=RC-4.33.0`, `PREV=4.32`.
2. Create a task list (TaskCreate): update repo, export git data, classify, Jira, read diffs of High areas, BT1 alerts, write Analysis, write Testplan, write Test cases, write Other team alerts, verify, save.
3. Check the output folder for existing notes:
   - `RC-<PREV> Analysis.md`: read it. Use it to spot repeating risk areas and to compare numbers.
   - `RC-<RC> *.md` already present: this is a **re-run** during the test period. Follow "Re-run" below, never overwrite blindly.

## Step 1: update the repo (read-only use)

Run in PowerShell via Desktop Commander, one `start_process` call per step:

```
cd C:\Git\vacam-twincat; git status -sb | Select-Object -First 3; git fetch --all --prune --tags 2>&1 | Select-Object -Last 5
```

Rules:
- Only `fetch`. Do not `checkout`, `pull`, `reset` or `merge`. The local `develop` can have Herbert's own commits (on 2026-10-02 it was "ahead 3"). All analysis reads refs (`origin/RC-4.33.0`, tags), so the working tree does not matter.
- Check that `origin/RC-<RC>.0` exists: `git branch -r --list "origin/RC-4.33.0"`. If not, list `git branch -r | Select-String "RC-4\."` and ask Herbert which branch he means.
- Find the baseline: `git tag --list "4.32.*" --sort=-v:refname | Select-Object -First 1`. If no tag exists, ask.
- Record: RC tip hash and date (`git log -1 --format="%h %cI" origin/RC-4.33.0`), baseline tag and its hash. These go in the frontmatter. The RC branch keeps moving during the 8 weeks, so the hash shows which state was analysed.

## Step 2: export the change set

Write the exports into the connected RC-Testing folder so they can be staged:

```
cd C:\Git\vacam-twincat; New-Item -ItemType Directory -Force -Path 'C:\DevOps\hnsoftwaredevelopment\Obsidian\Work\Voortman\RC-Testing\_data\RC-4.33' | Out-Null; git log 4.32.17..origin/RC-4.33.0 --no-merges --name-only --format='@@@%H|%h|%cI|%an|%s' | Out-File -FilePath 'C:\DevOps\hnsoftwaredevelopment\Obsidian\Work\Voortman\RC-Testing\_data\RC-4.33\commits.txt' -Encoding utf8; git diff --numstat --no-renames 4.32.17 origin/RC-4.33.0 | Out-File -FilePath 'C:\DevOps\hnsoftwaredevelopment\Obsidian\Work\Voortman\RC-Testing\_data\RC-4.33\numstat.txt' -Encoding utf8
```

Reference size for RC 4.33 vs 4.32.17: 2,937 commits, about 4,685 changed files. This is a monorepo, so most commits belong to other product lines. Do not report raw totals as "risk".

PowerShell notes: send one command line per `start_process`. If a `$variable` gets stripped, avoid variables and write intermediate results to a file with `Out-File`, then read it back in a new call.

## Step 3: classify with the script

1. Stage `_data\RC-4.33\commits.txt`, `numstat.txt` and `_tools\rc_classify.py` with `device_stage_files`. If `_tools\rc_classify.py` is missing, write it from the appendix to the scratchpad and also commit a copy to `_tools\` for next time.
2. Run `python3 rc_classify.py commits.txt numstat.txt analysis.json` in the cloud workspace.
3. The script tags every file with an area and the machines it affects, drops out-of-scope product lines, and gives each area a first risk score: impact (3 for safety/collision, configuration/upgrade, cycle list; 2 otherwise; minus 1 if only one machine is touched) times likelihood (1 to 3 by commit count and changed lines). 6 or more is High, 3 to 5 Medium, below 3 Low.
4. Sanity check the output. For RC 4.33 the result was 1,132 of 2,937 commits relevant, 111 ticket keys, 16 areas, 23 BT1 alert entries. If almost every commit lands in "VACAM application" or "PLC core", the rules are too broad: inspect the top files and tighten `RULES`.
5. The score is a triage, not the final answer. Step 5 adjusts it with what the diffs and tickets show.

## Step 4: Jira enrichment

1. Take the ticket keys from `analysis.json` (`tickets` plus the `ticket` of every `bt1_alerts` entry). Look up BT1, BT2 and SWMS keys. Look up a FAB/MCPL key only if its commits touch drill or saw files (they are in machine-specific areas in the output).
2. Use `searchJiraIssuesUsingJql` with `key in (...)` and `fields: ["summary","status","issuetype","priority","labels"]`, `maxResults: 50`. With an explicit `fields` list the description is left out, so 20 to 45 keys per call work (tested 2026-10-02). If a result is too large it is saved to a file: read it with `jq -r '.issues.nodes[] | [.key,.fields.issuetype.name,.fields.status.name,.fields.priority.name,.fields.summary] | @tsv'`. Store every ticket in a `jira.tsv` (key, type, status, priority, summary) and commit it to `_data\RC-4.33\`. Use `getJiraIssue` only when you need the description of one ticket.
3. Adjust risk with Jira facts:
   - Bug fix in safety, collision, clamping or positioning: raise to High.
   - Ticket mentions a customer site, a field issue or "RC" test: raise one level.
   - Ticket status To Do / Rejected / Canceled but code is in the RC: flag it in the Analysis ("code without finished ticket").
   - Refactoring with no functional change and green tests: may lower one level, say why.
4. Tickets with BT1/BT2/SWMS in Jira for fixVersion `4.33.0` that have no commit in the range: list them in the Analysis as "in Jira, not found in code". Do not make test cases for them. On 2026-10-02 `fixVersion = "4.33.0"` returned 0 tickets for BT1, BT2 and SWMS: then say in Findings that the cross-check was not possible.
5. Check for invalid keys: a key that Jira does not return (e.g. `BT1-11254` in RC 4.33, which was SWMS-11254) is a typo. Name the commit and the likely correct key in Findings.

## Step 5: read the High-risk changes

For every High area, and every area that touches only one or two of Herbert's machines:
- Read the commit subjects and the top changed files from `analysis.json`.
- Read the actual diff for the most changed files: `git diff 4.32.17 origin/RC-4.33.0 -- "<path>"` (Desktop Commander, cap output with `Select-Object -First 300`).
- Write down in plain words what behaviour can change on the machine: e.g. "drill unit 4 now checks the horizontal clamp position before moving in Z", "probe truck search speed is a new parameter". This sentence is what Herbert tests. A file name alone is not a risk description.
- Note new or changed machine parameters and configuration items. Every new parameter needs a check that the upgrade keeps or sets a sane default.

## Step 5b: BT1 other team alerts

Herbert also wants to know which Beam Team 1 changes can affect machines he does not test. In RC 4.33 BT1 mostly worked on the V912 (outfeed gripper, movable conveyor, material control), but it changed shared code too.

1. The script writes `bt1_alerts` in `analysis.json`: one entry per BT1 ticket with
   - `direct`: other machine types whose files the ticket touched (rules in `OTHER_MACHINES`: Fabricator, V912, V353, V807/V808, V623, plate machines, V325, V613, blasting/marking, material handling and transverse transport, CNC/robot motion),
   - `shared`: shared areas (configuration, transport, measuring, safety, cycle list, PLC core, VACAM application) that run on every machine type,
   - `own_machines`: Herbert's machines that are also touched directly.
   Per-file churn in the output is the RC total for that file, not per ticket. Do not report it as the size of a ticket.
2. Use the Jira data from Step 4 for status and summary. Flag BT1 tickets that are not Done (In Progress, Analysis Review, Ready to Develop) and invalid BT1 keys.
3. For the most important shared changes (transport groups, measuring unit, collision models, config migration script, object registry) read the commit subjects and, where needed, a diff, so the note says what changed in plain words.
4. Cross-reference: BT1 changes that also hit Herbert's own machines go in the Analysis and get a test case. The alerts note links to those case IDs.

## Step 6: write the four notes

Write each note to `/mnt/user-data/outputs/` with the Write tool, then commit it with `device_commit_files` to `C:\DevOps\hnsoftwaredevelopment\Obsidian\Work\Voortman\RC-Testing\<name>.md`. Use Obsidian features: YAML frontmatter, `[[wikilinks]]` between the four notes, callouts (`> [!danger]`, `> [!warning]`, `> [!info]`), tables, and `- [ ]` checkboxes.

Common frontmatter:

```yaml
---
rc: "4.33"
branch: RC-4.33.0
rc_commit: ed77b6064c4
rc_commit_date: 2026-10-01
baseline: 4.32.17
analysed: 2026-10-02
machines: [V630, V631, V633, VB Standard, WB Standard + Probe Truck, VB 1040]
tags: [rc-testing, rc-4-33]
---
```

### `RC-4.33 Analysis.md`

1. **Summary** (5 to 8 lines): commits in range, relevant commits, tickets, number of High/Medium/Low areas, the 3 biggest risks in one line each, compared with `[[RC-4.32 Analysis]]` if it exists.
2. **Scope**: baseline, RC commit, machines, what was excluded and why.
3. **Risk matrix**: table `Area | Risk | Machines | Commits | Key tickets | What can change on the machine`. Sorted High first. Add one cross-cutting row for large refactorings that span many areas.
4. **Per machine**: one `###` section per test machine with its areas, its tickets, and a one-line verdict ("Full regression needed", "Focus on saw feed and clamping", "Shared changes only").
5. **Ticket list**: table `Ticket | Type | Status | Summary | Area | Machines`. Link tickets as `[BT2-3857](https://voortman.atlassian.net/browse/BT2-3857)`.
6. **Findings**: code without a finished ticket, Jira tickets without code, invalid keys, reverts, migrations added and removed, large late changes (commits in the last 14 days before the RC tip), new parameters with old and new values.
7. **Method**: one short paragraph so a reader knows how the risk was scored.

### `RC-4.33 Other team alerts.md`

Frontmatter as above plus `team: BT1`.

1. **Summary**: number of BT1 tickets with code, how many touch other machine types directly, how many change shared code, unfinished or invalid tickets. A `> [!danger]` callout with the top 3 alerts.
2. **Direct impact on other machines**: table `Machine | Ticket | Status | What changed | Files`. Put the V912 (BT1's own machine) in a separate short table "for completeness".
3. **Shared code changed by BT1**: table `Shared area | Tickets | Files | Who should look at it`.
4. **Impact on your own machines**: the BT1 changes that hit Herbert's machines, with the TC IDs that cover them.
5. **Suggested messages**: one line per affected team or machine that Herbert can paste into Teams or mail.
6. **Method**: one short paragraph.

### `RC-4.33 Testplan.md`

1. **Goal and period**: RC commit, start date, release date (start + 8 weeks).
2. **Priorities**: High areas first, then Medium. Low only as smoke test.
3. **Machine by week schedule**: table `Week | Dates | Machine | Focus areas | Test cases`. Spread 8 weeks; put the High safety and configuration tests in week 1 and 2 so findings reach development in time. Leave week 7 and 8 for retest of fixes and a final smoke test on every machine.
4. **Upgrade test**: always include an upgrade from the baseline (`4.32.x`) to the RC on at least one drill line and one saw line, with a check of machine parameters and configuration after the upgrade. List the migration changes to check.
5. **Smoke test per machine**: home all axes, load and run one standard job, emergency stop and recovery, door/fence interlock, shutdown and restart.
6. **Entry and exit criteria**: entry = RC installs cleanly; exit = all High cases passed or accepted by the PO, no open safety findings.
7. **Links**: `[[RC-4.33 Analysis]]`, `[[RC-4.33 Test cases]]`, `[[RC-4.33 Other team alerts]]`.

### `RC-4.33 Test cases.md`

- ID format `TC-433-001`, numbered in plan order.
- Each case:

```markdown
### TC-433-001 Drill unit 4 clamp check before Z move (V633)
status:: open
- **Risk:** High, area Drill V633, tickets [SWMS-11520](...)
- **Why:** one sentence on what changed and what can go wrong.
- **Machines:** V633
- **Type:** Scripted | Exploratory (timebox 60 min)
- **Precondition:** ...
| # | Step | Expected result |
|---|------|-----------------|
| 1 | ... | ... |
- **Result:** - [ ] V633 pass  - [ ] V633 fail
- **Notes:**
```

- Exploratory cases get a charter ("Explore <area> with <resources> to find <risk>") and 3 to 6 concrete focus points instead of steps.
- One case per behaviour change, not per ticket. Group tickets that change the same behaviour. Aim for 15 to 40 cases per RC.
- Shared-code cases list one drill line and one saw line as minimum machines.
- End the note with a status count table. The inline `status::` field per case lets Herbert query progress with Dataview.

## Step 7: verify before saving

- Every High area has at least one test case. Every test case points to an area and a ticket or commit.
- Every machine in scope appears in the Testplan schedule.
- Numbers in the Analysis match `analysis.json`.
- File names are exactly `RC-4.33 Analysis.md`, `RC-4.33 Testplan.md`, `RC-4.33 Test cases.md`, `RC-4.33 Other team alerts.md`.
- Counts in the alerts note match `bt1_alerts` (count the invalid key separately).
- Wikilinks resolve to those names.
- Run the prose through the `avoid-ai-writing-patterns` check (grep for the em dash character, it must return 0).

## Step 8: deliver and save

1. Commit the four notes to the output folder. Commit `analysis.json` and `jira.tsv` to `_data\RC-4.33\` and the current script to `_tools\rc_classify.py`.
2. Tell Herbert in 3 to 5 lines: where the files are, the number of High areas, the top 3 risks, the top BT1 alerts, anything you need him to confirm (machine mapping, odd findings).
3. Save a short summary (RC, baseline, commit, counts, top risks, BT1 alerts, mapping changes) to the Claude Project with `project_write` at `claude/RC-4.33 summary.md`.
4. Offer the PractiTest push. If he says yes, use the `practitest-access` skill: build the bulk-import JSON from the test cases and run it **without** `--commit` first. Only commit after he approves the dry run.

## Re-run during the test period

When notes for the same RC already exist (Herbert asks again after new commits on the RC branch):

1. Read the existing notes (stage them). Get the old `rc_commit` from the frontmatter.
2. Export only the new commits: `git log <old rc_commit>..origin/RC-4.33.0 --no-merges --name-only ...` and classify them.
3. In the Analysis, add a section `## Update <date> (<old>..<new>)` at the top with the new changes and risk. Update the frontmatter `rc_commit`.
4. In Test cases, **keep every existing case and its checkbox state and notes unchanged**. Add new cases with the next free ID. If a new commit touches an area whose cases already passed, add a line `- [ ] Retest after <commit>` to those cases.
5. In the Testplan, adjust the remaining weeks only.
6. In Other team alerts, add an `## Update <date>` section with new BT1 tickets only.
7. Commit with `expectedMtimeMs` from staging, so Herbert's edits in Obsidian are never overwritten. If the commit is refused, stage again and merge.

## Lessons from earlier runs

- RC 4.33 (2026-10-02): the biggest risk was a PLC refactoring (MCPL layer violations, BT2 decoupling of Drill, MeasureUnit, Saw, MaterialClamping), about 185 tagged commits with no intended behaviour change. Expect more of this in later RCs. Treat it as one cross-cutting risk with exploratory regression on every machine.
- `MC_BranchScript.sql` (config migration) was changed by 20 tickets in RC 4.33. Always list the tickets that touch it: `git log <base>..<rc> --no-merges --format="%h %s" -- "*MC_BranchScript.sql"`.
- A migration can be added and removed again in the same RC (BT1-2305 then BT2-3827). Check the final state, and still test the upgrade.
- Read the final file on the RC (`git show origin/RC-4.33.0:<path>`) before describing behaviour. Single commits can be reverted later (BT2-3694 reduced speed was added and removed).
- Desktop Commander PowerShell handled `$_` and `foreach` fine on 2026-10-02. Long `foreach` output can stop early: use `read_process_output` or split the command.

## Appendix: `rc_classify.py`

Keep this copy in sync with `RC-Testing\_tools\rc_classify.py`. When you change the rules on a run, update both and mention it to Herbert.

```python
#!/usr/bin/env python3
"""Classify RC commits by machine relevance and functional area.

Usage: python3 rc_classify.py <commits.txt> <numstat.txt> <out.json>
commits.txt: git log <base>..<rc> --no-merges --name-only --format='@@@%H|%h|%cI|%an|%s'
numstat.txt: git diff --numstat --no-renames <base> <rc>
"""
import json, re, sys
from collections import defaultdict

ALL = ["V630", "V631", "V633", "VB Standard", "WB Standard + Probe Truck", "VB 1040/1250"]
DRILL = ["V630", "V631", "V633"]
SAW = ["VB Standard", "WB Standard + Probe Truck", "VB 1040/1250"]

# (regex on path or subject, machines, area). First match per file wins, so specific rules go first.
RULES = [
    # out of scope product lines
    (r"fabricator|/Fab[A-Z]|FabXml|V912|V35X|V353|LARS|V807|V808|V80x|V623|Transport_V623|"
     r"Laser|Plasma|Robot|Manipulator|ProfileCutter|Punch|Shear|ShotBlaster|PaintDry|"
     r"CuttingUnit|V310|V325|V304|V303|V210|NozzleHandler|GasController|ChainLifter|Trolley|"
     r"MoveableScanner|AutomaticPlateMeasurer|Chiller|LoadingCrane|InterpolationManager|"
     r"KinematicTransformation|Machine\.Robotics|Machine\.Plates|WeldAssemblies|PathValidation|"
     r"ImprintUnit|MovableConveyor", [], "Out of scope"),
    # tests, docs, build: no machine behaviour
    (r"^(docs/|\.github/|vacam/Tests/|twincat/test/|twincat/UnitTest|twincat/BDD|twincat/TestDriver|twincat/src/UnitTest)", [], "Test/Docs/Build"),
    (r"TranslationResources|\.resx$|phrase", ALL, "Translations / UI text"),
    # machine specific
    (r"ProbeTruck|V100StandAlone", ["WB Standard + Probe Truck"], "Probe truck / standalone saw"),
    (r"SawFixedRotatableTable|VB_?Standard", ["VB Standard", "WB Standard + Probe Truck"], "Saw (fixed rotatable table)"),
    (r"Saw/OldStyle|E_SawType|VBS?1x50|VB1[0-9]50", ["VB 1040/1250"], "Saw (VB1050/1250 old style)"),
    (r"Saw|SawBand|ShortPieceRemover", SAW, "Saw shared"),
    (r"V630", ["V630"], "Drill V630"),
    (r"V631", ["V631"], "Drill V631"),
    (r"V633|Suhner", ["V633"], "Drill V633"),
    (r"Main Objects/Drill_V2|ToolClamp", ["V631", "V633"], "Drill V2 (V631/V633)"),
    (r"Main Objects/Drill/|DrillZone|DrillChanger|Drill", DRILL, "Drill shared"),
    # shared core, affects every machine
    (r"twincat/src/.*(Safety|DoorControl|SystemControl|Collision)|vacam/.*Collision", ALL, "Safety / collision"),
    (r"twincat/src/-MAIN/ApplicationConfiguration|MachineHardCoded|_Global Variables|Migrat|Upgrade|"
     r"VacamInstaller|Voortman\.Backups|Voortman\.Settings|VersionCheck|MachineConfiguration", ALL, "Configuration / upgrade"),
    (r"Transport|Conveyor|RollerConveyor|MaterialClamp|Clamp|MeasureUnit|MeasureRoll|DisplacementSensor|Carriage", ALL, "Material transport / measuring"),
    (r"CycleList|Cyclelist|Command|Interpreter|ProcessController|Automatic", ALL, "Cycle list / process control"),
    (r"^twincat/src/|^twincat/MachineControl", ALL, "PLC core"),
    (r"^vacam/", ALL, "VACAM application"),
]
RULES = [(re.compile(p, re.I), m, a) for p, m, a in RULES]
OUT_PREFIXES = {"FAB", "MCPL", "V35X", "V353", "SYS", "DEVOPS", "TST"}
MACHINE_SPECIFIC_AREAS = {"Probe truck / standalone saw", "Saw (fixed rotatable table)", "Saw (VB1050/1250 old style)",
                          "Saw shared", "Drill V630", "Drill V631", "Drill V633", "Drill V2 (V631/V633)", "Drill shared"}
# Other teams' machines, used for the BT1 "Other team alerts" note. First match wins.
OTHER_MACHINES = [
    (r"Fabricator|/Fab[A-Z]|FabXml|WeldAssemblies|Machine\.Robotics|ChainLifter|Trolley", "Fabricator"),
    (r"V912", "V912 profile laser"),
    (r"V35X|V353|LARS|Machine\.Plates|LaserHead|LaserSource|LaserBeam|NozzleHandler|NozzlePositioner|GasController|Chiller", "V353 plate laser"),
    (r"V807|V808|V80x|Plasma|ProfileCutter|Manipulator|Robot", "V807/V808 coping robot"),
    (r"V623|Transport_V623|SawIntegratedShortPieceRemover|ToolStorage|ToolManipulator|MaterialPusher|OutfeedTable", "V623"),
    (r"V310|V304|V303|V210|CuttingUnit|Punch|Shear|AutomaticPlateMeasurer|MoveableScanner", "Plate machines (V30x/V310/V210)"),
    (r"V325|Carousel/", "V325"),
    (r"V613", "V613"),
    (r"ShotBlaster|VSB|PaintDry|Primer|InkJet|ImprintUnit|V704", "Blasting/marking (VSB, VP, V704)"),
    (r"LoadingCrane|V3000|VCT|TranverseTransport|LoadingPanel", "Material handling (V3000/VCT/crane)"),
    (r"InterpolationManager|KinematicTransformation|PathValidation", "CNC/robot motion (laser, coping)"),
]
OTHER_MACHINES = [(re.compile(p, re.I), n) for p, n in OTHER_MACHINES]
ALERT_PREFIX = "BT1"
HIGH_IMPACT = {"Safety / collision", "Configuration / upgrade", "Cycle list / process control"}
KEY_RE = re.compile(r"\b(BT1|BT2|SWMS|TST|FAB|V35X|MCPL|SYS|DEVOPS)-\d+\b", re.I)


def classify(path):
    for rx, machines, area in RULES:
        if rx.search(path):
            return machines, area
    return [], "Other"


def main(commits_path, numstat_path, out_path):
    churn = {}
    for line in open(numstat_path, encoding="utf-8-sig"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) == 3:
            a, d, p = parts
            churn[p] = (int(a) if a.isdigit() else 0) + (int(d) if d.isdigit() else 0)

    commits, cur = [], None
    for line in open(commits_path, encoding="utf-8-sig"):
        line = line.rstrip("\n")
        if line.startswith("@@@"):
            h, sh, date, author, subj = line[3:].split("|", 4)
            cur = {"hash": h, "short": sh, "date": date, "author": author, "subject": subj, "files": []}
            commits.append(cur)
        elif line.strip() and cur is not None:
            cur["files"].append(line.strip())

    areas = defaultdict(lambda: {"commits": set(), "files": set(), "machines": set(), "tickets": set(), "churn": 0})
    machine_hits = defaultdict(lambda: {"commits": set(), "areas": set(), "tickets": set()})
    relevant = []
    for c in commits:
        keys = sorted({m.group(0).upper() for m in KEY_RE.finditer(c["subject"])})
        c["tickets"] = keys
        c_machines, c_areas = set(), set()
        other_line = bool(keys) and all(k.split("-")[0] in OUT_PREFIXES for k in keys)
        c["other_line"] = other_line
        for f in c["files"]:
            ms, area = classify(f)
            if not ms:
                continue
            if other_line and area not in MACHINE_SPECIFIC_AREAS:
                continue
            c_machines.update(ms); c_areas.add(area)
            A = areas[area]
            A["commits"].add(c["short"]); A["machines"].update(ms); A["tickets"].update(keys)
            if f not in A["files"]:
                A["files"].add(f); A["churn"] += churn.get(f, 0)
        # subject can name a machine even if the path does not
        for rx, ms, area in RULES[3:12]:
            if rx.search(c["subject"]) and not other_line:
                c_machines.update(ms)
        if c_machines:
            c["machines"], c["areas"] = sorted(c_machines), sorted(c_areas)
            relevant.append(c)
            for m in c_machines:
                machine_hits[m]["commits"].add(c["short"]); machine_hits[m]["areas"].update(c_areas)
                machine_hits[m]["tickets"].update(keys)

    # BT1 tickets that touch other teams' machines (direct) or shared code (indirect)
    alerts = defaultdict(lambda: {"commits": set(), "direct": defaultdict(set), "shared": defaultdict(set),
                                  "own": set(), "subjects": [], "dates": []})
    for c in commits:
        bt1 = [k for k in c["tickets"] if k.startswith(ALERT_PREFIX + "-")]
        if not bt1:
            continue
        for f in c["files"]:
            if re.search(r"^(docs/|\.github/|vacam/Tests/|twincat/test/|twincat/UnitTest|twincat/BDD|twincat/TestDriver|twincat/src/UnitTest)", f):
                continue
            other = next((n for rx, n in OTHER_MACHINES if rx.search(f)), None)
            ms, area = classify(f)
            for k in bt1:
                T = alerts[k]
                T["commits"].add(c["short"])
                if c["subject"] not in T["subjects"]:
                    T["subjects"].append(c["subject"]); T["dates"].append(c["date"][:10])
                if other:
                    T["direct"][other].add(f)
                elif set(ms) == set(ALL) and area != "Translations / UI text":
                    T["shared"][area].add(f)
                if ms and set(ms) != set(ALL):
                    T["own"].update(ms)
    bt1_alerts = []
    for k, T in alerts.items():
        if not T["direct"] and not T["shared"]:
            continue
        lines = lambda files: sum(churn.get(f, 0) for f in files)
        bt1_alerts.append({
            "ticket": k, "commits": len(T["commits"]), "last_date": max(T["dates"]),
            "subjects": T["subjects"][:8],
            "direct": {n: {"files": len(fs), "churn": lines(fs), "top": sorted(fs, key=lambda f: -churn.get(f, 0))[:5]}
                       for n, fs in sorted(T["direct"].items())},
            "shared": {a: {"files": len(fs), "churn": lines(fs), "top": sorted(fs, key=lambda f: -churn.get(f, 0))[:5]}
                       for a, fs in sorted(T["shared"].items())},
            "own_machines": sorted(T["own"]),
            "level": "Direct" if T["direct"] else "Shared code",
        })
    bt1_alerts.sort(key=lambda x: (x["level"] != "Direct", -sum(v["churn"] for v in list(x["direct"].values()) + list(x["shared"].values()))))

    def score(name, A):
        impact = 3 if name in HIGH_IMPACT else 2
        if len(A["machines"]) <= 1:
            impact -= 1 if impact > 1 else 0
        n = len(A["commits"])
        likelihood = 3 if (n >= 15 or A["churn"] >= 1500) else 2 if (n >= 4 or A["churn"] >= 300) else 1
        s = impact * likelihood
        return s, ("High" if s >= 6 else "Medium" if s >= 3 else "Low")

    out_areas = []
    for name, A in areas.items():
        s, lvl = score(name, A)
        out_areas.append({"area": name, "risk_score": s, "risk": lvl, "commits": len(A["commits"]),
                          "files": len(A["files"]), "churn": A["churn"], "machines": sorted(A["machines"]),
                          "tickets": sorted(A["tickets"]), "top_files": sorted(A["files"], key=lambda f: -churn.get(f, 0))[:10]})
    out_areas.sort(key=lambda x: (-x["risk_score"], -x["commits"]))

    result = {
        "total_commits": len(commits),
        "relevant_commits": len(relevant),
        "areas": out_areas,
        "machines": {m: {"commits": len(v["commits"]), "areas": sorted(v["areas"]), "tickets": sorted(v["tickets"])}
                     for m, v in sorted(machine_hits.items())},
        "tickets": sorted({k for c in relevant for k in c["tickets"]}),
        "bt1_alerts": bt1_alerts,
        "relevant": [{k: c[k] for k in ("short", "date", "author", "subject", "tickets", "machines", "areas")} | {"files": c["files"][:15]}
                     for c in relevant],
    }
    json.dump(result, open(out_path, "w", encoding="utf-8"), indent=1)
    print(f"commits={len(commits)} relevant={len(relevant)} tickets={len(result['tickets'])}")
    for a in out_areas:
        print(f"{a['risk']:6} {a['risk_score']}  {a['area']:35} commits={a['commits']:4} churn={a['churn']:6} {','.join(a['machines'])}")
    for m, v in result["machines"].items():
        print(f"{m:28} commits={v['commits']} tickets={len(v['tickets'])}")
    print(f"BT1 alerts: {len(bt1_alerts)} tickets")
    for t in bt1_alerts:
        print(f"  {t['level']:11} {t['ticket']:9} commits={t['commits']:3} direct={','.join(t['direct'])} shared={','.join(t['shared'])}")


if __name__ == "__main__":
    main(*sys.argv[1:4])
```
