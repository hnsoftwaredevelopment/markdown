# E13 Query insight

See how MySQL runs a query and how objects depend on each other. From the comparison with SSMS (Display Execution Plan, View Dependencies).

## US-1301 Explain plan

**Status:** Done (accepted 2026-11-03)

As a developer, I want to see the execution plan of a query, so that I can find full table scans and missing indexes.

**Acceptance criteria**

- [x] Command *Explain* in the MySQL Query Editor (key binding as SSMS *Display Estimated Execution Plan*, Ctrl+L), on the selection or the statement at the caret.
- [x] Runs `EXPLAIN FORMAT=JSON` (MySQL 5.7+, MariaDB) without running the query, and shows the plan as a tree in a *Plan* tab of the results pane: per step the table, access type, key used, rows examined, filtered and cost.
- [x] Steps with a full table scan (`ALL`) or a filesort/temporary table are marked.
- [x] Statements that cannot be explained (DDL) give a clear message.

**Tasks**

- [x] T-1301-01 JSON reader for the EXPLAIN output (`PlanJson`), `ExplainPlanParser` with `PlanNode`, `ExplainStatement` (statement at the caret, explainable check) + tests
- [x] T-1301-02 `QueryRunner.ExplainAsync` + tests
- [x] T-1301-03 *Plan* tab in the results pane, command *Explain* (Ctrl+L, context menu, button in the query bar)

**Implementation notes**

- *Explain* takes the selection; without a selection the statement at the caret: the last statement that starts on or before the caret line. With several statements in the selection, the first one is explained.
- It runs `EXPLAIN FORMAT=JSON <statement>` in the session of the document, in the database of the query bar. The statement itself does not run, so an UPDATE or DELETE changes nothing.
- Explainable: statements that start with SELECT, WITH, TABLE, INSERT, UPDATE, DELETE or REPLACE (also after an opening parenthesis). Others get the message *The statement at line n has no plan: ...* and nothing is sent to the server.
- Core has no JSON library. Adding System.Text.Json to the VSIX brings binding redirects, so a small JSON reader in Core reads the EXPLAIN output. Numbers stay text, as MySQL writes costs as text.
- The parser knows the steps of MySQL 5.7/8.0 (`query_block`, `table`, `nested_loop`, `ordering_operation`, `grouping_operation`, `duplicates_removal`, `windowing`, `union_result`, `materialized_from_subquery`, the subquery lists) and MariaDB (`filesort`, `temporary_table`, `read_sorted_file`, `subqueries`, `materialized`). An unknown object is searched for known steps, so a newer server still shows its tables. MySQL 8.0.32+ with `explain_json_format_version = 2` writes a tree of iterators (`operation`, `inputs`); that format is shown as well, with the operation as the title.
- A node shows the step, a summary (access type, key, rows, or the cost of a query block) and, for a costly step, a warning icon and the warning text. The tooltip lists every value of the step as EXPLAIN names it (`possible_keys`, `filtered`, `attached_condition`, `prefix_cost`, ...).
- Marked: access type `ALL` (full table scan, not for the target table of an INSERT), `using_filesort`, `using_temporary_table`, and the MariaDB `filesort` and `temporary_table` steps.
- The *Plan* tab only shows while there is a plan and opens after *Explain*. The Messages tab gets *Estimated plan of the statement at line n in ...; the statement did not run.* plus the warnings of the server; MySQL adds note 1003 with the rewritten query.
- Ctrl+L only works in the MySQL Query Editor (its own key binding scope, ADR-013); in other editors Ctrl+L stays *Cut Line*.
- Icon: the Visual Studio catalog has no icon for an estimated plan, so *Explain* has its own image: a small plan tree with the costly step in orange (decision 2026-11-03, may be replaced in E11). It comes from `ObjectExplorerImages.imagemanifest` (PNG 16/24/32, drawn from `Resources/Images/Explain.svg`) and is used by the menu command and the button in the query bar (`ObjectExplorerMonikers.Explain`). The grey parts are inverted in the dark theme.

