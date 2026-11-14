# Extension Overlap

Visual Studio-extensie die laat zien waar geïnstalleerde extensies en Visual Studio zelf hetzelfde doen in de editor, zoals dubbele kleurvakjes, tooltips of lampjes. Ook vindt hij extensiemappen die VS niet meer gebruikt. Doel: overbodige extensies aanwijzen, zodat VS sneller start en sneller update.

Dit is het leerdocument. Per stap staat hier hoe het werkt en waarom. Het voorstel met het vooronderzoek staat in `Haalbaarheid en voorstel v1.md`.

## Mappen

```
ExtensionOverlap/
├─ ExtensionOverlap.sln
├─ Directory.Build.props            ← output naar Builds\<project>\
├─ src/ExtensionOverlap/            ← de extensie (VSIX, net48)
│  ├─ source.extension.vsixmanifest ← wat zit erin, voor welke VS-versies
│  ├─ Properties/
│  ├─ Scanning/                     ← manifesten en DLL's lezen, zonder VS, getest
│  └─ Analysis/                     ← indelen en overlap zoeken, zonder VS, getest
├─ tests/ExtensionOverlap.Tests/    ← unit tests (MSTest, net48)
└─ tools/build-and-test.ps1         ← bouwen en testen zonder de IDE
```

Later komen erbij: `VisualStudio/` (de koppeling met VS), `ToolWindow/`, `Localization/` en `Options/`.

Deze handleiding en de andere bouwdocumenten staan alleen in Obsidian. In de repo staat alleen wat de eindgebruiker nodig heeft: README, CHANGELOG en LICENSE.

## Bouwen en testen

```powershell
powershell -File tools\build-and-test.ps1
```

