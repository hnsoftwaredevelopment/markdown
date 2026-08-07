# FontManager — Architectuur en Ontwerp

Status: concept v0.1 — ter review
Auteur: Claude (Cowork) i.o.v. Herbert Nijkamp
Datum: 2026-08-07

## 1. Doel

Een Windows-desktopapplicatie die alle op de computer aanwezige fonts detecteert en toont (geïnstalleerd én niet-geïnstalleerd), met een duidelijke preview per font, uitgebreide organisatiemogelijkheden (categorie, tags, projecten, mappen) en de mogelijkheid fonts direct te installeren of te verwijderen. De app moet modern en visueel aansprekend zijn, met meerdere kleurthema's en drie talen (NL/EN/DE).

Dit document beschrijft de architectuur en het ontwerp vóórdat er code wordt gebouwd, zodat de aanpak eerst kan worden beoordeeld.

## 2. Belangrijkste features (uit de aanvraag)

1. Fonts op de computer detecteren en tonen: naam + preview-regel, met duidelijke status "geïnstalleerd" / "niet geïnstalleerd".
2. Presentatie op meerdere manieren:
   - Categorisatie op visuele classificatie (Serif, Sans Serif, Script, Display, etc.) met subcategorieën (licentietype, gewicht, stijl, breedte).
   - Eigen tags toevoegen aan fonts.
   - Fonts koppelen aan projectnamen.
   - Overzicht van fonts per map (directory).
3. Detailweergave per font: uitgebreide voorbeeldtekst (niet alleen "quick brown fox"), met cijfers, leestekens en speciale/diakritische tekens.
4. Fonts kunnen installeren en verwijderen vanuit de app.
5. Drie talen: Nederlands (standaard), Engels, Duits — opgeslagen in ResX-bibliotheken, direct te wisselen in de app.
6. Meerdere kleurthema's: donker, licht, rood, blauw, groen, lime, etc. — te wisselen zonder herstart.
7. Moderne, verzorgde UI die een sterke eerste indruk maakt.
8. Geïntegreerde Character map

## 3. Technologiekeuze

| Onderdeel | Keuze | Reden |
|---|---|---|
| Platform | Windows-desktop, .NET 8 | Font-installatie/-verwijdering en fontmetadata zijn Windows-specifiek. |
| UI-framework | WPF | Native, volwassen, uitstekende ResX-ondersteuning, flexibel voor custom theming. |
| Modern uiterlijk | WPF-UI (Fluent 2 componentenset) als basis, met eigen kleurthema's erboven | Geeft direct een moderne Fluent-look (afgeronde hoeken, acrylic/mica-achtergronden, animaties) zonder alles from scratch te bouwen. |
| MVVM-toolkit | CommunityToolkit.Mvvm | Minder boilerplate voor commands/properties, goed onderhouden, past bij WPF Handbook-aanpak (bindings/commands/converters). |
| Data-opslag | SQLite (lokaal bestand, via Microsoft.EntityFrameworkCore.Sqlite) | Lichtgewicht, geen server nodig, geschikt voor tags/categorieën/projecten/mapkoppelingen en scan-cache. |
| Fontmetadata-uitlezing | DirectWrite (via P/Invoke of Vortice.DirectWrite) + fallback System.Drawing.Text | DirectWrite geeft rijkere informatie (family/subfamily, gewicht, stijl, breedte, naam-tabel-velden zoals licentie-omschrijving) dan de oudere GDI-API's. |
| Lokalisatie | .resx per taal + gegenereerde Resources-klassen | Sluit aan bij de wens "talen in ResX-bibliotheek"; standaard .NET-mechanisme, goed te onderhouden. |

## 4. Projectstructuur (solution)

```
FontManager/
├─ FontManager.sln
├─ src/
│  ├─ FontManager.App/            → WPF-project (Views, App.xaml, thema's, resx)
│  │  ├─ Views/                   → MainWindow, FontDetailView, SettingsView, ...
│  │  ├─ ViewModels/
│  │  ├─ Themes/                  → Dark.xaml, Light.xaml, Red.xaml, Blue.xaml, Green.xaml, Lime.xaml, ...
│  │  ├─ Resources/
│  │  │  └─ Strings/              → Strings.nl-NL.resx (default), Strings.en-US.resx, Strings.de-DE.resx
│  │  └─ Converters/, Behaviors/
│  ├─ FontManager.Core/           → Domeinmodellen, services (interfaces + implementatie), geen UI-afhankelijkheden
│  │  ├─ Models/
│  │  ├─ Services/                → FontScanService, FontInstallService, PreviewRenderService, ClassificationService
│  │  └─ Localization/            → ILocalizationService
│  └─ FontManager.Data/           → EF Core DbContext, migraties, repositories
├─ tests/
│  └─ FontManager.Tests/          → Unit tests voor services (scanning, classificatie, install-logica met mocks)
└─ docs/                          → Kopie van ontwerpdocumenten (gespiegeld vanuit Obsidian)
```

