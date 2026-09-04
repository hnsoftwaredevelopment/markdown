# Milestone 32 Handmatige Testchecklist

Gebruik uitsluitend de actuele Debug-build uit `Builds\Debug\Saga.exe`.

## Hoofdroute

- [x] Open een bibliotheek met een boek dat onder `Mogelijk titel/auteur omgewisseld` verschijnt: de titel lijkt op een persoonsnaam, het boek heeft precies één bruikbare auteur en die auteur lijkt niet op een persoonsnaam. ✅ 2026-09-04
- [x] Open de Quality Page, kies deze melding en selecteer het boek. ✅ 2026-09-04
- [ ] Controleer dat alleen de herstelknop `Titel en auteur omwisselen` zichtbaar is en actief wordt.
- [x] Open de actie en controleer dat `Huidig` de bestaande titel en auteur toont. ✅ 2026-09-04
- [x] Controleer dat `Na omwisselen` de huidige auteur als nieuwe titel en de huidige titel als nieuwe auteur toont. ✅ 2026-09-04
- [x] Kies `Omwisselen` en controleer dat de melding voor dit boek direct verdwijnt. ✅ 2026-09-04
- [x] Controleer in het hoofdscherm dat titel en auteur zijn omgewisseld en dat het auteursfilter direct de nieuwe auteur toont. ✅ 2026-09-04

## Annuleren en gegevensveiligheid

- [x] Herhaal de route voor een ander boek en kies `Annuleren`; controleer dat niets is gewijzigd. ✅ 2026-09-04
- [x] Open het venster opnieuw en annuleer met `Escape`; controleer opnieuw dat niets is gewijzigd. ✅ 2026-09-04
- [x] Controleer na een geslaagde omwisseling dat beschrijving, taal, uitgever, publicatiedatum, tags, serie, serienummer, ISBN, omslag, leesstatus en beschikbare formaten gelijk zijn gebleven. ✅ 2026-09-04
- [x] Open `metadata.json` naast het herstelde boekbestand en controleer dat alleen titel en auteur zijn aangepast. ✅ 2026-09-04
- [x] Controleer dat het ebookbestand zelf niet wordt gewijzigd; native ebook-write-back is nog niet ondersteund. ✅ 2026-09-04

## Niet-herstelbare en verouderde meldingen

- [x] Selecteer binnen deze categorie, indien aanwezig, een boek met een lege of `Unknown` auteur en controleer dat de omwisselknop uitgeschakeld blijft. ✅ 2026-09-04
- [x] Corrigeer titel of auteur buiten de nog open Quality Page en probeer daarna de oude melding te herstellen; controleer, indien praktisch na te bootsen, dat Saga de actuele geldige gegevens niet overschrijft. ✅ 2026-09-04
- [x] Controleer dat `Dit is correct` beschikbaar blijft wanneer de voorgestelde omwisseling niet gewenst is. ✅ 2026-09-04

## Toetsenbord, venstergrootte en regressie

- [x] Doorloop de volledige route met `Tab`, `Enter` en `Escape` zonder de muis te gebruiken. ✅ 2026-09-04
- [x] Maak het bevestigingsvenster smaller en groter en controleer dat huidige en nieuwe waarden en beide knoppen leesbaar en bereikbaar blijven. ✅ 2026-09-04
- [x] Controleer dat lange titel- en auteursnamen worden afgebroken en volledig leesbaar blijven via de verticale scrollbar. ✅ 2026-09-04
- [x] Controleer, indien een gecontroleerde fouttest beschikbaar is, dat een opslag- of sidecarfout een begrijpelijke melding geeft en de actuele boekgegevens zichtbaar laat. ✅ 2026-09-04
- [x] Controleer dat `Auteur wijzigen`, `Taal wijzigen`, `Serie wijzigen`, `Dit is correct` en `Openen in bibliotheek` nog steeds werken in hun eigen context. ✅ 2026-09-04
- [x] Sluit Saga, open dezelfde bibliotheek opnieuw en controleer dat de omgewisselde titel en auteur behouden zijn. ✅ 2026-09-04