Het script zoekt via `vswhere` een volledige VS-installatie (Enterprise, Professional of Community, geen Build Tools), bouwt de solution en draait de tests. De uitvoer komt in `Builds\ExtensionOverlap\Debug\` (met het `.vsix`-bestand) en `Builds\ExtensionOverlap.Tests\Debug\net48\`.

**Waarom twee keer `Directory.Build.props`?** In `C:\DevOps\hnsoftwaredevelopment` staat er al een die de output naar `<repo>\Builds\<project>\` stuurt. De repo heeft een eigen kopie met dezelfde regel, omdat GitHub Actions alleen de repo ophaalt en de map erboven niet kent. MSBuild neemt het dichtstbijzijnde bestand en zoekt daarna niet verder omhoog. Het resultaat is op je laptop hetzelfde.

## 1. Het VSIX-project

Opgezet zoals ResourcePreview, met deze verschillen:

| Onderdeel | Waarde | Waarom |
|---|---|---|
| `MinimumVisualStudioVersion` | 18.0 | alleen VS 2026 |
| `InstallationTarget` in het manifest | `[18.0,19.0)` | VS 2026 en zijn updates, geen VS 2022 |
| `Microsoft.VSSDK.BuildTools` | 18.9.820 | de build-tools van VS 2026 |
| `GeneratePkgDefFile` | false | er is nog geen package; dat komt met het venster en de Opties |

`Microsoft.VisualStudio.SDK` staat er met `ExcludeAssets="runtime"`. Dat betekent: compileer ertegen, maar stop de DLL's niet in de VSIX, want VS heeft ze al. Hetzelfde geldt voor `System.Reflection.Metadata`, die via de SDK binnenkomt (versie 9.0). VS 2026 stuurt in `devenv.exe.config` elke versie tot en met 10.0.0.14 door naar zijn eigen 10.0.0.14, dus de extensie gebruikt in VS altijd de versie van VS. Zou je hem toch meeleveren, dan heb je twee versies naast elkaar, met rare fouten als gevolg.

## 2. Waar VS extensies bewaart

| Soort | Map |
|---|---|
| Per gebruiker | `%LocalAppData%\Microsoft\VisualStudio\18.0_<instanceId>\Extensions\<willekeurig>\` |
| Experimental Instance | `...\18.0_<instanceId>Exp\Extensions\` |
| Machine-breed, van derden | `<installatiemap>\Common7\IDE\Extensions\<willekeurig>\` |
| Van VS zelf | `Common7\IDE\CommonExtensions\...` en `Common7\IDE\Extensions\Microsoft\...` |

De `instanceId` is dezelfde als die `vswhere` toont. Elke extensie heeft een eigen map met een willekeurige naam, zoals `nylyr3fo.51b`, en daarin een `extension.vsixmanifest`.

Niet elke map is in gebruik. Bij een update blijft de oude map soms staan, en een uitgeschakelde extensie houdt zijn map. Op de laptop kent VS 63 van de 83 mappen; de andere 20 zijn wezen. De extensie vraagt VS daarom straks zelf welke extensies geïnstalleerd zijn (`IVsExtensionManagerAsync`), in plaats van alleen mappen te lezen. De wezen worden een eigen onderdeel in het venster.

## 3. Het manifest lezen

`Scanning\ExtensionManifest.cs` haalt uit `extension.vsixmanifest` de id, naam, versie, uitgever en de MEF-assemblies.

Een DLL met MEF-onderdelen staat in het manifest als asset:

```xml
<Asset Type="Microsoft.VisualStudio.MefComponent" Path="RainbowBraces.dll" />
```

Oude extensies gebruiken het schema van 2010, met `<Content><MefComponent>Old.dll</MefComponent></Content>`. De lezer kent beide. Hij herkent het schema aan het element `Metadata/Identity` (2011) of `Identifier` (2010).

**Veiligheid.** Het manifest komt van iemand anders. Daarom:

- `DtdProcessing.Prohibit` en `XmlResolver = null`. Een DTD kan entiteiten definiëren die het bestand opblazen of externe bestanden binnenhalen. Een manifest heeft er nooit een nodig, dus de lezer weigert ze.
- Elk pad uit het manifest moet binnen de map van de extensie blijven. `..\Outside.dll` telt als ontbrekend. Zo kan een manifest de scanner niet naar een willekeurig bestand sturen.
- Een pad met `|`, zoals `|%CurrentProject%|`, is een build-token dat bij het bouwen vervangen had moeten worden. Dat telt ook als ontbrekend.

## 4. Metadata lezen zonder de DLL te laden

Dit is de kern: `Scanning\AssemblyScanner.cs`.

**Wat er in een DLL staat.** Een .NET-DLL is een PE-bestand (hetzelfde formaat als een .exe). Daarin zit, naast de code, een metadata-blok: tabellen met alle types, velden, methoden en attributen. MEF leest bij het opstarten van VS precies deze tabellen om te weten wat een DLL exporteert. Wij doen hetzelfde.

**De stappen.**

```csharp
using (var stream = new FileStream(path, FileMode.Open, FileAccess.Read, FileShare.ReadWrite | FileShare.Delete))
using (var pe = new PEReader(stream, PEStreamOptions.PrefetchMetadata))
{
    var md = pe.GetMetadataReader();
    foreach (var typeHandle in md.TypeDefinitions) { ... }
}
```

| Klasse | Doet |
|---|---|
| `PEReader` | opent het PE-bestand en vindt het metadata-blok |
| `MetadataReader` | geeft toegang tot de tabellen: `TypeDefinitions`, velden, properties, attributen |
| `CustomAttribute.DecodeValue` | leest de waarden van één attribuut |

`FileShare.ReadWrite | FileShare.Delete` zorgt dat VS of de VSIX-installer het bestand gewoon kan gebruiken terwijl wij lezen. `PrefetchMetadata` kopieert het metadata-blok in één keer naar het geheugen.

**Waarom er niets geladen wordt.** `Assembly.Load` en `Assembly.LoadFrom` maken een DLL onderdeel van het proces; daarna kan er code uit draaien, bijvoorbeeld een statische constructor. `System.Reflection.Metadata` leest alleen bytes. Er ontstaat geen `Assembly`-object en het type `IViewTaggerProvider` hoeft niet te bestaan. De test `Scanning_does_not_load_the_assembly` bewijst het: hij kopieert een DLL naar een nieuwe naam, scant die, en controleert dat geen geladen assembly die locatie heeft.

**Attribuutwaarden lezen.** Een attribuut staat in de metadata als verwijzing naar de constructor plus een blok bytes met de argumenten. `DecodeValue` leest die bytes, maar moet weten hoe het een type moet weergeven. Daarvoor is `TypeNameProvider`: een `ICustomAttributeTypeProvider<string>` die van elk type gewoon de volledige naam als tekst maakt.

Dat werkt omdat `typeof(X)` in een attribuut niet als echt type wordt opgeslagen, maar als tekst:

```
Microsoft.VisualStudio.Text.Editor.IntraTextAdornmentTag, Microsoft.VisualStudio.Text.UI.Wpf, Version=17.0.0.0, ...
```

`StripAssemblyNames` haalt het assembly-deel eraf. Bij generieke types zit het assembly-deel ook binnen de haken (`G`1[[C.D, Asm2]], Asm1`); de reguliere expressie haalt beide weg.

