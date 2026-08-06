# HN Software Development website

Blazor website voor de publieke softwareproducten van HN Software Development.

## Snel aanpassen

- **Pagina-inhoud per product:** `Components/Pages/*.razor`
- **Vertaalde teksten:** `Resources/SharedResources.resx`, `SharedResources.en.resx`, `SharedResources.de.resx`
- **Gedeelde productopbouw:** `Components/Shared/ProductPageShell.razor`
- **Downloads:** `wwwroot/downloads/<product>/manuals` en `wwwroot/downloads/<product>/installers`
- **Screenshots:** `wwwroot/downloads/<product>/screenshots`
- **Vlaggen:** `wwwroot/flags`
- **Logo:** `wwwroot/logo.svg`
- **Algemene styling:** `wwwroot/app.css`

## Pagina's

De gewone websitepagina's staan in `Components/Pages`.

- `Home.razor`: homepage met hero en productoverzicht.
- `About.razor`: over-mij pagina.
- `Saga.razor`: productpagina Saga.
- `ModelbouwerDekbeplanking.razor`: productpagina Modelbouwer Dekbeplanking.
- `ModelbouwerWerkbank.razor`: productpagina Modelbouwer Werkbank.
- `MySqlAnalyzer.razor`: productpagina MySqlAnalyzer.
- `AmusingAndroid.razor`: productpagina Amusing Android app.

Productpagina's gebruiken `ProductPageShell`. De shell geeft een vaste kop, downloads en supportblok. De inhoud tussen de start- en eindtag van `ProductPageShell` is vrij per productpagina. Daar kun je dus extra secties, tekstblokken en screenshots plaatsen.

Code-behind staat in `.razor.cs` bestanden. Houd de `.razor` bestanden bij voorkeur voor markup en plaats C# logica, properties, events en lifecycle methods in het bijbehorende `.razor.cs` bestand.

Pagina-specifieke styling kan in een `.razor.css` bestand naast de pagina. Gebruik dat alleen voor styling die echt bij één pagina hoort. Algemene styling blijft in `wwwroot/app.css`.

## Meertaligheid

De site gebruikt `.resx` bestanden zodat teksten met ResX Manager aangepast kunnen worden.

- `SharedResources.resx`: Nederlands, de basistaal.
- `SharedResources.en.resx`: Engels.
- `SharedResources.de.resx`: Duits.

Gebruik in Razor:

```razor
@Language.Text("ResourceKey")
```

De taalkeuze zelf staat in `Services/SiteLanguageService.cs`. Die service bewaart de huidige taal, levert de vlaggen voor de taalkeuze en leest teksten uit de `.resx` bestanden.

## Screenshots

Screenshots hoeven niet verplicht in de vaste screenshotsectie te staan. Voor productpagina's is het vaak beter om screenshots direct bij de uitleg te plaatsen waar ze inhoudelijk horen.

Omdat screenshots taalafhankelijk kunnen zijn, gebruik bij voorkeur een map per taal:

```text
wwwroot/downloads/<product>/screenshots/nl/
wwwroot/downloads/<product>/screenshots/en/
wwwroot/downloads/<product>/screenshots/de/
```

Voorbeeld in een productpagina:

```razor
<img src="@($"downloads/modelbouwer-dekbeplanking/screenshots/{Language.CurrentLanguage}/voorbeeld.png")"
     alt="@Language.Text("ModelbouwerDekbeplanking_Name")" />
```

De standaard screenshotsectie in `ProductPageShell` is vooral bedoeld als tijdelijke plek zolang er nog geen screenshots zijn. Als een productpagina eigen screenshots op de juiste plek toont, kan de shell later worden uitgebreid met een optie om die standaardsectie uit te zetten.

## Downloads

Downloads zijn voorbereid per product:

```text
wwwroot/downloads/<product>/manuals/
wwwroot/downloads/<product>/installers/
```

Zolang een bestand nog ontbreekt, toont `DownloadPanel` automatisch dat de download binnenkort beschikbaar is.

## Header en layout

- Hoofdnavigatie: `Components/Layout/MainLayout.razor`
- Taalkeuze: `Components/Shared/LanguageSelector.razor`
- Algemene styling: `wwwroot/app.css`

De taalkeuze gebruikt SVG-vlaggen uit `wwwroot/flags` en bewaart de gekozen taal in `localStorage`.

## Build

```powershell
dotnet build
```

Lokaal starten:

```powershell
dotnet run --urls http://localhost:5206
```
