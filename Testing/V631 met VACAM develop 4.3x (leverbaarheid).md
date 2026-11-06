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
| C1 | | |
| C2 | | |
| C3 | | |
| C4 | | |
