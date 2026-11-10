# BT1-2291 Detected material is teleported to a high x position

Ticket: [BT1-2291](https://voortman.atlassian.net/browse/BT1-2291) · status In Test · fix door Vincent Veluwenkamp

## Probleem en fix

Na het detecteren van het materiaal door de fotocellen zet de PLC de velocity generator van de transportgroep op een nieuwe positie. Als PLC, VACAM en VASIM opnieuw gestart worden zonder de VACAM Launcher, geeft de velocity generator soms een grote negatieve waarde. VASIM rekende daarmee de verplaatste millimeters uit en zette de balk op een veel te hoge X ("teleport").

Fix (VASIM, `ConveyorSimulator.cs`, commit `797f28f9`, PR #538, gemerged in `rc` op 2026-11-10 09:26 als `7be053a7`): VASIM rekent de verplaatsing alleen uit als de nieuwe positie past bij de bewegingsrichting. Dezelfde controle bestond al voor conveyors met een encoder.

## Opzet

- Backup uit het ticket: `20250031_V631_260526_104013.zip`.
- TwinCAT in kernel mode via de VACAM Launcher RC (de user mode runtime laadt op deze laptop geen NC-drivers, zie BT1-2325).
- Reproductie volgens Vincent: na de start via de Launcher de PLC, VACAM en VASIM opnieuw starten zonder de Launcher.
- Baseline: VASIM rc 2026.11.6.373 (zonder fix).
- Fix: VASIM gebouwd uit `rc` op `7be053a7`, `C:\Git\Vasim-BT1-2291\VASIM\bin\Debug\VASIM.exe`.

## Testgevallen

| # | Geval | Verwacht |
|---|---|---|
| T1 | Baseline: herstart zonder Launcher, balk op de infeed, detectie door de fotocellen | balk springt naar een hoge X (probleem gereproduceerd) |
| T2 | Fix: zelfde herstart en zelfde balk | balk blijft op de juiste X en komt onder de zaag voor de clear cut |
| T3 | Fix: verse start via de Launcher | normaal gedrag, geen regressie |

## Resultaat

| # | Resultaat | Opmerking |
|---|---|---|
| T1 | | |
| T2 | | |
| T3 | | |