Namespace-root: `FontManager` (consistent met je overige HNSoftware-projecten).

## 5. Datamodel

Kernentiteiten (SQLite, via EF Core):

- **FontFamily** — Id, FamilyName, Foundry/Producer (indien afleidbaar), SourceType (Installed / DirectoryScan), PrimaryDirectoryId.
- **FontFace** — Id, FontFamilyId, StyleName (bv. "Bold Italic"), Weight (numeriek 100-900 + labeltekst Thin..Black), Slant (Regular/Italic/Oblique), Stretch (Condensed..Expanded), FilePath, FileFormat (TTF/OTF/WOFF/...), IsInstalled (bool), InstallScope (PerUser/Machine/NotInstalled), LicenseTypeRaw (uitgelezen uit naam-tabel indien aanwezig), FileHash, LastSeenUtc.
- **Category** (vaste taxonomie, zie §6) — Id, Key, DisplayNameKey (verwijst naar resx-sleutel voor vertaling).
- **SubCategoryValue** — Id, Type (LicenseType/Weight/Style/Width), Key, DisplayNameKey.
- **FontFaceCategory** — koppeltabel FontFace ↔ Category (een font kan door de gebruiker eventueel in meerdere categorieën worden gezet, met één "primaire" classificatie die automatisch is voorgesteld).
- **Tag** — Id, Name, ColorHex (optioneel, voor gekleurde tag-chips).
- **FontFaceTag** — koppeltabel FontFace ↔ Tag (n:n).
- **Project** — Id, Name, Description, CreatedUtc.
- **FontFaceProject** — koppeltabel FontFace ↔ Project (n:n) — een font kan aan meerdere projecten hangen.
- **WatchedDirectory** — Id, Path, IncludeSubdirectories (bool), LastScanUtc — de mappen die de gebruiker heeft toegevoegd om (nog niet geïnstalleerde) fonts in te vinden.
- **AppSettings** — sleutel/waarde-achtige tabel: huidige taal, huidig thema, venstergrootte, etc.

Automatische classificatie (visuele categorie, gewicht, stijl) wordt bij het scannen voorgesteld op basis van fontmetadata en heuristieken (zie §7.3); de gebruiker kan dit altijd overschrijven — overschrijvingen worden apart bewaard zodat een herscan de handmatige keuzes niet overschrijft.

## 6. Classificatietaxonomie (visuele categorie)

Vaste hoofdcategorieën (uitbreidbaar, maar met een gecureerde startset zodat het overzichtelijk blijft):

1. Serif
2. Sans Serif
3. Script / Handwriting
4. Display / Decorative
5. Slab Serif
6. Monospace
7. Blackletter
8. Symbol / Icon (bv. Wingdings-achtige fonts, iconfonts)

Subcategorieën (per font onafhankelijk van elkaar in te stellen):

- **Licentietype**: Vrij voor commercieel gebruik, Persoonlijk gebruik, Trial, Commercieel/betaald, Onbekend.
- **Gewicht**: Thin, Extra Light, Light, Regular, Medium, SemiBold, Bold, Extra Bold, Black (gekoppeld aan numerieke waarden 100-900 voor correcte sortering).
- **Stijl**: Regular, Italic, Oblique.
- **Breedte**: Condensed, Normal, Extended.

## 7. Functionele modules

### 7.1 Font-detectie

- **Geïnstalleerde fonts**: uitlezen via DirectWrite `IDWriteFontCollection` (systeem + per-gebruiker collectie), aangevuld met de registry-sleutels `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts` en `HKCU\...\Fonts` om installatie-scope (machine/gebruiker) te bepalen.
- **Niet-geïnstalleerde fonts**: de gebruiker voegt mappen toe ("watched directories", bv. een download- of archiefmap); deze worden gescand op .ttf/.otf/.woff/.woff2-bestanden. Voor elk gevonden bestand wordt gecontroleerd of de familie al geïnstalleerd is (via bestandshash en family/style-vergelijking) → status "Geïnstalleerd" of "Niet geïnstalleerd" per fontbestand.
- Scannen gebeurt op de achtergrond (async, met voortgangsindicatie) en de resultaten worden gecachet in de SQLite-database zodat de app bij opstarten niet steeds alles opnieuw hoeft te lezen; een handmatige "Herscannen"-actie is altijd beschikbaar, en gewijzigde mappen worden gevolgd met een `FileSystemWatcher`.

