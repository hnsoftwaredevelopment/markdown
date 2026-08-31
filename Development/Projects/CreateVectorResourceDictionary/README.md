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
  uitlegt wat de knop doet.
- "Selectie tonen" en "in alle categorieën zoeken" zijn schuifknoppen
  (toggle switches) in plaats van een aparte checkbox/toggle-knop.
- Bouwnummer (zie hieronder) zichtbaar rechts in de statusbalk.

## Architectuur

- `src/CreateVectorResourceDictionary.Core` (net8.0, class library)
  bevat de logica, los van UI: modellen (`IconEntry`, `IconCategory`,
  `SelectedIconRecord`, `IconProjectFile`), het inlezen van de Metro
  Studio-dictionaries (`MetroIconLibraryReader`), het wegschrijven van een
  nieuwe ResourceDictionary (`ResourceDictionaryWriter`) en het opslaan/
  openen van een selectie (`IconProjectStore`).
- `src/CreateVectorResourceDictionary.App` (net8.0-windows, WPF, MVVM met
  CommunityToolkit.Mvvm) is de UI.

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

- Eerste keer een categorie openen duurt soms een paar seconden; er staat
  nu een wachtcursor tijdens het laden, maar de grid is nog niet
  ge-virtualiseerd. Bij categorieën met 1000+ iconen (met name in
  FontIcons) kan dat op termijn alsnog traag aanvoelen; een echte
  virtualiserende grid is de volgende stap als dat in de praktijk stoort.
