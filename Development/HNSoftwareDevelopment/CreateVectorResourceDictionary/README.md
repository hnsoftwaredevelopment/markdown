# CreateVectorResourceDictionary

WPF-app om uit de Syncfusion Metro Studio icon-library (mappen `Icons` en
`FontIcons`) een eigen, schone ResourceDictionary samen te stellen: alleen
de iconen die je nodig hebt, onder je eigen naam, zonder vaste kleur en
zonder tags, klaar om in een eigen WPF/C#-project te gebruiken met
`{StaticResource JouwNaam}` en een `Fill` die het thema volgt.

## Status

Werkt en is getest: categorieën inlezen, iconen selecteren en hernoemen,
opslaan als nieuwe ResourceDictionary, bestaand project weer openen. Bouwt
zonder fouten (`dotnet build CreateVectorResourceDictionary.slnx`).

## Functies

- Boom links met Icons/FontIcons, per bron alle categorieën.
- Grid rechts per categorie: preview, checkbox, eigen naam.
- Selectie blijft actief als je van categorie wisselt.
- "Selectie tonen": laat alle op dit moment aangevinkte iconen zien, over
  alle categorieën heen, op één plek.
- Zoeken binnen de huidige categorie, of met "in alle categorieën" aan
  door de hele bibliotheek heen (laadt bij eerste gebruik alle categorieën,
  met een wachtcursor).
- Dubbele namen in je selectie worden direct rood gemarkeerd (rand,
  achtergrond en tekst), met een duidelijke melding bij het opslaan zodat
  je niet per ongeluk twee iconen onder dezelfde naam wegschrijft.
- "Nieuwe ResourceDictionary maken..." voor een nieuw bestand,
  "Bijwerken" om de laatst geopende of opgeslagen dictionary in place te
  overschrijven met de huidige selectie.
- "Openen..." leest een eerder opgeslagen `.iconproj.json` weer in: alle
  iconen komen aangevinkt en onder hun eigen naam terug, in de
  selectie-weergave, klaar om te verwijderen of aan te vullen.
- "Nieuwe ResourceDictionary maken..." en "Bijwerken" zijn uitgeschakeld
  zolang er dubbele namen in de selectie staan, zodat opslaan met een
  naamconflict niet eens mogelijk is.
- Werkbalk met iconen in plaats van tekstknoppen, elk met een tooltip die
  uitlegt wat de knop doet. De iconen zelf staan als WPF Geometry-resources
  in `src/CreateVectorResourceDictionary.App/Resources/Icons.xaml`, gemaakt
  op basis van eigen SVG-ontwerpen.
- "Selectie tonen" en "in alle categorieën zoeken" zijn schuifknoppen
  (toggle switches) in plaats van een aparte checkbox/toggle-knop.
- Zoeken wacht 250 ms na je laatste toetsaanslag voordat het filter
  toepast (debounce), met een kruisje-knop om het zoekveld in één klik
  leeg te maken.
- De iconengrid is ge-virtualiseerd (NuGet-package `VirtualizingWrapPanel`):
  bij een categorie met 1000+ iconen worden alleen de iconen die
  daadwerkelijk in beeld zijn ook echt opgebouwd, in plaats van de hele
  categorie in één keer te renderen.
- Icoonnamen worden gevalideerd: alleen letters, cijfers en underscore,
  niet beginnend met een cijfer (nodig om als x:Key en als
  SVG-bestandsnaam te kunnen gebruiken). De standaardnaam van elk icoon
  wordt daarom automatisch opgeschoond (`IconItemViewModel.SanitizeName`):
  spaties worden verwijderd waarbij het volgende teken een hoofdletter
  wordt ("Language Dutch" → "LanguageDutch"), een "-" wordt "_"
  ("Add-Folder" → "Add_Folder") en overige leestekens vallen weg. Pas je
  de naam daarna zelf nog aan tot iets ongeldigs, dan wordt die pas
  oranje gemarkeerd, met dezelfde soort duidelijke melding en blokkade
  bij opslaan als bij dubbele namen.
- De app onthoudt de laatst geopende categorie en de standen van
  "Selectie tonen"/"in alle categorieën zoeken" bij het afsluiten, en
  herstelt die bij de volgende start.
- "Exporteren naar SVG..." schrijft de huidige selectie weg als losse
  SVG-bestanden (één per icoon, bestandsnaam = eigen naam), met een
  automatisch berekende viewBox op basis van de daadwerkelijke afmetingen
  van de geometrie.
