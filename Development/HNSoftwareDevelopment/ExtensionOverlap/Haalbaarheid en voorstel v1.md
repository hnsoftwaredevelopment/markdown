# Extension Overlap: haalbaarheid en voorstel v1

Onderzoek op 12 november 2026, op nb1164. Nog geen code voor de extensie; wel een proof of concept (PoC) om de aannames te testen. De PoC staat in `%TEMP%\overlap-research\` en is de basis voor de scanner in v1.

## Kort antwoord

| Vraag | Antwoord |
|---|---|
| Extensies en hun MEF-assemblies vinden? | Ja. In VS via `IVsExtensionManagerAsync.GetEnabledExtensionsAsync()`: alleen ingeschakelde extensies, met installatiemap en assets. Manifesten zelf lezen werkt ook, maar geeft te veel (oude versies, uitgeschakelde extensies). |
| Exports lezen zonder te laden? | Ja. `System.Reflection.Metadata` leest 319 DLL's in 1,0 tot 1,5 seconde, zonder één assembly te laden. |
| Ingebouwde VS-functies herkennen? | Ja, met dezelfde scan op de DLL's van VS. De twee kleurvakjes-taggers van VS komen er direct uit. De plek om ze uit te zetten staat niet in de metadata; daarvoor is een eigen tabel nodig. |
| Waar tonen? | Een tool window, met een knop om het resultaat als Markdown-rapport te kopiëren. |

## Wat er op de laptop staat

`vswhere -all -prerelease` vindt twee installaties:

| Instance | Versie | Product |
|---|---|---|
| `3fdcf796` | 18.13 (VS 2026 Insiders) | Community |
| `b634e2df` | 16.11 (VS 2019) | Professional |

Er staat geen VS 2022 op de laptop. De mappen `17.0_...` in `%LocalAppData%\Microsoft\VisualStudio` zijn resten van eerdere installaties. Daarom is het minimum VS 2026; zie "Besluiten".

## 1. Geïnstalleerde extensies vinden

### Waar ze staan

| Soort | Map | Op deze laptop |
|---|---|---|
| Per gebruiker | `%LocalAppData%\Microsoft\VisualStudio\18.0_3fdcf796\Extensions\<willekeurig>\` | 81 extensies, 40 met een `MefComponent` |
| Experimental Instance | `...\18.0_3fdcf796Exp\Extensions\` | 2 |
| Machine-breed, van derden | `<installatiemap>\Common7\IDE\Extensions\<willekeurig>\` | o.a. XAML Styler in `qbhos1mt.vs5` |
| Van VS zelf | `Common7\IDE\CommonExtensions\...` en `Common7\IDE\Extensions\Microsoft\...` | 177 manifesten met samen 309 `MefComponent`-assets |

De naam van de hive is `<hoofdversie>_<instanceId>`. Die instanceId is dezelfde als in `vswhere`. Een extensie in VS weet zelf in welke hive hij draait, dus dat hoef je niet te raden.

Elke map heeft een `extension.vsixmanifest`. De regel die telt:

```xml
<Asset Type="Microsoft.VisualStudio.MefComponent" Path="RainbowBraces.dll" />
```

Zonder die regel heeft een extensie geen MEF-onderdelen. CodeMaid en Productivity Power Tools hebben alleen een `VsPackage`-asset: die doen hun werk via commands en het package, niet via de editor-MEF.

### Valkuil: de mappen geven te veel

Mappen scannen leverde dubbelingen op:

- Rainbow Braces staat er drie keer: twee keer 1.0.172 en één keer 1.0.176.
- Productivity Power Tools Options Page drie keer, Markdown Lint, EasyFilePath en Code Mind Map elk twee keer.

VS laat oude versies staan tot een opruimronde, en een uitgeschakelde extensie blijft gewoon in zijn map. Wie alleen mappen leest, meldt dus overlap die er niet is.

### De oplossing in VS: de Extension Manager vragen

VS 2026 heeft de service `SVsExtensionManager` met de interface `IVsExtensionManagerAsync` (in `PrivateAssemblies\Microsoft.VisualStudio.ExtensionManager.dll`). Die heeft:

```csharp
GetInstalledExtensionsAsync()
GetEnabledExtensionsAsync()
GetExtensionByIdAsync(...)
```

Elke extensie is een `IInstalledExtension` (in `Microsoft.VisualStudio.ExtensionEngineContract.dll`) met onder meer:

| Eigenschap | Waarvoor |
|---|---|
| `InstallPath` | de map met de DLL's |
| `State` | `Enabled`, `Disabled`, `PendingDisable`, `PendingEnable`, ... |
| `InstalledPerMachine` | per gebruiker of machine-breed |
| `Header.Name`, `Header.Identifier`, `Header.Version` | naam en id voor het rapport |
| `Header.SystemComponent`, `Header.InstalledByMsi` | onderdeel van VS zelf |
| `Content` | de assets: `ContentTypeName` = `Microsoft.VisualStudio.MefComponent`, `RelativePath` = de DLL |

Dit is dezelfde bron als het venster Manage Extensions. Je krijgt precies de versie die VS gebruikt, en alleen wat ingeschakeld is.

Let op: deze API is niet officieel gedocumenteerd. De types heb ik uitgelezen uit de DLL's van VS 2026. Een volgende VS-versie kan hem wijzigen. Als terugvaloptie leest de extensie de manifesten zelf; dat werkt al in de PoC.

## 2. MEF-exports lezen zonder de assembly te laden

### Hoe het werkt

Een .NET-DLL bevat naast code een metadata-tabel: welke types er zijn, welke attributen erop staan en met welke waarden. `System.Reflection.Metadata` leest die tabel als bytes. Er komt geen code in het geheugen die kan draaien, en de DLL wordt niet geladen in het AppDomain van VS.

```csharp
using var pe = new PEReader(File.OpenRead(path));
var md = pe.GetMetadataReader();
foreach (var th in md.TypeDefinitions)
{
    var type = md.GetTypeDefinition(th);
    foreach (var ah in type.GetCustomAttributes())
    {
        var attr = md.GetCustomAttribute(ah);
        // Name of the attribute class, e.g. "ContentTypeAttribute"
        // Values: attr.DecodeValue(provider)
    }
}
```

`DecodeValue` heeft een `ICustomAttributeTypeProvider` nodig: een klasse die zegt hoe je een type weergeeft. In de PoC is dat gewoon een string. Dat werkt omdat `typeof(IntraTextAdornmentTag)` in een attribuut niet als type wordt opgeslagen, maar als tekst: `"Microsoft.VisualStudio.Text.Editor.IntraTextAdornmentTag, Microsoft.VisualStudio.Text.UI.Wpf, ..."`. Er hoeft dus niets opgezocht of geladen te worden.

### Resultaat van de PoC

Alle 319 MEF-DLL's (VS zelf plus de extensies per gebruiker): 1,0 tot 1,5 seconde, 8.876 geëxporteerde klassen, geen fouten. Voor jouw eigen extensie:

```
ResourcePreview.Editor.ColorSwatchTaggerProvider
  [Export("Microsoft.VisualStudio.Text.Tagging.IViewTaggerProvider")]
  [ContentType("XAML")]
  [ContentType("XML")]
  [TagType("Microsoft.VisualStudio.Text.Editor.IntraTextAdornmentTag")]
