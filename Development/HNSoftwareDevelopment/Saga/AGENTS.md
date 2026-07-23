# Saga — projectinstructies

## Aard en afbakening

Deze werkmap is bestemd voor een lokale e-bookbibliotheek en is geen broncodeproject. Werk bij inventarisatie, herstel of diagnose standaard alleen-lezen, tenzij de gebruiker expliciet om een wijziging vraagt.

Wijzig bibliotheekdata, de SQLite-database of instellingen van de beheerapplicatie niet ongevraagd. Voer geen destructieve Git- of bestandscommando's uit.

## Bibliotheekintegriteit

- Behandel `ELibrary\library.db` en `ELibrary\books` als één gekoppelde set.
- Hernoem technische boekmap-id's niet en wijzig geen individuele boekbestanden of databasegegevens buiten de oorspronkelijke beheerapplicatie.
- Maak een kopie alleen wanneer de beheerapplicatie volledig is afgesloten, of gebruik een consistente back-up/snapshot.
- Gebruik geen gedeeltelijk gesynchroniseerde of online-only bibliotheek voor een eerste controle.

## Werkwijze

- Gebruik voor bestands- en tekstzoekacties bij voorkeur `rg` en `rg --files`.
- Wees terughoudend met grote recursieve scans: de bibliotheek kan tienduizenden mappen en meerdere GB aan data bevatten.
- De oorspronkelijke beheerapplicatie, versie, licentie en profielinstellingen zijn niet uit deze werkmap afleidbaar. Vraag om bevestiging voordat die worden gewijzigd of geconfigureerd.

## Markdown-spiegeling

Wanneer een Markdown-bestand in dit project wordt gemaakt of gewijzigd, spiegel dan dezelfde relatieve structuur naar:

`C:\Data\Obsidian\markdown\Development\HNSoftwareDevelopment\Saga`

Meld expliciet wanneer die spiegeling niet kan worden uitgevoerd.