Eén ding kan `DecodeValue` niet zonder hulp: het onderliggende type van een enum uit een andere DLL. Of het een `int` of een `byte` is, staat in die andere DLL. `TypeNameProvider` zegt altijd `Int32`. Dat klopt voor vrijwel elke enum. Klopt het niet, dan gooit `DecodeValue` een `BadImageFormatException`; de scanner vangt die op en noteert `(unreadable)` voor dat ene attribuut.

**Wat een export is.** Alleen `System.ComponentModel.Composition.ExportAttribute` telt. De scanner vergelijkt de volledige naam, zodat een eigen klasse die toevallig `ExportAttribute` heet niet meetelt. Het contract:

| Schrijfwijze | Contract |
|---|---|
| `[Export(typeof(IViewTaggerProvider))]` | `Microsoft.VisualStudio.Text.Tagging.IViewTaggerProvider` |
| `[Export("FixtureContract")]` | `FixtureContract` |
| `[Export]` op een klasse | de klasse zelf |
| `[Export]` op een veld of property | het type van het veld of de property |

Alle andere attributen op dezelfde klasse of hetzelfde lid worden metadata, op korte naam: `ContentTypeAttribute` wordt `ContentType`. Benoemde argumenten krijgen hun naam erbij: `[Order(After = "X", Before = "Y")]` wordt `After=X, Before=Y`. Staan er twee `[Export]`'s op één klasse, dan worden het twee exports met dezelfde metadata.

**Eigen export-attributen.** Roslyn gebruikt bijvoorbeeld `[ExportCompletionProvider]`, een klasse die afgeleid is van `ExportAttribute`. Welk contract die geeft, staat in de DLL van Roslyn. De scanner volgt dat nog niet, maar zet de namen in `CustomExportAttributes`, zodat zichtbaar is dat er iets gemist wordt.

## 5. Exports op velden en properties

Niet alles wat VS exporteert is een klasse. Content types, adornment layers en kleurdefinities zijn velden of properties:

```csharp
[Export]
[Name("XAML")]
[BaseDefinition("code")]
internal static ContentTypeDefinition XamlContentType;
```

Hier staat `[Export]` zonder type. Het contract is dan het type van het veld, en dat staat niet in het attribuut maar in de **signatuur** van het veld. Die lees je met `FieldDefinition.DecodeSignature`, met een `ISignatureTypeProvider`. `TypeNameProvider` implementeert beide interfaces, want ze vragen grotendeels hetzelfde: maak van een type-handle een naam.

Voor een property zit het type in de signatuur van de property als `ReturnType`. Een methode met `[Export]` (zeldzaam, voor delegates) krijgt contract `(method)`.

