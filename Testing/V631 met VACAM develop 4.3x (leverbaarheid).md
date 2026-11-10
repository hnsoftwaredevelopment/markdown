# V631 met VACAM develop 4.3x (leverbaarheid)

Geen ticket. Vraag: de V631 wordt nu geleverd met VACAM 4.11. Kan hij ook geleverd worden met 4.3x (develop)?

## Opzet

- VACAM `4.34.0-develop.2611060855` (nieuwste in `\\vasoftware\setups\VACAM\Vacam-develop`), TwinCAT user mode runtime met het boot project van dezelfde setup, VASIM rc. Gestart met de vacam-simulation-plugin.
- Backup: AMADA V631 `20250067_V631_260404_112234` (VACAM 4.11.32). VACAM werkt de databases bij van 4.11 naar 4.34.
- Terugvaloptie: regressiebackup `20250027_V631_261023_162024.zip` (Van Rijbroek, al op 4.34) met `HEA140_8000_minus12000.material.xml`.

## Controles

| # | Controle | Verwacht |
|---|---|---|
| C1 | VACAM en de machine starten | geen foutmeldingen, behalve de standaardmeldingen die met een machine Reset verdwijnen |
| C2 | Reference run | loopt af zonder fouten |
| C3 | Automatisch produceren, meerdere batches | boren, frezen en markeren lopen af tot "Remove material manually" |
| C4 | Handfuncties in de Operator view | assen bewegen, klemmen openen en sluiten, tool change, enzovoort |

## Resultaat

| # | Resultaat | Opmerking |
|---|---|---|
| C1 | **OK met opmerkingen:** na de Reset (16:16:10) zijn alle startmeldingen weg (luchtdruk, noodstop, deuren, lichtschermen). Er staan nog 2 waarschuwingen: W1-103 "Machine reference point invalid" (verdwijnt met de reference run) en W70-111 LayoutMarkingUnit "Z-axis not in rest position". Alleen in het log: 6 keer ERROR "TwinCAT truncated the implemented interfaces of ..." bij het opstarten (FB_MeasureUnit, FB_Shear, FB_Imprint, FB_DrillV2, FB_Saw, FB_InkJetMarker) en 1 keer "Missing translation for keys: Main.Unknown.Tags.Unknown" | Gestart via VACAM Launcher RC (kernel mode TwinCAT), VACAM `4.34.0-develop.2611061323`, VASIM rc. Log `Log 2026-11-06 15-50-51.log`. Eerst de configuratiefout van BT1-2334: "Too low oil level" van de zaag op DI 113 gezet |
| C2 | **OK:** reference run zelfstandig gestart (Reset 16:21:40, Start 16:21:44, dialogen "Reference run" en "Reference points unknown" automatisch afgehandeld). W70-111 "Z-axis not in rest position" verdween bij de start, W1-103 "Machine reference point invalid" om 16:22:38. Geen nieuwe meldingen | ongeveer 1 minuut, script `reference-only.ps1` op basis van de produce-scripts van de plugin |
| C3 | | |
| C4 | | |
