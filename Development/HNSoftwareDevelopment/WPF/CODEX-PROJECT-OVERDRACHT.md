# CODEX-projectoverdracht — WPF

## Doel en afbakening

Dit is een compacte, lokale documentatieprojectmap. Het doel is het genereren en bewaren van het Nederlandstalige Word-handboek **“WPF Handboek - Grid”**: een praktisch overzicht van veelgebruikte properties, layout, interactie, resources, styling, binding en attached properties van `System.Windows.Controls.Grid`.

De map bevat **geen WPF-solution, applicatiebroncode, NuGet-project, buildpipeline of implementatie van een WPF-applicatie**. De naam `WPF` duidt hier op het onderwerp van de documentatie, niet op een te bouwen applicatie.

Peildatum van deze inventaris: 16 juli 2026. De inventaris is opgesteld op basis van leesbare lokale bestanden en de aanwezige Git-metadata.

## Benodigde bestanden, mappen en repositories

Kopieer ten minste deze hoofdmapinhoud naar de nieuwe laptop:

| Pad | Rol | Noodzaak |
| --- | --- | --- |
| `make_wpf_grid_doc.py` | Bron/generator van het handboek. Schrijft `WPF_Handboek_Grid_Overzicht.docx` naar de huidige werkmap. | Essentieel voor wijzigingen en reproductie. |
| `WPF_Handboek_Grid_Overzicht.docx` | Huidige gegenereerde oplevering. | Essentieel als referentie en direct bruikbaar resultaat. |
| `rendered_grid_doc_direct/WPF_Handboek_Grid_Overzicht.pdf` | Eerdere PDF-rendercontrole van het handboek. | Referentie; opnieuw te genereren. |
| `rendered_grid_doc_direct/page-1.png` t/m `page-4.png` | Visuele controle-uitvoer van de vier pagina’s. | Referentie; opnieuw te genereren. |
| `.codex_tmp/pymupdf/` | Lokale, tijdelijke PyMuPDF-installatie gebruikt bij eerdere PDF-/beeldcontrole; de metadata vermeldt versie 1.27.2.3. | Niet essentieel; op de nieuwe machine liever opnieuw als tijdelijke dependency aanmaken. |
| `docx_render_dependency_property/`, `docx_render_dependency_property_check/`, `rendered_grid_doc/` | Lege, achtergebleven werkmappen voor render-/dependencyonderzoek. | Niet nodig voor functioneren; alleen behouden als historische context gewenst is. |

Er is geen bruikbare repositorybron om te clonen: `.git` bestaat wel, maar bevat geen `HEAD`, geen commits, geen getrackte bestanden en geen remote. Bewaar de map daarom zelf (bijvoorbeeld in OneDrive) of initialiseer pas na de overdracht bewust een nieuwe Git-repository.

## Instructies die Codex altijd moet volgen

Er is in deze projectmap geen fysiek `AGENTS.md` aangetroffen. Wel is de volgende bovenliggende projectinstructie van toepassing en moet die in de nieuwe Codex-omgeving opnieuw beschikbaar zijn:

> Wanneer binnen een HN Software Development-project een Markdown-bestand wordt aangemaakt of gewijzigd, kopieer dan de bijgewerkte versie ook naar `C:\Data\Obsidian\markdown\Development\HNSoftwareDevelopment\<Projectnaam>`. Gebruik de repositorymapnaam als projectnaam, tenzij anders opgegeven, en behoud waar praktisch de relatieve mapstructuur. Meld expliciet als die kopie niet lukt.

Voor deze map is `<Projectnaam>` `WPF`. Dit overdrachtsbestand moet daarom na elke wijziging ook bestaan op:

`C:\Data\Obsidian\markdown\Development\HNSoftwareDevelopment\WPF\CODEX-PROJECT-OVERDRACHT.md`

Werkconventies die uit de aanwezige artefacten blijken:

- Behoud Nederlands als documenttaal en houd de inhoud praktisch en voorbeeldgericht.
- Wijzig de generator als bron van waarheid; genereer daarna de DOCX opnieuw in plaats van alleen de DOCX handmatig te wijzigen.
- Gebruik A4, 2 cm marges, Arial voor gewone tekst en koppen, Consolas voor XAML-codevoorbeelden en een blauw palet voor koppen en tabelkoppen.
- Houd tabellen expliciet van breedte, met herhaalde koprijen, celmarges en gecentreerde verticale uitlijning, zoals in de generator geïmplementeerd.
- Controleer een gewijzigde DOCX visueel door deze te renderen en alle pagina-afbeeldingen te bekijken voordat je de DOCX oplevert.

## Beschikbare skills en herkomst

Er zijn geen projectgebonden Codex-skills, lokale skillmappen, plug-inmanifests of `.codex`-instellingen in deze hoofdmap gevonden.

| Skill/hulpmiddel | Herkomst | Toepassing in dit project |
| --- | --- | --- |
| `documents` | Algemeen, door de Codex-runtime aangeboden | Gebruik voor wijzigingen aan de DOCX: render de DOCX naar PNG’s en inspecteer de pagina’s visueel. |
| Python + `python-docx` | Lokale runtime/dependency; niet in de projectmap vastgelegd | Vereist om `make_wpf_grid_doc.py` uit te voeren. |
| PyMuPDF 1.27.2.3 | Eerder lokaal in `.codex_tmp/pymupdf/` neergezet | Eerdere render-/PDFcontrole; geen vastgepinde projectdependency. |
| Pandoc 3.9.0.2 | Lokaal aangetroffen hulpmiddel | Niet door de generator gebruikt; geen vereiste. |

De huidige machine heeft geen werkende Python-installatie op de standaardopdracht `python`; die verwijst naar de Microsoft Store-alias. Dit is een lokale omgevingsconstatering, geen projectconfiguratie.