### 7.2 Preview-rendering

- Per fontface wordt een preview gerenderd met `Glyphs`/`FormattedText` (WPF) op basis van het eigenlijke fontbestand (ook als het nog niet is geïnstalleerd — WPF kan direct uit een bestand renderen via `GlyphTypeface`).
- **Lijstweergave**: één regel per font met de fontnaam (in het eigen font gerenderd) — vergelijkbaar met een systeemlettertypekiezer, maar met status-badge.
- **Detailweergave**: een ruime voorbeeldtekst die per taal wisselt en het volgende bevat:
  - Een pangram per taal (NL: "Pa's wijze lynx bezag vroom het fikse aquaduct", EN: "The quick brown fox jumps over the lazy dog", DE: "Zwölf Boxkämpfer jagen Viktor quer über den großen Sylter Deich").
  - Alle cijfers: `0123456789`.
  - Leestekens en symbolen: `!@#$%&*()_+-=[]{}|;:'",.<>/?~\``.
  - Diakritische tekens relevant voor NL/DE: `é è ë ï ö ü à â ç ñ ß Ä Ö Ü`.
  - Een vrij tekstveld waarin de gebruiker eigen tekst kan typen om te testen.
  - Een lettergrootte-schuifregelaar (bv. 12–120 px) en weergave van alle beschikbare gewichten/stijlen van die familie naast elkaar.
- Thumbnails voor de lijstweergave worden op de achtergrond voorgerenderd en als bitmap gecachet voor snelle scroll-performance bij grote fontverzamelingen.

### 7.3 Automatische classificatie (heuristiek)

Bij het scannen wordt een voorstel voor hoofdcategorie gedaan op basis van:

- OS/2-tabelvelden in het fontbestand (indien aanwezig: `panose`-classificatie geeft een directe indicatie van Serif/Sans/Script/etc.).
- Aanwezigheid van "Mono"/"Code"/"Console" in de naam → Monospace; vaste-breedte-detectie als extra check.
- Sleutelwoorden in de familienaam (Script, Hand, Brush, Display, Slab, Condensed, etc.) als aanvullende heuristiek wanneer PANOSE-data ontbreekt.
- Dit is altijd een *voorstel*: de gebruiker kan de categorie met één klik aanpassen, en die keuze blijft daarna behouden.

### 7.4 Installeren en verwijderen

- **Per-gebruiker installatie** (geen rechten nodig): bestand kopiëren naar `%LOCALAPPDATA%\Microsoft\Windows\Fonts`, registreren onder `HKCU\...\Fonts`, en het systeem laten weten via `AddFontResource` + het uitzenden van een `WM_FONTCHANGE`-bericht.
- **Systeembrede installatie** (voor alle gebruikers): kopiëren naar `%WINDIR%\Fonts` en registreren onder `HKLM\...\Fonts` — dit vereist administratorrechten. De app detecteert of verhoogde rechten nodig zijn en vraagt dan (via een kleine elevated helper, of een `app.manifest`-aanvraag) om een UAC-bevestiging; dit gebeurt alleen op het moment dat de gebruiker daadwerkelijk op "Installeren (systeembreed)" klikt, niet bij het opstarten van de app.
- **Verwijderen**: spiegelbeeld van installeren — `RemoveFontResource`, registry-sleutel opruimen, bestand verwijderen (met bevestigingsdialoog), rekening houdend met per-gebruiker vs. systeembrede scope.
- Na installeren/verwijderen wordt de betreffende fontface direct in de UI bijgewerkt (geen volledige herscan nodig).

### 7.5 Organisatie & navigatie (UI)

Schermindeling:

- **Linker navigatiepaneel**: Alle fonts · Categorieën (uitklapbaar met subcategoriefilters) · Tags · Projecten · Mappen. Aantallen per item worden getoond (bv. "Sans Serif (128)").
- **Hoofdpaneel**: sorteerbare/filterbare lijst of grid met per font: naam (gerenderd in het font zelf), status-badge (Geïnstalleerd/Niet geïnstalleerd), hoofdcategorie, tags als chips. Een zoekbalk filtert direct op naam/tag/project.
- **Detailpaneel** (rechterzijde of dialoog bij dubbelklik): grote preview zoals in §7.2, metadata (bestandslocatie, formaat, gewicht/stijl, licentietype), tags toevoegen/verwijderen, koppelen aan project(en), categorie aanpassen, installeren/verwijderen-knop, "Toon in Verkenner"-knop.
- **Mappen-overzicht**: lijst van watched directories met per map het aantal gevonden fonts en hoeveel daarvan al geïnstalleerd zijn; van hieruit mappen toevoegen/verwijderen en per map herscannen.