ResourcePreview.QuickInfo.ResourceQuickInfoSourceProvider
  [Export("Microsoft.VisualStudio.Language.Intellisense.IAsyncQuickInfoSourceProvider")]
  [Name("XAML Resource Preview Quick Info")]
  [ContentType("XAML")]
  [ContentType("XML")]
```

Rainbow Braces laat zien waarom je naar het contract kijkt en niet naar de klassenaam: de klasse heet `CreationListener`, maar is een `IViewTaggerProvider` voor `IClassificationTag` in 24 content types.

### Wat de PoC nog niet doet

| Beperking | Gevolg | Aanpak in v1 |
|---|---|---|
| Alleen attributen op klassen | Exports op velden en properties ontbreken, zoals `AdornmentLayerDefinition`, `EditorFormatDefinition` en `ContentTypeDefinition` | Ook velden, properties en methoden langslopen |
| Eigen export-attributen | Roslyn gebruikt `[ExportCompletionProvider]` en dergelijke, afgeleid van `ExportAttribute` | Voor v1 negeren: dat zijn Roslyn-interne onderdelen, geen editor-functies. Later: de basisklasse volgen in de metadata van de andere DLL, ook alleen lezend |
| Enum-waarden in attributen | Het onderliggende type van een enum uit een andere DLL is onbekend | Aannemen dat het `Int32` is; dat geldt voor vrijwel alle enums |
| Content type-hiërarchie | Editor Info registreert zijn margins voor `text`, en `text` geldt voor elk tekstbestand | In VS `IContentTypeRegistryService` vragen: `XAML.IsOfType("text")` |
| VisualStudio.Extensibility (nieuw model) | Die extensies gebruiken geen MEF en draaien buiten VS | In v1 tonen als "niet geanalyseerd" |

### Veiligheid

- Alleen `PEReader` en `MetadataReader`. Nooit `Assembly.Load`, `LoadFrom`, `ReflectionOnlyLoad` of `MetadataLoadContext`.
- Een kapot of geen .NET-bestand geeft `BadImageFormatException` of `HasMetadata == false`. Overslaan en melden.
- Bestanden openen met `FileShare.ReadWrite | FileShare.Delete`, zodat VS en de installer niet geblokkeerd worden.
- Geen waarde uit een attribuut uitvoeren of als pad gebruiken zonder controle.

### Welke versie van System.Reflection.Metadata

VS laadt zelf al `System.Reflection.Metadata`. VS 2026 stuurt in `devenv.exe.config` elke versie tot 10.0.0.14 door naar zijn eigen 10.0.0.14. De extensie levert die DLL dus niet mee in de VSIX, en compileert tegen een versie die niet hoger is dan wat VS 2026 meebrengt.

### Afgewezen: de MEF-cache van VS lezen

In `ComponentModelCache` staat wat VS bij het opstarten gecomponeerd heeft (`Microsoft.VisualStudio.Default.catalogs`, 5,7 MB). Dat zou precies de actieve onderdelen geven, ook die op velden. Getest met de eigen `Microsoft.VisualStudio.Composition.dll` van VS: laden duurde 7 tot 23 seconden en gaf een lege catalogus. Het formaat is intern en verandert per versie. Niet bruikbaar.

## 3. Ingebouwde VS-functies herkennen

### Ze komen uit dezelfde scan

VS is zelf grotendeels een verzameling MEF-onderdelen. De scan van de VS-DLL's vindt in `CommonExtensions\Microsoft\XamlLanguageService\Microsoft.VisualStudio.DesignTools.XamlLanguageService.dll`:

```
XamlLocalColorAdornmentTaggerProvider     IViewTaggerProvider  XAML  IntraTextAdornmentTag
XamlResourceColorAdornmentTaggerProvider  IViewTaggerProvider  XAML  IntraTextAdornmentTag
```

Dat zijn de kleurvakjes van VS: één voor letterlijke kleuren, één voor resources. Precies dezelfde handtekening als `ColorSwatchTaggerProvider` in ResourcePreview.

Alles groeperen per content type `XAML`, contract en tag type, en alleen tonen waar twee of meer DLL's in een groep zitten:

| Groep | Wie |
|---|---|
| inline adornments (`IntraTextAdornmentTag`) | VS: `XamlLocalColorAdornmentTaggerProvider`, `XamlResourceColorAdornmentTaggerProvider`; ResourcePreview: `ColorSwatchTaggerProvider` |
| completion (`ICompletionSourceProvider`) | VS: `XamlCompletionSourceProvider`; ResourcePreview |
| lampjes (`ISuggestedActionsSourceProvider`) | VS: Copilot "Fix with Copilot", Roslyn; ResourcePreview |
| `IWpfTextViewCreationListener` | VS; ResourcePreview |
| `ICommandHandler` | 5 van VS en Roslyn |

De eerste regel is het kleurvakjesprobleem, automatisch gevonden. De laatste twee laten zien dat niet elke groep een probleem is: een creation listener tekent niets, en VS heeft altijd veel command handlers. v1 werkt daarom met vaste categorieën (zie hieronder) en verbergt groepen zonder zichtbaar effect.

Quick Info voor XAML staat niet in de lijst. VS registreert die waarschijnlijk op een bovenliggend content type. Dat is precies wat de content type-hiërarchie in v1 oplost.

### Waar zet je het uit?

Dat staat niet in de metadata. Twee bronnen:

**VS-functies: een eigen tabel.** Een JSON-bestand in de extensie, per bekende provider:

```json
{
  "provider": "Microsoft.VisualStudio.DesignTools.Xaml.LanguageService.LanguageService.Adornments.XamlLocalColorAdornmentTaggerProvider",
  "feature": "Inline color previews (XAML)",
  "setting": "languages.xaml.advanced.showInlineColorPreviews",
  "path": "Languages > XAML > Advanced > Show inline color previews"
}
```

De moniker `languages.xaml.advanced.showInlineColorPreviews` komt uit `CommonExtensions\Microsoft\DesignTools\Settings\XamlDesignerSettings.registration.json`. Met `ISettingsManager` (dezelfde API als in ResourcePreview, sectie 10) leest de extensie de huidige waarde. Het rapport kan dus zeggen: "staat aan". VS heeft 62 van die `registration.json`-bestanden; die kun je doorzoeken bij het aanvullen van de tabel. Voor v1 begin ik met een handvol bekende functies.

**Extensies: automatisch.**
- Altijd: Extensions > Manage Extensions > uitschakelen.
- Vaak: de eigen Opties-pagina van de extensie. Die staat in de `.pkgdef` (`ToolsOptionsPages`) of in een `registration.json` met `ProvideSettingsManifest`. Beide zijn tekst en staan in de installatiemap.

Dat een extensie een instelling heeft, betekent niet dat die instelling deze ene functie uitzet. Het rapport zegt dus "Opties-pagina: Extra > Opties > XAML Resource Preview", niet "zet X uit".

## 4. Waar het resultaat tonen

Een tool window: **View > Other Windows > Extension Overlap**, net als het venster XAML Resources.

```
XAML
├─ Inline adornments (3)                         ⚠ overlap
│  ├─ Visual Studio: Inline color previews        staat aan · Languages > XAML > Advanced
│  ├─ Visual Studio: Resource color previews      staat aan · Languages > XAML > Advanced
│  └─ XAML Resource Preview: ColorSwatchTagger    Extra > Opties > XAML Resource Preview
├─ Completion (2)                                 ⚠ overlap
└─ Lampjes (3)                                    ⚠ overlap
CSharp
└─ ...
```

- Filters: alleen overlap, VS-functies verbergen, zoeken op extensie.
- Dubbelklik op een regel opent de Opties-pagina of Manage Extensions.
- Knop "Kopieer als Markdown": hetzelfde als rapport, handig voor een GitHub-issue bij een andere extensie.
- Het content type van het actieve document staat bovenaan, uitgeklapt.

Waarom geen los rapport als eerste? Het venster kan de huidige instellingen tonen en de Opties openen. Een rapport is een momentopname; dat komt er als export bij.

## Voorstel v1

### Wat erin zit

1. Ingeschakelde extensies ophalen via `IVsExtensionManagerAsync`; terugval op manifesten lezen.
2. Elke `MefComponent`-DLL van die extensies en van VS zelf lezen met `System.Reflection.Metadata`, op een achtergrondthread, met een cache per DLL op basis van pad, grootte en wijzigingsdatum.
3. Content types uitbreiden met hun bovenliggende types via `IContentTypeRegistryService`.
4. Indelen in categorieën:

| Categorie | Herkend aan |
|---|---|
| Inline adornments (kleurvakjes, inlay hints) | tagger met `IntraTextAdornmentTag` |
| Tekstkleuren | tagger met `IClassificationTag`, `IClassifierProvider` |
| Fout- en kronkellijnen | tagger met `IErrorTag` |
| Quick Info | `IAsyncQuickInfoSourceProvider`, `IQuickInfoSourceProvider` (oud) |
| Completion | `IAsyncCompletionSourceProvider`, `ICompletionSourceProvider` (oud) |
| Lampjes | `ISuggestedActionsSourceProvider` |
| Margins | `IWpfTextViewMarginProvider`, per `MarginContainer` |
| Outlining | tagger met `IOutliningRegionTag` |

   Oud en nieuw tellen als dezelfde categorie: twee Quick Info-bronnen tonen ook dubbel als de ene de oude API gebruikt.
5. Tabel met bekende VS-functies en hun instelling; huidige waarde lezen met `ISettingsManager`.
6. Verweesde extensiemappen melden (zie hieronder).
7. Tool window plus Markdown-export.
8. Strings.resx in 15 talen, instellingen in beide Opties-vensters (bijvoorbeeld: "VS-functies standaard verbergen", "alleen overlap tonen").

### Verweesde extensiemappen

Het doel van de extensie is aanwijzen wat weg kan: minder extensies betekent een sneller VS en snellere updates. Mappen die VS niet meer gebruikt, horen daarbij. Ze kosten geen opstarttijd, wel schijfruimte.

**Wat de nameting liet zien.** Van de 83 mappen in `18.0_3fdcf796\Extensions\` staan er 20 (135 MB) niet in de extensielijst van VS (`ExtensionMetadata2.0.mpack`). Bijna alle zijn op 8 en 15 juni 2026 aangemaakt, waarschijnlijk bij het overzetten van extensies naar VS 2026. Bij Rainbow Braces en Productivity Power Tools Options Page kent VS één van de drie mappen, de nieuwste; bij acht andere extensies kent VS geen van beide mappen. Herbert laat ze bewust staan als testgeval voor deze functie.

**Hoe de extensie ze vindt.** Alle mappen in `Extensions\` van de eigen hive, min de `InstallPath`'s uit `GetInstalledExtensionsAsync()` (alle geïnstalleerde, ook uitgeschakelde). Wat overblijft is wees. Niet het `.mpack`-bestand gebruiken: dat is een intern formaat; de nameting zocht er alleen tekst in.

**Valkuil.** Een extensie die net is geïnstalleerd of bijgewerkt, telt pas na een herstart van VS echt mee. Een map die nieuwer is dan de start van VS wordt daarom nooit als wees gemeld, en een map met een openstaande wijziging (`PendingEnable`, `PendingDisable`) ook niet.

**Wat het venster toont.** Per wees: naam en versie uit het manifest, datum, grootte, en of er een geïnstalleerde versie van dezelfde extensie is ("oude versie van Rainbow Braces 1.0.176") of niet ("restant van een verwijderde extensie"). Knoppen: map openen in Verkenner, en naar de Prullenbak verplaatsen na bevestiging. Prullenbak en niet definitief verwijderen, zodat je een vergissing kunt herstellen.

**Later.** Hele hives van VS-installaties die niet meer bestaan. Op deze laptop zijn dat vijf mappen `17.0_...`, terwijl `vswhere` geen VS 2022 meer vindt. Die liggen buiten de eigen hive, dus voorzichtiger: alleen melden, niet opruimen.

### Wat er niet in zit

- Commands en sneltoetsen. Die staan in de gecompileerde `.vsct` (de `.cto` in de DLL-resources) en vragen een eigen lezer. Kandidaat voor v2.
- Extensies in het nieuwe VisualStudio.Extensibility-model analyseren.
- Roslyn-analyzers en code fixes (die zitten in de lampjes, maar via Roslyn's eigen registratie).
- Zelf iets uitzetten. De extensie wijst de plek aan; jij beslist.

### Opbouw van de repo

Overgenomen van ResourcePreview:

```
ExtensionOverlap/
├─ Directory.Build.props            ← output naar Builds\<project>\
├─ ExtensionOverlap.sln
├─ src/ExtensionOverlap/            ← VSIX, net48
│  ├─ Scanning/                     ← metadata lezen, geen VS-code, getest
│  ├─ Analysis/                     ← categorieën, groeperen, bekende VS-functies (JSON)
│  ├─ VisualStudio/                 ← Extension Manager, content types, instellingen lezen
│  ├─ ToolWindow/
│  ├─ Localization/                 ← Strings.resx + 14 vertalingen
│  └─ Options/                      ← registration.json + oude Opties-pagina
├─ tests/ExtensionOverlap.Tests/    ← MSTest, net48
├─ tests/Fixtures/                  ← kleine DLL's met bekende exports, als testdata
├─ tools/build-and-test.ps1
├─ publishManifest.json, README.md, CHANGELOG.md
└─ .github/workflows/release.yml    ← zet ik in obj\, jij kopieert
```

`Scanning` en `Analysis` hebben geen VS nodig. De tests bouwen een fixture-DLL met bekende `[Export]`-attributen en controleren wat de scanner eruit haalt, plus enkele overlap-gevallen. Eén extra test scant de echte `XamlLanguageService.dll` als die op de machine staat, en slaat over als hij er niet is (zodat de build in GitHub Actions blijft werken).

## Besluiten (12 november 2026)

1. **Minimum is VS 2026.** `InstallationTarget Version="[18.0,19.0)"`. Daarmee vervalt de controle op VS 2022: `IVsExtensionManagerAsync` is in VS 2026 aanwezig, en de extensie compileert tegen de `System.Reflection.Metadata` die VS 2026 zelf meebrengt (en levert die niet mee in de VSIX). Dit wijkt af van ResourcePreview, dat ook 17.14 ondersteunt.
2. **Naam: ExtensionOverlap.** Lokaal `C:\DevOps\hnsoftwaredevelopment\ExtensionOverlap`, op GitHub `hnsoftwaredevelopment/ExtensionOverlap`. Herbert maakt de map en de GitHub-repository aan.
3. **Color Picker Tool** wordt opnieuw geïnstalleerd. Daarna draait de scan nog een keer, zodat er een voorbeeld is met twee extensies en VS.

Let op bij de build: in `C:\DevOps\hnsoftwaredevelopment` staat al een `Directory.Build.props` die de output naar `<repo>\Builds\<project>\` stuurt. De repo krijgt toch een eigen `Directory.Build.props` (zoals ResourcePreview), want in GitHub Actions bestaat die bovenliggende map niet. MSBuild neemt de dichtstbijzijnde, dus de eigen wint.

## Nameting met Color Picker Tool (12 november 2026)

Na het opnieuw installeren van Color Picker Tool 3.3.0.3 draaide de scan nog een keer: 321 DLL's in 1,1 seconde. Color Picker Tool registreert:

```
ColorPickerTool.TagAdornment.ColorPickerAdornmentTaggerProvider
  [Export(IViewTaggerProvider)]
  [ContentType("code")] [ContentType("text")] [ContentType("projection")]
  [TagType(IntraTextAdornmentTag)]
