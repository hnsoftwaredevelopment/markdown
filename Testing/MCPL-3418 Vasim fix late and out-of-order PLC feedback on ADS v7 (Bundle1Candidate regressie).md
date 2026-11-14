---
ticket: MCPL-3418
jira: https://voortman.atlassian.net/browse/MCPL-3418
epic: MCPL-3088
branch: Vasim MCPL-3418_Bundle1Candidate (7b66f54e, 2026-11-02)
baseline: VASIM rc (MSIX)
vacam: develop setup via de Launcher
tags: [testplan, regressie, vasim, ads-v7]
---

# MCPL-3418 Vasim fix late and out-of-order PLC feedback on ADS v7 (Bundle1Candidate regressie)

## Doel

Controleren dat VASIM van de branch `MCPL-3418_Bundle1Candidate` (bundle 1 van de ADS v7-fixes) op de machinetypes V630, V631, V633 en V100 met probe truck minstens zo goed werkt als VASIM rc, met dezelfde VACAM develop, TwinCAT en backup. Een fout die alleen met de branch optreedt, is een regressie. Een fout die alleen met VASIM rc optreedt, kan een probleem zijn dat de bundle oplost.

> [!note] Baseline zit al op ADS v7
> VASIM rc draait sinds 9.0.16 op ADS v7 zonder deze fixes. De baseline kan dus zelf al de bekende symptomen laten zien (late of verkeerd geordende feedback). Noteer die apart.

## Wat er in de bundle zit

| Ticket | Wijziging | Waar je het merkt |
|---|---|---|
| MCPL-3090 | Beckhoff ADS 7.0.389 | verbinding met de PLC, opstarten |
| MCPL-3429 | Alle PLC-writes via één geordende wachtrij met ADS sum writes | sensoren en drive-feedback op tijd en in volgorde |
| MCPL-3430 | Notificaties per abonnement, in volgorde, niet op de ADS-thread | NC-assen, C300-drives |
| MCPL-3434 | Materiaal op een transportgroep springt niet meer bij een positiereset | V100 probe truck: -14903 "Probe does not detect material anymore" |
| MCPL-3449 | Conveyors draaien op de referentiesnelheid van de PLC (niet vast 1000 mm/s) | alle rollerbanen, jogsnelheid, positioneren |
| MCPL-3440 | 8-byte PLC-structs houden hun velden | variabelenboom van VASIM |
| MCPL-3432 / MCPL-3433 | Valk- en Stäubli-robots | niet op deze machines |

## Machines en backups

Alle backups komen uit `\\vasoftware\Testdata\RegressionTests`.

| Machine | Backup | Aandachtspunt |
|---|---|---|
| V630 | `20210779_V630_220419_105753.zip` | measure rollers, zaag (klemdruk -2458), conveyors |
| V631 | `V631\20250027_V631_261023_162024.zip` (materiaal `V631\HEA140_8000_minus12000.material.xml`) | measure rollers, boren, conveyors |
| V633 | `20200047_V633_250319_141727.zip` | tool length measurement ("Check the measured tool length", faalde altijd op ADS v7) |
| V100 met probe truck (VB Standard) | `LES\V100ProbeTruck\20240168_V100_260108_104405.zip` (materiaal `MaterialFileV100ProbeTruck.material.xml`) | probe truck verliest materiaal (-14903), transportgroep |
| VB1050 / VB1250 | geen backup gevonden | voorlopig niet in scope |

## Opzet

- **VACAM:** develop setup via de Launcher, per backup dezelfde versie voor de baseline en de branch.
- **TwinCAT:** via de Launcher (de plugin-route blijft op deze PC in Config hangen).
- **VASIM baseline:** VASIM rc, gestart door de Launcher.
- **VASIM branch:** lokale build uit de worktree `C:\git\Vasim-MCPL-3418` (beheerd door Claude). Na de baseline wordt VASIM rc gesloten en de branch-VASIM gestart. Die leest hetzelfde `VASIM.exe.ini` in `%LOCALAPPDATA%\Voortman\VASIM`.
- **Volgorde per machine:** eerst het hele scenario met VASIM rc, daarna met de branch. Tussen de twee runs worden de batch en het materiaal in VASIM gereset.

