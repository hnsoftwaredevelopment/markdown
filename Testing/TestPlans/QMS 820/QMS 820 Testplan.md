---
type: epic-testplan
jira: BT1-2432
title: "QMS 820 Testplan"
fix_version: 4.11 (RC-4.11.36 + PR #23387)
rc_branch: Release-4.11
machines: [V630Mk2, V631, V633]
risk: High
tester: Herbert Nijkamp
created: 2026-11-25
test_start:
test_end:
status: draft
tags: [testplan, epic, qms820]
---

# QMS 820 Testplan

Zie ook [[QMS 820 Analyse]], [[QMS 820 Testwerkwijze]] en [[QMS 820 Testproducten]].

## 1. Doel

- **Jira:** epic [BT1-2432](https://voortman.atlassian.net/browse/BT1-2432), PR [#23387](https://github.com/voortman-steel-machinery/vacam-twincat/pull/23387) (4.11).
- **Wat de klant na deze wijziging kan:** op een V630Mk2, V631 of V633 met measure rollers bewerkingen in het gebied van de measure wheels maken met zo min mogelijk heen-en-weer-bewegingen, ook na een flange removal. Een batch die vroeger stopte met "There should at least be one take over path" loopt door, eventueel zonder de bewerkingen die echt niet kunnen, en die worden gemeld.
- **Klaar met testen als:** alle testgevallen hieronder een resultaat hebben, de klantbatches uit de QMS-tickets met de standaardinstelling lopen of een verklaard resultaat hebben, en er een V631- en een V633-job in VASIM met Minimize material reversals volledig is afgewerkt.

## 2. Scope

| Machine | In scope | Waarom | Grootste risico |
|---|---|---|---|
| V630Mk2 measure rollers | Ja, beperkt | zelfde planner-code als V631 | geen eigen backup bekend |
| V631 measure rollers | Ja | meeste tickets, standalone en B2B | take overs, flange removals |
| V633 measure rollers | Ja | x'-as-groepen, eigen sortering | clamping en groepen rond divisions |
| Machines met feeder truck/gripper | Nee | instelling bestaat daar niet | controleren dat de instelling er niet is |

**Buiten scope:** nauwkeurigheid op een echte machine (BT1-2444), de develop-versie (PR #22638, aparte test), BT1-2469 oplossen (wel vastleggen).

## 3. Stories

| Story | Samenvatting | Status | Test hier |
|---|---|---|---|
| BT1-2433 | Spike: materiaalverplaatsing en cyclustijd | In Review | gebruiken als referentie voor cyclustijd |
| BT1-2434/2435/2436/2439 | interne refactoring planner | In Review | indirect via alle tests |
| BT1-2437 | sorteren V630Mk2/V631 | In Review | S-, V-tests |
| BT1-2438 | x'-as-groepen V633 | In Review | X-tests |
| BT1-2440 | annuleren in het meetgebied | Ready to Develop (deels in 4.11) | M-tests |
| BT1-2441 | take overs volgen de pass | In Review | T-tests |
| BT1-2442 | instelling (in 4.11: "Operation sorting") | In Review | I-tests |
| BT1-2443 | fallback | In Review | F-tests |
| BT1-2444 | validatie op een machine | Ready to Develop | buiten scope |
| BT1-2469 | bug take over path bij flange removals | New | M-07 |

## 4. Wat kan met en zonder VASIM

Legenda: **A** = zonder VASIM (planning, cycle tab), **B** = met VASIM, **C** = alleen op een echte machine.

| Onderdeel | A zonder VASIM | B met VASIM | C machine |
|---|---|---|---|
| Instellingen: bestaan, waarden, standaard, gebruikersniveau, helptekst, machines zonder measure rollers | ✔ volledig | - | - |
| Upgrade: standaardwaarde na update van een 4.11-backup | ✔ volledig | - | - |
| Volgorde van de stappen (passes, stijgend/dalend, detected pieces, divisions eerst) | ✔ volledig | bevestigen | - |
| Welke MRU vasthoudt, plaats van take overs | ✔ uit de lijst | ✔ echt uitgevoerd | - |
| Validatie: undoable bewerkingen en melding aan de operator | ✔ volledig | bevestigen dat ze echt niet gemaakt worden | - |
| Fallback: wanneer, welke lijst, log, undoable-markeringen | ✔ volledig | ✔ de geredde job ook draaien | - |
| Default gelijk aan voorheen (regressie) | ✔ lijsten vergelijken | steekproef | - |
| Operation bundling distance | ✔ volledig | - | - |
| Gereedschapswissels (aantal, handmatig gegroepeerd) | ✔ tellen | ✔ ook uitvoeren | - |
| Band per profieltype, measure wheel position | ✔ uit undoable/volgorde | ✔ wheel niet boven bewerking | - |
| Take over voor de outfeed, automatisch afvoeren | deels (commando zichtbaar) | ✔ | - |
| Afzagen bij de zaag (B2B) | deels | ✔ | - |
| V633 clamps en force calculation | deels | ✔ | - |
| Stop en herstart, regeneratie | - | ✔ | - |
| Cyclustijd | schatting (aantal wissels, verplaatsing) | ✔ bij benadering | ✔ |
| Positieafwijking | - | - | ✔ (BT1-2444) |

Ongeveer 70% van de testgevallen kan zonder VASIM.

## 5. Risico's

Zie [[QMS 820 Analyse]] §5. Hoogste: R10 (BT1-2469), R1 (Default verandert), R2 (standaard Default with fallback), R3 (stil annuleren), R4/R5 (measure wheel en take overs tijdens uitvoering).

## 6. Testgevallen

Per testgeval: niveau, producten, en het resultaat later. "Min" = Minimize material reversals, "DwF" = Default with fallback.

### I. Instellingen (A)

| # | Test | Verwacht | Resultaat |
|---|---|---|---|
| I-01 | "Operation sorting" op V630MK2, V631, V633 met measure rollers | aanwezig, 3 waarden, standaard **Default with fallback**, gebruikersniveau Operator, categorie Automatic, helptekst klopt | deels geslaagd (V631, 25-11): zichtbaar als Experienced operator onder "Automatic production", waarde Default with fallback, helptekst gelijk aan de PR maar te lang voor het beschrijvingsvak (afgekapt). V633 en V630MK2 nog open. |
| I-02 | "Operation bundling distance" | V630MK2/V631 ja, V633 nee; standaard 10, min 0, eenheid mm | deels geslaagd (V631, 25-11): 10.0 mm. V633 nog open. |
| I-03 | Machine zonder measure rollers (feeder truck V631/V633, V630 oud, VB) | beide instellingen niet zichtbaar | open |
| I-04 | Upgrade van een 4.11-backup (vóór de PR) | instellingen krijgen de standaardwaarde, geen fout bij starten | open |
| I-05 | Instelling wijzigen en lijst opnieuw genereren | nieuwe sortering wordt gebruikt (zonder herstart, of melding dat herstart nodig is) | open |
| I-06 | Preferred measure roll unit samen met elke sortering | wordt gebruikt bij Default en DwF, niet bij Min | open |

### S. Sortering V630Mk2/V631 (A, bevestigen in B)

| # | Test | Producten | Verwacht | Resultaat |
|---|---|---|---|---|
| S-01 | Standalone, één stuk | P01, P05 | Min: alle stappen stijgend; Default: per gereedschap; minder reversals en meer automatische wissels met Min | deels 25-11, V631 KSH (20240105, zonder zaag in de lijst): P01 Default en Min gelijk, 51 bewerkingen, 0 reversals, 6003 mm, 16 automatische wissels. Default groepeert hier ook niet per gereedschap, dus de verwachting klopt niet voor deze machine. Herhalen op V633 B2B. P05 nog niet gemaakt |
| S-02 | B2B, nesting | P02 | controleregels 1 t/m 5 (Testwerkwijze §4) | deels 25-11, V631 KSH: Default, DwF en Min gelijk, 29 bewerkingen, 0 reversals, 10816 mm, 38 wissels, stukken één voor één van voor naar achter. Geen zaagsneden in de V631-lijst (VB1050 zaagt), dus de regels voor divisions niet getest. Herhalen op V633 B2B.<br>25-11, V631 met zaag (Overhalla 20250057), 4 stuks van 1800 op 12000: **Default en DwF**: eerst alle gaten oplopend (5059 → 11667), daarna terug voor alle zaagsneden (6964, 5162, 3359, 1556). **Min**: materiaal door naar 11667, dan één aflopende pass met per stuk boren en direct afzagen. Volgt de outfeed-pass-regel van BT1-2437. Verplaatsing in beide 24,4 m. 3 van 35 bewerkingen zonder uitvoerder (nog uitzoeken). Lijsten in `C:\Temp\Customers\_jira\QMS820\P02-V631saw\` |
| S-03 | Flange removal op twee flenzen | P03 | Min: één doorgang; Default: geen extra slag terug meer voor flange removals | geslaagd voor Default 25-11, V631 KSH: Default, DwF en Min gelijk, 27 bewerkingen, 0 reversals. Elke flange removal is één freesbewerking van 4000 mm (DU3 bij 1053, DU2 bij 5037), niet meer naar het einde geschoven |
| S-04 | Handmatige wissel | P04 | handmatige wissels gegroepeerd waar mogelijk, toegevoegd waar de volgorde dat vraagt; geen gat verschoven naar een ander stuk (job 5089) | open |
| S-05 | Bundling distance 0 / 10 / 600 bij Default | P01 | 600: weer bundelen per gereedschap (meer reversals), 10 en 0: in X-volgorde | open |
| S-06 | Korte stukken en schuine einden | P30, P31 | geen exception, regel 1 gerespecteerd, short parts forwarding werkt | open |

### X. V633 (A en B)

| # | Test | Producten | Verwacht | Resultaat |
|---|---|---|---|---|
| X-01 | Groepen volgen de passes | P02 op V633 | geen groep met twee passes of detected pieces; volgorde zoals regel 2 | open |
| X-02 | Gat vlak bij de zaagsnede | P32 | Min: aparte groepen; Default: één groep | open |
| X-03 | Block-out voor de snede (job 22343) | P33 | lijst wordt gemaakt, forwards piece na zijn division | open |
| X-04 | Clamps bij begin/einde en division | P34 | in VASIM: juiste clamps, geen force-melding | open |

### T. Take overs (A, B)

| # | Test | Producten | Verwacht | Resultaat |
|---|---|---|---|---|
| T-01 | Outfeed MRU tijdens de outfeed pass, één take over naar infeed | P02 | zoals BT1-2441 happy flow | open |
| T-02 | Late take over in het meetgebied | P11 | take over op het laatste moment, gat gemaakt | open |
| T-03 | Take over voor de outfeed | P02, P01 | materiaal zo ver mogelijk naar buiten, automatisch afgevoerd (B) | open |
| T-04 | Take over voor de outfeed onmogelijk | P10 | infeed MRU voert uit, geen exception | open |
| T-05 | Division die de outfeed MRU niet kan vasthouden | P02 variant met kort stuk aan de infeed-kant | gemaakt met de infeed MRU | open |

### M. Measure wheel en validatie (A, bevestigen in B)

| # | Test | Producten | Verwacht | Resultaat |
|---|---|---|---|---|
| M-01 | Blokkerend gat in het meetgebied, take over onmogelijk | P10 | undoable + zichtbaar voor de operator; rest gemaakt; geen exception | nog niet bereikt met een eigen product. P10L/P10Lz (L150x14, 6000, gaten in de band aan de infeed-kant, 26-11): Default, DwF en Min plannen alles, niets blokkeert (na die gaten hoeft niet meer gemeten te worden). P10N (27-11, zie M-02): Min plant alles. P10M (27-11, dichter: 12 stukken van 500 op 12000, gaten in de band op x 40, 250 en 460 van elk stuk): Default faalt, DwF en Min plannen alle 84 gaten en 13 zaagsneden; de DwF-lijst is op bewerkingen gelijk aan Min. Een eigen product waarbij ook Min bewerkingen moet weghalen, heb ik nog niet. Wel gezien bij klantjobs: SWMS-10421, -10635, -11058 en -11375 (zie F-02 en M-10). |
| M-02 | Blokkerend gat, take over mogelijk | P11 | gemaakt | **geslaagd** (27-11, P10N: 6 stukken L150x14 van 1000 op een staaf van 12000, V631 Overhalla, gaten Ø22 in de band op x 100 en 900 van elk stuk). Default faalt: "The measure roll units can't take over the material where the plan needs it." DwF: "Planning attempt 1 ... failed MaterialTakeOverNotPossibleException", daarna "Planned ... with planning attempt 2". De DwF-lijst is gelijk aan Min: measure roll unit 2 neemt bij 730,5 over, boren en zagen wisselen elkaar af, alle 30 gaten en 6 zaagsneden zitten erin, niets verwijderd. Lijsten in `C:\Temp\Customers\_jira\QMS820\P10N-V631saw`. |
| M-03 | Gat in de band buiten het meetgebied | P12 | gemaakt, wheel loopt er niet over terwijl hij meet (B) | open |
| M-04 | Gat buiten de band / in de voorste flens | P13, P14 | blokkeert niet | open |
| M-05 | Kopplaat-patroon + blokkerend gat | P15 | patroon gemaakt, alleen blokkerende feature eventueel undoable | open |
| M-06 | Flange removal en gat gemengd | P16 | zelfde regels | open |
| M-07 | BT1-2469 reproduceren | P17 | bekende bug: vastleggen met elke sortering | **niet uitvoerbaar met een NC1-product** (27-11): flange removals van 10 mm in de band van een I-profiel geven "Milling not possible" (zie [[QMS 820 Testproducten]], groep B). Het ticket komt uit een synthetische characterization test. Dezelfde foutmelding treedt wel op bij SWMS-10421, -10635 en -11058 met de baseline 4.11.36.1; met de PR en DwF krijgen die jobs een lijst. |
| M-08 | Lange sleuf | P18 | geen exception; sleuf gemaakt of verklaarbaar undoable | open |
| M-09 | Band per profieltype | P20 t/m P26 | gat in de band blokkeert, net erbuiten niet; RHS volgt de measure wheel position; special/bundel: niets blokkeert | open |
| M-10 | Undoable-markering in de UI | P10 | operator ziet welke bewerkingen niet gemaakt worden en waarom; ongedaan maken werkt | **niet geslaagd** (26-11, SWMS-11058, V633, DwF): de fallback verwijdert 1 van 33 bewerkingen (de DU2-freesbewerking op y 41 van het vierde stuk, vlak voor de zaagsnede bij 4011; DU3 op y 20 blijft). De operator krijgt geen melding: geen pop-up, statusregel "No automatic list available", de Cycle-lijst ziet er normaal uit. In de database hebben alle bewerkingen status 0 (geen undoable-markering). De log noemt alleen het aantal ("1 out of 33 operation(s) could not be planned"), niet welke bewerking. Zie bevinding 7. |

### F. Fallback (A, één geval ook in B)

| #    | Test                                        | Verwacht                                                                                    | Resultaat                                                                                                                                                                                                                                                |
| ---- | ------------------------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| F-01 | DwF, Default slaagt                         | lijst gelijk aan Default, niets in de log over fallback                                     | geslaagd (27-11, SWMS-10455 en SWMS-10758, V633): de DwF-lijst is regel voor regel gelijk aan de Default-lijst; geen regel over een planningspoging of fallback in de log. |
| F-02 | DwF, Default faalt (take over), Min slaagt  | job loopt; waarschuwing + info in de log; alleen undoable wat de tweede validatie annuleert | geslaagd (25-11, SWMS-11375): "Planning attempt 1 for 39473 failed MaterialTakeOverNotPossibleException", "2 out of 100 operation(s) could not be planned", "Planned 39473 with planning attempt 2". Aanvulling 27-11: bij SWMS-10421, -10635 en -11058 is de DwF-lijst regel voor regel gelijk aan een losse Minimize-run, met hetzelfde aantal verwijderde bewerkingen (5/108, 4/108, 1/33). De fallback verwijdert dus alleen wat de Minimize-validatie verwijdert. Zichtbaarheid voor de operator: zie M-10. |
| F-03 | DwF, beide falen (P17)                      | de fout van de eerste poging; undoable zoals na de eerste poging                            | niet uitvoerbaar in de UI (geen job of NC1-product waarbij beide pogingen falen, zie M-07). Code review PR #23387: na twee mislukte pogingen gooit VACAM de exception van de eerste poging opnieuw en zet de undoable-markering van de eerste poging terug. Komt overeen met de verwachting. |
| F-04 | DwF, Default faalt met een andere exception | geen tweede poging (alleen bij take over not possible)                                      | niet uitvoerbaar in de UI (geen klantjob gevonden waarbij Default met een andere exception faalt). Code review: alleen `MaterialTakeOverNotPossibleException` leidt tot een tweede poging; elke andere exception bij de eerste poging wordt direct doorgegeven. Komt overeen met de verwachting. |
| F-05 | Default (zonder fallback), job die faalt    | één poging, zelfde fout als voorheen                                                        | geslaagd met opmerking (25-11, SWMS-11375): één poging, batch geannuleerd. De melding is nu "The measure roll units can't take over the material where the plan needs it." in plaats van "There should at least be one take over path."                  |
| F-06 | Planning annuleren tijdens het plannen      | geen tweede poging                                                                          | niet uitvoerbaar in de UI: plannen duurt hier ongeveer 1 seconde. Code review: `OperationCanceledException` wordt niet afgevangen, dus geen tweede poging. Opmerking: `CalculateSchedule` geeft `CancellationToken.None` mee aan het execution framework; annuleren tijdens die aanroep werkt dus niet. Dat was vóór de PR al zo. |
| F-07 | Een met DwF geredde job in VASIM draaien    | loopt af, bewerkingen zoals gepland                                                         | geblokkeerd: VASIM werkt nog niet op deze laptop (BT1-2325). |

### R. Regressie en klantbatches (A, steekproef B)

| # | Test | Verwacht | Resultaat |
|---|---|---|---|
| R-01 | Per QMS-backup (11 stuks): plannen met 4.11 zonder PR en met de PR (Default, DwF, Min) | DwF lost de cancellation-tickets op of het resultaat is verklaard; Min vermindert reversals bij de sequencing-tickets | bezig. SWMS-11118 (V631, SHS400x400x16): DwF en Min geven een lijst (identiek, één stuk); de oude fout was "Expected exactly one clamp" (andere bug). SWMS-11375 (V631, L200x100x15, 19 producten): Default faalt, DwF redt de job via Min (zie F-02). SWMS-10421 (V633 standalone, L10x10x1-3/8, 12192 mm): DwF redt de job via Min, 5 van 108 bewerkingen vallen af, 2 reversals in het laatste stuk (take over naar unit 1 en terug). Voor de simulatie: Tekla EPM-koppeling van de batches gewist (`CutListItemId = 0`) en de robotbatterij-waarschuwing met No beantwoord. SWMS-10635 (V633 standalone): DwF redt de job via Min, 4 van 108 bewerkingen vallen af, 2 reversals. SWMS-11058 (V633 B2B, backup 260519): DwF redt de job via Min, 1 van 33 bewerkingen valt af, 3 reversals. SWMS-10455 (V633, KK200/120/6, 11,2 m, zelfde materiaal als bij de klant: "22 out of 103"): plant nu al bij poging 1 met Default, 0 reversals, geen fallback nodig (waarschijnlijk door de 5 mm measure wheel margin en het niet meer uitstellen van flange removals). SWMS-10576 (V631, HE180A) en SWMS-10758 (V633, HE220A): DwF en Min geven identieke lijsten (10576: 1 reversal, 31,9 m verplaatsing, 54 automatische wissels; 10758: 0 reversals). Let op: de cycle tab neemt het eerste bufferitem; of dat het materiaal uit de klacht is (flange removals op twee flenzen) moet nog nagegaan worden. SWMS-11000: zip zonder index.xml (oud formaat), nog niet gestart. SWMS-11017: productielijn met de loading panel als hoofdmachine, cycle tab van de V631 niet direct bereikbaar, nog niet gelukt. SWMS-10725 kan niet: backup is VACAM 4.28.<br>**Baseline 4.11.36.1 zonder de PR (26-11):** SWMS-10421, -10635 en -11058 worden geannuleerd met "There should at least be one take over path", zoals in de tickets; met de PR redt DwF ze alle drie (5, 4 en 1 bewerking verwijderd). SWMS-10758: baseline schuift de DU2-flange removals naar het einde (terug naar 4401 en 8809), 2 reversals, 16,7 m; met de PR frezen DU2 en DU3 op dezelfde positie, 0 reversals, 7,9 m. Precies de klacht, opgelost. SWMS-10455 en -11118: baseline plant ook, lijsten gelijk (10455: 11115 tegen 11170 mm). P02 op V631 Overhalla: baseline regel voor regel gelijk aan PR Default. Op geen enkele job is de PR slechter dan de baseline. Bewijs: `C:\Temp\Customers\_jira\QMS820\R-*` (BASE-4.11.36.1-*) |
| R-02 | Bestaande backups zonder QMS-probleem (V631, V633) met Default | lijst gelijk aan 4.11 zonder PR, op de bekende verschillen na | open |
| R-03 | Twee klantbatches met Min in VASIM volledig produceren (één V631, één V633) | loopt af zonder melding | open |

### E. Exploratory (B)

- **E-01, 90 min, V631 B2B:** stop, E-stop en herstart midden in een Min-lijst, bewerkingen handmatig ongedaan maken en opnieuw plannen, instelling wisselen tussen batches.
- **E-02, 90 min, V633:** zelfde, plus x'-as-groepen rond divisions en korte stukken.

## 7. Niet-functioneel

- [ ] **Cyclustijd:** P01, P02 en twee klantbatches met Default en Min. Default: ___ s, Min: ___ s, aantal automatische wissels ___ / ___.
- [ ] **Planningstijd:** DwF met een falende eerste poging (verwacht ongeveer twee keer zo lang). Vastleggen bij de grootste klantbatch.
- [ ] **Log:** waarschuwing en info van de fallback zijn begrijpelijk voor support.
- [ ] **Vertalingen:** nieuwe instellingen en waarden in het Engels en Nederlands.

## 8. Upgrade

| Instelling | Standaard na upgrade | Gecontroleerd op |
|---|---|---|
| Operation sorting | Default with fallback | |
| Operation bundling distance | 10 mm (V630MK2/V631) | |

## 9. Tijdsinschatting

Uitgaande van dat ik de lijsten zelf genereer en analyseer, en dat er een actuele installer is. Dagen van 8 uur.

| Onderdeel | Tijd | Opmerking |
|---|---|---|
| Voorbereiding: installer, referentieversie, backups uitpakken, machineconfiguraties vastleggen | 1 dag | wacht op een nieuwe installer |
| Testproducten maken (NC1) en het analysescript voor de cycle list | 1 dag | eenmalig, daarna herbruikbaar |
| I. Instellingen en upgrade | 0,5 dag | |
| S. Sortering V630Mk2/V631 | 1 dag | |
| X. V633 (zonder VASIM) | 0,5 dag | |
| T. Take overs (lijst) | 0,5 dag | |
| M. Measure wheel en validatie, inclusief profieltypes | 1,5 dag | grootste blok, veel producten |
| F. Fallback | 0,5 dag | |
| R. Klantbackups plannen (11 backups, 4 varianten) | 1,5 dag | grotendeels automatisch |
| **Subtotaal zonder VASIM** | **8 dagen** | |
| Proef: V631 en V633 met measure rollers in VASIM | 0,5 dag | bepaalt of niveau B haalbaar is |
| VASIM: T, M, X-04, F-07, R-03 uitvoeren met ADS-log | 2,5 dagen | |
| VASIM: exploratory E-01, E-02 en cyclustijd | 1 dag | |
| **Subtotaal met VASIM** | **4 dagen** | |
| Rapportage, bevindingen in Jira, testgevallen in PractiTest (Machine QMS 820) | 1,5 dag | |
| **Totaal** | **ongeveer 13,5 dagen** | plus hertests na fixes |

Volgorde: eerst I en R (snel beeld of de standaardinstelling de klantproblemen oplost), dan S, M, F, T en X zonder VASIM, daarna VASIM.

## 10. Bevindingen

| # | Bevinding | Machine | Story | Jira | Ernst | Status |
|---|---|---|---|---|---|---|
| 1 | De installer van de PR (23-11, `ed3c48d4`) loopt achter op de PR (`e7a8685d`, planner `-x.7`) | - | - | - | blokkerend voor testen | opgelost 25-11: nieuwe installer (run 45571260263) in `C:\Temp\BT1-2432\e7a8685d\`, planner `-x.7` gecontroleerd |
| 3 | SWMS-11375 met Min (via fallback): na de infeed pass gaat het materiaal ~1300 mm terug voor 3 freesbewerkingen (DU2) en volgen 8 take overs om en om zonder bewerking ertussen (1880 → 944) voordat het stuk wordt losgelaten. Werkt, maar is dit de bedoeling? | V631 | BT1-2441 | - | vraag | open |
| 4 | SWMS-11375: de freesbewerkingen van product 9 en 10 vallen af en de laatste 10 producten (300 mm) worden handmatig gezaagd. Nagaan of dit zonder de PR (zonder EF) ook zo was en of de operator het ziet | V631 | BT1-2440 | - | vraag | open |
| 5 | Foutmelding bij een onmogelijke take over is veranderd ("The measure roll units can't take over the material where the plan needs it."); support kent de oude tekst | alle | BT1-2443 | - | laag | open |
| 6 | Helptekst "Operation sorting" past niet in het beschrijvingsvak van het eigenschappenvenster | alle | BT1-2442 | - | laag | open |
| 7 | Bewerkingen die de fallback verwijdert zijn voor de operator onzichtbaar: geen melding, geen markering in de lijst of database; de log noemt alleen het aantal, niet welke. Voorbeeld SWMS-11058: DU2-freesbewerking van het vierde stuk valt weg. Het stuk komt zonder die bewerking van de machine. | V633 (alle) | BT1-2440/2443 | - | hoog (product mist een bewerking zonder dat iemand het ziet) | open, nog bespreken met Wiebren |
| 2 | 4.11-instelling wijkt af van BT1-2442 (naam, waarden, standaard Default with fallback, Operator-niveau, fallback alleen bij take over not possible) | alle | BT1-2442/2443 | - | - | gesloten 25-11: bewuste keuze (Wiebren). Default gaat nu vaker fout; Default + fallback hoort in theorie altijd een lijst te geven en is daarom de standaard |

## 11. Afronding

- [ ] Alle testgevallen hebben een resultaat of een geaccepteerde opmerking.
- [ ] V631 en V633 hebben elk een volledig in VASIM afgewerkte Min-job.
- [ ] Geen open bevindingen over botsing of stil annuleren.
- [ ] Cyclustijd en planningstijd vastgelegd.

**Advies:** Go / Go met opmerkingen / No go
**Opmerkingen:**
**Datum:**
