# XAML Resource Preview

Visual Studio-extensie die een preview toont als je in XAML over `{StaticResource X}` of `{DynamicResource X}` hovert. Werkt voor `Geometry`, `GeometryGroup`, `Drawing`, `DrawingImage`, `BitmapImage` (en andere `ImageSource`), `Brush` en `Color`.

Hover je over de definitie zelf (`x:Key="Renew"`), dan krijg je ook een preview.

Bij een `Style` toont de tooltip een tabel: `TargetType`, `BasedOn`, de setters met kleurvakjes en mini-iconen, de setters die uit basisstijlen komen, en de triggers.

Klik op het plaatje of op de bestandsnaam onder de preview, en VS opent het bestand met de naam in `x:Key` geselecteerd. Staat een key in meerdere bestanden, dan staan de andere definities eronder, elk als eigen link.

## Mappen

```
ResourcePreview/
├─ ResourcePreview.sln              ← de extensie
├─ src/ResourcePreview/
│  ├─ source.extension.vsixmanifest ← wat zit erin, voor welke VS-versies
│  ├─ QuickInfo/                    ← koppeling met de editor van VS
│  ├─ Resources/                    ← zoeken en XAML samenstellen (geen VS, geen WPF)
│  ├─ Preview/                      ← WPF-weergave in de tooltip
│  ├─ Navigation/                   ← bestand openen en naar x:Key springen
│  ├─ Localization/                 ← teksten per taal (Strings.resx + 14 vertalingen)
│  ├─ Options/                      ← instellingen: registration.json, SettingsService, oude Opties-pagina
│  └─ ResourcePreviewPackage.cs     ← AsyncPackage, nodig voor de Opties-pagina
├─ tests/ResourcePreview.Tests/     ← unit tests (MSTest)
└─ samples/SampleApp/               ← WPF-app om mee te testen, ook gebruikt door de tests
```

## Instellingen

Extra > Opties > XAML Resource Preview. Dat werkt in het nieuwe Opties-venster van VS 2026 en in het Legacy-venster. Beide tonen dezelfde waarden.

| Instelling | Standaard | Wat het doet |
|---|---|---|
| Taal | Automatisch | Automatisch volgt de taal van VS. Je kunt ook een vaste taal kiezen, waaronder Nederlands. |
| Maximum aantal andere definities | 5 | Hoeveel andere definities van dezelfde key als link onder de preview staan. 0 = geen lijst. |
| Tegelgrootte | 64 | Breedte en hoogte van een tegel in pixels, 16 tot 256. |
| Tegels | Licht en donker | Beide tegels, alleen de lichte of alleen de donkere. |
| Kleuren | zwart op wit, wit op #1E1E1E | Voorgrond en achtergrond per tegel. De voorgrond geldt alleen voor een `Geometry`, die zelf geen kleur heeft. |
| Live voorbeeld tonen | Aan | Een echt control met de stijl of ControlTemplate erop. Uit: alleen de setter-tabel, en bij een ControlTemplate de boom. |

Kleuren vul je in het nieuwe venster in als `#RRGGBB`, `#AARRGGBB` of een WPF-kleurnaam (`Red`, `SteelBlue`). Het Legacy-venster heeft een kleurkiezer.

De extensie vraagt minimaal VS 2022 17.14. Daarin kwam de API voor het nieuwe Opties-venster.

## Eerste keer starten

1. Open de **Visual Studio Installer**, kies **Wijzigen** bij Visual Studio 2026 en vink de workload **Visual Studio extension development** aan. Zonder die workload kan VS het project wel bouwen, maar niet openen als VSIX-project en niet debuggen.
2. Open `ResourcePreview.sln` en druk op **F5**.
3. Er start een tweede Visual Studio: de **Experimental Instance**. Die heeft eigen instellingen en eigen extensies, los van je gewone VS. De eerste keer duurt het opstarten wat langer.
4. Open daarin `samples/SampleApp/SampleApp.sln`, open `MainWindow.xaml` en hover over `Renew`, `Report` of `Warning`.

Breakpoints in de extensie werken gewoon: zet er een in `ResourceQuickInfoSource.GetQuickInfoItemAsync` en hover in de Experimental Instance.

Bouwen vanaf de command line:

```powershell
& "C:\Program Files\Microsoft Visual Studio\18\Community\Insiders\MSBuild\Current\Bin\MSBuild.exe" ResourcePreview.sln -restore -p:Configuration=Release
```

Het installeerbare bestand komt in `src\ResourcePreview\bin\Release\ResourcePreview.vsix`. Dubbelklikken installeert het in je gewone VS.

## Hoe Visual Studio de extensie laadt

### 1. Het manifest

`source.extension.vsixmanifest` beschrijft het pakket. De belangrijkste regel:

```xml
<Asset Type="Microsoft.VisualStudio.MefComponent" ... />
```

Die zegt: "deze DLL bevat MEF-onderdelen". Zonder deze regel installeert VS de extensie wel, maar laadt het je klassen nooit. Je krijgt dan geen foutmelding, er gebeurt gewoon niets.

`InstallationTarget Version="[17.14,19.0)"` betekent: VS 2022 vanaf 17.14, en VS 2026 (18.x). De vierkante haak telt mee, de ronde niet. 17.14 is het minimum omdat daar Unified Settings in zit (zie sectie 10).

### 2. MEF: VS roept jou aan

MEF (Managed Extensibility Framework) is het plugin-systeem van de VS-editor. Je schrijft een klasse, zet er `[Export]` boven, en VS vindt hem. Jij maakt nooit zelf een instantie.

In `ResourceQuickInfoSourceProvider`:

```csharp
[Export(typeof(IAsyncQuickInfoSourceProvider))]
[ContentType("XAML")]
```

Bij het opstarten leest VS alleen deze attributen (dat wordt gecachet, daarom start VS snel). Pas als je een bestand opent met content type `XAML`, maakt VS een instantie van de provider. Met `[Import]` vraag je andere onderdelen van VS op, zoals hier `ITextDocumentFactoryService` voor het bestandspad.

