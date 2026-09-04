# Milestone 29 Handmatige Testchecklist

Gebruik bij voorkeur een testbibliotheek of een bibliotheek met een actuele back-up. Deze workflow wijzigt de auteur in SQLite, de draagbare `metadata.json`-sidecar en ondersteunde ebookmetadata via Saga's bestaande opslagroute.

De kernworkflow met auteursuggesties, vrije invoer, annuleren, directe dashboardupdate en bijgewerkte hoofdbibliotheek is op 1 september 2026 door de gebruiker goedgekeurd. De knoptekst is op verzoek verduidelijkt naar `Auteur wijzigen`.

## Beschikbaarheid en venster

- [x] Open de Quality Page en selecteer `Ontbrekende auteur`. ✅ 2026-09-04
- [x] Controleer dat `Auteur wijzigen` alleen beschikbaar is wanneer een boek in deze categorie is geselecteerd. ✅ 2026-09-04
- [x] Selecteer een andere kwaliteitscategorie en controleer dat de actie niet beschikbaar is. ✅ 2026-09-04
- [x] Open het herstelvenster en controleer de boektitel, uitleg, auteursinvoer en knoppen. ✅ 2026-09-04
- [x] Controleer dat de focus in de auteursinvoer staat. ✅ 2026-09-04

## Bekende auteur kiezen

- [x] Typ enkele letters van een auteur die al in de actieve bibliotheek voorkomt. ✅ 2026-09-04
- [x] Controleer dat treffers die met de invoer beginnen vóór andere gedeeltelijke treffers staan. ✅ 2026-09-04
- [x] Controleer dat lege waarden, `Unknown` en dubbele schrijfwijzen niet als suggestie verschijnen. ✅ 2026-09-04
- [x] Kies een suggestie met de muis en controleer dat de bekende schrijfwijze wordt overgenomen. ✅ 2026-09-04
- [x] Herhaal dit met pijltoetsen en `Enter`. ✅ 2026-09-04
- [x] Sla op en controleer dat uitsluitend de auteur van het geselecteerde boek wijzigt. ✅ 2026-09-04

## Nieuwe auteur invoeren

- [x] Open een ander testboek zonder auteur. ✅ 2026-09-04
- [x] Voer een auteursnaam in die nog niet in de bibliotheek voorkomt. ✅ 2026-09-04
- [x] Controleer dat de getrimde nieuwe naam kan worden opgeslagen. ✅ 2026-09-04
- [x] Open de herstelactie voor een volgend boek en controleer dat de nieuwe auteur nu als suggestie beschikbaar is. ✅ 2026-09-04
- [x] Controleer dat lege invoer, alleen spaties en `Unknown` niet kunnen worden opgeslagen. ✅ 2026-09-04

## Annuleren en toetsenbord

- [x] Wijzig de invoer en kies `Annuleren`; controleer dat het boek ongewijzigd blijft. ✅ 2026-09-04
- [x] Herhaal dit met `Escape`. ✅ 2026-09-04
- [x] Bedien invoer, suggesties, opslaan en annuleren volledig met het toetsenbord. ✅ 2026-09-04
- [x] Controleer dat focus na sluiten logisch terugkeert naar de Quality Page. ✅ 2026-09-04

## Directe herevaluatie

- [x] Controleer dat de herstelde rij direct uit `Ontbrekende auteur` verdwijnt. ✅ 2026-09-04
- [x] Controleer dat categorie- en totaalaantallen direct veranderen. ✅ 2026-09-04
- [x] Controleer dat de logisch volgende rij wordt geselecteerd, of niets wanneer de categorie leeg is. ✅ 2026-09-04
- [x] Controleer dat andere geldige kwaliteitsmeldingen voor hetzelfde boek zichtbaar blijven. ✅ 2026-09-04
- [x] Controleer dat een eerder via `Dit is correct` genegeerde melding niet opnieuw verschijnt. ✅ 2026-09-04
- [x] Controleer dat de nieuwe auteur direct in de hoofdbibliotheek en het auteursfilter staat. ✅ 2026-09-04

## Bibliotheekgrenzen en fouten

- [x] Wissel van bibliotheek en controleer dat alleen auteurs uit de actieve bibliotheek als suggestie verschijnen. ✅ 2026-09-04
- [x] Controleer dat een boek dat inmiddels een geldige auteur heeft niet via deze herstelroute wordt overschreven. ✅ 2026-09-04
- [x] Simuleer indien praktisch een opslagfout en controleer dat Saga een duidelijke melding toont en de actuele opgeslagen toestand blijft weergeven. ✅ 2026-09-04
- [x] Simuleer indien praktisch dat de auteur wel wordt opgeslagen maar een bijbehorend metadata- of ebookbestand niet kan worden bijgewerkt; controleer dat de kwaliteitsrij verdwijnt en Saga een duidelijke waarschuwing toont. ✅ 2026-09-04

## Lokalisatie

- [x] Controleer de Nederlandse teksten, inclusief `Auteur wijzigen`, op begrijpelijkheid. ✅ 2026-09-04
- [x] Wissel steekproefsgewijs naar een andere ondersteunde taal en controleer dat geen interne sleutel zichtbaar is. ✅ 2026-09-04

## Eindresultaat

- [x] Alle relevante controles zijn geslaagd zonder regressie in `Dit is correct`, openen, dubbelklik, splitter, filters of bibliotheekwissel. ✅ 2026-09-04
