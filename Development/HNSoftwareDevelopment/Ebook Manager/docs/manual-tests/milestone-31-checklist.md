# Milestone 31 Handmatige Testchecklist

Gebruik uitsluitend de actuele Debug-build uit `Builds\Debug\Saga.exe`.

## Hoofdroute

- [x] Open een bibliotheek met minstens één boek dat wel een serienummer maar geen serienaam heeft. ✅ 2026-09-04
- [x] Open de Quality Page en selecteer `Serienummer zonder serie`. ✅ 2026-09-04
- [x] Controleer dat alleen de herstelknop `Serie wijzigen` zichtbaar is en dat deze actief wordt zodra een boek is geselecteerd. ✅ 2026-09-04
- [x] Open `Serie wijzigen` en controleer dat de juiste boektitel en het bestaande serienummer zichtbaar zijn. ✅ 2026-09-04
- [x] Typ een deel van een bestaande serienaam en controleer dat passende series uit de actieve bibliotheek als suggestie verschijnen. ✅ 2026-09-04
- [x] Kies een suggestie met het toetsenbord, sla op en controleer dat de melding voor dit boek direct verdwijnt. ✅ 2026-09-04
- [x] Controleer in het hoofdscherm dat de serienaam is gewijzigd en dat het serienummer gelijk is gebleven. ✅ 2026-09-04
- [x] Controleer dat het seriefilter direct de nieuwe waarde en telling toont. ✅ 2026-09-04

## Nieuwe serienaam en validatie

- [x] Herhaal de route voor een ander boek en voer een volledig nieuwe serienaam in. ✅ 2026-09-04
- [x] Controleer dat de nieuwe naam na opslaan in de bibliotheek en het seriefilter verschijnt. ✅ 2026-09-04
- [x] Controleer dat alleen spaties invoeren de knop `Opslaan` uitgeschakeld laat. ✅ 2026-09-04

## Annuleren en gegevensveiligheid

- [x] Wijzig de invoer en annuleer met `Annuleren`; controleer dat niets is opgeslagen. ✅ 2026-09-04
- [x] Open het venster opnieuw en annuleer met `Escape`; controleer opnieuw dat niets is opgeslagen. ✅ 2026-09-04
- [x] Controleer bij het herstelde boek dat titel, auteur, taal, tags, omslag en leesstatus niet zijn gewijzigd. ✅ 2026-09-04
- [x] Verander de serienaam van het boek buiten de open Quality Page, probeer daarna de oude melding te herstellen en controleer dat Saga de geldige actuele serienaam niet overschrijft. ✅ 2026-09-04

## Toetsenbord en venstergrootte

- [x] Doorloop de volledige route met `Tab`, pijltjestoetsen, `Enter` en `Escape` zonder de muis te gebruiken. ✅ 2026-09-04
- [x] Controleer dat de invoer direct focus krijgt en dat `Enter` de geselecteerde suggestie overneemt. ✅ 2026-09-04
- [x] Maak het herstelvenster smaller en groter en controleer dat titel, serienummer, uitleg en knoppen leesbaar en bereikbaar blijven. ✅ 2026-09-04
- [x] Maak de Quality Page smaller en controleer dat de onderste acties bruikbaar blijven bij langere teksten. ✅ 2026-09-04

## Foutafhandeling en regressie

- [x] Open na een geslaagd herstel de `metadata.json` naast het boekbestand en controleer dat de serienaam is gewijzigd en het serienummer gelijk is gebleven. ✅ 2026-09-04
- [x] Controleer dat het ebookbestand zelf niet wordt gewijzigd. Native metadata-write-back is in deze milestone nog voor geen enkel ebookformaat ondersteund; de draagbare metadata wordt opgeslagen in `metadata.json`. ✅ 2026-09-04
- [x] Controleer in een gecontroleerde fouttest dat een mislukte sidecar- of ebook-write-back een duidelijke waarschuwing geeft en de actuele boekgegevens zichtbaar laat. Als deze fout handmatig niet veilig en betrouwbaar is na te bootsen, leg dat vast; de route wordt ook afgedekt door `RepairAsync_reports_saved_with_writeback_errors_when_database_update_succeeded`. ✅ 2026-09-04
- [x] Controleer dat `Auteur wijzigen`, `Taal wijzigen`, `Dit is correct` en `Openen in bibliotheek` nog steeds werken in hun eigen context. ✅ 2026-09-04
- [x] Sluit Saga, open dezelfde bibliotheek opnieuw en controleer dat de opgeslagen serienaam en het serienummer behouden zijn. ✅ 2026-09-04