Verandert er iets aan je `[Export]`-attributen en ziet VS dat niet, dan zit de oude MEF-cache in de weg. Oplossing: sluit de Experimental Instance en start **Reset the Visual Studio Experimental Instance** vanuit het Startmenu (de exacte naam verschilt iets per VS-versie). Of verwijder de map `ComponentModelCache` in `%LocalAppData%\Microsoft\VisualStudio\18.0_...Exp\`.

### 3. Quick Info: de hover

Bij elke hover roept VS `GetQuickInfoItemAsync` aan op alle Quick Info-sources voor dat bestand. Elke source geeft een `QuickInfoItem` terug of `null`. VS zet alle items samen in één tooltip. Daarom zie je onze preview naast de standaard XAML-info van VS.

Een `QuickInfoItem` heeft twee delen:

- een **applicable span**: het stuk tekst waar de tooltip bij hoort. Beweegt de muis daarbuiten, dan sluit VS de tooltip.
- **content**: wat er getoond wordt.

### 4. Threads

Dit is het onderdeel waar de meeste extensies op vastlopen.

- De UI-thread van VS tekent alles. Duurt iets op die thread lang, dan hangt VS.
- Bestanden lezen en XML parsen doe je daarom op een achtergrondthread: `await TaskScheduler.Default;` in `ResourceQuickInfoSource` regelt dat.
- WPF-objecten horen bij de thread waarop ze gemaakt zijn. Maak je een `Path` op de achtergrondthread, dan crasht de tooltip.

De oplossing is een scheiding in twee stappen:

| Stap | Thread | Klasse | Doet |
|---|---|---|---|
| 1 | achtergrond | `ResourceQuickInfoSource` | key vinden, index doorzoeken, XAML-tekst samenstellen |
| 2 | UI | `ResourcePreviewElementFactory` | `XamlReader.Parse`, `Path`/`Image` maken |

Tussen die twee zit `ResourcePreviewData`: een gewone klasse met alleen tekst.

### 5. Van data naar beeld: IViewElementFactory

VS kan zelf `string`, `ClassifiedTextElement` (gekleurde tekst) en `ContainerElement` (meerdere onderdelen onder elkaar) tonen. Voor `ResourcePreviewData` weet VS dat niet. Dan zoekt het via MEF een factory:

```csharp
[Export(typeof(IViewElementFactory))]
[TypeConversion(from: typeof(ResourcePreviewData), to: typeof(UIElement))]
```

Zo heeft de Quick Info-source geen WPF nodig, en de factory geen kennis van bestanden. De tekst in de tooltip (type, key, bestandsnaam) is een `ClassifiedTextElement`. Die kleurt VS automatisch volgens het actieve thema.

### 6. Naar de definitie springen

Twee soorten klikbare onderdelen:

- **De bestandsnaam.** Een `ClassifiedTextRun` kan een `navigationAction` meekrijgen. VS tekent die run dan als link en voert de `Action` uit bij een klik. Roslyn gebruikt hetzelfde voor links in C#-tooltips.
- **Het plaatje.** `PreviewRenderer` hangt een `MouseLeftButtonUp`-handler aan de tegels. Het paneel krijgt `Background = Transparent`, anders vangt de lege ruimte tussen de tegels geen klikken op.

`DefinitionNavigator` doet de rest. Hier kom je de twee API-werelden van VS tegen:

| Wereld | Herkenbaar aan | Waarvoor |
|---|---|---|
| Shell (COM, oud) | `IVs...`: `IVsWindowFrame`, `IVsTextView`, `IVsStatusbar` | vensters, documenten openen, statusbalk |
| Editor (beheerd, nieuw) | `IWpfTextView`, `ITextSnapshot`, `SnapshotSpan` | tekst, selectie, cursor, scrollen |

Een document openen kan alleen via de shell (`VsShellUtilities.OpenDocument`). De cursor verplaatsen gaat het makkelijkst via de editor-API. `IVsEditorAdaptersFactoryService` is de brug: je geeft een `IVsTextView` en krijgt de bijbehorende `IWpfTextView`.

Het verloop van een klik:

1. `session.DismissAsync()` sluit de tooltip. Anders blijft hij hangen boven het andere bestand.
2. `VsShellUtilities.OpenDocument(..., LOGVIEWID.TextView_guid, ...)` opent het bestand in de teksteditor, of activeert het tabblad als het al open is.
3. `GetWpfTextView` geeft de editor-view.
4. De regel en kolom van `x:Key` komen uit de index (`IXmlLineInfo` op het attribuut). In die regel zoeken we `"Renew"` op, selecteren de naam en scrollen hem naar het midden.
5. Gaat er iets mis, dan verschijnt een melding in de statusbalk van VS (`SVsStatusbar`).

De services komen via MEF binnen in `ResourceQuickInfoSourceProvider`:

```csharp
[Import] internal SVsServiceProvider ServiceProvider { get; set; }
[Import] internal IVsEditorAdaptersFactoryService EditorAdaptersFactoryService { get; set; }
[Import] internal JoinableTaskContext JoinableTaskContext { get; set; }
```

### 7. Threading-analyzers

Het VS SDK-pakket bevat analyzers die threadingfouten melden tijdens het bouwen. Twee die je hier tegenkomt:

- **VSSDK007**: je start een async taak en wacht er niet op. Faalt hij, dan merk je daar niets van. `.FileAndForget("ResourcePreview/...")` maakt het "niet wachten" expliciet, en VS logt fouten onder die naam.
- **VSTHRD010**: je roept iets aan dat de UI-thread nodig heeft, vanaf een thread waar dat niet zeker is. Code die met `IVs...`-interfaces werkt, begint daarom met `ThreadHelper.ThrowIfNotOnUIThread()` of met `await SwitchToMainThreadAsync()`.

De analyzer werkt per methode en kan niet alles zien. In `ResourceQuickInfoSource` maken we op de achtergrondthread een `Action` die VS later op de UI-thread uitvoert. De analyzer denkt dat die methode de UI-thread nodig heeft en markeert de hele keten tot en met `GetQuickInfoItemAsync`. Dat is een valse melding. Die onderdrukken we met `#pragma warning disable VSTHRD010` op alleen die twee regels, met uitleg erbij. Onderdruk nooit het hele bestand: dan mis je echte fouten.

