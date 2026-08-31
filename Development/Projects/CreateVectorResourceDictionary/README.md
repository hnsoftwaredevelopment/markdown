# CreateVectorResourceDictionary

WPF-app om uit de Syncfusion Metro Studio icon-library (mappen `Icons` en
`FontIcons`) een eigen, schone ResourceDictionary samen te stellen: alleen
de iconen die je nodig hebt, onder je eigen naam, zonder vaste kleur en
zonder tags, klaar om in een eigen WPF/C#-project te gebruiken met
`{StaticResource JouwNaam}` en een `Fill` die het thema volgt.

## Status

Basisopzet staat en bouwt zonder fouten (`dotnet build CreateVectorResourceDictionary.slnx`).
De app is nog niet lokaal getest: zie "Bekend probleem" hieronder.

## Architectuur

- `src/CreateVectorResourceDictionary.Core` (net8.0, class library)
  bevat de logica, los van UI: modellen (`IconEntry`, `IconCategory`,
  `SelectedIconRecord`, `IconProjectFile`), het inlezen van de Metro
  Studio-dictionaries (`MetroIconLibraryReader`), het wegschrijven van een
  nieuwe ResourceDictionary (`ResourceDictionaryWriter`) en het opslaan/
  openen van een selectie (`IconProjectStore`).
- `src/CreateVectorResourceDictionary.App` (net8.0-windows, WPF, MVVM met
  CommunityToolkit.Mvvm) is de UI: een boom met bronnen/categorieën links,
  een grid met iconen (checkbox, preview, eigen naam) rechts.

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

## Bouwen en starten

```
cd C:\DevOps\hnsoftwaredevelopment\CreateVectorResourceDictionary
dotnet build CreateVectorResourceDictionary.slnx
dotnet run --project src\CreateVectorResourceDictionary.App\CreateVectorResourceDictionary.App.csproj
```

## Bekend probleem: crash bij opstarten (niet onze code)

Op deze machine crasht op dit moment elke WPF-app (ook een kale, verse
`dotnet new wpf`-app zonder enige aanpassing) direct bij het opstarten met:

```
System.UriFormatException: Invalid URI: The format of the URI could not be determined.
   at MS.Internal.FontCache.Util..cctor()
```

Dit gebeurt in de WPF-runtime zelf, vóór er ook maar één regel van dit
project draait. Vermoedelijke oorzaak: een corrupte of beschadigde
Windows font-cache, mogelijk na een recente Windows-update. Mogelijke
vervolgstappen (buiten dit project, meestal met beheerdersrechten):

- de services `FontCache` en `FontCache3.0.0.0` stoppen, de map
  `C:\Windows\ServiceProfiles\LocalService\AppData\Local\FontCache`
  legen en de pc herstarten;
- controleren op recente Windows-updates rond half augustus 2026 die de
  WPF font-stack raken, en die eventueel tijdelijk verwijderen;
- testen of een kale `dotnet new wpf`-app op een andere pc wel start, om
  te bevestigen dat het aan deze machine ligt en niet aan dit project.

Zodra dat is opgelost, kan de app echt getest worden.