## 8. Theming-systeem

- Elk thema is een aparte `ResourceDictionary` (bv. `Themes/Dark.xaml`, `Light.xaml`, `Red.xaml`, `Blue.xaml`, `Green.xaml`, `Lime.xaml`, ...) die dezelfde set kleursleutels invult: `Color.Background`, `Color.Surface`, `Color.Border`, `Color.TextPrimary`, `Color.TextSecondary`, `Color.Accent`, `Color.AccentHover`, `Color.Success/Warning/Danger`.
- Wisselen van thema = de betreffende dictionary in `App.xaml`'s `MergedDictionaries` vervangen; geen herstart nodig, alle bindings updaten automatisch omdat WPF `DynamicResource` gebruikt voor deze sleutels.
- Bovenop de kleurthema's ligt de WPF-UI/Fluent 2-stijllaag (afgeronde hoeken, zachte schaduwen, subtiele hover/press-animaties) zodat elk kleurthema er even verzorgd uitziet.
- Thema-keuze wordt onthouden in `AppSettings` en direct toegepast bij opstarten.

## 9. Lokalisatie (i18n)

- Eén resx-set per taal onder `Resources/Strings/`: `Strings.resx` (Nederlands = standaard/fallback), `Strings.en-US.resx`, `Strings.de-DE.resx`.
- Alle UI-teksten (labels, knoppen, categorienamen, foutmeldingen) via resource-sleutels, geen hardcoded tekst in XAML.
- Taal wisselen in de app (instellingenscherm) past direct `Thread.CurrentThread.CurrentUICulture` aan en herlaadt de gebonden teksten via een lichte `LocalizationManager`-service (zodat, net als bij thema's, geen herstart nodig is).
- Categorienamen, gewichtslabels etc. worden ook via resx vertaald, zodat de hele taxonomie meertalig is.

## 10. Fasering

**Fase 1 — Kernfunctionaliteit**
Scannen van geïnstalleerde fonts, lijst + statusbadge, basis-preview (pangram + cijfers + speciale tekens), installeren/verwijderen (per gebruiker), NL/EN/DE-taalwissel, één donker + één licht thema.

**Fase 2 — Organisatie**
Automatische + handmatige categorisatie met subcategorieën, tags, projecten, mappen-overzicht (watched directories), uitgebreid detailpaneel met eigen invoertekst en lettergrootte-schuif.

**Fase 3 — Afwerking**
Volledige themaset (rood/blauw/groen/lime/etc.), systeembrede installatie met UAC-elevatie, thumbnail-caching voor performance bij grote collecties, zoek/filter-verfijning.

**Fase 4 — Nice-to-have (optioneel, later te bepalen)**
Font-vergelijking naast elkaar, exporteren van een projectoverzicht (bv. naar PDF), favorieten/sterren, "vergelijkbare fonts"-suggesties.

## 11. Aannames & open vragen

- Licentietype wordt waar mogelijk uit fontmetadata gehaald (naam-tabel-ID's 13/14, EULA-omschrijving), maar dit is niet altijd aanwezig — in dat geval staat het standaard op "Onbekend" en kan de gebruiker het handmatig invullen.
- Systeembrede installatie/verwijdering vereist adminrechten; dit is een bewuste Windows-beperking, geen keuze van de app.
- Deze cloud-sessie kan de C#/XAML-code schrijven maar niet bouwen/uitvoeren (geen Windows/.NET-runtime met echte fonts hier) — bouwen en testen gebeurt door jou op je eigen machine (Visual Studio 2022 / .NET 8 SDK), met de bestanden rechtstreeks in `C:\DevOps\hnsoftwaredevelopment\FontManager`.
- Naamgeving/mapstructuur is afgestemd op je bestaande HNSoftware-projecten; laat het weten als je een andere indeling gewend bent.

## 12. Volgende stap

Na akkoord op dit document: aanmaken van de solution-skeleton (projecten, NuGet-referenties, lege Views/ViewModels, resx-bestanden met basissleutels, thema-dictionaries) rechtstreeks in `C:\DevOps\hnsoftwaredevelopment\FontManager`, gevolgd door de implementatie in de volgorde van de fasering in §10.