### 8. Package en Opties-pagina

Tot hier liep alles via MEF. Een Opties-pagina kan dat niet: die moet bij een **VS-package** horen. `ResourcePreviewPackage` is een `AsyncPackage` met één taak: de pagina Extra > Opties > XAML Resource Preview > General.

Zo vindt VS het package zonder de DLL te laden:

1. Bij het bouwen maakt de VSSDK uit de attributen (`[PackageRegistration]`, `[ProvideOptionPage]`) een `ResourcePreview.pkgdef`. Dat is tekst met registersleutels. Je vindt het in `bin\Debug`.
2. In het manifest staat een tweede asset, `Microsoft.VisualStudio.VsPackage`, die naar die `.pkgdef` wijst.
3. Bij installatie leest VS de `.pkgdef` in. VS weet dan dat de pagina bestaat en welk package erbij hoort.
4. Pas als iemand de pagina opent, laadt VS de DLL en roept het `InitializeAsync` aan.

Onze Quick Info is MEF en heeft de taalinstelling nodig voordat het package geladen is. Daarom roept `GetQuickInfoItemAsync` bij de eerste hover `ResourcePreviewPackage.EnsureLoadedAsync` aan. Die laadt het package via `IVsShell7.LoadPackageAsync`. Daarna kost het niets meer.

`GeneralOptionsPage` is een `DialogPage`. Elke publieke property wordt een regel in het eigenschappenraster, en VS bewaart de waarde zelf. Na OK gaat het event `Changed` af en wordt de taal direct opnieuw bepaald.

### 9. Meertaligheid

De teksten staan in `Localization\Strings.resx` (Engels) en `Strings.xx.resx` per taal. De build maakt van elke vertaling een **satellite assembly**: `de\ResourcePreview.resources.dll`, `ja\ResourcePreview.resources.dll`, enzovoort. De VSSDK neemt die automatisch mee in het `.vsix`-bestand.

`Localizer` kiest de taal:

| Instelling | Wat er gebeurt |
|---|---|
| Automatisch | VS vragen welke taal de interface toont (`IUIHostLocale.GetUILocale`), en de best passende van de 14 VS-talen nemen. Geen match: Engels. |
| Een vaste taal | Die taal, ook als VS iets anders toont. Nederlands kan alleen zo, want VS zelf bestaat niet in het Nederlands. |

Waarom niet gewoon `CultureInfo.CurrentUICulture`? Staat VS op "Hetzelfde als Windows" en is Windows Nederlands, dan kan die `nl-NL` zijn terwijl VS Engels toont. `IUIHostLocale` geeft de taal die VS zelf gekozen heeft.

Het matchen loopt de "ouders" van een cultuur af. VS geeft bijvoorbeeld `zh-TW` (LCID 1028), en via `zh-CHT` komt die uit bij ons `zh-Hant`. Portugees uit Portugal (`pt-PT`) matcht niet met `pt-BR` en valt terug op Engels.

Ook de Opties-pagina zelf is vertaald. `[DisplayName]`, `[Description]` en `[Category]` accepteren alleen vaste tekst. `LocalizedAttributes.cs` leidt ervan af en haalt de tekst pas op als het raster erom vraagt. De talen in de keuzelijst staan in hun eigen taal ("Deutsch", "日本語"). Dat regelt `ExtensionLanguageConverter`.

Een nieuwe tekst toevoegen:

1. Voeg hem toe aan `Strings.resx` (Engels) en maak een constante in de klasse `Strings` in `Localizer.cs`.
2. Vertaal hem in de 14 andere `.resx`-bestanden. Vergeet je er een, dan toont die taal de Engelse tekst.
3. Gebruik `Localizer.Get(Strings.Naam)` of `Localizer.Format(Strings.NaamFormat, ...)`.

Wat niet vertaalt: foutmeldingen van `XamlReader`. Die komen uit .NET en volgen de taal van Windows.

In de DLL heet de resource `VSPackage` (via `<LogicalName>` in de `.csproj`). Onder die naam zoekt VS de teksten van een package. Daardoor dienen dezelfde `.resx`-bestanden voor twee dingen:

| Wie leest | Hoe | Welke taal |
|---|---|---|
| Wij (tooltip, Legacy-pagina) | `Localizer.Get(...)` | de taalinstelling van de extensie |
| VS (nieuw Opties-venster) | `"@Naam;{package-guid}"` in `registration.json` | altijd de taal van VS zelf |
| VS (naam van Legacy-pagina) | resource-ID's `100` en `101` in `[ProvideOptionPage]` | altijd de taal van VS zelf |

Kies je als taal Nederlands terwijl VS Engels is, dan is het nieuwe Opties-venster dus Engels en de tooltip Nederlands. VS bepaalt zelf in welke taal het zijn eigen venster toont.

De vertalingen zijn niet door moedertaalsprekers gecontroleerd. Laat ze nakijken voordat je de extensie op de Marketplace zet.

### 10. Het nieuwe Opties-venster (Unified Settings)

VS 2026 heeft een nieuw Opties-venster. Een `DialogPage` verschijnt daarin niet; die zie je alleen in het Legacy-venster. Voor het nieuwe venster beschrijf je je instellingen in een JSON-bestand, en VS bouwt het venster zelf.

**`Options\registration.json`** bevat twee delen:

- `properties`: elke instelling met `type` (`string`, `integer`, `boolean`), `default`, en eventueel `minimum`/`maximum`, `enum` met `enumItemLabels` (keuzelijst), `pattern` (controle met een reguliere expressie) en `enableWhen` (alleen te wijzigen als aan een voorwaarde voldaan is).
- `categories`: de boom links in het venster.