**Manual test**

Use the *sakila* sample database (or any database with a few tables).

1. Open a New Query on *sakila*. Type ``SELECT f.title, a.last_name FROM film f JOIN film_actor fa ON fa.film_id = f.film_id JOIN actor a ON a.actor_id = fa.actor_id ORDER BY f.title;``. Press Ctrl+L: the results pane opens on the *Plan* tab. The query did not run (no Results grid).
2. The tree shows *Query block 1* with its cost, *Order by* with a warning (filesort, temporary table), a *Nested loop join* and a node per table with access type, key and rows.
3. Hover a table node: the tooltip lists the values (`possible_keys`, `filtered`, `prefix_cost`, ...). A table with access type *ALL* has the warning icon and *Full table scan: every row is read.*
4. Messages tab: *Estimated plan of the statement at line 1 ...; the statement did not run.* and the note 1003 of the server.
5. Put two statements in the document, place the caret on the second one, press Ctrl+L: the plan is of the second statement and the message names its line. Select the first one and press Ctrl+L: the plan is of the selection.
6. Explain ``UPDATE film SET rental_rate = rental_rate WHERE film_id = 1;``: a plan shows; check that the row is not changed.
7. Explain ``CREATE TABLE x (a INT);``: Messages tab with *The statement at line n has no plan: ...*; the Plan tab is hidden; the table is not created.
8. Explain ``SELECT * FROM does_not_exist;``: an error with the line in the Messages tab.
9. Press Ctrl+Shift+E after Explain: the Plan tab disappears, the Results tab shows the rows.
10. The context menu of the editor has *Explain* between *Execute* and *Cancel Query*; the query bar has an Explain button next to Execute.
11. Ctrl+L in a C# file still cuts the line.
12. MariaDB (if available): the plan shows, including *Filesort* for an ORDER BY on a column without an index.
13. Theme (Dark, Light, Blue): the Plan tab is readable.

## US-1302 Explain analyze

**Status:** Ready for test

As a developer, I want to see how many rows each step really read and how long it took, so that I can see where the optimizer guessed wrong.

**Acceptance criteria**

- [x] Command *Explain Analyze*: `EXPLAIN ANALYZE` (MySQL 8.0.18+) or `ANALYZE FORMAT=JSON` (MariaDB), with the actual rows and time per step next to the estimates.
- [x] Only for SELECT (the statement really runs); other statements get a message.

**Tasks**

- [x] T-1302-01 `AnalyzeTreeParser` for the MySQL text tree, actual rows and time in `ExplainPlanParser` (MariaDB `r_rows`, `r_total_time_ms`), `ExplainStatement.IsAnalyzable` + tests
- [x] T-1302-02 `QueryRunner.ExplainAnalyzeAsync` (server type and version decide the statement) + tests
- [x] T-1302-03 Command *Explain Analyze* (context menu, button in the query bar) with its own icon

**Implementation notes**

