# Codex-projectoverdracht — Ebook Manager

## Doel en afbakening

Deze werkmap bevat een lokale e-bookbibliotheek. De overdracht is bedoeld om dezelfde bibliotheek en de voor dit project geldende Codex-werkwijze op een andere laptop beschikbaar te maken.

Dit is **geen broncodeproject**: in de hoofdmap is geen Git-repository, applicatiebroncode, buildconfiguratie of zichtbaar Codex-projectbestand aangetroffen. De inventaris beschrijft daarom de aanwezige bibliotheekdata en de reproduceerbare werkwijze eromheen, niet de installatie van de onbekende beheerapplicatie.

Onderzoek uitgevoerd: alleen lezen van de zichtbare projectstructuur, bestandsmetadata, enkele representatieve bibliotheekmetadata en de SQLite-bestandsheader. Bestaande bestanden, instellingen en taken zijn niet gewijzigd.

## Benodigde bestanden, mappen en repositories

Kopieer de volledige huidige hoofdmap inclusief verborgen bestanden naar de nieuwe laptop. De feitelijk benodigde bibliotheekdata is:

| Pad | Functie | Vastgestelde staat |
| --- | --- | --- |
| `ELibrary\\library.db` | Primaire SQLite-database met de bibliotheekcatalogus en vermoedelijk aanvullende applicatiestatus. | 5.981.048.832 bytes; gewijzigd 10 juli 2026 17:04 (CEST); header `SQLite format 3`. |
| `ELibrary\\books\\` | Boekopslag. Elke boekmap heeft een 32-tekens hexadecimale id als naam. | 33.745 directe boekmappen vastgesteld. |
| `ELibrary\\books\\<id>\\<boekbestand>` | Het e-bookbestand. | 33.703 EPUB, 37 PDF, 4 CBR en 1 CBZ vastgesteld. |
| `ELibrary\\books\\<id>\\cover.jpg` | Omslagafbeelding per boek waar aanwezig. | 31.921 JPG-bestanden vastgesteld. |
| `ELibrary\\books\\<id>\\metadata.json` | Losse aanvullende metadata, slechts bij sommige boeken. | 4 JSON-bestanden vastgesteld; schema bevat onder meer titel, auteurs, beschrijving, taal, uitgever, datum, tags, serie en ISBN. |

Er is geen repository-URL of Git-metadata in de zichtbare hoofdmap aangetroffen. Er is dus geen repository te klonen voor een gelijkwaardige herstelactie; kopieer in plaats daarvan de volledige data-map.

### Belangrijke integriteitsregel

Behandel `library.db` en `books` als één gekoppelde set. De boekmapnamen zijn technische id's; hernoem ze niet en wijzig geen individuele bestanden of databasegegevens buiten de originele beheerapplicatie. Maak een kopie wanneer de beheerapplicatie volledig is afgesloten, of gebruik een consistente back-up/snapshot. Een losse kopie tijdens actieve databasewijzigingen kan inconsistent zijn.

## Instructies die Codex altijd moet volgen

- Werk bij inventarisatie, herstel of diagnose standaard alleen-lezen, tenzij expliciet om een wijziging wordt gevraagd.
- Wijzig de bestaande bibliotheek-, database- of app-instellingen niet ongevraagd.
- Gebruik voor snelle bestands- en tekstzoekacties bij voorkeur `rg`/`rg --files`.
- Wees terughoudend met grote, recursieve scans: de bibliotheek bevat tienduizenden mappen en meerdere GB aan data.
- Voer geen destructieve Git- of bestandscommando's uit; er is geen zichtbaar Git-project in deze map.
- Bij het maken of wijzigen van een Markdown-bestand in dit HN Software Development-project moet dezelfde relatieve Markdown-bestandsstructuur worden gespiegeld naar `C:\Data\Obsidian\markdown\Development\HNSoftwareDevelopment\Ebook Manager`. Meld het expliciet als die spiegeling niet lukt.

## Skills, hulpmiddelen, plug-ins en koppelingen

### Projectgebonden

Geen projectgebonden Codex-skills, `.codex`-instellingen, MCP-configuratie, plug-inmanifesten of `AGENTS.md`-bestanden zijn in de zichtbare projectmap aangetroffen.

### Algemeen beschikbaar in de huidige Codex-omgeving

De onderstaande mogelijkheden zijn omgevingsbreed beschikbaar, niet opgeslagen in dit project en dus niet automatisch overdraagbaar met de map:

- Codex Desktop met PowerShell als shell.
- Algemene instructie voor de Markdown-spiegeling naar Obsidian (zoals hierboven vastgelegd).
- De globale Codex-skillcatalogus; voor dit databestand waren geen gespecialiseerde projectskills nodig.

Voor een gelijkwaardige nieuwe omgeving zijn de relevante basisvereisten: Codex Desktop, toegang tot de lokale werkmap en PowerShell. Voor directe databaseinspectie is daarnaast een SQLite-client of runtime met read-only SQLite-ondersteuning praktisch; die was in deze omgeving niet aantoonbaar beschikbaar als `sqlite3`-CLI of Python.

### Vereiste externe koppelingen, accounts of instellingen