## Scenario per machine

| Stap | Wat | Waar let je op |
|---|---|---|
| S1 | VASIM starten en verbinden met de PLC | geen ADS-fouten, geen ontbrekende variabelen in de VASIM-log, machine komt in een normale toestand |
| S2 | Reset en reference run | reference point valid, geen halt of foutmelding |
| S3 | In- en outfeed conveyor joggen (op-view) | actual speed volgt de setpoint, geen sprongen, geen halt (ADS-logger op `Conveyor[i]`) |
| S4 | Handfuncties van de hoofdas en klemmen | assen bewegen, klemmen bereiken druk |
| S5 | Eén productiebatch (`produce.ps1`) | infeed, detect front/end, bewerkingen, afvoer; geen plausibiliteitsfouten |
| S6 | Machinespecifiek | V633: tool length measurement; V100: probe truck detecteert en volgt het materiaal; V630/V631: zaagklem op druk |

Bij een fout worden de VACAM-log, de VASIM-log en de StateMessages bewaard, met de tijd van de fout.

## Resultaat

| Machine | Stap | VASIM rc | Branch | Opmerking |
|---|---|---|---|---|
| V630 | S1–S6 | | | |
| V631 | S1–S6 | | | |
| V633 | S1 | OK met kanttekening: 211 keer "Slow ADS access" (178 WriteAny op de .NET-threadpool, één keer 847 ms wachten), 102 keer DeviceSymbolNotFound (DEBUG) | | VACAM develop 4.34.0-develop.2611041127, VASIM rc 2026.11.4.354 |
| V633 | S1 branch | | OK: verbinding gelijk aan rc (poort 501 "Invalid" bij beide), 18109 symbolen. Bij het opstarten een paar "Slow ADS access" van 110 tot 150 ms. Nieuw: `SwallowedFailureLog` voor `DrillChanger[0]` en `DrillChanger[2]` `.Tool[0].ToolID` (handle mislukt, wordt één keer gelogd; rc logt dit niet) | branch-VASIM gestart 16:06 |
| V633 | S2 | OK (reference run door Herbert) | OK | |
| V633 | S3 branch | | Conveyor[1] veel rustiger: bij ±308 mm/s meestal 304, 1 keer terugval naar 0 per richting, één piek van -456 bij het optrekken (rc: tot 608 en 10 keer 0). Conveyor[0] gelijk aan rc. Jog wel korter dan bij rc (ongeveer 2 s per richting) | 16:25:58 tot 16:26:08, `v633-branch-velocity.csv` |
| V633 | S4 branch | | OK (Herbert) | |
| V633 | S3 | Conveyor[0] volgt de setpoint (afwijking ongeveer 10 mm/s). Conveyor[1] springt: bij setpoint 308 mm/s actual tussen 0 en 608 (gemiddeld 286, spreiding 129), bij -308 tussen 0 en -570 | | 15:41:13 tot 15:41:54, `v633-rc-velocity2.csv` |
| V633 | S4 | OK (handfuncties door Herbert) | | |
| V633 | S5 | OK: lijst van 31 commands van 15:59:40 tot 16:04:00 afgerond ("Automatic ready, HasMoreLists=False"). Daarvoor 2 keer -3001 "No material on transverse transport" (materiaal lag nog niet op de dwarstransporteur) en 1 keer -1291 "Closing horizontal clamps at this position to measure material width not possible". Tijdens de run een paar keer W7-101-Y2/Z2 "Actual position passed calculated minimum" (boorunit 2, komt en gaat). Na afloop ERROR "MachineRootCycleEvent: Event 1002 status still active" (event 1002 twee keer ontvangen, 16:04:00.29 en 16:04:01.74). VASIM: 187 keer "Slow ADS access" in 4,5 minuut (113 ReadAny, 45 WriteAny, 26 Read), langste wachttijd **4921 ms** | | batch EF2, HE140A 7500 mm, operation list `15_59_40.8506.csv` |
| V633 | S5 herhaling (2026-11-05) | OK met fout in S6: VACAM 4.34.0-develop.2611041545 (de versie van 04-11 was niet meer beschikbaar). Balk HE140A 7500 mm op de infeed-rollerbaan (X -15000, Y 0), "Get material" op Redo. Lijst van 36 commands van 08:56:00 tot 09:06:50, daarna "Remove material manually" en "Automatic ready, HasMoreLists=False". Gripper (command 7) OK. Na afloop weer ERROR "Event 1002 status still active". W7-101-Y2/Z2 komt en gaat. VASIM: 26 keer "Slow ADS access", maximaal 302 ms | | |
| V633 | S5 rc, zelfde start als branch (2026-11-05 10:12) | OK: nieuwe lijst, balk op de rollerbaan, lijst afgerond om 10:18:01 (HasMoreLists=False). Command 7 OK. 6 keer "Slow ADS access", maximaal 156 ms. Na afloop weer "Event 1002 status still active" | **Fout:** command 7 -1219 "No material found in sensing move" (09:29:08), 2 van de 2 runs. Zie bevindingen: de balk springt bij de reset | |
| V633 | S5 branch, derde run (2026-11-05 10:36) | | **OK:** balk op X -15000 neergelegd, VASIM zet hem op -7000. Bij de reset (10:28) en tijdens de run geen sprong. Lijst van 33 commands afgerond om 10:43:04 (HasMoreLists=False), command 7 OK. **0 keer "Slow ADS access"** (rc: 6, maximaal 156 ms). PLC write queue: gemiddeld 4,1 ms en maximaal 16,7 ms latency, 0 failed. W7-101-Y2/Z2 en "Event 1002 still active" net als bij rc | |
| V633 | S6 branch handmatig (2026-11-05 10:53 tot 10:59) | | **OK:** 13 handmatige tool length measurements (DU-1 3, DU-2 5, DU-3 5), geen enkele keer "Check the measured tool length". **Nieuw:** op DU-1 werd de knop voor de tool measurement grijs na 3 metingen, ook na een tool change (nog met rc vergelijken) | telling door Herbert |
| V633 | S6 rc handmatig (2026-11-05 11:10 tot 11:35) | OK: 15 handmatige tool length measurements (5 per unit), geen enkele keer "Check the measured tool length". De DU-1-knop was ook met rc grijs, direct na het starten, en werkte weer na metingen op DU-2 en DU-3. VASIM rc 2026.11.5.358 (alleen een pipeline-wijziging, PLTS-1761, ten opzichte van 2026.11.4.354) | | DU-1-knop: geen verschil met de branch |
| V633 | S6 herhaling (2026-11-05) | **Fout:** "Check the measured tool length": HMDrill gemeten 306 mm, maximum 305 (08:56:23). Na Retry wel OK | | het bekende ADS v7-symptoom |
| V633 | S6 | OK: tool length measurement op boorunit 3 en 2 (begin van de lijst) en boorunit 2 na een tool change, geen "Check the measured tool length" | | |
| V100 probe truck | S1 | OK: VASIM rc 2026.11.5.358 om 12:11 verbonden, 18109 symbolen. 60 keer "Slow ADS access" (maximaal 221 ms), 4 keer een vertraagde simulatiestap (ConveyorOutfeed, SawHorizontalClampAxis, OTT, ITT), 15 keer DeviceSymbolNotFound | | VACAM 4.34.0-develop.2611041545, backup `20240168_V100_260108_104405.zip` |
| V100 probe truck | S2 | OK (Herbert) | | |
| V100 probe truck | S3 | Infeed `Conveyor[0]` volgt de setpoint ±208 mm/s binnen enkele mm/s. Outfeed `Conveyor[2]`: eerste poging 2 keer -7208 "Invalid start velocity" (12:17:21 en 12:17:22), tweede poging wel in beide richtingen. Daarbij te snel en springerig: bij +208 actual 266 tot 342 (gemiddeld 312), bij -208 tussen 0 en -494 (4 keer 0) | | `v100-rc-velocity.csv`, `v100-rc-velocity2.csv` (12:26:45 tot 12:26:55) |
| V100 probe truck | S4–S6 | niet uitgevoerd | niet uitgevoerd | test gestopt, zie hieronder |

