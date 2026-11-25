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
| I-01 | "Operation sorting" op V630MK2, V631, V633 met measure rollers | aanwezig, 3 waarden, standaard **Default with fallback**, gebruikersniveau Operator, categorie Automatic, helptekst klopt | open |
| I-02 | "Operation bundling distance" | V630MK2/V631 ja, V633 nee; standaard 10, min 0, eenheid mm | open |
| I-03 | Machine zonder measure rollers (feeder truck V631/V633, V630 oud, VB) | beide instellingen niet zichtbaar | open |
| I-04 | Upgrade van een 4.11-backup (vóór de PR) | instellingen krijgen de standaardwaarde, geen fout bij starten | open |
| I-05 | Instelling wijzigen en lijst opnieuw genereren | nieuwe sortering wordt gebruikt (zonder herstart, of melding dat herstart nodig is) | open |
| I-06 | Preferred measure roll unit samen met elke sortering | wordt gebruikt bij Default en DwF, niet bij Min | open |

### S. Sortering V630Mk2/V631 (A, bevestigen in B)

| # | Test | Producten | Verwacht | Resultaat |
|---|---|---|---|---|
| S-01 | Standalone, één stuk | P01, P05 | Min: alle stappen stijgend; Default: per gereedschap; minder reversals en meer automatische wissels met Min | open |
| S-02 | B2B, nesting | P02 | controleregels 1 t/m 5 (Testwerkwijze §4) | open |
| S-03 | Flange removal op twee flenzen | P03 | Min: één doorgang; Default: geen extra slag terug meer voor flange removals | open |
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
| M-01 | Blokkerend gat in het meetgebied, take over onmogelijk | P10 | undoable + zichtbaar voor de operator; rest gemaakt; geen exception | open |
| M-02 | Blokkerend gat, take over mogelijk | P11 | gemaakt | open |
| M-03 | Gat in de band buiten het meetgebied | P12 | gemaakt, wheel loopt er niet over terwijl hij meet (B) | open |
| M-04 | Gat buiten de band / in de voorste flens | P13, P14 | blokkeert niet | open |
| M-05 | Kopplaat-patroon + blokkerend gat | P15 | patroon gemaakt, alleen blokkerende feature eventueel undoable | open |
| M-06 | Flange removal en gat gemengd | P16 | zelfde regels | open |
| M-07 | BT1-2469 reproduceren | P17 | bekende bug: vastleggen met elke sortering | open |
| M-08 | Lange sleuf | P18 | geen exception; sleuf gemaakt of verklaarbaar undoable | open |
| M-09 | Band per profieltype | P20 t/m P26 | gat in de band blokkeert, net erbuiten niet; RHS volgt de measure wheel position; special/bundel: niets blokkeert | open |
| M-10 | Undoable-markering in de UI | P10 | operator ziet welke bewerkingen niet gemaakt worden en waarom; ongedaan maken werkt | open |

### F. Fallback (A, één geval ook in B)

| # | Test | Verwacht | Resultaat |
|---|---|---|---|
| F-01 | DwF, Default slaagt | lijst gelijk aan Default, niets in de log over fallback | open |
| F-02 | DwF, Default faalt (take over), Min slaagt | job loopt; waarschuwing + info in de log; alleen undoable wat de tweede validatie annuleert | open |
| F-03 | DwF, beide falen (P17) | de fout van de eerste poging; undoable zoals na de eerste poging | open |
| F-04 | DwF, Default faalt met een andere exception | geen tweede poging (alleen bij take over not possible) | open |
| F-05 | Default (zonder fallback), job die faalt | één poging, zelfde fout als voorheen | open |
| F-06 | Planning annuleren tijdens het plannen | geen tweede poging | open |
| F-07 | Een met DwF geredde job in VASIM draaien | loopt af, bewerkingen zoals gepland | open |

### R. Regressie en klantbatches (A, steekproef B)

| # | Test | Verwacht | Resultaat |
|---|---|---|---|
| R-01 | Per QMS-backup (11 stuks): plannen met 4.11 zonder PR en met de PR (Default, DwF, Min) | DwF lost de cancellation-tickets op of het resultaat is verklaard; Min vermindert reversals bij de sequencing-tickets | open |
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
| 2 | 4.11-instelling wijkt af van BT1-2442 (naam, waarden, standaard Default with fallback, Operator-niveau, fallback alleen bij take over not possible) | alle | BT1-2442/2443 | - | vraag aan Wiebren | open |

## 11. Afronding

- [ ] Alle testgevallen hebben een resultaat of een geaccepteerde opmerking.
- [ ] V631 en V633 hebben elk een volledig in VASIM afgewerkte Min-job.
- [ ] Geen open bevindingen over botsing of stil annuleren.
- [ ] Cyclustijd en planningstijd vastgelegd.

**Advies:** Go / Go met opmerkingen / No go
**Opmerkingen:**
**Datum:**
