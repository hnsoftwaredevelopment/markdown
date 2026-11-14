# Workflow

## Roles

| Who | Does what |
|---|---|
| Claude | Writes code and unit tests, reviews its own code, updates documentation and backlog status, commits |
| Herbert | Runs manual tests in Visual Studio, accepts or rejects a user story |

## Backlog structure

- **Epic** (`E01`): a large functional area. One file per epic in `docs/backlog/`.
- **User Story** (`US-0101`): a piece of value for the user, with acceptance criteria. Number = epic number + sequence.
- **Sub Story** (`US-0101a`): only when a story is too big to test in one go.
- **Task** (`T-0101-01`): a technical step within a story.

## Status values

| Status | Meaning |
|---|---|
| Todo | Not started |
| In progress | Claude is working on it |
| Ready for test | Code done, unit tests green, self-review done, manual test steps written |
| Rejected | Herbert found issues, see notes in the story |
| Done | Herbert accepted it, pushed to GitHub |
| Parked | Postponed until further notice |

## Definition of Done for a task

1. Code compiles without warnings (`TreatWarningsAsErrors` in Core).
2. Unit tests for the new logic exist and pass.
3. No hardcoded user-visible strings (see ADR-005).
4. Self-review done against the checklist below.
5. Committed locally with message `T-0101-01: <short description>`.

## Definition of Done for a user story

1. All tasks done.
2. Acceptance criteria checked off in the story.
3. Manual test steps written in the story under *Manual test*.
4. Status set to *Ready for test*.
5. Herbert tests and sets status to *Done* (or *Rejected* with notes).
6. Claude commits the final changes (`US-0101: accepted`) and pushes to GitHub.

Nothing is pushed to `main` before a story is accepted. Local commits are made per completed task.

Exception: when a story can only be tested on GitHub (for example the build pipeline), it is developed on a branch `us-<number>-<name>` that is pushed for testing. After acceptance it is merged into `main` and the branch is deleted. The build workflow runs on these branches too.

## Self-review checklist

- Async all the way: no `.Result` or `.Wait()` on the UI thread; database calls run off the UI thread with `CancellationToken`.
- Connections are opened per operation and disposed (`await using`).
- Identifiers in generated SQL are quoted with backticks and embedded backticks are doubled.
- User input never ends up in SQL without parameters or identifier quoting.
- Exceptions from the database are shown to the user in a readable message and logged to the Output window pane "Object Explorer for MySQL".
- Theme colors come from `EnvironmentColors`/`TreeViewColors`, never fixed colors.
- No password in logs, exceptions or settings files.

## Commit message format

```
<ID>: <what changed, imperative>

<optional details>
```

## Documentation mirror

All Markdown documentation lives in this repository under `docs/` and in `README.md`. After every change it is mirrored to:

`C:\DevOps\hnsoftwaredevelopment\Obsidian\Development\HNSoftwareDevelopment\Object Explorer for MySQL\`

The repository is leading. The Obsidian copy is read-only by convention: edit in the repository, then mirror.