De sleutel van een instelling heet een **moniker**: `resourcePreview.appearance.tileSize`. Het deel vóór de laatste punt is de categorie. De monikers staan ook in `SettingMonikers` in `ExtensionSettings.cs`. Die twee moeten gelijk blijven.

**Registratie.** `[ProvideSettingsManifest(PackageRelativeManifestFile = @"Options\registration.json")]` op het package zet in de `.pkgdef`:

```
[$RootKey$\SettingsManifests\{69E55270-...}]
"ManifestPath"="$PackageFolder$\Options\registration.json"
```

In de `.csproj` staat `registration.json` als `Content` met `IncludeInVSIX`, anders zit hij niet in het pakket.

**De oude pagina verbergen in het nieuwe venster.** Dat gaat in twee stappen, en ze zijn allebei nodig:

1. `legacyOptionPageId` in de categorie `resourcePreview.general` in `registration.json` is de GUID van `GeneralOptionsPage`. Daarmee weet VS dat die categorie de opvolger is van de oude pagina.
2. `IsInUnifiedSettings = true` op `[ProvideOptionPage]` zet `"IsInUnifiedSettings"=dword:00000001` in de `.pkgdef`. Pas dan toont het nieuwe venster de oude pagina niet meer als losse, tweede "XAML Resource Preview". `UnifiedSettingsCategoryMoniker` wijst naar de opvolger.

Het Legacy-venster toont de oude pagina gewoon nog. Dat ontdekte ik door de `.pkgdef` van de XAML-designer van VS te vergelijken met de onze.

**Lezen in code.** `SettingsService` vraagt de service `SVsUnifiedSettingsManager` op en krijgt een `ISettingsManager`:

```csharp
ISettingsReader reader = settingsManager.GetReader();
SettingRetrieval<int> size = reader.GetValue<int>("resourcePreview.appearance.tileSize", SettingReadOptions.NoRequirements);
if (size.Outcome == SettingRetrievalOutcome.Success) { ... size.Value ... }
```

Elke leesactie geeft een `Outcome`. `NotSupportedInClassicMode` betekent dat Unified Settings uit staat. Dan valt `SettingsService` terug op de oude `DialogPage` als opslag.

**Wijzigingen volgen.** `reader.SubscribeToChanges(callback, monikers)` roept de callback aan als iemand in het nieuwe venster opslaat. De callback kan op elke thread komen, dus `SettingsService` wisselt eerst naar de UI-thread en leest dan alles opnieuw.

**Twee vensters, één opslag.** Is Unified Settings actief, dan is `GeneralOptionsPage` alleen nog een venster op dezelfde waarden:

- `OnActivate` en `LoadSettingsFromStorage` halen de actuele waarden uit `SettingsService`.
- `SaveSettingsToStorage` schrijft via `ISettingsWriter.EnqueueChange(...)` en `RequestCommit(...)` naar Unified Settings, in plaats van naar de eigen registeropslag.

**Momentopname.** `ExtensionSettings` is onveranderlijk. Na elke wijziging maakt `SettingsService` een nieuw object en vervangt het in één keer. De tooltip leest `SettingsService.Current` op een achtergrondthread, de preview op de UI-thread. Beide zien altijd een complete set waarden, nooit een half bijgewerkte.

**Hoe ik dit uitzocht.** De documentatie van Microsoft voor extensies is hier nog mager. De bruikbaarste bronnen waren:

- de `registration.json`-bestanden van VS zelf, bijvoorbeeld `Common7\IDE\CommonExtensions\Microsoft\DesignTools\Settings\XamlDesignerSettings.registration.json`;
- de broncode van de open-source SQLFluff-extensie voor SSMS;
- de types in `Microsoft.VisualStudio.Utilities.dll` (namespace `Microsoft.VisualStudio.Utilities.UnifiedSettings`), uitgelezen via reflection.

Zoek je later iets uit, kijk dan eerst hoe VS het zelf doet.

### 11. Style-preview

Een `Style` heeft geen plaatje, dus die toont de tooltip als tabel:

```
Button · BasedOn BaseButton
Foreground   ■ White
FontSize     15
Tag          ✓ Check (GeometryGroup)
Template     ControlTemplate
inherited from BaseButton
Padding      8,4
Background   ■ AccentBrush (#FF002BBD)
Triggers (4): IsMouseOver, IsPressed, IsBusy, IsMouseOver + IsFocused
```

**Uit de XML, niet via WPF.** `StyleInfoBuilder` (in `Resources\StyleInfo.cs`) leest de stijl rechtstreeks uit de XML. Bij iconen gebruiken we `XamlReader`, maar een stijl voor een eigen control (`TargetType="{x:Type local:FancyControl}"`) zou dan niet laden, omdat VS jouw assembly niet kent. Voor een tabel met setters hoeft de stijl niet echt uitgevoerd te worden. Het resultaat is een `StyleInfo` met alleen tekst, zodat hij op de achtergrondthread gemaakt kan worden, net als de rest van de Quick Info.

**De waarde van een setter** krijgt een soort (`SetterValueKind`):

| Soort | Voorbeeld | Weergave |
|---|---|---|
| `Text` | `Value="8,4"` | de tekst |
| `Color` | `Property="Foreground" Value="White"` | kleurvakje + tekst. Alleen bij properties die op `Background`, `Foreground`, `Brush`, `Color`, `Fill` of `Stroke` eindigen, zodat `Content="Red"` gewoon tekst blijft. |
| `ResourceReference` | `Value="{StaticResource AccentBrush}"` | de resource wordt opgezocht: een brush krijgt een kleurvakje, een geometry of drawing een icoontje van 16 pixels, en het type of de kleur staat erachter |
| `Element` | `<Setter.Value><ControlTemplate>` | alleen het type. Een `SolidColorBrush` met een vaste kleur krijgt ook een kleurvakje. |