```

Hij staat dus niet in de groep XAML, maar in de groep `text`. Groeperen op de letterlijke naam van het content type mist hem, terwijl hij in een .xaml-bestand wel vakjes tekent. Dat bewijst dat de content type-hiërarchie (`IContentTypeRegistryService`) in v1 nodig is: een registratie op `text` of `code` geldt ook voor XAML.

De groep `text` met `IntraTextAdornmentTag` laat ook zien dat één categorie verschillende dingen bevat:

| Provider | Wat het tekent |
|---|---|
| VS: `IntraTextAdornmentTaggerProvider`, `OutliningAdornmentManagerFactory` | infrastructuur van de editor, geen zichtbare functie op zich |
| Color Picker Tool: `ColorPickerAdornmentTaggerProvider` | kleurvakjes |
| Visual chatGPT Studio: `GhostTextTaggerProvider` | grijze voorgestelde tekst |

De scanner weet niet wat een adornment tekent. Gevolgen voor v1:

- Een lijst met bekende infrastructuur-providers van VS, die standaard verborgen zijn.
- De categorie "Inline adornments" toont alle kandidaten; jij ziet aan de naam welke kleurvakjes zijn. Het venster zegt dus "deze vier kunnen iets tussen de tekst zetten in XAML", niet "deze vier tekenen kleurvakjes".

Ook gevonden: **Color Preview** (`EditorColorPreview.dll`) tekent kleurvakjes voor `css` en `typescript`. Dat raakt XAML niet.

## Open punten

1. **Opties openen op een moniker.** Of je het nieuwe Opties-venster vanuit code op een bepaalde instelling kunt openen, weet ik nog niet. Zo niet, dan toont v1 het pad als tekst.

## Volgende stap

Zodra de map er is: de opbouw van ResourcePreview overnemen en beginnen met `Scanning` plus de tests. Daarna `Analysis`, dan de VS-koppeling, dan het venster.
