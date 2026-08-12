**Scope:** Functional release testing of the ProbeTruck, executed **without the bundle plate** (single beams / profiles) and **with the bundle plate** (bundles). Behaviour is driven by the PLC variable `inUseBundlePlate` (requested bundle-plate position).

**Source documentation:** ProbeTruck (1049) space on Confluence — steerings (SearchMaterial, MoveMaterial, MeasureMaterialLength, MoveAbsoluteX, PushMaterial, GoToRest, ReferenceRun, CheckPositionAskOperator, CheckBundlePlatePosition), `FB_ProbeTruck_MoveMaterial`, `ProbeTruck_Method_Event`, `RestPositionX`, and "Probe truck improvement and changes during testing". Code reference: `vacam-twincat` repository.

---

## How to use this protocol

Each test case has a fixed structure:

- **Config** — bundle plate OFF (`inUseBundlePlate = FALSE`), ON (`inUseBundlePlate = TRUE`), or *both* (run twice).
- **Precondition** — machine/material state required before starting.
- **Steps** — operator actions.
- **Expected result** — what must happen to pass, including relevant error/warning codes.
- **Result** — mark ☐ Pass / ☐ Fail.
- **Notes** — anomalies, deviations, measured values.

Run every "both" case **once with the bundle plate removed/deactivated and once with it fitted/activated**, recording each run separately.

### Test record header (fill in before starting)

| Field | Value |
|---|---|
| Machine / serial | |
| PLC (vacam-twincat) build / commit | |
| Vacam version | |
| Tester | |
| Date | |
| Material used (single) | |
| Material used (bundle) | |

### Error-code discrepancy — resolved against the code

The `ProbeTruck_Method_Event` Confluence page is **outdated**: it lists -14915/-14916 as the bundle-plate errors. The PLC global variable list (`GVL_ProbeTruck.TcGVL` in `vacam-twincat`) is authoritative and this protocol now uses those values. The `CheckBundlePlatePosition` steering page (-14918 / -14919) was correct.

- **-14918** = `cERROR_BundlePlateInWrongPosition`
- **-14919** = `cERROR_BundlePlatePositioningCancelled`
- **-14915** = `cERROR_NotAllowedIfCycleIsActive`
- **-14916** = `cERROR_TimeOutMovingMaterialAgainstTruck`

### Reference — method IDs, error codes, warnings (from `GVL_ProbeTruck.TcGVL`)

| Method | ID | | Error const | Code | Meaning |
|---|---|---|---|---|---|
| GoToRest | 0004 | | cERROR_LengthMeasuringPhotocellOperated | -14900 | Length photocell operated, move material backwards |
| ReferenceRun | 0005 | | cERROR_NoMaterialFound | -14901 | No material found |
| Stop | 0006 | | cERROR_ProbeInEmergencyStopZone | -14902 | Probe in emergency-stop zone |
| SearchMaterial | 1000 | | cERROR_ProbeDoesNotDetectMaterial | -14903 | Probe does not detect material anymore |
| MeasureMaterialLength | 1001 | | cERROR_NoMaterialInformation | -14904 | No material information available |
| MoveAbsoluteX | 1002 | | cERROR_ExternalEStopRequest | -14905 | External emergency stop request |
| PushMaterial | 1003 | | cERROR_TruckCanNotReachTargetpositionX | -14906 | Truck cannot reach requested target position X |
| TryToMoveMaterialAndX | 1004 | | cERROR_MaterialIsNotInPosition | -14907 | Material position not within tolerance |
| MoveAbsoluteMaterial | 1005 | | cERROR_ProbeDetectsMaterial | -14908 | Probe detects material |
| CheckPositionAskOperator | 1006 | | cERROR_MaterialIsTooShort | -14909 | Material length is too short |
| CheckBundlePlatePosition | 1007 | | cERROR_ExternalStopRequest | -14910 | External stop request |
| | | | cERROR_MaterialIsNotMoving | -14911 | Roller conveyors cannot move the material |
| | | | cERROR_CalculatingMotionProfile | -14912 | Calculation error determining motion profile |
| | | | cERROR_OnlyInPositiveMovingDirection | -14913 | Only possible in positive moving direction |
| | | | cERROR_OnlyInNegativeMovingDirection | -14914 | Only possible in negative moving direction |
| | | | cERROR_NotAllowedIfCycleIsActive | -14915 | Not allowed if cycle is active |
| | | | cERROR_TimeOutMovingMaterialAgainstTruck | -14916 | Timeout moving material against truck |
| | | | cERROR_MaterialPushedTruck | -14917 | Probe truck pushed out of position by material |
| | | | cERROR_BundlePlateInWrongPosition | -14918 | Bundle plate in wrong position |
| | | | cERROR_BundlePlatePositioningCancelled | -14919 | Bundle plate positioning cancelled |
| | | | cERROR_HaltOnXAxisTimeOut | -14920 | Halt on X-axis timeout |
| | | | cERROR_DigitalInputForLengthMeasuringDisabled | -14921 | Digital input for length measuring disabled |
| | | | cERROR_UseOfBundlePlateDisabled | -14922 | Use of bundle plate disabled |
| | | | (framework) | -700 | Axis not claimed or not able to claim |
| | | | (framework) | -5 | Part already active with other action |

