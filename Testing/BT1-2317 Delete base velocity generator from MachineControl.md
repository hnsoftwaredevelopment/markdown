# BT1-2317 Delete base velocity generator from MachineControl

Ticket: [BT1-2317](https://voortman.atlassian.net/browse/BT1-2317) · status In Test · ontwikkelaar André Holtschlag · kloon: BT1-2461

## Wijziging

PR #22779 (BT1-2461, gemerged in `develop` van vacam-twincat op 2026-11-06, merge `b2283e82eb7`):
- MaterialHandling-library van 0.64.0 naar 0.91.0. De TransportGroup en de velocity generator (VG) van de motion library zitten in deze library.
- Nieuwe machine-instelling "Use motion library velocity generator" (`bUseMotionLibraryVeloGenerator`, categorie Motion, standaard No). Met Yes gebruiken de transportgroep en de V623-outfeed de VG van de motion library, met No de oude VG. Na het wijzigen is een herstart van VACAM nodig.
- V912: de instelling staat altijd aan (gezet bij het opstarten, niet zichtbaar in VACAM).
- V623-integratie: AutomaticListAvailable en AutomaticListActive worden niet meer naar het klemsysteem geschreven.

Volgens André (2026-11-06) is vooral belangrijk dat een V100 PT, V623 en V807 met de instelling uit werken zoals voorheen. Testen met de instelling aan mag; daarvoor komen aparte tickets voor echte machines. V623 is getest door Martijn (2026-11-09, geslaagd).

## Risico

De X-beweging van de V807 en de PT-beweging van de V100 hangen direct af van de snelheidscurve van de VG. Met de instelling uit loopt de oude VG, maar de library-update (0.64 naar 0.91) raakt ook andere delen van materiaaltransport.

## Opzet

- VACAM develop 4.34 via de VACAM Launcher RC, kernel mode TwinCAT (de user mode runtime laadt geen NC-drivers op deze laptop, zie BT1-2325).
- Vergelijking: dezelfde lijst met dezelfde balk in VASIM, met de instelling uit en aan. Ik log over ADS elke 100 ms de doelpositie en doelsnelheid van de transportgroep en de werkelijke snelheid van de assen en rollen.
- Backups:
  - V100: `20250103_V100_261012_152224` (VB1250 European Staal Hamm)
  - Rollen-outfeed (TransportGroupRollers): V631 `20250031_V631_260526_104013` (Maksim)
  - V807: `C:\Temp\20200036_V807_210331_115626.zip` (backup uit 2021, met robot en plasmabron)
  - V912: valt buiten deze test, de instelling staat daar altijd aan en BT1-2325 blokkeert de V912 in simulatie

## Testgevallen

| # | Machine | Geval | Verwacht |
|---|---|---|---|
| T1 | V100 | instelling uit (standaard): referentierun en een lijst produceren, PT/X-beweging loggen | lijst loopt zonder fouten, transport zoals voorheen |
| T2 | V100 | instelling aan, VACAM herstarten, dezelfde lijst | lijst loopt zonder fouten, snelheidscurve gelijk aan T1 (kleine afwijkingen toegestaan) |
| T3 | V631 | instelling uit: outfeed via de rollen | outfeed zonder fouten |
| T4 | V631 | instelling aan: outfeed via de rollen | gelijk aan T3 |
| T5 | V807 | instelling uit en aan, X-beweging | gelijk gedrag |
| T6 | alle | de instelling bestaat in VACAM (categorie Motion), standaard No; bij de V912 niet zichtbaar | zoals beschreven |

## Resultaat

| # | Resultaat | Opmerking |
|---|---|---|
| T1 | open | 2026-11-12, VB1250 (`20250103_V100_261012_152224`), VACAM 4.34.0-develop.2611121154. Batch1 (IPE270, 6000 mm, 6 producten) door Herbert aangemaakt. Referentierun goed; lijst gemaakt (26 commando's), maar de productie bleef staan na "Execute trim cut" (Start ontvangen, geen beweging). Deze machine positioneert met een stop truck (Axis[2]) en handmatige acties; de waarden van TransportGroup[0..1] bleven 0. Herbert vraagt André of deze backup geschikt is voor de PT-beweging. |
| T2 | open | wacht op T1 |
| T3 | open | V631, nog niet uitgevoerd |
| T4 | open | V631, nog niet uitgevoerd |
| T5 | geslaagd | 2026-11-12, V807 Pamo Metaalwerken (`20200036_V807_210331_115626`, backup VACAM 4.11.0), VACAM 4.34.0-develop.2611121422, VASIM rc, kernel TwinCAT via de Launcher. Batch "RegressionTest" (IPE300, 3000 mm, 2 producten, 60 commando's), balk in VASIM voorkant X 0 / Y 0. Uit (16:58) en aan (18:45, na een verse Launcher-start, instelling in de MC-database op Yes en een herstart van PLC, VASIM en VACAM; `bUseMotionLibraryVeloGenerator` in de PLC TRUE): beide lijsten volledig afgewerkt ("Automatic ready, HasMoreLists=False"), dezelfde operatorstappen (Clean material, Remove material manually). TransportGroup[0] doet in beide runs dezelfde 21 positioneringen; de eindpositie van de voorkant verschilt per positionering hooguit 0,02 mm (beide ~1 mm voor het doel, bekend VASIM-gedrag), de reistijd tot binnen 1 mm verschilt hooguit 0,4 s (de ADS-log tikt per 50 ms). Bewijs: `C:\Temp\Customers\_jira\BT1-2317\V807-*` |
| T6 | deels | De instelling staat niet in de MC-database tot hij gewijzigd wordt (standaard No; PLC FALSE op VB1250 en V807). Met de rij `UseMotionLibraryVeloGenerator` = 0x01 (ClassID 1) zet VACAM de PLC-variabele op TRUE. Niet gecontroleerd: het VACAM-scherm (categorie Motion) en de V912. |

Bijzonderheden:
- Alleen VACAM herstarten na het wijzigen van de instelling (zonder PLC-herstart) gaf "Configuration failure: PLC is into Error state". Na een herstart van PLC, VASIM en VACAM was dat weg. Niet nagegaan of dit ook gebeurt met de instelling uit; de helptekst noemt alleen een VACAM-herstart.
- Bij het sluiten van VACAM op de V807 bleef het proces hangen op verbindingen met de robotcontroller (192.168.6.40, bestaat niet in simulatie); met akkoord van Herbert beëindigd.
- Een vergissing in mijn sluitscript beantwoordde "delete old products and completed batches?" met Yes: 3 producten zonder batch zijn uit VACAM_20200036 verwijderd. De testbatch en het bufferitem bleven intact.