`[BaseDefinition]` is belangrijk voor later: daarmee bouw je de boom van content types (`XAML` is een `code`, `code` is een `text`). Color Picker Tool registreert zich op `text` en `code`, niet op `XAML`, en tekent toch kleurvakjes in XAML. Zonder die boom mis je hem.

## 6. Testen

`tests\ExtensionOverlap.Tests` bevat tests die zonder Visual Studio draaien: 15 voor `Scanning` (hieronder) en 15 voor `Analysis` (sectie 7).

**Testdata in de testassembly zelf.** In plaats van een aparte DLL met testklassen staan die in `Fixtures.cs`, in het testproject. De tests scannen het eigen bestand van de testassembly (`typeof(AssemblyScannerTests).Assembly.Location`). MEF komt er nooit aan; de klassen hoeven alleen te compileren. Daarom zijn ze `abstract` en implementeren ze de interfaces niet.

| Bestand | Wat het test |
|---|---|
| `AssemblyScannerTests` | contract, content types en tag type van een tagger; twee exports op één klasse; contract als tekst; klassen zonder export; `[Export]` zonder type op een veld; benoemde argumenten op een property; geneste klassen (`Outer+Inner`); dat er niets geladen wordt; kapotte en ontbrekende bestanden; assembly-namen weghalen; korte attribuutnamen; de twee kleurvakjes-taggers van VS 2026 zelf |
| `ExtensionManifestTests` | id, naam en MEF-assemblies; ontbrekende bestanden, build-tokens en paden buiten de map; het schema van 2010; ontbrekend, kapot of met een DTD |