- "Openen..." accepteert ook een kale `.xaml` zonder eigen
  `.iconproj.json` (bijvoorbeeld een handmatig beheerde
  ResourceDictionary): de iconen erin komen aangevinkt in de
  selectie-weergave, met dat bestand als actief project. Selecteer je
  daarna extra iconen uit de bibliotheek, dan komen die er via
  "Bijwerken" gewoon bij in hetzelfde bestand, en krijgt het vanaf dat
  moment ook een sidecar-projectbestand zodat het voortaan als volwaardig
  project geopend wordt. Herkende iconvormen: `<Geometry x:Key="...">`,
  `<Path Data="...">`, `<GeometryGroup x:Key="...">` met daarin één of
  meer ongesleutelde `<Geometry>`-kinderen (de meest voorkomende Metro
  Studio-exportvorm) en `<PathGeometry Figures="...">`. Niet herkend:
  `DrawingImage`/`GeometryDrawing` (die hebben een vaste kleur per vorm
  ingebakken, wat botst met het "geen vaste Fill"-uitgangspunt van deze
  app) en een volledig uitgeschreven `<PathFigure>`/segment-boomstructuur.
- Eigen AppIcon (`Resources/appicon.ico`, met een bijbehorende
  `appicon.svg` als bron): zichtbaar op de taakbalk, in Verkenner op het
  .exe-bestand, en in de titelbalk van het venster.
- Bouwnummer (zie hieronder) zichtbaar rechts in de statusbalk.

## Architectuur

- `src/CreateVectorResourceDictionary.Core` (net8.0, class library)
  bevat de logica, los van UI: modellen (`IconEntry`, `IconCategory`,
  `SelectedIconRecord`, `IconProjectFile`), het inlezen van de Metro
  Studio-dictionaries (`MetroIconLibraryReader`), het inlezen van een
  willekeurige, niet door deze app aangemaakte ResourceDictionary
  (`ExternalResourceDictionaryReader`), het wegschrijven van een nieuwe
  ResourceDictionary (`ResourceDictionaryWriter`) en het opslaan/openen
  van een selectie (`IconProjectStore`).
- `src/CreateVectorResourceDictionary.App` (net8.0-windows, WPF, MVVM met
  CommunityToolkit.Mvvm) is de UI, met o.a. `Services/SvgExporter.cs` voor
  het wegschrijven van losse SVG-bestanden (hoort hier in plaats van in
  Core omdat het WPF's `Geometry`-klasse gebruikt om de viewBox te
  berekenen).

## Bronbestanden (SourceIcons)

De app verwacht een map `SourceIcons` naast de projectmap, met daarin de
submappen `Icons` en `FontIcons` zoals gekopieerd uit
`C:\Program Files (x86)\Syncfusion\Metro Studio\`:

```
CreateVectorResourceDictionary\
  SourceIcons\
    Icons\...
    FontIcons\...
```

Staat die map ergens anders, klik dan in de app op "Bronmap kiezen..." om
hem handmatig aan te wijzen. Die keuze wordt onthouden in
`%AppData%\CreateVectorResourceDictionary\settings.json`.

## Bouwnummer

Elke build (ook zonder codewijzigingen) krijgt een oplopend versienummer
in het formaat `YYYY.MM.dd.xxx`, bijvoorbeeld `2026.08.31.004`: de eerste
build van de dag krijgt `000`, elke build daarna telt op. De teller staat
in `build\buildnumber.txt` en wordt automatisch bijgewerkt door een
MSBuild-target in `CreateVectorResourceDictionary.App.csproj`
(`SetBuildVersion`). Design-time builds van Visual Studio (voor
IntelliSense) tellen niet mee, alleen echte builds. Het nummer staat
rechts in de statusbalk van de app.

## Bouwen en starten

```
cd C:\DevOps\hnsoftwaredevelopment\CreateVectorResourceDictionary
dotnet build CreateVectorResourceDictionary.slnx
dotnet run --project src\CreateVectorResourceDictionary.App\CreateVectorResourceDictionary.App.csproj
```

## Bekende verbeterpunten (nog open)

- Eerste keer een categorie openen duurt soms nog even omdat het bestand
  op dat moment van schijf wordt gelezen; er staat een bezig-indicator
  tijdens het laden (op de achtergrondthread, zie hierboven), maar het is
  geen instant proces bij hele grote categorieën.
