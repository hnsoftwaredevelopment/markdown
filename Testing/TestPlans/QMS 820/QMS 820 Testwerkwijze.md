---
type: testwerkwijze
jira: BT1-2432
title: "QMS 820 Testwerkwijze"
created: 2026-11-25
tags: [qms820, werkwijze]
---

# QMS 820 Testwerkwijze

Hoe we testen, welke middelen we gebruiken en hoe we bewijs vastleggen. Wat we testen staat in [[QMS 820 Testplan]], de producten in [[QMS 820 Testproducten]].

## 1. Drie niveaus

| Niveau | Wat het laat zien | Middel | Wat het niet laat zien |
|---|---|---|---|
| **A. Planning zonder VASIM** | volgorde van de stappen, welke MRU vasthoudt, take overs, geannuleerde bewerkingen, exceptions, fallback in de log, instellingen | VACAM 4.11 met de PR, cycle tab (Play/Step), geen PLC nodig | of de machine het ook zo uitvoert |
| **B. Uitvoering met VASIM** | of de lijst echt doorloopt: take overs, afzagen, uitvoer naar de outfeed, stop en herstart, cyclustijd bij benadering | VACAM + TwinCAT kernel runtime + VASIM rc, via de VACAM Launcher | echte positiefout (VASIM heeft geen slip of meetfout) |
| **C. Echte machine** | of de afwijking echt kleiner wordt | BT1-2444, testafdeling, meetlint/meetarm | - |

Het grootste deel (de regels van de sortering, validatie, instellingen, regressie) zit in niveau A. Niveau B is nodig voor alles wat met de machine-uitvoering te maken heeft. Niveau C valt buiten deze test (BT1-2444), maar de testproducten zijn er wel geschikt voor.

## 2. Testomgeving

1. **VACAM-versie.** Nieuwe installer van PR #23387 op commit `e7a8685d` (planner `1.148.31-...-x.7`). De installer van 23-11 (`ed3c48d4`, planner `-x.3`) mist de fixes van EP#654. Alternatief voor niveau A: de branch `BT1-2432_Develop-4.11` lokaal bouwen en VACAM zonder TwinCAT starten (`start-vacam-backup.ps1 -Worktree`).
2. **Referentie.** Dezelfde backup ook met de huidige 4.11 (RC-4.11.36 zonder de PR), om "Default is gelijk aan voorheen" te kunnen vergelijken.
3. **Backups.** Per test een verse kopie van de backup (databases opnieuw terugzetten), zodat instellingen en geannuleerde bewerkingen van een vorige run niet meetellen. Klantdata blijft lokaal in `C:\Temp\Customers`.
4. **Machineconfiguratie vastleggen.** Per backup noteer ik: machinetype en subcategorie, standalone of B2B, offsets van de drive wheel en de measure wheel per MRU, clamping margin, measure wheel position (M-profielen), preferred measure roll unit, zaagpositie.

## 3. Niveau A: planning lezen

Per product en per instelling (Default / Default with fallback / Minimize material reversals):

1. Batch importeren of producten (NC1) toevoegen, bufferitem maken, batch kiezen in de cycle tab.
2. Lijst laten genereren (Play, of Step tot de lijst er is).
3. Vastleggen:
   - de cycle list (export of schermafdruk van de commando's met X-positie);
   - welke MRU per commando vasthoudt en waar de take overs staan;
   - welke bewerkingen "set undoable by execution framework" zijn;
   - de VACAM-log: waarschuwing van de eerste poging, info over de fallback, exceptions.
4. Uitrekenen uit de lijst:
   - **aantal reversals:** hoe vaak de materiaalpositie van richting verandert, per MRU-periode;
   - **totale materiaalverplaatsing** (som van |ΔX|);
   - **aantal automatische en handmatige gereedschapswissels**.
5. Vergelijken met de verwachting uit de regels (§4) en met de referentie.

Ik maak hiervoor een script dat de cycle list uit de VACAM-database leest en de drie getallen per lijst berekent. Dan is de vergelijking tussen Default en Minimize meteen objectief.

## 4. Controleregels (het "orakel")

Voor elke lijst met **Minimize material reversals** moet gelden:

1. Divisions die een stuk maken dat detectie nodig heeft, komen eerst.
2. Zolang de outfeed MRU vasthoudt, daalt de materiaalpositie (of blijft gelijk). Zolang de infeed MRU vasthoudt, stijgt hij.
3. Alle stappen van het forwards piece komen na de stappen van de backwards pieces van hetzelfde detected piece.
4. Een backwards piece wordt afgezaagd zodra zijn snede bij de zaag is.
5. Hooguit één take over naar de infeed MRU (aan het begin van de infeed pass), hooguit één late take over naar de outfeed MRU (meetgebied), en een take over voor de outfeed als die mogelijk is.
6. Geen stap waarbij de measure wheel van de vasthoudende MRU in een eerder gemaakte bewerking in de band staat (rekenen met de windows: positie - wheel offset ligt niet in een bewerkt stuk ± 5 mm).
7. Standalone: alle stappen in stijgende materiaalpositie.
8. V633: een x'-as-groep bevat geen stappen van twee passes of twee detected pieces; groepen volgen regel 2.

Voor **Default**: de lijst is gelijk aan die van 4.11 zonder de PR, op deze bekende verschillen na: flange removals aan de measure wheel-kant worden niet meer naar het einde geschoven, en de bundling distance komt uit de nieuwe instelling (standaard 10, dus gelijk).

Voor **Default with fallback**: als Default slaagt, dan precies de Default-lijst en geen fallback in de log. Als Default faalt met "take over not possible", dan een Minimize-lijst, een waarschuwing en een info-regel in de log, en alleen de bewerkingen die de tweede validatie annuleert zijn undoable.

## 5. Niveau B: uitvoeren in VASIM

1. Machine opstarten via de VACAM Launcher (kernel mode TwinCAT, VASIM rc). Zelf de batch, het bufferitem en de balk in VASIM klaarzetten.
2. Over ADS loggen (50 ms): materiaalpositie, actieve MRU, positie van de measure wheels, clamps, zaag. De symbolen zoek ik per machine op (zoals bij BT1-2317).
3. Controleren:
   - de lijst loopt af zonder melding;
   - take overs gebeuren waar de lijst ze heeft;
   - de measure wheel staat nooit boven een gemaakte bewerking in de band (uit de log: positie wheel op het materiaal t.o.v. de gemaakte features);
   - het product gaat zo ver mogelijk naar de outfeed en wordt automatisch afgevoerd als de take over voor de outfeed kon;
   - stop midden in de lijst en herstart: welke lijst komt er dan (regeneratie), en klopt die nog met de regels.
4. Cyclustijd vastleggen voor Default en Minimize (zelfde product).

Eerst een korte proef: één V631 en één V633 met measure rollers in VASIM opstarten en P11 draaien. Werkt VASIM niet met measure rollers, dan valt niveau B terug op wat de lijst en de PLC-commando's laten zien.

## 6. Bewijs en vastleggen

- Per testgeval een map `C:\Temp\Customers\_jira\QMS820\<testgeval>` met de cycle list, de log, de ADS-log en de berekende getallen.
- Resultaten in [[QMS 820 Testplan]] (resultaatkolom), bevindingen in §10 van het testplan en zo nodig als bug in Jira (BT1).
- Testgevallen gaan later naar PractiTest (project 16733), veld Machine = **QMS 820**, één test per testgeval uit het testplan. Script-based voor de regels en de instellingen, exploratory voor de klantbatches en de VASIM-sessies.
