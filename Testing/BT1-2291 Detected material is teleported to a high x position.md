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
- Materiaal na de referentierun opnieuw zetten: tijdens de referentierun schuift VASIM de balk naar Y ~1007 (van de rollen af), waarna de infeed een time-out geeft op de fotocel. Zet de balk in VASIM terug op Y 0. Let op: Material > Open material file voegt een balk toe; verwijder daarna de oude rij.
- Fix: VASIM gebouwd uit `rc` op `7be053a7`, `C:\Git\Vasim-BT1-2291\VASIM\bin\Debug\VASIM.exe`.

## Handmatige stappen

Voorbereiding (saw-route terughalen):
1. Sluit VACAM en VASIM.
2. Start in de VACAM Launcher RC de backup `20250031_V631_260526_104013` met develop, VASIM rc en "delete existing database" aan.
3. Controleer na de start dat de operatielijst "Infeed operation to fc 1 (saw)" bevat (in VACAM of in `<VACAM-map>\Logs\AutomaticProductionList`). Sla de trim cut later niet over: dan plant VACAM daarna de drill-route (fc 2).

Herstart zonder Launcher (zoals Vincent):
4. Sluit VASIM en VACAM (VACAM: "Do you want to shut down VACAM?" met Yes).
5. Herstart de PLC zonder Reset of Reset Origin: TwinCAT-icoon in het systeemvak, System, Config; daarna System, Start/Restart. Wacht tot het icoon groen is (Run).
6. Start VASIM rc en direct daarna `C:\Temp\Vacam\4.34.0-develop.2611091634\VACAM.exe`.

Productie:
7. Druk in VASIM op Reset en daarna op Start voor de referentierun. Wacht tot de referentierun klaar is.
8. Zet de balk in de VASIM-tabel terug: X -10299,5 (voorkant), Y 0, lengte 6100. Tijdens de referentierun schuift VASIM hem naar Y ~1007.
9. Druk op Start. Op "Confirm material on datumline" antwoord je Yes.
10. Volg de X position in de VASIM-tabel. Rond de fotocel (X ~-5800) stopt de balk even voor de frontdetectie.
    - Probleem: X springt naar een hoge waarde (~+8000).
    - Goed: X loopt gelijkmatig door en de balk stopt voor de trim cut onder de zaag.

Met de fix (T2): herhaal stap 4 t/m 10, maar start bij stap 6 `C:\Git\Vasim-BT1-2291\VASIM\bin\Debug\VASIM.exe` in plaats van VASIM rc. Controleer dat de titel `MC_20250031_V631` toont.

## Testgevallen

| # | Geval | Verwacht |
|---|---|---|
| T1 | Baseline: herstart zonder Launcher, balk op de infeed, detectie door de fotocellen | balk springt naar een hoge X (probleem gereproduceerd) |
| T2 | Fix: zelfde herstart en zelfde balk | balk blijft op de juiste X en komt onder de zaag voor de clear cut |
| T3 | Fix: verse start via de Launcher | normaal gedrag, geen regressie |

## Resultaat

| # | Resultaat | Opmerking |
|---|---|---|
| T1 | niet gereproduceerd (3 cycli) | Cyclus 3 (14:02) in de volgorde van Vincent (VASIM en VACAM sluiten, PLC herstarten, VASIM en direct daarna VACAM starten): de balk liep gelijkmatig naar X 69, geen sprong bij de fotocel (~X -5800). Cyclus 1 volgde de saw-route (fc 1, trim cut); cycli 2 en 3 volgden de drill-route (fc 2, front detectie en breedtemeting). |
| | | Cycli 1 en 2: 2026-11-10, VACAM 4.34.0-develop.2611091634, VASIM rc 2026.11.6.373. Per cyclus: VACAM en VASIM netjes gesloten, kernel TwinCAT Config en dan Run, VACAM en VASIM gestart zonder Launcher, referentierun, daarna de balk opnieuw gezet (6100 mm, voorkant X -10299,5, Y 0). Cyclus 1: de balk liep gelijkmatig naar X -3158 (trim cut). Cyclus 2: de balk liep gelijkmatig naar X 70 (daarna "Unable to measure the width", door het gesimuleerde profiel). Geen sprong in X. Beelden: `C:\Temp\Customers\_jira\BT1-2291\T1-cycle*-baseline-x.png` |
| T2 | | |
| T3 | | |