**Warning-flag messages (`cWMSG_*`, DINT):** 100 = bundle plate position invalid (clamp between activated/deactivated); 101 = bundle plate position wrong (changed during operation); 102 = probe position sensor has error; 103 = probe position is too much negative.

**Bundle-plate dialog events (DINT):** 104900 = activate bundle plate; 104901 = deactivate bundle plate.

**Axis min/max & halt causes (DINT):** 100 probe detects material; 101 collision back side material; 102 probe truck past last roller; 103 cycle active; 104 bundle plate position; 105 probe position sensor error.

Key constants / vacam settings referenced: probe follow distance 160 mm (reduced to 25 mm during deceleration), push accel/decel limit 200 mm/s², nominal max reverse velocity 700 mm/s, bundle probe start position accepted up to 10 mm, push start gap 1 mm, "Material detection distance", "Search material velocity of X-axis", "Maximum search material velocity of X-axis", "Velocity percentage of rollers moving backwards", "Material follow distance", "Material tolerance on position", "Probe emergency stop distance", "Maximum velocity when pushing material".

---

## Section A — Safety, claim and pre-conditions (both configs)

### TC-A01: X-axis claim failure is reported
- **Config:** both
- **Precondition:** Force a condition where the X-axis cannot be claimed (e.g. axis already claimed by another owner / in error).
- **Steps:** Start any probe-truck steering that claims the axis (e.g. MoveAbsoluteX).
- **Expected result:** Steering goes to `Error` with "Axis not claimed or not able to claim" (**-700**). No motion occurs.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-A02: Emergency stop / light curtain during movement
- **Config:** both
- **Precondition:** Material on rollers, a movement-with-material steering running (e.g. MoveAbsoluteMaterial).
- **Steps:** Trigger the safety interruption (E-stop button or light curtain) mid-move.
- **Expected result:** `FastStop` — X-axis and conveyor come to a complete standstill; steering ends with external emergency stop (**-14905**). Material is not driven into the truck.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-A03: External / panel stop request during movement
- **Config:** both
- **Precondition:** Movement-with-material steering running.
- **Steps:** Issue a controlled stop (panel stop).
- **Expected result:** `ControlledStop` — conveyor stops, truck maintains the following distance (controlled stop), steering ends with "External stop request" (**-14910**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-A04: X-axis halt while moving with material (forward)
- **Config:** both
- **Precondition:** Truck following material in positive direction.
- **Steps:** Apply an X-axis halt in the moving direction.
- **Expected result:** X-axis stops immediately; conveyor stops with high deceleration (state `Halted`); truck does not lose the material. When the halt clears, movement restarts automatically.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-A05: X-axis halt while moving with material (backward)
- **Config:** both
- **Precondition:** Truck following material in negative direction.
- **Steps:** Apply an X-axis halt.
- **Expected result:** X-axis stops immediately; conveyor stops quickly so the material does not collide with the truck; movement restarts when halt clears.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-A06: Probe enters emergency-stop zone
- **Config:** both
- **Precondition:** Truck moving in positive direction, material approaching.
- **Steps:** Let the probe distance to the material fall below "Probe emergency stop distance".
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-A07: X-axis halt persists too long → timeout
- **Config:** both
- **Precondition:** Truck moving with material; force the X-axis into a `Halted` state (e.g. sustained halt / calculated max not clearing).
- **Steps:** Keep the halt active beyond the allowed time.
- **Expected result:** `Error` "Halt on X-axis timeout" (`cERROR_HaltOnXAxisTimeOut`, **-14920**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

---

## Section B — Reference run & Go to rest (both configs)

### TC-B01: Reference run
- **Config:** both
- **Precondition:** Machine idle, no automatic cycle active.
- **Steps:** Start ReferenceRun (0005).
- **Expected result:** Axis is claimed; because the truck has an absolute encoder, the axis moves to its rest position at 100% feed override (max X velocity) and finishes successfully.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-B02: Go to rest without material (from op-view)
- **Config:** both
- **Precondition:** No material against the truck; no automatic cycle active.
- **Steps:** Start GoToRest (0004) from the probe-truck operation view.
- **Expected result:** Axis claimed; `RestPositionX` determines `bMoveWithMaterial = FALSE`; X moves to rest position at 100% override; finishes successfully.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-B03: Go to rest with material (automatic cycle)
- **Config:** both
- **Precondition:** Material detected against the truck; automatic cycle active (cycle run).
- **Steps:** Trigger GoToRest as part of the cycle.
- **Expected result:** `bMoveWithMaterial = TRUE`; material is moved out of the machine zone and the material front is left just in front of the length-measuring photocell; truck and material finish at the requested position.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-B04: Go to rest blocked from op-view during active cycle
- **Config:** both
- **Precondition:** Automatic cycle active.
- **Steps:** Attempt GoToRest from the operation view.
- **Expected result:** Not permitted while the automatic cycle is active (rejected).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

---

## Section C — Move Absolute X (both configs)

### TC-C01: Move to a free position (no material)
- **Config:** both
- **Precondition:** No material on rollers; no automatic cycle active.
- **Steps:** MoveAbsoluteX (1002) to a valid target on the infeed side.
- **Expected result:** X reaches the target and finishes successfully. Positive-direction velocity limited to "Maximum search material velocity of X-axis"; reverse limited to 700 mm/s nominal.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-C02: Positive move stops when probe detects material (detection not allowed)
- **Config:** both
- **Precondition:** Material present on rollers.
- **Steps:** MoveAbsoluteX in positive direction toward the material with detection not allowed.
- **Expected result:** Movement stops when probe detects material; `Error` with "Probe detects material" (**-14908**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-C03: Positive move with detection allowed but target beyond material back side
- **Config:** both
- **Precondition:** Material present; detection allowed; requested target > calculated maximum (material back side).
- **Steps:** MoveAbsoluteX toward material.
- **Expected result:** `Error` "Probe detects material" (**-14908**) — cannot reach a target beyond the material back side.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-C04: Move absolute X blocked during active cycle (op-view)
- **Config:** both
- **Precondition:** Automatic cycle active.
- **Steps:** Attempt MoveAbsoluteX from operation view.
- **Expected result:** Not permitted while automatic cycle is active (rejected).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-C05: Axis error during move is propagated
- **Config:** both
- **Precondition:** Induce an axis error mid-move if safely possible.
- **Steps:** Start MoveAbsoluteX; force axis error.
- **Expected result:** `Error` state with the error message from the axis object.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

---

## Section D — Search material (both configs)

> With bundle plate ON, this is the primary place the *bundle* start-position handling is exercised (see TC-D06).

### TC-D01: Normal search — X-axis only (photocell driven rollers operated)
- **Config:** both
- **Precondition:** Material present with its back within the driven-roller section (photocell between driven/non-driven rollers operated); auto transport available.
- **Steps:** Start SearchMaterial (1000).
- **Expected result:** Axis claimed; X moves in positive direction at search speed ("Search material velocity of X-axis"); when the probe detects material, X stops and the function finishes successfully.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-D02: Search transitions to X + conveyor when material not at driven rollers
- **Config:** both
- **Precondition:** Material present but photocell between driven/non-driven rollers *not* operated at start.
- **Steps:** Start SearchMaterial.
- **Expected result:** X moves alone first; when the between-rollers photocell reports no material, conveyor restarts (`SearchMaterialWithXAxisAndConveyor`); conveyor moves slowly backwards at "Velocity percentage of rollers moving backwards"; probe detects material → both stop → finish successfully.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-D03: Search — no material found
- **Config:** both
- **Precondition:** No material on the rollers.
- **Steps:** Start SearchMaterial.
- **Expected result:** X reaches target (length photocell position − 2500 mm) without detecting material; `Error` "No material found" (**-14901**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-D04: Search — length photocell already operated (limit switch)
- **Config:** both
- **Precondition:** Material already covering the length-measuring photocell.
- **Steps:** Start SearchMaterial.
- **Expected result:** Steering stops; `Error` "Photocell length measuring is operated, please move material backwards" (**-14900**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-D05: Search — manual transport runs at search speed only
- **Config:** both
- **Precondition:** Transport configured as manually operated only.
- **Steps:** Start SearchMaterial.
- **Expected result:** X-axis always runs at search speed (max search velocity equals search velocity); material may sit at non-driven rollers and is still found.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-D06: Bundle probe start position (probe cannot reach 0)
- **Config:** **ON (bundle)**
- **Precondition:** Bundle loaded; bundle plate fitted and in position; expect probe cannot fully reach 0.
- **Steps:** Start SearchMaterial and let it run into `MoveMaterialAgainstTruck`.
- **Expected result:** Rollers move material backwards to reduce probe distance; if probe reaches 0 → `ProbeStartPosition = 0`; if a timeout occurs with probe ≤ 10 mm → accepted, `fProbeStartPosition = actual probe position` (used for later bundle positioning); if timeout with probe > 10 mm → `Error` "Timeout moving material against probe truck" (**-14916**).
- **Result:** ☐ Pass ☐ Fail
- **Notes (record fProbeStartPosition):**

### TC-D07: Probe pushed out of position by material
- **Config:** both
- **Precondition:** In `MoveMaterialAgainstTruck`.
- **Steps:** Cause the material to push the truck off position.
- **Expected result:** `Error` "Probe truck pushed out of position by material" (**-14917**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

---

## Section E — Measure material length (both configs)

### TC-E01: Normal length measurement
- **Config:** both
- **Precondition:** Probe detects material; material information available; length photocell free; not blocked by active cycle rules.
- **Steps:** MeasureMaterialLength (1001) with `inStopAfterMeasuring` as required.
- **Expected result:** Conveyor moves material to the length photocell; on the rising edge the length is calculated from X and probe position; if `bKeepMovingAfterMeasurement`/keep-moving requested, material front continues toward the saw X-offset, otherwise it stops immediately. Function finishes successfully (or length checked, see TC-E05).
- **Result:** ☐ Pass ☐ Fail
- **Notes (record measured length):**

### TC-E02: Measure blocked — probe not detecting material
- **Config:** both
- **Precondition:** Probe not against material.
- **Steps:** Start MeasureMaterialLength.
- **Expected result:** Rejected — "Probe does not detect material anymore" (**-14903**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-E03: Measure blocked — no material information
- **Config:** both
- **Precondition:** Unknown material (no material info in vacam).
- **Steps:** Start MeasureMaterialLength.
- **Expected result:** Rejected — "No material information available" (**-14904**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-E04: Measure blocked — length photocell already operated
- **Config:** both
- **Precondition:** Length photocell already covered.
- **Steps:** Start MeasureMaterialLength.
- **Expected result:** Rejected — "Photocell length measuring is operated, please move material backwards" (**-14900**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-E05: Measure — material too short
- **Config:** both
- **Precondition:** Material shorter than measurable at target.
- **Steps:** Start MeasureMaterialLength.
- **Expected result:** Target reached without a rising edge; `Error` "Material length is too short" (**-14909**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-E06: Measure from op-view blocked during active cycle
- **Config:** both
- **Precondition:** Automatic cycle active; start from op-view.
- **Steps:** Attempt MeasureMaterialLength.
- **Expected result:** Rejected — not allowed if cycle is active (`cERROR_NotAllowedIfCycleIsActive`, **-14915**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-E07: Measure length check in automatic cycle (tolerance)
- **Config:** both
- **Precondition:** Automatic cycle active; measured length within/outside accepted tolerance.
- **Steps:** Let the cycle measure the length; vacam checks tolerance.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-E08: Measure blocked — length-measuring digital input disabled
- **Config:** both
- **Precondition:** The digital input used for length measuring is disabled.
- **Steps:** Start MeasureMaterialLength.
- **Expected result:** Rejected — "Digital input for length measuring disabled" (`cERROR_DigitalInputForLengthMeasuringDisabled`, **-14921**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

---

## Section F — Move material (MoveAbsoluteMaterial / TryToMoveMaterialAndX) (both configs)

### TC-F01: Move material forward to position
- **Config:** both
- **Precondition:** Probe detects material; material info available; part not busy.
- **Steps:** MoveAbsoluteMaterial (1005) to a positive target.
- **Expected result:** Truck follows at 160 mm; during conveyor deceleration the follow distance reduces (down to 25 mm); on reaching target the rollers move the material against the truck; finishes with material at requested position (within "Material tolerance on position").
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-F02: Move material blocked — probe not detecting material
- **Config:** both
- **Precondition:** Probe not against material.
- **Steps:** Start MoveAbsoluteMaterial.
- **Expected result:** Rejected — "Probe does not detect material anymore" (**-14903**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-F03: Move material blocked — unknown material
- **Config:** both
- **Precondition:** No material information.
- **Steps:** Start MoveAbsoluteMaterial.
- **Expected result:** Rejected — "No material information available" (`cERROR_NoMaterialInformation`, **-14904**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-F04: Move material blocked — part already busy
- **Config:** both
- **Precondition:** A move-material function already running.
- **Steps:** Start a second MoveAbsoluteMaterial.
- **Expected result:** Rejected — "Part already active with other action" (**-5**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-F05: Move material — conveyor cannot move material, timeout → ask operator
- **Config:** both
- **Precondition:** Material that the conveyor cannot move (poor grip).
- **Steps:** Start MoveAbsoluteMaterial; allow the position timeout.
- **Expected result:** On timeout positioning against the truck, the operator is asked to position the material (`ManuallyMoveMaterialAgainstTruck` event). OK within tolerance → success; OK outside tolerance → "Material position not within tolerance" (**-14907**); Cancel → `Error` from event 1001.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-F06: TryToMoveMaterialAndX — negative direction, loss of material allowed
- **Config:** both
- **Precondition:** Target in negative direction; material may be lost during move.
- **Steps:** TryToMoveMaterialAndX (1004) to a negative target.
- **Expected result:** Conveyor moves material, truck follows; if material stops moving, rollers stop and the X-axis finishes its movement at nominal velocity.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-F07: TryToMoveMaterialAndX rejected in positive direction
- **Config:** both
- **Precondition:** Target lies in positive direction.
- **Steps:** Start TryToMoveMaterialAndX with a positive target.
- **Expected result:** Rejected — "Only possible in negative moving direction" (**-14914**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-F08: Small move — CreateSpaceForXAxis (conveyor can't do tiny absolute move)
- **Config:** both
- **Precondition:** Requested move smaller than the conveyor's minimum (e.g. 10 mm vs 50 mm tolerance).
- **Steps:** Request a small MoveAbsoluteMaterial.
- **Expected result:** Conveyor creates enough space for the X-axis to reach the target instead of a full absolute move; final position within tolerance.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-F09: Calculated maximum/minimum reached mid-move
- **Config:** both
- **Precondition:** Target requiring the X-axis to pass through its calculated max/min.
- **Steps:** Run the move.
- **Expected result:** X positions to the calculated max/min and waits in `Halted` until it can continue; material is kept at calculated max + follow distance; movement completes to the final target.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

---

## Section G — Push material (both configs)

### TC-G01: Push — gap present, close then push
- **Config:** both
- **Precondition:** Probe detects material; material info available; a gap > 1 mm between truck and material.
- **Steps:** PushMaterial (1003) to target.
- **Expected result:** X closes the gap (`MoveAbsoluteXAgainstMaterial`), then pushes (`PushMaterialToPosition`) using the conveyor's motion profile with accel/decel limited to 200 mm/s² and velocity capped at "Maximum velocity when pushing material"; target reached, finishes successfully.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-G02: Push — material already within 1 mm
- **Config:** both
- **Precondition:** Material already within 1 mm of the truck.
- **Steps:** PushMaterial to target.
- **Expected result:** Pushing starts immediately (skips gap-closing); target reached.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-G03: Push blocked — probe not detecting material
- **Config:** both
- **Precondition:** Probe not against material.
- **Steps:** Start PushMaterial.
- **Expected result:** Rejected — "Probe does not detect material anymore" (**-14903**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-G04: Push blocked — unknown material
- **Config:** both
- **Precondition:** No material information.
- **Steps:** Start PushMaterial.
- **Expected result:** Rejected — "No material information available" (**-14904**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-G05: Push — probe loses material mid-push
- **Config:** both
- **Precondition:** During push, force loss of contact.
- **Steps:** Push and interrupt contact.
- **Expected result:** `Error` "Probe does not detect material anymore" (**-14903**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-G06: Push — saw non-driven rollers blocked
- **Config:** both
- **Precondition:** Truck pushing material onto the saw table.
- **Steps:** Start pushing.
- **Expected result:** Block-rollers request is sent to the saw (via V100StandAloneIntegration) so the saw-table non-driven rollers are blocked, keeping material against the probe.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

---

## Section H — Check position & ask operator (both configs)

### TC-H01: Material already in position (no dialog)
- **Config:** both
- **Precondition:** Material back side already within tolerance of the requested position.
- **Steps:** CheckPositionAskOperator (1006).
- **Expected result:** If the material stays within tolerance for 2 seconds, the function finishes successfully **without** showing a dialog.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-H02: Material out of position — operator corrects (OK, within tolerance)
- **Config:** both
- **Precondition:** Material out of tolerance.
- **Steps:** Run CheckPositionAskOperator; operator moves material against the truck; press OK.
- **Expected result:** Dialog shown; after OK with material within tolerance → finishes successfully.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-H03: Material still out of tolerance after OK
- **Config:** both
- **Precondition:** Material out of tolerance and left out of tolerance.
- **Steps:** Press OK without correcting.
- **Expected result:** "Material position is not within tolerance of the requested position" (**-14907**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-H04: Operator cancels the dialog
- **Config:** both
- **Precondition:** Dialog shown.
- **Steps:** Press Cancel.
- **Expected result:** `Error` state with the message from event 1001 (`ManuallyMoveMaterialAgainstTruck`).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

---

## Section I — Bundle plate specific (Config ON)

> These are the core "with bundle plate" cases. `CheckBundlePlatePosition` (1007) only starts at the **start of a cycle list**.

### TC-I01: Bundle plate already in requested position → ready immediately
- **Config:** ON
- **Precondition:** Bundle plate already in the position requested by `inUseBundlePlate`.
- **Steps:** Start a cycle list that requests the bundle-plate position.
- **Expected result:** CheckBundlePlatePosition reports ready immediately; no dialog; no X-axis rest move required.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-I02: Bundle plate wrong → move X to rest → operator sets plate → OK
- **Config:** ON
- **Precondition:** Bundle plate not in the requested position at the start of a cycle list.
- **Steps:** Start the cycle list. Observe X moves to rest (`ClaimAxis` → `GoToRest`); operator activates/deactivates the plate per the dialog; press OK.
- **Expected result:** X moves to rest first (to allow changing the plate); dialog asks operator to move the plate; after OK with the plate correctly positioned → function finishes successfully.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-I03: Bundle plate still incorrect after OK
- **Config:** ON
- **Precondition:** Plate dialog shown; plate left in the wrong position.
- **Steps:** Press OK without correctly positioning the plate.
- **Expected result:** Error "Bundle plate in wrong position" (`cERROR_BundlePlateInWrongPosition`, **-14918**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-I04: Operator cancels bundle-plate dialog
- **Config:** ON
- **Precondition:** Plate dialog shown.
- **Steps:** Press Cancel.
- **Expected result:** `Error` "Bundle plate positioning cancelled" (`cERROR_BundlePlatePositioningCancelled`, **-14919**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-I05: Bundle-plate position changes during operation → X halted + warning
- **Config:** ON
- **Precondition:** Bundle plate confirmed in position (stored locally); a movement using the plate is running.
- **Steps:** Change the bundle-plate position during operation.
- **Expected result:** X-axis is halted in **both** directions (halt cause 104, bundle plate position) and warning "bundle plate position is wrong" is shown (`cWMSG_BundlePlatePositionWrong`, WMSG **101**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-I06: Bundle clamp between activated and deactivated → warning + X halted
- **Config:** ON
- **Precondition:** Move the clamp so its actual position is neither fully activated nor fully deactivated.
- **Steps:** Observe the truck behaviour.
- **Expected result:** Warning "bundle plate position is invalid" shown for the in-between clamp position (`cWMSG_BundlePlatePositionInvalid`, WMSG **100**); X-axis halted in both directions.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-I07: Full bundle cycle end-to-end (with plate)
- **Config:** ON
- **Precondition:** Bundle loaded; cycle list prepared.
- **Steps:** Run a complete cycle: CheckBundlePlatePosition → SearchMaterial → MeasureMaterialLength → position/move material → GoToRest.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-I08: Bundle-plate action while use of bundle plate is disabled
- **Config:** ON
- **Precondition:** Bundle-plate usage disabled in configuration, but a bundle-plate request (`inUseBundlePlate`) is issued.
- **Steps:** Start a cycle / method that requests the bundle plate.
- **Expected result:** Rejected — "Use of bundle plate disabled" (`cERROR_UseOfBundlePlateDisabled`, **-14922**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-I09: Probe position sensor error
- **Config:** both
- **Precondition:** Induce a probe-position sensor fault (if safely possible on the bench).
- **Steps:** Observe the truck behaviour during/after the fault.
- **Expected result:** Warning "probe position sensor has error" shown (`cWMSG_ProbePositionSensorHasError`, WMSG **102**); X-axis halted via halt cause 105 (probe position sensor error).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-I10: Probe position too much negative
- **Config:** both
- **Precondition:** Drive the probe to an abnormally negative position (if reproducible).
- **Steps:** Observe the warning.
- **Expected result:** Warning "probe position is too much negative" shown (`cWMSG_ProbePositionIsTooMuchNegative`, WMSG **103**).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

---

## Section J — Regression: single-material full cycle (Config OFF)

### TC-J01: Full single-material cycle without bundle plate
- **Config:** OFF
- **Precondition:** Single beam/profile loaded; bundle plate removed/deactivated; cycle list prepared.
- **Steps:** Run a complete cycle: SearchMaterial → MeasureMaterialLength → move/position material → (push if applicable) → GoToRest.
- **Expected result:** No bundle-plate check is required or triggered; probe start position reaches 0; all steerings complete; material ends at requested positions.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-J02: Keep material clamped for operation
- **Config:** both
- **Precondition:** Material positioned against the truck; probe-truck setting `bKeepMovingMaterialAgainstTruck` enabled.
- **Steps:** Let the saw signal `MaterialIsClampedForOperation` (via V100Integration).
- **Expected result:** While not yet clamped, rollers keep pushing material against the truck; when `MaterialIsClampedForOperation` becomes true, the rollers stop.
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

### TC-J03: Pull material apart at infeed
- **Config:** both
- **Precondition:** Two pieces to be separated at the infeed side.
- **Steps:** Trigger the pull-apart action.
- **Expected result:** Truck first moves 20 mm backwards, then only the conveyors pull the material apart (truck+material combined move is no longer used).
- **Result:** ☐ Pass ☐ Fail
- **Notes:**

---

## Sign-off

| Role | Name | Date | Signature |
|---|---|---|---|
| Tester | | | |
| Reviewer | | | |
| Release approved | | | |

**Overall result:** ☐ Pass ☐ Pass with notes ☐ Fail

**Open issues / tickets raised:**