Voor de zichtbare bibliotheekdata zijn geen externe accounts, cloud-API's, plug-ins of koppelingen aangetroffen. De map staat nu onder OneDrive (`C:\Users\hnijk\OneDrive\Data\Ebook Manager`); het is aannemelijk dat OneDrive voor synchronisatie/back-up wordt gebruikt, maar dat is geen bewijs van een vereiste voor de beheerapplicatie zelf.

Als de bibliotheek via een aparte e-bookbeheerapp wordt gebruikt, moeten op de nieuwe laptop **dezelfde applicatie, versie, profiel-/gegevensmapinstelling en eventuele licentie of account** worden achterhaald en opnieuw ingesteld. De naam, versie en instellingen daarvan zijn niet afleidbaar uit de zichtbare projectmap.

## Context uit eerdere taken

Er is in de huidige toegankelijke taakcontext geen eerdere taakgeschiedenis, besluitlog of terugkerende projectworkflow beschikbaar. De volgende conventies zijn wel uit de data afgeleid:

- Boekopslag is id-gebaseerd en niet op auteur/titel; behoud de technische mapnamen.
- EPUB is veruit het dominante formaat; omslagen worden als `cover.jpg` naast het boek opgeslagen.
- Losse `metadata.json` gebruikt `SchemaVersion: 1` en bevat leesbare catalogusvelden. Deze bestanden zijn aanvullend en mogen niet als vervanging van `library.db` worden gezien.
- De catalogusdatabase is groot (ca. 5,98 GB); plan voldoende lokale schijfruimte, overdrachtstijd en back-upruimte.

## Nieuwe laptop: concrete inrichting

1. Installeer Codex Desktop en meld aan met het gewenste Codex-account.
2. Installeer of herstel OneDrive als dit de gekozen synchronisatie/back-upmethode blijft. Wacht tot de complete map lokaal beschikbaar is; gebruik geen gedeeltelijk online-only bibliotheek tijdens de eerste controle.
3. Sluit op de oude laptop de e-bookbeheerapp af en kopieer vervolgens de volledige map `Ebook Manager`, inclusief `ELibrary`, naar de nieuwe laptop. Bewaar exact dezelfde relatieve structuur.
4. Zorg voor minimaal ruim 6 GB vrije ruimte voor de huidige data, plus ruimte voor groei en een afzonderlijke back-up; reserveer in de praktijk aanzienlijk meer dan de huidige omvang.
5. Open de gekopieerde hoofdmap als nieuw Codex-project.
6. Kopieer of maak het bestand `CODEX-PROJECT-OVERDRACHT.md` mee over. Controleer dat de Obsidian-spiegellocatie bestaat als je Markdown door Codex laat maken of aanpassen.
7. Installeer de oorspronkelijke e-bookbeheerapplicatie opnieuw zodra de naam/versie bekend is. Configureer haar gegevenslocatie uitsluitend volgens haar eigen documentatie en maak vooraf een extra kopie van `ELibrary`.
8. Controleer eerst met alleen-lezen acties dat de applicatie dezelfde bibliotheek toont. Pas pas daarna eventueel de standaardgegevensmap of synchronisatie-instellingen aan.

## Korte controlelijst

- [ ] De nieuwe hoofdmap bevat `ELibrary\\library.db` en `ELibrary\\books`.
- [ ] `library.db` opent als SQLite 3-bestand en heeft ongeveer de verwachte grootte (5,98 GB op het moment van inventarisatie).
- [ ] Het aantal directe mappen in `ELibrary\\books` is circa 33.745.
- [ ] Een steekproef van boekmappen bevat boekbestand(en) en waar verwacht `cover.jpg`; mapnamen zijn ongewijzigd.
- [ ] De e-bookbeheerapp toont de verwachte catalogus zonder een nieuwe, lege bibliotheek aan te maken.
- [ ] Openen van een EPUB, een PDF en een boek met losse `metadata.json` werkt zoals op de oude laptop.
- [ ] OneDrive (indien gebruikt) heeft de volledige map gesynchroniseerd en er zijn geen conflictkopieën of online-only placeholders.
- [ ] Codex kan de projectmap lezen en een test-Markdownbestand, indien gemaakt, naar de Obsidian-spiegellocatie kopiëren.

## Niet uitleesbare of niet-aangetroffen informatie

- Verborgen Codex Desktop-appinstellingen, accountsessies, modelinstellingen, lokale chat-/taakhistorie en projectmetadata buiten de werkmap zijn niet toegankelijk via dit projectonderzoek.
- De exacte e-bookbeheerapplicatie, versie, installatiepad, licentie, profielinstellingen en database-schema konden niet worden vastgesteld uit de zichtbare bestanden.
- De inhoud van de 5,98-GB SQLite-database is niet uitgelezen: er was geen aantoonbare lokale SQLite-client/runtime beschikbaar, en volledige inhoudsanalyse valt buiten een proportionele alleen-lezen inventarisatie.
- Er zijn geen zichtbare `.codex`-bestanden, `AGENTS.md`-bestanden, projectskills, plug-inconfiguraties, bronmappen of documentatiebestanden aangetroffen. Dit sluit niet uit dat zulke configuratie buiten deze werkmap bestaat.
- Windows-, OneDrive- en applicatie-specifieke verborgen instellingen, credentials, API-sleutels, externe koppelingen en niet-toegankelijke metadata zijn niet uit deze map af te leiden en worden niet in dit document opgenomen.