**Test gestopt op 2026-11-05:** het team heeft genoeg informatie. De V100 is alleen met rc getest (S1 tot en met S3). V100 met de branch, V631 en V630 zijn niet getest.

## Conclusie V633

- **Geen regressie in de productie:** EF2 loopt met de branch tot het einde, net als met rc (2026-11-05 10:36 tegenover 10:12).
- **Verbetering:** de branch geeft 0 keer "Slow ADS access" tijdens de productie (rc: 6 tot 187 per run, maximaal 4921 ms). Conveyor[1] volgt de setpoint bij het joggen veel beter.
- **Tool length (S6):** de fout "Check the measured tool length" (306 mm) kwam één keer met rc, in de lijst van 08:56. Met de branch kwam hij in 13 handmatige metingen en 2 lijsten niet voor. Met rc kwam hij in de handmatige serie ook niet voor. De fout komt dus af en toe, en met deze aantallen is niet hard te bewijzen dat de branch hem oplost.
- **Te melden aan de ontwikkelaar (MCPL-3434):** de branch legt een balk op een andere X dan rc (X -15000 wordt -7000, bij rc -10500), Het verschuiven van een opgeslagen balk bij het opstarten doet rc ook. Eén keer sprong de balk bij een reset (09:26:52), met -1219 bij de gripper als gevolg. Dit was niet te reproduceren.
- **Geen verschil:** W7-101-Y2/Z2, "Event 1002 status still active", de grijze DU-1-knop, en "Get material" van de dwarstransporteur (faalt met beide versies).