- Same input as *Explain*: the selection, or the statement at the caret. The plan shows in the same *Plan* tab.
- Server type and version come from the explorer node, or from `SELECT VERSION()` in the session when the node was not connected yet. MySQL 8.0.18+ gets `EXPLAIN ANALYZE <statement>`, MariaDB gets `ANALYZE FORMAT=JSON <statement>`. Older MySQL versions get the message *Explain Analyze needs MySQL 8.0.18 or later ...* and nothing runs.
- MySQL returns a text tree, not JSON (`EXPLAIN ANALYZE` has no JSON format before 8.3). `AnalyzeTreeParser` reads it: one step per line, four spaces per level, the estimate `(cost=.. rows=..)` and the measurement `(actual time=first..last rows=.. loops=..)` or `(never executed)`. The title is the step text without those parts.
- Summary per step: the estimated rows, then *actual n rows*, the time until the last row in ms and, above 1, the number of loops. MySQL gives rows and time per loop.
- Accepted: SELECT, TABLE, and WITH unless an INSERT, UPDATE, DELETE or REPLACE stands outside the parentheses (for MySQL 8 `WITH ... UPDATE`). Everything else gets the message *Explain Analyze runs the statement, so it only takes a SELECT ...* and nothing is sent. A `WITH ... SELECT ... FOR UPDATE` is refused as well; that is on purpose.
- Marked as in US-1301 (full scan: *Table scan on*, sort: *Sort*, temporary table), and new: an estimate that is off by a factor of 10 or more and by at least 100 rows (*Estimated 10 rows, actually 1000.*). Smaller differences are normal and are not marked.
- No default shortcut: SSMS uses Ctrl+M as a toggle and in Visual Studio Ctrl+M starts the outlining chords. The command is *MySQL.ExplainAnalyze*; a key can be assigned in *Tools > Options > Environment > Keyboard* under the scope *MySQL Query Editor*.
- Icon: the plan tree of *Explain* with a clock (`ObjectExplorerMonikers.ExplainAnalyze`, image 2 in the manifest).
- Cancel Query (Alt+Break) stops a long Explain Analyze, as it stops Execute.

**Manual test**

Use *sakila* on MySQL 8.0.18 or later.

1. Type ``SELECT f.title, a.last_name FROM film f JOIN film_actor fa ON fa.film_id = f.film_id JOIN actor a ON a.actor_id = fa.actor_id ORDER BY f.title;`` and click the Explain Analyze button in the query bar (plan tree with clock): the Plan tab shows steps such as *Sort: f.title*, *Nested loop inner join*, *Table scan on ...*, each with estimated rows, actual rows and ms.
2. Hover a step: the tooltip lists cost, rows, actual time, actual rows and loops. A step with more than one loop shows *n loops* in the summary.
3. Messages tab: *Plan of the statement at line 1 with the actual rows and times, in ...; the statement ran.*
4. Wrong estimate: run ``SELECT * FROM payment WHERE amount > 0 AND customer_id > 0;`` and compare the estimated and actual rows of the scan. When they differ by 10× and at least 100 rows, the step has the warning icon and *Estimated n rows, actually m.* When no step differs that much, no step has that warning.
5. A filter on a branch that does not run shows *never executed*.
6. Explain Analyze on ``UPDATE film SET rental_rate = rental_rate WHERE film_id = 1;``: the message *Explain Analyze runs the statement, so it only takes a SELECT ...*; nothing ran.
7. Explain Analyze on ``WITH x AS (SELECT film_id FROM film) SELECT COUNT(*) FROM x;``: a plan. On ``WITH x AS (SELECT film_id FROM film LIMIT 1) DELETE film FROM film JOIN x USING (film_id);``: the message, nothing deleted.
8. Explain Analyze on ``SELECT SLEEP(10);`` and press Alt+Break: *Cancelled after ...*.
9. The editor context menu shows *Explain Analyze* below *Explain*; assign a key in Tools > Options > Keyboard (scope *MySQL Query Editor*, command *MySQL.ExplainAnalyze*) and use it.
10. MariaDB (if available): the plan with *actual n rows* and *ms* per table.
11. Theme (Dark, Light, Blue): both icons and the Plan tab are readable.

## US-1303 View dependencies

**Status:** Todo

As a developer, I want to see what uses a table or routine before I change it.

**Acceptance criteria**

- [ ] Context menu *View Dependencies* on a table, view, procedure and function.
- [ ] *Used by*: views (`INFORMATION_SCHEMA.VIEW_TABLE_USAGE`, MySQL 8.0.13+), foreign keys of other tables, triggers, and routines and events whose source contains the name (marked as a text match).
- [ ] *Uses*: the tables of a view, the tables a table refers to with foreign keys.
- [ ] Shown as a tree in a tool window; double-click selects the object in the explorer.