**`BasedOn`.** De builder loopt de hele keten af (`DangerButton` → `PrimaryButton` → `BaseButton`). Een property die al gezien is, is overschreven en komt er niet nog eens in, dus je ziet altijd de waarde die echt geldt. Per basisstijl komt er een tussenkopje "inherited from ...". Een kringverwijzing stopt vanzelf, omdat elke stijl maar één keer bezocht wordt. `BasedOn="{x:Type Button}"` (de impliciete stijl) staat in de kop, maar wordt niet gevolgd: die stijl heeft geen key om op te zoeken.

**Triggers.** Alleen het aantal en per trigger een naam, zodat de tooltip kort blijft:

| Trigger | Naam |
|---|---|
| `Trigger` | de property: `IsMouseOver` |
| `DataTrigger` | het binding-pad: `IsBusy`, ook bij `{Binding RelativeSource=..., Path=IsBusy}` |
| `MultiTrigger` / `MultiDataTrigger` | de condities met een plus: `IsMouseOver + IsFocused` |
| `EventTrigger` | het event: `MouseEnter` |

Het aantal telt alle triggers, maar elke naam staat er één keer in. Twee triggers op `IsMouseOver` (voor `True` en `False`) geven dus "Triggers (2): IsMouseOver". Setters binnen een trigger tellen niet als setters van de stijl, en triggers van een basisstijl tonen we niet.

**Weergave.** `StylePreviewRenderer` bouwt een `Grid` met twee kolommen. De teksten krijgen de kleur van het VS-thema via `EnvironmentColors.ToolTipTextBrushKey`, en de icoontjes ook (`TryFindResource`). Buiten VS, in de tests, is dat grijs.

### 12. Waarden: fonts, marges, hoeken, sys: en effecten

Niet elke resource is een plaatje. Voor deze types toont de preview iets anders:

| Resource | Preview |
|---|---|
| `FontFamily` | "AaBbCc 0123" in dat lettertype, normaal en vet, met de naam eronder |
| `Thickness` | een grijs vlak met blauwe randen op schaal, plus "Left 12 · Top 8 · Right 12 · Bottom 8" |
| `CornerRadius` | een rechthoek met die hoeken, plus de vier waarden |
| `sys:Double`, `sys:String`, `sys:Boolean`, `sys:Int32` | alleen de waarde: `18`, `"Opslaan"`, `True` |
| structs en enums (`FontWeight`, `Visibility`, `GridLength`, `Point`, ...) | de waarde zoals je hem in XAML schrijft: `SemiBold`, `2*` |
| `DropShadowEffect`, `BlurEffect` | een vierkantje met het effect op de licht/donker-tegels, plus de instellingen |

**Waar het zit.** `PreviewRenderer.GetVisualFactory` kent de types die op een tegel passen (geometry, drawing, brush, kleur en nu ook `Effect`). Geeft die `null`, dan probeert de renderer `ValuePreviewRenderer.TryRender`. Pas als dat ook `null` geeft, komt "No preview available". Een nieuw type toevoegen is dus: een `case` in een van die twee, en een test.

**Getallen in XAML-notatie.** `1.5` blijft `1.5`, ook als Windows op Nederlands staat. Met `1,5` zou een `Thickness` eruitzien als twee waarden. De teksten eromheen ("Links", "Boven") zijn wel vertaald.

**Grote waarden.** Een `Thickness` van 40 tekenen we niet 40 pixels dik: de dikste rand wordt 16 pixels en de rest schaalt mee. Bij `CornerRadius` is het maximum 20. De tekst toont altijd de echte waarden. Een negatieve marge (`-4`) tekenen we als 0.

**Bestaat het font?** Staat een lettertype niet op je pc, dan tekent WPF de voorbeeldtekst zonder melding in een ander font. Daarom vragen we WPF zelf of hij het fontbestand vindt (`Typeface.TryGetGlyphTypeface`). Zelf zoeken in `Fonts.SystemFontFamilies` werkt niet goed: "Segoe UI Semibold" staat daar niet in (alleen "Segoe UI"), terwijl WPF hem wel vindt. Alleen de eerste naam telt: bij `Inter, Segoe UI` is Segoe UI een bewuste terugval.

**Fonts uit je project.** `./Fonts/#Inter`, `/Fonts/#Inter`, `/MijnApp;component/Fonts/#Inter` en `pack://application:,,,/Fonts/#Inter` zet `PreviewXamlBuilder.ResolveFontFamily` om naar `file:///C:/.../Fonts/#Inter`. Let op de komma's in `,,,`: die mogen niet als scheiding tussen twee fontnamen gelden. Staat het font niet in die map, dan meldt de preview welke map hij doorzocht heeft.

**sys: uit een .NET 8-project.** In .NET 8 schrijf je `xmlns:sys="clr-namespace:System;assembly=System.Runtime"`. VS draait op .NET Framework 4.8, waar `System.Double` in `mscorlib` staat. De builder vervangt `System.Runtime`, `System.Private.CoreLib` en `netstandard` daarom door `mscorlib` (`NormalizeClrNamespace`).

### 13. Live voorbeeld en templates

**Live voorbeeld bij een Style.** Boven de setter-tabel staat een echt control met die stijl. Reageert de stijl op `IsEnabled`, dan staat er een tweede naast, met `IsEnabled="False"`. Bij `SearchBox` zie je zo meteen dat de trigger de achtergrond grijs maakt. Zonder zo'n trigger zou je twee keer hetzelfde plaatje zien; daarom komt de tweede dan niet. `HasIsEnabledTrigger` zoekt in de hele `BasedOn`-keten, in een ControlTemplate die de stijl via een setter zet, en herkent `Trigger`, `MultiTrigger`, `DataTrigger` en `MultiDataTrigger`. Het live voorbeeld is uit te zetten in de Opties. `IsMouseOver` en `IsPressed` bootsen we niet na: die zet WPF zelf op basis van de muis. Het voorbeeld is ook `IsHitTestVisible="False"`, anders reageert het op je muis in de tooltip en ziet het er elke keer anders uit.

Hoe het werkt (`LiveSampleRenderer`):