De test met de echte VS-DLL zoekt `Microsoft.VisualStudio.DesignTools.XamlLanguageService.dll` onder `Program Files\Microsoft Visual Studio\18\`. Staat VS 2026 er niet (zoals in GitHub Actions), dan wordt de test `Inconclusive` in plaats van rood.

**Een les uit de eerste testronde.** De test voor `[Order(After = PredefinedAdornmentLayers.Selection)]` verwachtte `After=Selection`. De scanner gaf `After=SelectionAndProvisionHighlight`. De scanner had gelijk: een constante wordt bij het compileren vervangen door zijn waarde, en `PredefinedAdornmentLayers.Selection` is de tekst `"SelectionAndProvisionHighlight"`. De metadata kent de naam van de constante niet meer. In het venster zie je dus de echte waarden, niet de namen uit de broncode.

`TempFolder` maakt per test een eigen map onder `%TEMP%\ExtensionOverlapTests\` en ruimt die daarna op.

## 7. Analysis: van exports naar overlap

`Analysis\` heeft geen VS nodig en werkt op de `MefExport`s uit de scanner. Vier klassen:

| Klasse | Doet |
|---|---|
| `FeatureCategories` | deelt een export in: inline adornment, tekstkleuren, kronkellijnen, markeringen, outlining, Quick Info, completion, signature help, lampjes, margins |
| `ContentTypeTree` | weet welk content type van welk afstamt |
| `KnownFeatures` | wat de metadata niet weet: welke VS-providers infrastructuur zijn, en waar je een VS-functie uitzet |
| `OverlapFinder` | zoekt per categorie en content type de providers van twee of meer eigenaren |

### Indelen

Bij de meeste contracten is de categorie het contract zelf: `IAsyncQuickInfoSourceProvider` en het oude `IQuickInfoSourceProvider` zijn allebei Quick Info. Oud en nieuw tellen als dezelfde categorie, want in de tooltip zie je ze allebei.

Bij een tagger (`IViewTaggerProvider`, `ITaggerProvider`) zegt het contract niets: een tagger kan van alles. De categorie komt dan uit `[TagType]`. `IntraTextAdornmentTag` is iets tussen de tekst, `IErrorTag` een kronkellijn, `IClassificationTag` een tekstkleur. De vergelijking gaat op korte naam, zodat zowel de interface (`IErrorTag`) als de klasse (`ErrorTag`) meetelt. Een tagger met twee tag types staat in twee categorieën.

Margins zijn een apart geval. Twee margins aan de onderkant zitten elkaar niet in de weg, maar een margin links en een links wel. `Provider.SubKey` is daarom de `[MarginContainer]`, en alleen margins in dezelfde container worden vergeleken.

### De content type-boom

VS definieert content types als velden:

```csharp
[Export] [Name("XAML")] [BaseDefinition("code")]
internal static ContentTypeDefinition XamlContentType;
```

`ContentTypeTree.FromExports` haalt die uit de scan. Gemeten in VS 2026:

| Content type | Basis | Gedefinieerd in |
|---|---|---|
| `XAML` | `code`, `code-languageserver-base` | `Microsoft.VisualStudio.LanguageServices.Xaml.dll` en de XAML language service |
| `code` | `text` | `Microsoft.VisualStudio.Platform.VSEditor.dll` |
| `text` | `any` | idem |
| `css` | `projection`, `text` | de web-tools |
| `XML` | (niet gevonden) | |

Let op de eerste regel: dat XAML een `code` is, staat in een andere DLL dan de XAML-editor zelf. De eerste versie van de test zocht in de verkeerde DLL en faalde. `XML` heeft geen MEF-definitie: dat content type komt uit de oude registratie van taaldiensten. Voor de complete boom vraagt de extensie straks VS zelf (`IContentTypeRegistryService`); de boom uit de metadata is genoeg voor de tests en voor wat MEF definieert.

`IsOfType` loopt de basistypes af met een stapel en een lijst van bezochte types. Zo hangt hij niet als iemand een kring definieert (A is een B, B is een A). Namen zijn hoofdletterongevoelig, net als in VS.

### Overlap zoeken

Per categorie (en per margin-container) is elk content type dat een provider noemt een **doel**. Voor elk doel verzamelt `OverlapFinder` de providers die daar werken. Zijn dat er van twee of meer eigenaren, en is er minstens één extensie bij, dan is het een overlapgroep.

Wanneer werkt een provider in een doel? Hier zat de belangrijkste keuze:

- **Een extensie** werkt in elk content type dat afstamt van een van zijn eigen types. Color Picker Tool registreert voor `text` en tekent ook in XAML.
- **Een VS-provider** telt alleen waar VS hem bij naam registreert. VS heeft tientallen algemene providers op `text` en `code` (markeringen, spellingcontrole, URL's). Die horen bij de editor zelf. Zou je ze via de boom meetellen, dan overlapt elke extensie overal met VS.

Daarna vallen dubbele groepen weg: heeft `code` precies dezelfde providers als `text`, dan zegt `text` het al.

Infrastructuur (`IntraTextAdornmentTaggerProvider` en `OutliningAdornmentManagerFactory` van de editor) blijft standaard buiten beeld.

### Nameting op de laptop

Met de gebouwde DLL, op VS 2026 en de 63 extensiemappen die VS kent: 240 manifesten, 7.885 exports, 323 providers in een categorie. De eerste versie (VS-providers via de boom) gaf 123 groepen. Met de regel hierboven: 73. Echte vondsten:

| Content type | Categorie | Wie |
|---|---|---|
| XAML | inline adornment | VS (2 taggers), XAML Resource Preview, Color Picker Tool, Visual chatGPT Studio |
| css | inline adornment | VS (`CssColorAdornmentTaggerProvider`), Color Preview |
| Output | tekstkleuren | VS, Output enhancer, VSColorOutput64 |
| AndroidLayoutXml | inline adornment, Quick Info | VS, XAML Resource Preview (via `XML`) |

Wat nog veel ruis geeft: Comment Studio en Rainbow Braces registreren zich voor tientallen talen, en staan daardoor in bijna elke groep tekstkleuren en Quick Info. Dat is niet fout (ze doen daar echt iets), maar zo'n lijst van 73 groepen leest niet. Dat lossen we op in het venster, niet in de analyse.

### Tests

15 nieuwe tests in `AnalysisTests`: indelen per tag type en contract, de boom (afstamming, onbekende types, kringen, opbouw uit exports), en overlap: het kleurvakjesgeval zoals gemeten, alleen VS, één extensie met twee providers, ongerelateerde content types, margins per container, infrastructuur aan en uit, en de echte boom van VS 2026 als die geïnstalleerd is. Samen 30 tests.

## 8. Weergave per extensie

Een lijst per content type leest niet (73 groepen). De vraag van de gebruiker is ook een andere: welke extensie kan weg? Daarom draait `ExtensionReport` de groepen om.

**Per extensie, per andere eigenaar, per categorie één regel.** Komt Color Picker Tool VS tegen in XAML en in css, beide als inline adornment, dan is dat één regel met twee content types. De volgorde:

- binnen een extensie eerst VS, dan de andere extensies op naam;
- de extensies zelf: die met de meeste andere eigenaren bovenaan. Dat zijn de beste kandidaten om te verwijderen.

VS krijgt geen eigen regel in de lijst; die kun je niet verwijderen.

**Filter op wat je gebruikt.** `ForUsedContentTypes` houdt alleen de groepen over die raken aan de content types die je gebruikt. Een groep op `text` telt mee als je XAML gebruikt, want XAML is een `text`. Zonder lijst (geen solution open) blijft alles staan.

Met dat filter toont een regel ook de gebruikte types in plaats van de interne namen: Comment Studio registreert Quick Info op `code`, en VS de zijne op `Roslyn Languages`. Wat je wilt weten is dat het om C# en XAML gaat. `Build(groups, tree, used)` vertaalt elke groep naar de gebruikte types die eronder vallen.

Resultaat op de laptop met filter XAML en C#: 10 extensies met overlap. Bovenaan Comment Studio (7 andere eigenaren), dan XAML Resource Preview (6), Color Picker Tool en Visual chatGPT Studio (elk 4). Onderaan drie margin-extensies die alleen met VS overlappen: Document Health, Editor Info en Match Margin 2022.

In de oplevering komt er een tweede weergave bij: de groepen per content type, zoals in sectie 7, als extra filter.

## 9. De koppeling met VS en het venster

Vanaf hier draait de code in VS. Het venster opent via **View > Other Windows > Extension Overlap**.

### Package, menu-item en venster

Zelfde opbouw als het venster XAML Resources in ResourcePreview:

| Onderdeel | Waar |
|---|---|
| `ExtensionOverlapPackage : AsyncPackage` | registreert het menu-item en het venster |
| `[ProvideToolWindow(..., Window = "3AE79031-...")]` | het venster opent als tabblad naast Solution Explorer |
| `ExtensionOverlapPackage.vsct` | knop in `IDG_VS_WNDO_OTRWNDWS1` (View > Other Windows), icoon `Extension` uit de image catalog |
| `GeneratePkgDefFile` = true en een `VsPackage`-asset in het manifest | zonder `.pkgdef` weet VS niet dat het package bestaat |

Het package laadt pas als je op het menu-item klikt, of bij het starten als het venster de vorige keer open stond. Er is geen `ProvideAutoLoad`: de extensie hoeft niets te doen zolang je het venster niet gebruikt. Dat past bij het doel: een extensie die VS trager maakt, is hier niet op zijn plek.

### Welke extensies: `InstalledExtensions`

1. **Eerst de Extension Manager.** `SVsExtensionManager` geeft een object dat `IVsExtensionManagerAsync` implementeert. Die interface zit in `Microsoft.VisualStudio.ExtensionManager.dll`, en die staat niet in de SDK-pakketten. De code werkt daarom met reflection:
   - het type `SVsExtensionManager` alleen voor zijn GUID (daarop zoekt `GetServiceAsync`);
   - de interface zoeken op naam tussen de interfaces van het service-object, zodat het altijd de versie is die VS zelf geladen heeft;
   - `GetEnabledExtensionsAsync()` aanroepen, de `Task` afwachten en `Result` uitlezen;
   - eigenschappen (`InstallPath`, `Header.Name`) ook via de interfaces zoeken, omdat een klasse ze expliciet kan implementeren.
2. **Terugval.** Lukt dat niet, dan leest de code de mappen zelf: de map met gebruikersextensies (`ShellSettingsManager.GetApplicationDataFolder(ApplicationDataFolder.UserExtensions)`) tot drie niveaus diep. Drie, want een extensie die F5 in de Experimental Instance zet, staat in `<uitgever>\<naam>\<versie>`, niet in een willekeurige map. Het venster meldt dan dat de lijst ook uitgeschakelde extensies kan bevatten.
3. **VS zelf.** Alle manifesten onder `Common7\IDE` (`VSSPROPID_InstallDirectory`). Behalve een map met een willekeurige naam direct in `Common7\IDE\Extensions` (zoals `qbhos1mt.vs5`): dat is een machine-brede extensie van iemand anders. `IsVisualStudioFolder` beslist dat en is getest.

### Content types: `VsContentTypes`

- `IContentTypeRegistryService` geeft alle content types met hun basistypes, ook de types zonder MEF-definitie zoals XML. Die gaan via `extendTree` in de boom uit de metadata.
- De bestandstypen van de solution: alle extensies onder de solution-map (behalve `bin`, `obj`, `.git`, `.vs` en dergelijke, en maximaal 20.000 bestanden), en per extensie het content type via `IFileExtensionRegistryService`.

### Threads

| Stap | Thread |
|---|---|
| services ophalen, solution-map, registry uitlezen | UI |
| mappen doorlopen, bestanden tellen, DLL's lezen, overlap zoeken | achtergrond (`await TaskScheduler.Default`) |
| de boom tekenen | UI |

Een nieuwe lading (knop Refresh) annuleert de vorige via een `CancellationTokenSource`. `AssemblyScanCache` onthoudt per DLL het resultaat, zolang grootte en wijzigingsdatum gelijk blijven. Een tweede keer openen is daardoor snel. Refresh leegt de cache.

Twee meldingen van de analyzers bij de eerste build:

- **VSSDK006**: controleer of `GetService` null teruggeeft. Nu `as IVsShell ?? throw ...` in plaats van een harde cast.
- **VSTHRD010** op `_onlySolution.Click += (s, e) => Draw();`. De analyzer kijkt per lambda, dus de lambda begint nu zelf met `ThreadHelper.ThrowIfNotOnUIThread()`.

En een compileerfout: `await TaskScheduler.Default` werkt alleen met `using Microsoft.VisualStudio.Threading;`. Die levert de `GetAwaiter` voor een `TaskScheduler`.

### Testen in de Experimental Instance

`MSBuild ... -p:DeployExtension=true` zet de extensie in de Exp-hive. De eerste keer meldt de build `VSSDK1031: Extension ... could not be found`: de bestanden staan er wel, maar de Exp-instance kent de extensie pas na de eerste start. Na een keer starten verdwijnt de melding.

Let op: de Experimental Instance heeft zijn eigen extensies. Daar zie je dus vooral overlap met VS zelf. Voor je echte situatie installeer je de `.vsix` in je gewone VS.

### Tests

`OverlapScanTests` (3 tests): twee nep-extensies met een kopie van de testassembly geven overlap, met de naam uit het manifest of uit de Extension Manager; de cache geeft hetzelfde resultaat tot het bestand verandert; en welke mappen van VS zijn. Samen 39 tests.

## Volgende stappen

1. Testen in de Experimental Instance en in de gewone VS.
2. Vertalingen (14 talen), Opties, de wezen, de weergave per content type.