## Bevindingen

- **V633, mogelijke regressie in de branch (materiaalpositie, gebied MCPL-3434):** dezelfde start (VACAM 2611041545, nieuwe lijst EF2, HE140A 7500 mm neergelegd op X -15000, Y 0), toch een ander verloop:
  - **rc (2026-11-05 10:10 tot 10:18):** VASIM zet de balk direct na het neerleggen op X -10500 (10:10:33). Bij de reset blijft hij daar liggen. De PLC draait de infeed-rollers, MaterialDetection1 wordt true (10:12:37), de feeder truck pakt de balk op X -4991 en de klemmen HC1/HC2 sluiten tot 133. De lijst loopt tot het einde.
  - **Branch (2026-11-05 09:26 tot 09:29):** VASIM zet de balk direct na het neerleggen op X -7000 (09:26:27). Bij de reset **springt de balk zonder conveyorcommando van X -7000 naar -1500** (09:26:52.277, terwijl as T3 beweegt), en alle front-detectiesensoren worden false. De PLC draait de infeed-rollers niet. De feeder truck zoekt op X -10626 (sensing move Y 66,5, Z 58), de klemmen sluiten tot 149 zonder materiaal, en command 7 faalt met -1219 "No material found in sensing move". Op 2026-11-04 om 16:39 gaf de branch dezelfde -1219.
  - **Derde branch-run (10:36):** geen sprong, en de lijst loopt tot het einde. De sprong om 09:26:52 viel samen met beweging van de assen T1 tot en met T3 bij de reset (280 naar 277, 80 naar 82,5). Bij de reset van 10:28 bewogen die assen niet. De sprong is dus niet elke keer te reproduceren.
  - **Wel elke keer anders:** bij het neerleggen op X -15000 zet de branch de balk op -7000 en rc op -10500 (2 van de 2). Bij het opstarten verschuift de branch een balk uit `MaterialV2.xml` van -5500 naar +2000. **Correctie (2026-11-05 12:11):** VASIM rc doet dit ook (bij de start van de V100-sessie van X 2000 naar 7500). Het verschuiven bij het opstarten is dus geen verschil tussen de versies.
- **V633, rc en branch:** "Get material" van de dwarstransporteur faalt met -3001 "No material on transverse transport", gevolgd door S11-105 "Axis stuck" op `TransverseInfeedAxis`. De as zoekt van Y ongeveer 1100 tot 7650 (`PositionEndTransverse`) en vindt de balk niet. Bij rc gebeurde dit om 15:48 en 15:50, bij de branch om 16:28. Dit is geen regressie. De geslaagde rc-run (15:59) begon met het materiaal al op de infeed-rollerbaan, zonder "Get material".