1. De stijl gaat door dezelfde `PreviewXamlBuilder` als de iconen. `BasedOn`, brushes en geometries uit andere bestanden komen dus mee.
2. `XamlReader.Parse` maakt er een echte `Style` van. `Style.TargetType` is dan een `Type`, en daar maken we met `Activator.CreateInstance` een control van.
3. `FillContent` geeft het control iets om te tonen: "Voorbeeld" als `Content`, `Text` of `Header`, twee items in een lijst, of waarde 60 bij een `Slider`.
4. `Measure` wordt meteen aangeroepen. Pas dan past WPF de template toe. Zit daar een fout in, dan vangen we die hier af. Anders gebeurt het later in de tooltip van VS en zie je niets.

Geen voorbeeld bij:

- **Eigen types** (`local:FancyControl`). VS kent je assembly niet. De tooltip zegt dat in één regel, en de tabel blijft staan.
- **`Window`, `Page`, `ToolTip`, `ContextMenu`, `Popup`.** Die mogen niet in een `StackPanel` staan. Die slaan we zonder melding over.
- **Een stijl zonder `TargetType`.** Dan weten we niet welk control we moeten maken.

**ControlTemplate.** Voor een standaard control werkt dit net zo: een `Button` met jouw template, normaal en uitgeschakeld. Zonder `TargetType` gebruiken we een `ContentControl`, zodat een `ContentPresenter` iets toont. Lukt het niet (eigen type), dan tonen we de boom hieronder, plus de reden.

**DataTemplate: de boom als tekst.** Een DataTemplate heeft data nodig. Zonder data blijft elk `{Binding}`-veld leeg en zie je een leeg kader. Daarom toont de preview wat erin zit:

```
DataType local:Book
Border
  Grid
    Path
    StackPanel
      TextBlock   x:Name = TitleText · Text = {Binding Title}
      TextBlock   Text = {Binding Author, StringFormat='door {0}'}
      TextBlock   "Boek"
```

`TemplateTreeBuilder` (in `Resources\TemplateTree.cs`) leest dit uit de XML, net als de Style-tabel. Daardoor werkt het op de achtergrondthread, en ook met eigen types. Wat we tonen en weglaten:

| Tonen | Weglaten |
|---|---|
| bindings: `{Binding}`, `{TemplateBinding}`, `{MultiBinding}` | `Margin`, `Width`, kleuren en de meeste andere attributen |
| `x:Name` en `Name` | property-elementen: `<Grid.ColumnDefinitions>`, `<Border.Background>`, `<ControlTemplate.Triggers>` |
| vaste tekst in `Text`, `Content` en `Header`, en tekst als inhoud (`<TextBlock>Boek</TextBlock>`) | `{StaticResource}` in `Text` of `Content` |

Na 20 regels of 10 niveaus diep stopt de boom, met een regel "… nog 6 elementen". `ItemsPanelTemplate` en `HierarchicalDataTemplate` tonen we ook als boom.

**Eerst controleren, dan pas laden.** Een type uit je project (`local:Book`) of uit een NuGet-pakket (`mah:MetroWindow`) kent VS niet. `XamlReader.Parse` gooit dan gegarandeerd een `XamlParseException`. Die vingen we wel op, maar de debugger van de Experimental Instance stopte er toch op. Daarom zoekt `PreviewXamlBuilder.FindUnloadableType` zulke types vooraf op, in de resource en in al zijn afhankelijkheden:

| Waar | Voorbeeld |
|---|---|
| een element | `<local:Rating />` in een template |
| een attribuut | `local:Help.Text="..."` |
| een waarde | `{x:Type local:Book}`, `{x:Static local:Icons.Save}`, `Property="local:Help.Text"`, `TargetType="local:FancyControl"` |

Of VS een namespace kan laden, beslist `IsLoadableNamespace`: WPF, `x:`, `d:`, `mc:` en `clr-namespace` met een assembly van .NET of WPF wel; `clr-namespace` zonder `assembly=` (je eigen project) en onbekende URI's niet. Een assembly die al in VS geladen is, telt ook als laadbaar.

Een valkuil onderweg: de index bewaart een losse kopie van elk element, zonder de root erboven. Daardoor staat `xmlns:local="..."` niet meer boven het element en geeft `GetNamespaceOfPrefix("local")` null. De prefixen van het bronbestand staan daarom apart in `ResourceEntry.Namespaces`.

Wordt er zo'n type gevonden, dan:

- toont een Style de tabel, met de regel "Geen live voorbeeld: local:FancyControl is geen WPF-type, dus Visual Studio kan het niet laden";
- toont een ControlTemplate de boom met diezelfde regel, en een DataTemplate alleen de boom;
- toont een andere resource "Geen preview: ..." met het type;
- krijgt een setter die naar zo'n resource verwijst geen icoontje, alleen de tekst.

`NoFirstChanceExceptionTests` bewaakt dit: elke resource uit de SampleApp gaat door de hele keten, en de test telt met `AppDomain.FirstChanceException` elke exceptie die onderweg gegooid wordt, ook als hij opgevangen wordt. Dat moet nul zijn. Voeg je een resource aan de SampleApp toe, dan test hij die automatisch mee.

Om dezelfde reden leest `ColorParser` kleuren nu zelf in plaats van via `ColorConverter.ConvertFromString`, die bij een ongeldige kleur een `FormatException` gooit.

## Hoe het zoeken werkt

VS heeft geen publieke API om te vragen waar een resource gedefinieerd is. `ResourceIndex` bouwt dat zelf op:

1. Zoek de solution-map: de eerste map boven het bestand met een `.sln` of `.slnx`. Geen gevonden, dan de root van de git-repository.
2. Lees alle `.xaml`-bestanden daaronder (behalve `bin`, `obj`, `.vs`, `.git`, `node_modules`) en onthoud elk element met een `x:Key`.
3. Een `FileSystemWatcher` houdt bij welke bestanden daarna wijzigen. Die worden bij de volgende hover opnieuw gelezen.
4. Het bestand dat open staat in de editor telt mee inclusief niet-opgeslagen wijzigingen.

### Afhankelijkheden