## Externe koppelingen, accounts en instellingen

Voor de feitelijke generator zijn geen externe API’s, cloudkoppelingen, accounts, geheimen, omgevingsvariabelen of plug-ins aangetroffen.

Nodig op een nieuwe laptop:

- Codex Desktop met de algemene documentworkflow beschikbaar.
- Een werkende Python 3-installatie met het pakket `python-docx`.
- Een DOCX-renderaar voor kwaliteitscontrole, bij voorkeur LibreOffice/`soffice`, zoals de documentworkflow gebruikt.
- Optioneel Microsoft Word voor handmatige beoordeling van het einddocument.
- Toegang tot de OneDrive-locatie als de map daar wordt bewaard.
- Voor de verplichte Markdown-spiegeling: toegang tot `C:\Data\Obsidian\markdown\Development\HNSoftwareDevelopment\WPF` of een expliciet gekozen equivalent op de nieuwe laptop.

## Belangrijke context uit eerdere werkzaamheden

De artefacten dateren van 27 mei 2026. De generator maakt een handboek met tien secties: onderwerpindeling, Grid-specifieke properties, basisvoorbeeld, algemene Grid-properties, layout, interactie, resources/styling/binding, minder vaak gebruikte properties, attached properties en een voorgestelde hoofdstukstructuur plus bronverwijzingen.

Het document is eerder succesvol naar een PDF en vier pagina-PNG’s gerenderd in `rendered_grid_doc_direct/`. De drie andere rendermappen zijn leeg. De tijdelijke PyMuPDF-map heeft circa 53 MB en lijkt een eerder geïnstalleerde hulpmiddeldependency; zij hoeft niet als broncode te worden onderhouden.

Er is geen toegankelijke historische Codex-taakgeschiedenis in de projectmap. De precieze oorspronkelijke prompt, gebruikersbeslissingen buiten de bestanden, Codex-appthreadmetadata en de exacte gebruikte renderopdracht zijn daarom niet te reconstrueren.

## Nieuwe laptop: concrete inrichting

1. Installeer Codex Desktop en zorg dat de algemene skill `documents` beschikbaar is.
2. Installeer een actuele Python 3-runtime en `python-docx` in een beheerde virtuele omgeving, bijvoorbeeld: `python -m venv .venv`, activeer die omgeving en voer `python -m pip install python-docx` uit.
3. Installeer LibreOffice als DOCX-rendering en verifieer dat `soffice` vanaf de opdrachtregel bereikbaar is. Installeer PyMuPDF alleen wanneer je die zelf voor een aanvullende PDF-/afbeeldingscontrole wilt gebruiken.
4. Kopieer de hoofdmapinhoud, inclusief `make_wpf_grid_doc.py` en de huidige DOCX. Gebruik geen bestaande `.git`-map als bron van versiegeschiedenis: die heeft geen bruikbare commitgeschiedenis. Initialiseer desgewenst een nieuwe repository en commit de bron én het document bewust.
5. Maak of heractiveer de bovenstaande HN Software Development-instructie voor Markdown-spiegeling. Maak de Obsidian-doelmap `C:\Data\Obsidian\markdown\Development\HNSoftwareDevelopment\WPF` beschikbaar.
6. Open de map als nieuw Codex-project. Leg desgewenst een project-`AGENTS.md` vast met de permanente spiegelinstructie, zodat deze niet uitsluitend van de app-/organisatiecontext afhankelijk is.
7. Voer vanuit de hoofdmap `python make_wpf_grid_doc.py` uit. Dit hoort `WPF_Handboek_Grid_Overzicht.docx` te vernieuwen.
8. Render de DOCX via de documentworkflow naar PDF/PNG en inspecteer alle pagina’s. Bewaar renderuitvoer alleen als controle-artefact; de DOCX en het script zijn de primaire projectbestanden.

## Korte gelijkwaardigheidscontrole

- [ ] De map bevat `make_wpf_grid_doc.py` en `WPF_Handboek_Grid_Overzicht.docx`.
- [ ] `python -c "import docx; print(docx.__version__)"` werkt in de gekozen omgeving.
- [ ] `python make_wpf_grid_doc.py` voltooit zonder fout en schrijft de DOCX in de hoofdmap.
- [ ] De gegenereerde DOCX bevat de titel “WPF Handboek - Grid” en de tien secties uit de generator.
- [ ] De documentrendering levert vier leesbare pagina’s op zonder afgeknipte tabellen of codeblokken.
- [ ] Een wijziging aan dit Markdown-bestand wordt gespiegeld naar `C:\Data\Obsidian\markdown\Development\HNSoftwareDevelopment\WPF\`.
- [ ] Codex kent de documentworkflow en voert visuele DOCX-controle uit na inhoudelijke wijzigingen.

## Niet uitleesbare of niet aanwezige informatie

- Verborgen Codex Desktop-appinstellingen, accountstatus, thread-/taakmetadata, opgeslagen prompts en persoonlijke voorkeuren zijn niet vanuit deze projectmap uit te lezen.
- Niet-toegankelijke externe koppelingen of accounts kunnen niet worden bevestigd; er zijn in de leesbare projectbestanden geen verwijzingen naar zulke koppelingen gevonden.
- Er zijn geen fysieke `AGENTS.md`-bestanden, `.codex`-configuratiebestanden, plug-inmanifests, lockfiles of dependencybestanden aangetroffen.
- Er is geen Git-remote, commitgeschiedenis, branch of getrackte bestandsset aanwezig die de oorspronkelijke herkomst of eerdere beslissingen kan herstellen.
- De exacte versie van `python-docx` waarmee het document is gegenereerd is niet vastgelegd.