`Report` verwijst naar `ReportDrawingGroup`, die verwijst naar `ReportGeometry`. `PreviewXamlBuilder` zoekt die keten af en zet alles in één tijdelijke `ResourceDictionary`, de diepste eerst:

```xml
<ResourceDictionary ...>
  <Geometry x:Key="ReportGeometry">...</Geometry>
  <DrawingGroup x:Key="ReportDrawingGroup">...</DrawingGroup>
  <DrawingImage x:Key="Report" Drawing="{StaticResource ReportDrawingGroup}" />
</ResourceDictionary>
```

`StaticResource` wordt tijdens het parsen opgelost en ziet alleen wat erboven staat. Daarom is die volgorde nodig.

Aanpassingen die de builder doet voor de preview:

- `DynamicResource` wordt `StaticResource`. In een losse dictionary is er geen visual tree die een `DynamicResource` ooit oplost.
- Attributen met `d:` en `mc:` gaan eruit.
- `pack://application:,,,/Images/x.png` wordt een pad op schijf, relatief aan de projectmap.
- Font-verwijzingen (`./Fonts/#Inter`) worden een pad op schijf, zie sectie 12.
- `assembly=System.Runtime` in een `clr-namespace` wordt `assembly=mscorlib`.

## Testen

### Unit tests

`tests\ResourcePreview.Tests` bevat 413 tests die zonder Visual Studio draaien. Open Test Explorer (Test > Test Explorer) en klik op Run All. Dat duurt een paar seconden.

| Bestand | Wat het test |
|---|---|
| `ResourceReferenceFinderTests` | welke key onder de muis staat: `{StaticResource X}`, `ResourceKey=`, element-syntax, `x:Key`, nesting, net ernaast |
| `ResourceIndexTests` | parsen, regel en kolom, ongeldige XML, de solution-map vinden, zoeken over bestanden, `bin`/`obj` overslaan, live tekst uit de editor, wijzigingen op schijf |
| `PreviewXamlBuilderTests` | volgorde van afhankelijkheden, kringverwijzingen, ontbrekende keys, `DynamicResource` → `StaticResource`, pack-URI's, relatieve paden |
| `EndToEndTests` | de iconen uit `samples\SampleApp` door de hele keten tot en met `XamlReader`, en de renderer: tegels, grootte, kleuren, foutmeldingen |
| `ValuePreviewTests` | fonts (geïnstalleerd, ontbrekend, in een map), `Thickness` en `CornerRadius` met schalen, losse waarden met Nederlandse regio-instellingen, effecten, font-paden in alle schrijfwijzen, `System.Runtime` → `mscorlib` |
| `TemplateTests` | de boom (bindings, property-elementen, prefixen, maximum aan regels en diepte), het live voorbeeld bij Style en ControlTemplate, eigen types, welke controls we kunnen maken, `FillContent` per control |
| `NoExceptionTests` | welke types VS niet kan laden, in elementen, attributen en waarden, ook via afhankelijkheden; elke resource uit de SampleApp zonder één exceptie; `ColorParser` tegen alle WPF-kleurnamen |
| `StyleTests` | `TargetType` in alle schrijfwijzen, de `BasedOn`-keten met overschreven setters, de soorten waarden, triggers en binding-paden, en de weergave van de tabel |
| `SettingsAndLanguageTests` | kleuren en getallen, taalcodes van VS, de converters van de Opties-pagina, `Localizer` |
| `ConsistencyTests` | alle vertalingen hebben dezelfde keys en placeholders, elke `@Naam` in `registration.json` bestaat, monikers en standaardwaarden in C# en JSON zijn gelijk, elk `.cs`-bestand staat in de `.csproj` |

Een paar dingen die je in de tests terugziet:

- **`Sta.Run(...)`**: WPF-objecten moeten op een STA-thread gemaakt worden. MSTest draait op een MTA-thread, dus de WPF-code gaat naar een eigen thread.
- **`TempSolution`**: elke test van `ResourceIndex` krijgt een eigen tijdelijke map met een `.sln`. Omdat de index per map cachet, beïnvloeden tests elkaar niet.
- **`InternalsVisibleTo`** in `Properties\InternalsVisibleTo.cs` geeft de tests toegang tot de `internal` klassen, zonder dat die public hoeven te worden.
- **`SetCurrentForTests` en `Localizer.SetCulture`**: twee kleine ingangen om instellingen en taal te zetten zonder VS.

Een test toevoegen voor een nieuwe feature: schrijf eerst een test met een voorbeeld-XAML die laat zien wat je wilt, en bouw dan tot hij slaagt. Dat is sneller dan telkens F5 en hoveren.

Vanaf de command line:

```powershell
& "C:\Program Files\Microsoft Visual Studio\18\Community\Insiders\MSBuild\Current\Bin\MSBuild.exe" ResourcePreview.sln -restore
cd tests\ResourcePreview.Tests\bin\Debug\net48
& "C:\Program Files\Microsoft Visual Studio\18\Community\Insiders\Common7\IDE\CommonExtensions\Microsoft\TestWindow\vstest.console.exe" ResourcePreview.Tests.dll
```

Start vstest vanuit de map van de test-DLL. Vanuit `C:\WINDOWS\system32` weigert hij, omdat hij daar een `TestResults`-map wil maken.

### Bekend probleem: build blijft hangen

Met Automatic Versions 3 bleef een build vanuit Test Explorer eens eindeloos op "(Building)" staan, zonder CPU-gebruik. Automatic Versions 3 herschreef `ResourcePreview.csproj` en `AssemblyInfo.cs` midden in die build. Sinds de versienummering uit staat voor Debug-builds van beide projecten, en voor het testproject ook bij Release, bouwt de solution zonder problemen. Dat het echt hierdoor kwam, is niet bewezen, maar het tijdstip paste precies.

Blijft een build toch hangen: controleer of een projectbestand tijdens de build gewijzigd is. Alleen de MSBuild-processen stoppen helpt dan niet, VS blijft op "(Building)" staan. Sluit VS en start hem opnieuw.

### Bekend probleem: Data Error 5 in het Output-venster

Tijdens het debuggen zie je bij elke tooltip deze regel:

```
System.Windows.Data Error: 5 : Value produced by BindingExpression is not valid for target property.
null BindingExpression:Path=(0); DataItem='WpfTextView' (Name='WpfTextView');
target element is 'WpfToolTipControl' (Name=''); target property is 'TextFormattingMode'
```

Die komt van VS zelf. `WpfToolTipControl` is het tooltip-venster van VS, en dat bindt zijn `TextFormattingMode` aan een attached property van de editor die `null` teruggeeft. WPF gebruikt dan de standaardwaarde, dus de tooltip werkt gewoon. Getest: de melding verschijnt ook bij hoveren over een methodenaam in een .cs-bestand, waar onze code niet draait (de provider is alleen geregistreerd voor `XAML` en `XML`).

Wil je de regels niet zien: Extra > Opties > Foutopsporing > Uitvoervenster > WPF-traceringsinstellingen > Gegevensbinding op `Warning` of `Off`. Dat geldt voor al je WPF-projecten, dus zet hem terug als je eigen bindingen debugt.

Let op bij testen zonder extension: uitschakelen werkt pas na een herstart, en F5 deployt de VSIX opnieuw naar de Experimental Instance en schakelt hem daarbij weer in.

### Handmatige checklist

Wat VS zelf doet, kun je niet met unit tests afdekken. Loop dit na vóór een release (ongeveer acht minuten, in de Experimental Instance met `samples\SampleApp\SampleApp.sln`):

1. Hover over `Renew`, `Report` en `Warning` in `MainWindow.xaml`: er verschijnt een preview met twee tegels.
2. Hover over `DoesNotExist`: de melding "not found under ...".
3. Hover over `Check`: onder de preview staat "Also defined in:" met `IconsLegacy.xaml`.
4. Hover over `PrimaryButton` en `DangerButton` in `MainWindow.xaml`: een tabel met setters, kleurvakjes, het icoontje bij `Tag`, "inherited from ..." en de triggerregel. Boven de tabel staat een echte knop. Controleer in een donker en een licht thema dat de tekst leesbaar is.
5. Hover over de resources in het grijze kader in `MainWindow.xaml` (`CardPadding`, `CardCorners`, `CardShadow`, `AppTitle`, `HeaderFont`, `HeaderFontSize`, `HeaderWeight`, `CodeFont`, `MissingFont`, `DebugVisibility`, `WideMargin`, `TabCorners`, `SoftBlur`, `MaxItems`, `ShowDebugInfo`): elk krijgt een schets, voorbeeldtekst of waarde. Bij `MissingFont` staat de melding dat het font niet geïnstalleerd is.
6. Hover over `SearchBox`, `RoundButtonTemplate`, `BookTemplate`, `FancyTemplate`, `FancyStyle` en `WrapPanelTemplate` onderaan `MainWindow.xaml`. `SearchBox` en `RoundButtonTemplate` tonen een echt control, normaal en uitgeschakeld, en die zien er verschillend uit. `DangerButton` toont er één, zonder label: die stijl heeft geen trigger op `IsEnabled`. `BookTemplate` toont de boom met bindings. `FancyTemplate` en `FancyStyle` tonen de melding dat VS `local:FancyControl` niet kan laden.
7. Klik op de bestandsnaam en op het plaatje: VS opent het bestand met de key geselecteerd, ook als het al open stond.
8. Typ in `Icons.xaml` een nieuwe `<Geometry x:Key="Nieuw">` zonder op te slaan, en hover erover in hetzelfde bestand: de preview werkt al.
9. Nieuw Opties-venster > XAML Resource Preview: er staat maar één categorie, met General en Appearance, en de labels zijn tekst (geen `@...`).
10. Zet Tegels op "Dark only" en tegelgrootte op 32, en hover: één kleine donkere tegel. De kleurvelden van de lichte tegel zijn grijs.
11. Legacy-Opties-venster: dezelfde waarden als in het nieuwe venster. Wijzig daar de taal naar Deutsch, klik OK en hover: "Zeile" in plaats van "line".
12. Zet de taal terug op Automatisch.

## Beperkingen

- **Eigen types.** Een resource die zelf een type uit je project is (`<local:IconDefinition x:Key=... />`) of een eigen markup extension bevat, kan niet laden. VS draait op .NET Framework 4.8 en kent je assembly niet. De tooltip toont dan de foutmelding.
- **Keys buiten de solution.** Resources uit een NuGet-pakket of een theme-DLL worden niet gevonden.
- **Meerdere definities.** Staat een key in meerdere bestanden, dan wint het huidige bestand, daarna alfabetisch. De tooltip meldt hoeveel andere definities er zijn. De echte volgorde van `MergedDictionaries` volgen we (nog) niet.
- **Excepties die blijven.** Twee situaties gooien nog een exceptie die we zelf opvangen: een XAML-bestand dat tijdens het typen even geen geldige XML is (`XmlException` in `ResourceIndex`), en een template die wel laadt maar pas bij het tekenen faalt (in `LiveSampleRenderer`). Het eerste valt niet vooraf te controleren zonder een eigen XML-parser. Zie je ze in de debugger, dan is dat geen fout.
- **Verwijzingen over meerdere regels** worden niet herkend. De finder kijkt per regel.

## Ideeën voor later

- Een instelling om het live voorbeeld uit te zetten, voor wie een kleinere tooltip wil.
- IsMouseOver en IsPressed tonen door de triggers van de stijl zelf toe te passen, zonder muis.
- Waarden die je al in het Legacy-venster had ingesteld automatisch overzetten naar Unified Settings (`migration` in `registration.json`, of eenmalig in code).
- `MergedDictionaries` volgen vanaf `App.xaml` om te bepalen welke definitie WPF echt gebruikt.
- De icoon-preview ook in IntelliSense tonen bij het typen van `{StaticResource `.
- Publiceren op de Visual Studio Marketplace: icoon en preview-afbeelding toevoegen aan het manifest.
