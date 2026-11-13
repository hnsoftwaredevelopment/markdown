# XAML Resource Preview

Visual Studio-extensie die een preview toont als je in XAML over `{StaticResource X}` of `{DynamicResource X}` hovert. Werkt voor `Geometry`, `GeometryGroup`, `Drawing`, `DrawingImage`, `BitmapImage` (en andere `ImageSource`), `Brush` en `Color`.

Hover je over de definitie zelf (`x:Key="Renew"`), dan krijg je ook een preview.

Bij een `Style` toont de tooltip een tabel: `TargetType`, `BasedOn`, de setters met kleurvakjes en mini-iconen, de setters die uit basisstijlen komen, en de triggers.

Klik op het plaatje of op de bestandsnaam onder de preview, en VS opent het bestand met de naam in `x:Key` geselecteerd. Staat een key in meerdere bestanden, dan staat bovenaan de definitie die WPF echt gebruikt, en de andere eronder, elk als eigen link met "overschreven door ..." of "in geen enkele MergedDictionaries" erachter. Definities die WPF nooit gebruikt, staan ook als waarschuwing in de Error List.

## Mappen

```
ResourcePreview/
├─ ResourcePreview.sln              ← de extensie
├─ src/ResourcePreview/
│  ├─ source.extension.vsixmanifest ← wat zit erin, voor welke VS-versies
│  ├─ QuickInfo/                    ← koppeling met de editor van VS
│  ├─ Resources/                    ← zoeken en XAML samenstellen (geen VS, geen WPF)
│  ├─ Preview/                      ← WPF-weergave in de tooltip
│  ├─ Navigation/                   ← springen, de menu-commands en het venster met verwijzingen
│  ├─ Refactoring/                  ← het lampje: een waarde naar een resource verplaatsen
│  ├─ IntelliSense/                 ← iconen en tooltip in de IntelliSense-lijst
│  ├─ Diagnostics/                  ← waarschuwingen voor overschreven keys in de Error List
│  ├─ Localization/                 ← teksten per taal (Strings.resx + 14 vertalingen)
│  ├─ Options/                      ← instellingen: registration.json, SettingsService, oude Opties-pagina
│  ├─ ResourcePreviewPackage.cs     ← AsyncPackage: Opties-pagina en het menu-command
│  └─ ResourcePreviewPackage.vsct   ← menu-item en sneltoets voor Go To Resource Definition
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
| Waarschuwen bij overschreven keys | Aan | Een waarschuwing in de Error List voor elke definitie die WPF nooit gebruikt, omdat een later gemergde dictionary dezelfde key heeft. |
| Resource-verwijzingen controleren | Aan | Een waarschuwing in de Error List voor verwijzingen die WPF tijdens runtime niet vindt (sectie 18). |
| Ongebruikte resources melden | Aan | Een bericht in de Error List voor resources die nergens gebruikt worden (sectie 20). |
| Previews tonen in IntelliSense | Aan | Iconen en de preview-tooltip in de IntelliSense-lijst na `{StaticResource `. |
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

**Live voorbeeld bij een Style.** Boven de setter-tabel staat een echt control met die stijl. Reageert de stijl op `IsEnabled`, dan staat er een tweede naast, met `IsEnabled="False"`. Bij `SearchBox` zie je zo meteen dat de trigger de achtergrond grijs maakt. Zonder zo'n trigger zou je twee keer hetzelfde plaatje zien; daarom komt de tweede dan niet. `HasIsEnabledTrigger` zoekt in de hele `BasedOn`-keten, in een ControlTemplate die de stijl via een setter zet, en herkent `Trigger`, `MultiTrigger`, `DataTrigger` en `MultiDataTrigger`. Het live voorbeeld is uit te zetten in de Opties. Reageert de stijl op `IsMouseOver` of `IsPressed`, dan komen daar ook voorbeelden van; hoe dat werkt staat in sectie 16. Het voorbeeld is ook `IsHitTestVisible="False"`, anders reageert het op je muis in de tooltip en ziet het er elke keer anders uit.

Hoe het werkt (`LiveSampleRenderer`):

1. De stijl gaat door dezelfde `PreviewXamlBuilder` als de iconen. `BasedOn`, brushes en geometries uit andere bestanden komen dus mee.
2. `XamlReader.Parse` maakt er een echte `Style` van. `Style.TargetType` is dan een `Type`, en daar maken we met `Activator.CreateInstance` een control van.
3. `FillContent` geeft het control iets om te tonen: "Voorbeeld" als `Content`, `Text` of `Header`, twee items in een lijst, of waarde 60 bij een `Slider`.
4. `Measure` wordt meteen aangeroepen. Pas dan past WPF de template toe. Zit daar een fout in, dan vangen we die hier af. Anders gebeurt het later in de tooltip van VS en zie je niets.

Geen voorbeeld bij:

- **Eigen types** (`local:FancyControl`). VS kent je assembly niet. De tooltip zegt dat in één regel, en de tabel blijft staan.
- **`Window`, `Page`, `ToolTip`, `ContextMenu`, `Popup`.** Die mogen niet in een `StackPanel` staan. Die slaan we zonder melding over.
- **Een stijl zonder `TargetType`.** Dan weten we niet welk control we moeten maken.

**ControlTemplate.** Voor een standaard control werkt dit net zo: een `Button` met jouw template, normaal, en per toestand waar de template op reageert. Zonder `TargetType` gebruiken we een `ContentControl`, zodat een `ContentPresenter` iets toont. Lukt het niet (eigen type), dan tonen we de boom hieronder, plus de reden.

**DataTemplate: de boom als tekst.** Een DataTemplate heeft data nodig. Zonder data blijft elk `{Binding}`-veld leeg en zie je een leeg kader. Daarom toont de preview wat erin zit. (Sinds sectie 29 staat er ook een gerenderde versie met voorbeelddata boven de boom.)

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

Na 20 regels of 10 niveaus diep stopt de boom, met een regel "… nog 6 elementen". `ItemsPanelTemplate` en `HierarchicalDataTemplate` tonen we ook als boom; een `ItemsPanelTemplate` krijgt sinds sectie 29 ook voorbeelditems.

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
- toont een ControlTemplate de boom met diezelfde regel; een DataTemplate maakt van eigen types een vak (sectie 29);
- toont een andere resource "Geen preview: ..." met het type;
- krijgt een setter die naar zo'n resource verwijst geen icoontje, alleen de tekst.

`NoFirstChanceExceptionTests` bewaakt dit: elke resource uit de SampleApp gaat door de hele keten, en de test telt met `AppDomain.FirstChanceException` elke exceptie die onderweg gegooid wordt, ook als hij opgevangen wordt. Dat moet nul zijn. Voeg je een resource aan de SampleApp toe, dan test hij die automatisch mee.

Om dezelfde reden leest `ColorParser` kleuren nu zelf in plaats van via `ColorConverter.ConvertFromString`, die bij een ongeldige kleur een `FormatException` gooit.

### 14. Ga naar resourcedefinitie (menu-command)

Rechtsklik in een XAML-bestand op `{StaticResource PrimaryButton}` en kies **Go To Resource Definition**, of druk op **Ctrl+Alt+F12**. VS opent het bestand met de definitie en selecteert de key. F12 blijft van VS zelf.

Tot nu toe kwam alles via MEF of via de Opties-pagina. Een menu-item is het derde soort onderdeel: een **command**. Dat bestaat uit twee delen.

**1. Het .vsct-bestand: wat en waar.** `ResourcePreviewPackage.vsct` beschrijft het menu-item zonder code:

| Element | Wat het doet |
|---|---|
| `<Group>` | een groep met een eigen scheidingslijn, met als ouder het contextmenu van de XAML-editor (`guidXamlUiCmds` / `IDM_XAML_EDITOR`, `0x0103`) |
| `<Button>` | het menu-item zelf, met een GUID en een ID (`cmdidGoToResourceDefinition`, `0x0100`) |
| `<CommandPlacement>` | dezelfde groep ook in het contextmenu van de code-editor (`IDM_VS_CTXT_CODEWIN`), voor `.xaml`-bestanden die in de XML-editor openen |
| `<KeyBinding>` | Ctrl+Alt+F12 in de scope Text Editor (zie sectie 15 waarom niet globaal) |

Drie `CommandFlag`s op de button:

- `DefaultInvisible`: verborgen zolang ons package niet geladen is.
- `DynamicVisibility`: de code mag zichtbaarheid per keer bepalen.
- `TextChanges`: de code mag de tekst wijzigen. Zo volgt de menutekst de taalinstelling van de extensie.

De GUID van het contextmenu van de XAML-editor staat nergens in de documentatie. Ik vond hem in de broncode van XAML Styler, die zijn "Format XAML" op dezelfde plek zet.

**2. Van .vsct naar VS.** In de `.csproj` staat het bestand als `VSCTCompile` met `ResourceName` `Menus.ctmenu`. De build maakt er een binaire resource van in de DLL. `[ProvideMenuResource("Menus.ctmenu", 1)]` op het package zet in de `.pkgdef` dat die resource bestaat. VS leest hem bij de eerste start na installatie en onthoudt de menu's in een cache. Verander je de `.vsct` en zie je niets, reset dan de Experimental Instance (sectie 2).

**3. De code: wat er gebeurt.** `GoToResourceDefinitionCommand.InitializeAsync` vraagt `IMenuCommandService` op en koppelt een `OleMenuCommand` aan dezelfde GUID en ID als in de `.vsct`:

```csharp
var command = new OleMenuCommand(instance.Execute, new CommandID(CommandSet, CommandId));
command.BeforeQueryStatus += instance.OnBeforeQueryStatus;
commandService.AddCommand(command);
```

`OleMenuCommandService` erft van `MenuCommandService` uit `System.Design.dll`. Die referentie staat daarom in de `.csproj`. Zonder kreeg ik `CS0012`.

**BeforeQueryStatus.** VS vraagt dit elke keer dat het contextmenu opent of de sneltoets ingedrukt wordt. Daarom doet `OnBeforeQueryStatus` zo weinig mogelijk: de actieve editor ophalen, de regel onder de cursor lezen en kijken of daar een verwijzing staat. `Visible` en `Enabled` volgen daaruit. De index doorzoeken gebeurt pas bij `Execute`.

**Het package moet geladen zijn.** `BeforeQueryStatus` werkt pas als ons package geladen is. Tot dan geldt `DefaultInvisible`, en het item verschijnt nooit. Daarom laadt het package zichzelf zodra er een XAML-bestand actief is:

```csharp
[ProvideAutoLoad(XamlFileContextGuidString, PackageAutoLoadFlags.BackgroundLoad)]
[ProvideUIContextRule(XamlFileContextGuidString, name: "XAML file active",
    expression: "XamlEditor | XamlFile",
    termNames: new[] { "XamlEditor", "XamlFile" },
    termValues: new[] { "ActiveEditorContentType:XAML", "HierSingleSelectionName:.xaml$" })]
```

Een **UI context rule** is een voorwaarde die VS zelf bijhoudt. Wordt hij waar, dan laadt VS het package op de achtergrond. Zo kost de extensie niets in een solution zonder XAML.

**Van de cursor naar de key.** Hier zie je weer de twee API-werelden uit sectie 6:

1. `IVsTextManager.GetActiveView` geeft de actieve editor als `IVsTextView` (shell).
2. `IVsEditorAdaptersFactoryService.GetWpfTextView` maakt daar een `IWpfTextView` van (editor).
3. `ITextDocumentFactoryService` geeft het bestandspad. Eindigt dat niet op `.xaml`, dan geen menu-item.
4. `ResourceReferenceFinder.TryFindReference` zoekt in de regel onder de cursor.

`TryFindReference` is `TryFind` zonder het laatste patroon, `x:Key`. Op een definitie springen naar de definitie heeft geen zin.

**Execute.** De tekst van de editor gaat mee, inclusief niet-opgeslagen wijzigingen (`SetLiveText`). Het zoeken gebeurt op een achtergrondthread, het springen op de UI-thread, via dezelfde `DefinitionNavigator` als de klik in de tooltip. Bij meerdere definities springt het naar de eerste (huidige bestand eerst, dan alfabetisch), en de statusbalk meldt hoeveel er nog zijn.

Bij de eerste keer hangt de command een handler aan `view.Closed`. Sluit je het bestand, dan haalt die de live tekst uit de index (`ClearLiveText`). Anders blijft de index een oude, niet-opgeslagen versie gebruiken.

**Andere sneltoets?** Extra > Opties > Omgeving > Toetsenbord, zoek op `ResourcePreview.GoToResourceDefinition`. Die naam komt uit `CanonicalName` in de `.vsct`.

### 15. Welke definitie wint: MergedDictionaries volgen

Staat een key in twee bestanden, dan gebruikt WPF er maar één. Welke, hangt af van de volgorde in `MergedDictionaries`. Wijzig je de verkeerde, dan zie je je wijziging nooit terug. Sinds deze versie volgt de extensie dezelfde volgorde als WPF.

**De volgorde van WPF.** Een `{StaticResource X}` zoekt zo:

1. het element zelf en zijn ouders, tot en met het `Window`;
2. daarna `Application.Resources` in `App.xaml`;
3. binnen één dictionary: eerst zijn eigen keys, dan de `MergedDictionaries` van **achter naar voor**, elk weer met zijn eigen merges.

Een voorbeeld uit de SampleApp. `App.xaml` merget onder andere:

```xml
<ResourceDictionary Source="Resources/Brushes.xaml" />   <!-- InfoBrush: blauw -->
<ResourceDictionary Source="Resources/Styles.xaml" />
<ResourceDictionary Source="Resources/Values.xaml" />    <!-- InfoBrush: groen -->
```

`Values.xaml` staat later, dus WPF zoekt daar eerst en de tekst wordt groen. De blauwe in `Brushes.xaml` doet niets.

**Wat de index nu onthoudt.** Per bestand bewaart `ResourceIndex` een `XamlFileModel` in plaats van alleen een lijst keys:

| Onderdeel | Voorbeeld |
|---|---|
| `RootKind` | `Application` (App.xaml), `ResourceDictionary`, of `Other` (Window, UserControl) |
| `MergedSources` | de `Source`-waarden uit `ResourceDictionary.MergedDictionaries`, in volgorde |
| `ResourceEntry.IsRootScope` | staat de key in de hoofd-dictionary van het bestand? Een key in `Grid.Resources` of `Style.Resources` is voor andere bestanden onzichtbaar |

**Source omzetten naar een pad.** `ResourceIndex.ResolveSource` doet wat WPF doet bij gecompileerde XAML:

| Source | Wordt |
|---|---|
| `Brushes.xaml`, `../Themes/Dark.xaml` | relatief aan de map van het bestand dat merget |
| `/Themes/Dark.xaml` | relatief aan de projectmap |
| `/MyApp.Styles;component/Dark.xaml` | in het project `MyApp.Styles.csproj` |
| `pack://application:,,,/...` | hetzelfde, zonder het voorvoegsel |
| `pack://siteoforigin:...` | niet gevolgd (null) |

**De graaf.** `MergeGraph` (in `Resources\MergeGraph.cs`) bouwt hieruit wie wie merget. `GetChain(bestand)` geeft het bestand, en daarna wat het merget: de laatste eerst, diepte-eerst. Elk bestand komt er één keer in, zodat twee dictionaries die elkaar mergen geen oneindige lus geven. `GetLookupChain` plakt daar de keten van `App.xaml` achter. Welke `App.xaml`? Eerst een die het bestand (via een omweg) merget, dan die in hetzelfde project, en anders de enige in de solution.

`Resolve` loopt die keten af en geeft elke definitie een status:

| Status | Betekenis | In de tooltip |
|---|---|---|
| `Used` | WPF vindt deze als eerste | "WPF gebruikt hier deze definitie." (alleen als er een andere overschreven is) |
| `Overridden` | wel bereikbaar, maar een andere komt eerst | "· overschreven door Values.xaml" |
| `Unknown` | niet op het zoekpad, bijvoorbeeld de resources van een ander venster | geen opmerking |

Los daarvan krijgt een definitie `IsInUnmergedFile` als het bestand een ResourceDictionary is die nergens gemerged wordt. `IconsLegacy.xaml` in de SampleApp is daar een voorbeeld van. `Themes\Generic.xaml` telt niet mee: die laadt WPF zelf.

`Find` gebruikt `Resolve` ook. Daardoor volgen de tooltip, Ga naar resourcedefinitie, `BasedOn` in de stijltabel en de afhankelijkheden in de preview allemaal dezelfde volgorde.

**Cache.** Een `Source` omzetten zoekt op schijf naar een `.csproj`. Daarom bouwt de index de graaf alleen opnieuw als er iets veranderd is. Elke wijziging (opslaan, live tekst uit de editor) verhoogt een versienummer, en de graaf onthoudt bij welke versie hij hoort. De projectmap per map staat in een eigen cache.

**De Error List.** `OverriddenKeyScanner` loopt voor elke `App.xaml` en elk venster de keten af. De eerste definitie van een key wint; elke volgende in een ander bestand is een waarschuwing. Niet gemeld:

- een venster dat een key uit `App.xaml` overschrijft: dat is meestal bewust;
- twee keer dezelfde key in één bestand: dat meldt de XAML-compiler al;
- dezelfde dictionary die twee keer gemerged wordt: dat is één definitie;
- keys in geneste scopes, zoals `Style.Resources`.

`OverriddenKeyErrorList` (in `Diagnostics\`) zet de resultaten in de Error List. Dat gaat via `ErrorListProvider`, de klassieke API van de VS SDK:

```csharp
var task = new ErrorTask
{
    ErrorCategory = TaskErrorCategory.Warning,
    Text = "...",
    Document = definition.FilePath,
    Line = definition.LineNumber - 1,   // de Error List telt vanaf 0
    Column = definition.Column - 1,
};
task.Navigate += (s, e) => _navigator.NavigateTo(definition);
_errorList.Tasks.Add(task);
```

Wanneer er gescand wordt:

| Moment | Hoe |
|---|---|
| het package laadt | `InitializeAsync`, na het openen van een XAML-bestand |
| een solution opent of sluit | `SolutionEvents.OnAfterOpenSolution` / `OnAfterCloseSolution` uit `Microsoft.VisualStudio.Shell.Events` |
| een .xaml-bestand wijzigt op schijf | het nieuwe event `ResourceIndex.FilesChanged`, vanuit de `FileSystemWatcher` |
| de instelling wijzigt | het nieuwe event `SettingsService.Changed` |

Elke aanvraag wacht 1,5 seconde en annuleert de vorige. Een Save All of een git checkout geeft zo één scan in plaats van tien. Het scannen zelf gebeurt op een achtergrondthread, het bijwerken van de Error List op de UI-thread.

De instelling "Waarschuwen bij overschreven keys" (standaard aan) zet dit uit. Die staat in `registration.json`, `ExtensionSettings`, `SettingsService` en `GeneralOptionsPage`, net als de andere instellingen (sectie 10).

**Sneltoets: scope en cache.** Ctrl+Alt+F12 opende eerst "Find Symbol Results". VS heeft die toets globaal aan `Edit.FindSymbol` gekoppeld, en onze binding was ook globaal (`editor="guidVSStd97"`). Nu staat hij in de scope **Text Editor** (`{8B382828-6202-11d1-8870-0000F87579D2}`). Een binding in een specifiekere scope wint zolang de cursor in een editor staat. Buiten de editor doet Ctrl+Alt+F12 nog steeds Find Symbol.

VS leest de menu's en sneltoetsen uit `Menus.ctmenu` maar één keer en bewaart ze in een cache. Na een wijziging in de `.vsct` moet die cache vernieuwd worden. De simpelste manier: verhoog het tweede getal in `[ProvideMenuResource("Menus.ctmenu", 2)]` (inmiddels 3). Ziet VS een hoger nummer, dan leest het de menu's opnieuw in. Dat werkt ook bij gebruikers die een nieuwe versie installeren. De andere manier is de Experimental Instance resetten (sectie 2).

### 16. Muis erover en ingedrukt nabootsen

Het live voorbeeld toont nu ook hoe een knop eruitziet met de muis erover en ingedrukt:

```
[ Voorbeeld ] [ Voorbeeld ] [ Voorbeeld ] [ Voorbeeld ]
   Normaal     Muis erover    Ingedrukt   Uitgeschakeld
```

**Het probleem.** `IsEnabled` kun je gewoon op `False` zetten, en WPF voert de triggers zelf uit. `IsMouseOver` en `IsPressed` zijn **read-only**: WPF zet ze alleen op basis van de echte muis. Er is geen `SetValue` voor. Ze faken via reflection zou kunnen, maar dat is breekbaar en kan per .NET-versie anders werken.

**De oplossing: doen wat de trigger doet.** Een trigger is niets anders dan "als deze voorwaarde waar is, zet dan deze waarden". `StateSimulator` (in `Preview\StateSimulator.cs`) zoekt de triggers die bij die toestand actief zouden zijn, en zet hun setters zelf als **lokale waarde** op het control. Een lokale waarde wint van stijl- en templatewaarden, net als een actieve trigger.

Zo gaat het, per voorbeeld:

1. `TriggersOf(style)` verzamelt alle triggers in de volgorde waarin WPF ze toepast. Eerst de triggers van de ControlTemplate, dan die van de stijl, van de basisstijl naar beneden. Een latere trigger wint, en in WPF wint een stijltrigger van een templatetrigger.
2. `IsActive` beslist per trigger of hij aan zou staan. `IsMouseOver` (en bij Ingedrukt ook `IsPressed`) telt als `True`. De andere condities van een `MultiTrigger` worden echt nagekeken op het control. Een trigger op `IsMouseOver` + `IsFocused` gaat dus niet aan, want het voorbeeld heeft geen focus.
3. Voor elke setter: zonder `TargetName` op het control zelf, met `TargetName` op het onderdeel uit de template (`Template.FindName("Chrome", control)`).
4. Gebruikt de template de `VisualStateManager` in plaats van triggers, dan gaat het control naar de toestand `MouseOver` of `Pressed` met `VisualStateManager.GoToState`.

Ingedrukt zet ook `IsMouseOver` op waar. Een knop indrukken kan alleen met de muis erop, en veel stijlen rekenen daarop.

**Welke kolommen er komen.** Net als bij Uitgeschakeld alleen als de stijl erop reageert: een trigger met setters op `IsMouseOver="True"` of `IsPressed="True"`, of een `VisualState` met die naam. Bij drie of vier voorbeelden wordt elk voorbeeld smaller (150 in plaats van 220 pixels), zodat de tooltip niet te breed wordt.

**Geen excepties.** Past een waarde niet bij de property, dan slaan we hem over. `DependencyProperty.IsValidValue` controleert dat vooraf, zodat `NoFirstChanceExceptionTests` groen blijft.

**Wat niet werkt:**

- `EnterActions` en `ExitActions` (storyboards in een trigger) voeren we niet uit. Een trigger met alleen een animatie levert geen extra kolom op.
- Een trigger op `IsMouseOver="False"` zetten we niet uit in het Muis erover-voorbeeld.
- Zit de trigger alleen in de standaardtemplate van WPF zelf (jouw stijl zet alleen kleuren), dan tonen we geen extra kolom. Dat is dezelfde keuze als bij Uitgeschakeld.

### 17. Previews in IntelliSense

Typ je `{StaticResource `, dan toont de XAML-editor een lijst met keys. De tooltip van het geselecteerde item toont dezelfde preview als bij hoveren. Eerst zette de extensie er ook een icoontje bij; waarom dat eruit ging, staat aan het eind van deze sectie.

**Eerst uitzoeken welke API de XAML-editor gebruikt.** VS heeft twee completion-API's:

| API | Herkenbaar aan | Wie gebruikt hem |
|---|---|---|
| klassiek | `ICompletionSource`, `CompletionSet`, `Completion` | o.a. de XAML-editor |
| async (nieuw) | `IAsyncCompletionSource`, `CompletionItem` | C#, de meeste nieuwe editors |

Welke de XAML-editor gebruikt, staat nergens. Ik heb `Microsoft.VisualStudio.DesignTools.XamlLanguageService.dll` uit de VS-installatie onderzocht (de metadata gelezen, zonder hem te laden). Daarin staat een `XamlCompletionSourceProvider` met `[Export(typeof(ICompletionSourceProvider))]`, `[ContentType("XAML")]` en `[Name("XAML Completion Source")]`. Dus de klassieke API, en we weten de naam.

**Geen eigen items, wel versieren.** Met de klassieke API roept VS elke `ICompletionSource` aan met dezelfde lijst `IList<CompletionSet>`. Voegen we zelf items toe, dan staat elke key er twee keer in. Daarom draait onze bron ná die van XAML:

```csharp
[Export(typeof(ICompletionSourceProvider))]
[ContentType("XAML")]
[Order(After = "XAML Completion Source")]
```

In `AugmentCompletionSession` lopen we de items van XAML af. Is `DisplayText` een key uit de index, dan:

1. krijgt het item een icoon via `Completion.IconSource`;
2. zetten we de `ResourceEntry` in de property bag van het item (`item.Properties`), zodat de tooltip hem terugvindt.

Dat gebeurt alleen als het stuk regel vóór de cursor eruitziet als `{StaticResource Acc` (`ResourceCompletionSource.IsKeyPosition`). In een `{Binding ` doen we niets.

**De UI-thread.** `AugmentCompletionSession` draait op de UI-thread, bij elke toetsaanslag in de lijst. Daarom:

- Is de index nog niet gevuld (`ResourceIndex.IsReady`), dan starten we de scan op de achtergrond en doen we deze keer niets. De volgende lijst heeft wel iconen.
- Iconen komen er alleen voor plaatjes, geometrieën, drawings, brushes en kleuren (`CompletionIconFactory.HasIcon`). Een stijl of template parsen voor elk item zou het typen traag maken.
- Elk icoon wordt één keer gemaakt en bewaard in een `ConditionalWeakTable<ResourceEntry, ...>`. Wijzigt een bestand, dan maakt de index nieuwe `ResourceEntry`-objecten, en verdwijnen de oude iconen vanzelf uit de cache.
- Lijsten met meer dan 500 items slaan we over.
- Iconen worden `Freeze()`d: dan zijn ze onveranderlijk en mag WPF ze overal delen.

**De tooltip.** De klassieke completion heeft een eigen uitbreidingspunt voor de tooltip van een item:

```csharp
[Export(typeof(IUIElementProvider<Completion, ICompletionSession>))]
[ContentType("XAML")]
[Order(Before = "Default")]
```

`GetUIElement` krijgt het geselecteerde item. Heeft het onze `ResourceEntry` in de property bag, dan geven we de preview terug. Anders `null`, en dan toont VS zijn eigen tooltip.

De preview zelf is dezelfde als bij hoveren. De code die de gegevens verzamelt (XAML met afhankelijkheden, stijltabel, templateboom) stond in `ResourceQuickInfoSource` en staat nu in `ResourcePreviewData.Create`, zodat Quick Info en IntelliSense hem allebei gebruiken.

**Wat onzeker was, en hoe het afliep.** De XAML-items hebben ook een `IconMoniker` (de nieuwere manier om iconen aan te geven, uit de image catalog). Bij de screenshots voor de release bleek het: VS 2026 toont die moniker, en negeert `Completion.IconSource` helemaal. De tooltip werkt wel, want die loopt via de property bag.

Een moniker kan geen eigen plaatje per resource zijn, dus de iconen zijn eruit gegaan. Dat scheelt ook werk: voor elk icoon werd XAML geladen, op de UI-thread, tijdens het typen. `CompletionIconFactory` bestaat nog, voor het venster XAML Resources (sectie 25). Les: een uitbreidingspunt dat compileert en geen fout geeft, doet nog niet wat je denkt. Kijk het na in de echte omgeving.

De instelling "Previews tonen in IntelliSense" (standaard aan) zet dit uit.

### 18. Verwijzingen controleren die WPF niet vindt

Een `{StaticResource X}` die WPF niet kan vinden, compileert gewoon. Pas als de app de XAML laadt, volgt een `XamlParseException`. Deze stap vindt zulke fouten al in de editor.

**Drie soorten problemen** (`ReferenceProblemKind`):

| Soort | Voorbeeld | Wanneer gemeld |
|---|---|---|
| `Missing` | `{StaticResource AccentBrsh}` | nergens in de solution gedefinieerd |
| `DefinedLater` | een stijl die `LateBrush` gebruikt boven `<SolidColorBrush x:Key="LateBrush">` | de enige bereikbare definitie staat lager in hetzelfde bestand |
| `NotLoaded` | `LegacyArrow`, dat alleen in het niet-gemergde `IconsLegacy.xaml` staat | er zijn definities, maar geen enkele op het zoekpad van WPF |

Een StaticResource kijkt niet vooruit: tijdens het laden kent WPF alleen wat erboven al gelezen is. Een DynamicResource zoekt tijdens runtime opnieuw, en code kan de key nog toevoegen (`Resources["X"] = ...`). Daarom krijgt een DynamicResource alleen een melding bij `Missing`, en dan als bericht in plaats van waarschuwing.

**Verwijzingen verzamelen.** De index bewaarde tot nu toe alleen definities. Nu krijgt elk bestand ook een lijst `Uses` met elke `{StaticResource X}` en `{DynamicResource X}`, met regel en kolom (`ResourceIndex.FindUses`). Dat gaat met een reguliere expressie per regel, niet via de XML: zo hebben we de exacte kolom van de key, voor de Error List. Commentaar wordt eerst vervangen door spaties, met behoud van de regeleinden, zodat de regelnummers kloppen.

**Liever een melding te weinig dan een valse.** Een extensie die onterecht klaagt, wordt snel uitgezet. Daarom meldt `ReferenceChecker` alleen wat zeker is:

- **`MergeGraph.IsLookupComplete`.** Merget `App.xaml` (of iets op de weg) een dictionary van buiten de solution, zoals `/MahApps.Metro;component/...`, dan kan die elke key bevatten. Is er geen `App.xaml` (een class library), dan bepaalt de app die de library gebruikt wat er geladen is. In beide gevallen geen `Missing` en geen `NotLoaded`. Om dat te weten geeft `ResolveSource` nu `null` terug voor een assembly die niet in de solution zit, in plaats van terug te vallen op het eigen project.
- **`NotLoaded` alleen voor Window, App.xaml en dictionaries.** Een UserControl ziet tijdens runtime ook de resources van het venster waar hij in staat. Welk venster dat is, weten we niet.
- **`DefinedLater` alleen als er nergens anders een bereikbare definitie is.** Staat de key ook in `App.xaml`, dan vindt WPF die, en gaat er niets mis.

**Hoofdletters.** Keys zijn hoofdlettergevoelig. Bestaat `AccentBrush` wel en verwijs je naar `accentBrush`, dan zegt de melding: "Bedoel je 'AccentBrush'?". Daarvoor houdt de checker een tabel bij met alle keys op hun kleine-letterversie.

**Waar je het ziet.**

- **Error List.** `OverriddenKeyErrorList` heet nu `ResourceErrorList` en toont beide soorten meldingen. Dubbelklik op een verwijzingsprobleem opent het bestand op de plek van de verwijzing (`ErrorListProvider.Navigate`).
- **Tooltip.** Hover je over een verwijzing met een probleem, dan staat de melding direct onder de kop. Quick Info en de Error List gebruiken dezelfde tekst, via `ProblemText.Describe`.

De SampleApp heeft een bestand `Broken\ReferenceProblems.xaml` met van elke soort een voorbeeld. Niets merget dat bestand, dus de SampleApp start nog steeds. De test `Sample_FindsExactlyTheKnownProblems` controleert dat er precies die vijf meldingen zijn: komt er per ongeluk een valse bij, dan faalt hij.

Uitzetten kan met de instelling "Resource-verwijzingen controleren".

### 19. Alle verwijzingen naar een key vinden

Rechtsklik op `{StaticResource AccentBrush}` of op `x:Key="AccentBrush"` en kies **Find Resource References** (Shift+Alt+F12). Er opent een venster met de definities en alle verwijzingen, per bestand.

**Geen nieuwe zoektocht.** Voor de controle uit sectie 18 houdt de index al per bestand alle verwijzingen bij (`XamlFileModel.Uses`). `UsageFinder` filtert die op de key. Er wordt dus geen bestand opnieuw gelezen. `ResourceUse` kreeg er alleen `LineText` bij: de regel zelf, voor in de lijst.

**Welke definitie krijgt elke verwijzing?** Per bestand bepaalt `MergeGraph.Resolve` welke definitie WPF daar neemt, net als in de tooltip. Begin je bij de definitie in `Brushes.xaml` en gebruikt een venster de versie uit `Values.xaml`, dan staat daar "gebruikt de definitie in Values.xaml". Zo zie je meteen welke verwijzingen een wijziging in jouw definitie niet zien. Vindt WPF de key op een plek helemaal niet, dan staat er "WPF vindt de key hier niet".

**Een eigen toolvenster.** Tot nu toe toonde de extensie alles in bestaande VS-onderdelen (tooltip, Error List, IntelliSense). Voor een lijst met resultaten is een eigen venster nodig: een `ToolWindowPane`.

```csharp
[ProvideToolWindow(typeof(ResourceReferencesWindow), Style = VsDockStyle.Tabbed,
    Window = "34E76E81-EE4A-11D0-AE2E-00A0C90FFFC3")]   // naast het Output-venster
```

- `[ProvideToolWindow]` op het package zet het venster in de `.pkgdef`. `Window` is de GUID van het venster waar het als tabblad naast komt, de eerste keer. Daarna onthoudt VS waar jij het neerzet.
- `ResourceReferencesWindow` erft van `ToolWindowPane` en heeft een eigen `[Guid]`. `Content` is gewoon een WPF-element, hier in code opgebouwd: een `DockPanel` met een samenvatting en een `TreeView`.
- De command opent het met `await package.ShowToolWindowAsync(typeof(ResourceReferencesWindow), 0, create: true, ...)`. Bestaat het nog niet, dan maakt VS het aan. Daarna vult `Show(report, ...)` de lijst.

**Thema.** Een standaard WPF-`TreeView` is wit met een blauwe selectie, ook in het donkere thema. VS levert stijlen die het thema volgen:

```csharp
tree.SetResourceReference(StyleProperty, VsResourceKeys.ThemedDialogTreeViewStyleKey);
item.SetResourceReference(StyleProperty, VsResourceKeys.ThemedDialogTreeViewItemStyleKey);
```

`SetResourceReference` (in plaats van een vaste waarde) zorgt dat de kleuren meeveranderen als je van thema wisselt. De achtergrond en tekstkleur komen uit `EnvironmentColors.ToolWindowBackgroundBrushKey` en `ToolWindowTextBrushKey`.

**Gedeelde code voor de twee commands.** Go To Resource Definition en Find Resource References moeten allebei weten wat er onder de cursor staat. Die code zat in `GoToResourceDefinitionCommand` en staat nu in `CaretResource.TryGet`. Find Resource References werkt ook op een `x:Key` (`includeDefinitions: true`); Go To niet, want op een definitie valt niets te springen.

`DefinitionNavigator` kan nu ook naar een verwijzing springen (`NavigateToUse`). Bij een definitie zoekt hij `"Key"` tussen aanhalingstekens; bij een verwijzing zoekt hij de key zelf, vanaf de kolom die de index onthouden heeft.

**Nieuwe sneltoets, nieuwe menu-versie.** De tweede knop in de `.vsct` heeft ID `0x0101` en zit in dezelfde groep. Shift+Alt+F12 staat, net als Ctrl+Alt+F12, in de scope Text Editor. Omdat de `.vsct` veranderd is, staat `[ProvideMenuResource("Menus.ctmenu", 3)]` nu op 3 (sectie 15).

### 20. Ongebruikte resources

Een resource die nergens gebruikt wordt, staat als **bericht** in de Error List (zet Messages aan in de werkbalk). Bericht en geen waarschuwing: het is opruimwerk, geen fout.

**Wanneer telt een key als gebruikt?** `UnusedResourceScanner` kijkt op twee plekken:

1. **XAML.** Alle `{StaticResource}`- en `{DynamicResource}`-verwijzingen uit de index (`XamlFileModel.Uses`, sectie 18). Ook `BasedOn="{StaticResource X}"` en `{Binding Source={StaticResource X}}` tellen mee.
2. **Code.** Elke string in een `.cs`- of `.vb`-bestand. `FindResource("AccentBrush")`, `Resources["AccentBrush"]` en `SetResourceReference(..., "AccentBrush")` bevatten de key als tekst. `CodeStrings` haalt met een reguliere expressie alle strings uit de code. Een key die je in code samenstelt (`"Icon" + name`) ziet hij niet; daarvoor is de instelling om dit uit te zetten.

`CodeStrings` onthoudt per bestand de strings en de laatste schrijftijd. Een volgende scan leest alleen gewijzigde bestanden opnieuw. Het zoeken naar bestanden deelt hij met de index (`ResourceIndex.EnumerateFiles`), dus `bin`, `obj` en `.git` worden ook hier overgeslagen.

**Welke bestanden worden gecontroleerd?** Een library-dictionary kan keys bevatten die een andere solution gebruikt. Om valse meldingen te voorkomen, alleen bestanden die de app zelf laadt:

| Bestand | Gecontroleerd |
|---|---|
| `App.xaml`, vensters, UserControls | ja |
| een dictionary die iets merget | ja |
| een dictionary die niets merget | nee: misschien laadt code of een andere solution hem |
| `Themes\Generic.xaml` en andere themabestanden | nee: WPF zoekt daar zelf, zonder key |
| de dictionaries in `ThemeDictionaries` (`x:Key="Dark"`) | nee: die keys gebruikt WPF zelf |
| een solution zonder `App.xaml` | nee: de app die de library gebruikt, zit ergens anders |

**Wanneer bijgewerkt?** Net als de andere meldingen na het opslaan van een `.xaml`-bestand. De `FileSystemWatcher` let alleen op `.xaml`. Gebruik je een key voor het eerst in code, dan verdwijnt de melding pas bij de volgende scan: na het opslaan van een `.xaml`-bestand of het opnieuw openen van de solution.

In de SampleApp is `UnusedBrush` in `Brushes.xaml` ongebruikt. `CodeOnlyBrush` wordt alleen in `MainWindow.xaml.cs` gebruikt (`TryFindResource("CodeOnlyBrush")`) en krijgt dus geen melding.

### 21. Een key hernoemen

Rechtsklik op een verwijzing of een `x:Key` en kies **Rename Resource Key...**. Na een nieuwe naam verandert de key in alle definities en verwijzingen van de solution.

**Twee helften.** Het tekstwerk staat los van VS, zodat het getest kan worden:

| Klasse | Doet | VS nodig |
|---|---|---|
| `KeyRenamer` | welke bestanden veranderen (`Plan`), of de naam mag (`Check`), en waar in de tekst de key staat (`FindSpans`) | nee |
| `RenameResourceKeyCommand` | de dialoog tonen en de wijzigingen in de editorbuffers zetten | ja |

`FindSpans` zoekt `x:Key="X"`, `{StaticResource X}`, `{DynamicResource ResourceKey=X}` en `<StaticResource ResourceKey="X"/>`. Na de key in een markup extension moet een spatie, komma of `}` komen. Zo blijft `{StaticResource AccentBrush}` staan als je `Accent` hernoemt. Tekst in commentaar en gewone attributen als `Tag="Accent"` blijven ook staan.

**Welke namen mogen niet?** Een spatie, aanhalingsteken, accolade, komma of `< > = &` maakt de XAML stuk. Een naam die al bestaat, weigert de dialoog ook: dan zouden twee resources dezelfde key krijgen, en wint er stilletjes één (sectie 15).

**De dialoog.** `RenameDialog` erft van `DialogWindow` uit `Microsoft.VisualStudio.PlatformUI`. Dat is de basisklasse van VS voor modale vensters: VS zet zelf de eigenaar, en `ShowModal()` blokkeert de rest van VS op de juiste manier. De kleuren komen uit `ThemedDialogColors`, en de tekstvakken en knoppen krijgen de VS-stijlen `VsResourceKeys.TextBoxStyleKey` en `ButtonStyleKey`. Bij elke toetsaanslag controleert de dialoog de naam opnieuw en zet hij de knop Hernoemen aan of uit.

**Wijzigen via de editor, niet via het bestand.** Rechtstreeks naar schijf schrijven zou mis gaan bij een bestand dat open staat met onopgeslagen wijzigingen: VS vraagt dan om opnieuw te laden, en die wijzigingen ben je kwijt. Daarom gaan alle wijzigingen via de tekstbuffer van VS:

1. `IVsInvisibleEditorManager.RegisterInvisibleEditor` geeft voor elk bestand de documentdata. Staat het bestand open, dan is dat dezelfde buffer als die in de editor. Zo niet, dan laadt VS het onzichtbaar.
2. `IVsEditorAdaptersFactoryService.GetDocumentBuffer` maakt van die `IVsTextLines` (de oude COM-kant) een `ITextBuffer` (de nieuwe editor-API, sectie 6).
3. Alle vervangingen in één bestand gaan in één `ITextEdit`. Dat is één stap in de undo-geschiedenis van dat bestand.
4. Stond het bestand open, dan blijft het onopgeslagen. Je ziet de wijziging en kunt hem met Ctrl+Z terugdraaien. Stond het niet open, dan slaat `IVsPersistDocData.SaveDocData` het direct op; anders zou de wijziging verdwijnen zodra de onzichtbare editor sluit.

Er is geen Ctrl+Z voor alle bestanden tegelijk. Daarvoor heeft VS geen eenvoudige publieke API. Voor bestanden die niet open waren, is je versiebeheer de weg terug.

**Geen standaard-sneltoets.** Ctrl+R, Ctrl+R is van de hernoem-functie van VS zelf. In de `.vsct` staat daarom geen `KeyBinding`; je kunt er zelf een toekennen. De menuversie is nu 4.

### 22. Een vaste waarde naar een resource verplaatsen

Zet de cursor in `Background="#FF2D7D9A"`, druk op **Ctrl+.** en kies **Naar resource verplaatsen...**. Kies een key en een dictionary; de waarde wordt een resource en het attribuut wordt `{StaticResource Key}`.

**Het lampje.** Ctrl+. toont de "suggested actions" van VS: het lampje. Een extensie voegt daar iets aan toe met drie klassen:

| Klasse | Rol |
|---|---|
| `ISuggestedActionsSourceProvider` | MEF-export voor content type XAML; maakt per editor een source |
| `ISuggestedActionsSource` | VS vraagt bij elke cursorbeweging `HasSuggestedActionsAsync` en bij het openen van het lampje `GetSuggestedActions` |
| `ISuggestedAction` | één regel in het menu; `Invoke` voert hem uit |

`HasSuggestedActionsAsync` wordt heel vaak aangeroepen. Daarom kijkt hij alleen naar de tekst van de regel (`ExtractPlanner.TryFind`), zonder de index. Pas `Invoke` doet het echte werk: op een achtergrondthread de doelbestanden bepalen, dan op de UI-thread de dialoog en de wijzigingen.

Een detail: `ThreadHelper.JoinableTaskFactory.RunAsync(...)` gaf de analyzer-waarschuwing VSSDK007, ook met `FileAndForget`. Het lampje is een MEF-onderdeel, dus het importeert de `JoinableTaskContext` van de editor en gebruikt `context.Factory`, net als de Quick Info (sectie 6).

**Welk type resource?** XAML-tekst heeft geen types. `ExtractPlanner.ResourceTypeFor` kijkt daarom naar de naam van de property en controleert of de waarde past: `Background` met een kleur wordt `SolidColorBrush`, `Margin` met 1, 2 of 4 getallen wordt `Thickness`, `FontSize` met een getal wordt `sys:Double`. Een onbekende property, of een waarde die niet past (`Width="Auto"`), krijgt geen lampje.

Voor `sys:Double` en `sys:String` moet het doelbestand de namespace kennen. Staat er al een `xmlns` voor `clr-namespace:System` (ook met `assembly=System.Runtime`), dan wordt dat voorvoegsel gebruikt. Anders voegt de extensie `xmlns:sys="clr-namespace:System;assembly=mscorlib"` toe aan het root-element. `mscorlib` werkt ook in .NET 8, via type forwarding.

**Waar komt de resource?** De keuzelijst bevat de dictionaries die het bestand kan zien: eigen merges en die van `App.xaml` (dezelfde opzoekvolgorde als in sectie 15), en `App.xaml` zelf. De laatste keuze wordt onthouden.

- In een dictionary komt de resource onderaan, vóór de laatste `</ResourceDictionary>`.
- In `App.xaml` vóór de `</ResourceDictionary>` binnen `Application.Resources`, of vóór `</Application.Resources>` als daar geen dictionary in staat.
- Staat de waarde in dezelfde dictionary als het doel, dan komt de resource boven het element dat hem gebruikt. Anders zou de StaticResource naar beneden moeten kijken, en dat doet hij niet (sectie 18).

**Meerdere attributen naar een Style.** Selecteer in een start-tag een paar attributen, bijvoorbeeld `Fill="White" Stretch="Uniform" Width="16"`, en druk Ctrl+. of gebruik het contextmenu:

- **Naar stijl verplaatsen...** maakt een nieuwe `Style` met een `Setter` per attribuut en `TargetType` gelijk aan het element. De attributen worden vervangen door `Style="{StaticResource Key}"`. Had het element al een stijl, dan wordt de nieuwe `BasedOn` die stijl.
- **Toevoegen aan stijl 'X'** verschijnt als het element al `Style="{StaticResource X}"` heeft. De attributen worden setters van die bestaande stijl, waar die ook gedefinieerd is. Welke definitie dat is, bepaalt dezelfde opzoekvolgorde als in de tooltip.

`StylePlanner` doet het tekstwerk:

| Stap | Hoe |
|---|---|
| welke attributen | de start-tag rond de selectie zoeken (een `>` binnen aanhalingstekens telt niet), en alle attributen die de selectie raakt |
| wat niet mee mag | events (`Click`, `MouseEnter`, alles op `Changed` of `Click`), `x:Name`, `x:Key`, `Style` zelf; die horen niet in een setter |
| het element aanpassen | de attributen weghalen inclusief de witruimte ervoor, zodat een tag over meerdere regels netjes blijft; het eerste wordt `Style="{StaticResource Key}"` |
| setters toevoegen aan een bestaande stijl | na de laatste bestaande `Setter`: setters moeten aaneengesloten staan en mogen niet ná `<Style.Triggers>` komen, anders geeft XAML een fout; een `<Style ... />` zonder inhoud wordt opengemaakt |
| bestaande setter | een stijl mag een property maar één keer zetten, dus die setter wordt vervangen |

Voor die laatste twee is het einde van een element nodig. `XDocument` geeft alleen de beginpositie (`IXmlLineInfo`). `StylePlanner.ElementEnd` telt daarom zelf de tags vanaf het begin, met diepte: een open-tag gaat omhoog, een sluit-tag omlaag, een `/>` blijft gelijk.

Elementen met een voorvoegsel (`local:MyControl`) worden overgeslagen: het doelbestand kent dat voorvoegsel misschien niet.

**Niet elk element kan een stijl hebben.** In een test selecteerde je `Value="White"` in een `<Setter>` en koos je de stijl-actie. Het resultaat: een `Style` met `TargetType="Setter"` en een `Setter` met een `Style`-attribuut. WPF weigert dat: alleen een `FrameworkElement` of `FrameworkContentElement` kan een stijl hebben. `AttributeSelection.CanHaveStyle` zoekt het type van het element op met reflectie (dezelfde `FindWpfType` als in sectie 23) en de stijl-acties verschijnen alleen als het antwoord ja is. Voor `Setter`, `Trigger` en `GradientStop` dus niet meer. Losse waarden kunnen daar wel nog een resource worden.

**Een waarde in een setter.** `<Setter Property="Background" Value="White" />` was eerst geen kandidaat voor "Naar resource verplaatsen": de property heet `Value`, en daarvan weet je het type niet. Nu leest `ExtractPlanner` de `Property` van dezelfde setter en kiest daarmee het type (`SolidColorBrush`). De voorgestelde key komt van de `TargetType` van de stijl eromheen: `ButtonBackground`. Een setter in `<Style.Triggers>` vindt ook de juiste stijl, omdat het zoeken naar `<Style` een spatie of `>` erachter eist en dus `<Style.Triggers>` overslaat.

En als zo'n verkeerde stijl toch in een bestand staat, probeert de preview hem niet meer live te laden: de settertabel staat er, het voorbeeld niet.

**Ook in het contextmenu.** Drie menu-items doen hetzelfde als het lampje: Extract to Resource..., Extract to Style... en Add to style 'X'. Elk verschijnt alleen als het van toepassing is. Lampje en menu delen de code in `ResourceRefactorings`; het lampje maakt per actie een `RefactoringAction`, het menu roept dezelfde methoden aan vanuit `RefactoringCommands`. Menuversie 5.

**Eén plek voor bufferwijzigingen.** Hernoemen (sectie 21) en verplaatsen wijzigen allebei bestanden via de editor. Die code staat nu in `BufferEditor.Apply(path, text => changes)`: open bestanden blijven onopgeslagen met één undo-stap, gesloten bestanden worden opgeslagen. De wijzigingen zelf zijn `TextChange`-waarden (start, lengte, nieuwe tekst), die de tests op een gewone string kunnen toepassen.

### 23. Een bestaande resource zoeken

Je typt `Fill="White"`, maar er bestaat al een `WhiteBrush`. Of je zet vijf attributen op een `Path`, terwijl er al een `IconStyle` is die precies dat doet. **Passende resource zoeken...** (contextmenu of Ctrl+.) zoekt die resources op en laat je kiezen. Er verandert niets tot je op Toepassen klikt.

Wat je selecteert bepaalt waar gezocht wordt:

- een selectie van attributen in één start-tag: stijlen en losse waarden voor die attributen;
- geen selectie: het attribuut onder de cursor, ook als de cursor net achter het sluitende aanhalingsteken staat (`StylePlanner.TryFindAt`).

**Wanneer past een stijl?** `ResourceMatcher.MatchStyle` verzamelt de setters van de stijl, inclusief de `BasedOn`-keten. Eigen setters winnen van die van de basis, net als in WPF. Daarna:

| Geval | Resultaat |
|---|---|
| elke setter is een geselecteerd attribuut met dezelfde waarde | past; de geselecteerde attributen die de stijl niet zet blijven op het element |
| de stijl zet een property die niet in de selectie zit | valt af: hij zou het uiterlijk ongemerkt veranderen |
| een setter met een andere waarde, of met `<Setter.Value>` | valt af |
| een `EventSetter`, of een `BasedOn` die we niet kunnen lezen | valt af: die stijl doet meer dan we kunnen zien |
| het element heeft al een `Style` | geen stijlen, alleen losse waarden: twee stijlen combineren gaat niet |

Triggers laten een stijl niet afvallen, maar staan wel in de lijst ("Triggers: 2"). Je ziet dan dat de stijl meer doet dan de setters.

**TargetType.** Een stijl voor `Shape` past op een `Path`, want `Path` erft van `Shape`. Om dat te weten zoekt `ResourceMatcher.FindWpfType` het type op in de WPF-assemblies (`PresentationFramework`, `PresentationCore`, `WindowsBase`) onder de gangbare namespaces, en vraagt `IsAssignableFrom`. Dat kan, omdat de extensie zelf op .NET Framework met WPF draait. Een eigen type (`local:IconPath`) kennen we niet; dat past alleen op zichzelf.

**Waarden vergelijken.** XAML-tekst kent veel spellingen voor dezelfde waarde. `ResourceMatcher.Normalize` maakt er één van, met hetzelfde type-gissen als sectie 22 (`ExtractPlanner.ResourceTypeFor`):

| Soort | Voorbeeld | Wordt |
|---|---|---|
| kleur bij een brush- of kleur-property | `White`, `#FFF`, `#FFFFFF` | `#FFFFFFFF` |
| `Thickness` | `8`, `8,8`, `8 8 8 8` | `8,8,8,8` |
| getal | `16`, `16.0` | `16` |
| `True`/`False`, `FontWeight` | `semibold` | hoofdletterongevoelig |
| markup extension | `{StaticResource  X }` | witruimte weg |

Een kleur alleen normaliseren bij een brush-property is bewust: `Content="Red"` is tekst, geen kleur.

Een setter met `Value="{StaticResource AccentBrush}"` wordt vergeleken met de waarde van `AccentBrush`, als dat een eenvoudige resource is (`ResourceMatcher.Dereference`). Zo past `BaseButton` op een knop met `Background="#FF002BBD"`.

Attribuutwaarden in het bestand zijn nog XML-escaped (`&amp;`), setterwaarden uit `XElement` niet. `WebUtility.HtmlDecode` trekt dat gelijk.

**Property-namen.** `Shape.Fill` in een setter is hetzelfde als `Fill`. `Grid.Row` is een attached property en moet `Grid.Row` blijven. Het verschil: `Shape` heeft een gewone instance-property `Fill`, `Grid` heeft geen property `Row` (alleen `GetRow`/`SetRow`). Let op: `Type.GetProperty(naam)` gooit een `AmbiguousMatchException` als een subklasse een property verbergt met `new`. Daarom zoekt de code in `GetProperties()`.

**Welke resources ziet het element?** `ResourceMatcher.VisibleEntries` loopt de opzoekvolgorde van sectie 15 af en houdt per key de eerste definitie. In het bestand zelf tellen alleen resources boven het element, omdat een StaticResource niet vooruit kijkt (sectie 18).

**Toepassen.** Een losse waarde wordt `{StaticResource Key}`. Bij een stijl verdwijnen de attributen die de stijl overneemt, en komt `Style="{StaticResource Key}"` op de plek van de eerste. Dat is `StylePlanner.PointElementAtStyle` uit sectie 22, met alleen de overgenomen attributen.

**De keuzelijst.** `MatchResourceDialog` is een `DialogWindow` met een `ListBox`. Elke regel toont de key, wat hij overneemt, wat er op het element verandert en het bestand. De `ItemTemplate` is in code gebouwd met `FrameworkElementFactory`; dat is de oude manier om een `DataTemplate` te maken zonder XAML-bestand. Dubbelklik of Enter past de gekozen resource toe.

**Rekenwerk van de UI-thread af.** Het zoeken gebruikt de index en kan bij de eerste keer alle `.xaml`-bestanden lezen. Daarom gebeurt het in `ResourceRefactorings.FindMatchingAsync` op een achtergrondthread; pas de dialoog gaat naar de UI-thread. Het menu-item zelf kijkt alleen naar de tekst (staat er een attribuut?), net als de andere menu-items. Menuversie 6.

### 24. Kleurvakjes in de code

Voor elke kleurwaarde in een .xaml-bestand staat een klein vierkantje met die kleur. Ook bij `{StaticResource AccentBrush}`: dan zoekt de extensie op welke kleur die brush heeft.

**Iets tussen de tekst zetten: een intra-text adornment.** De editor kent drie manieren om iets extra's te tekenen:

| Manier | Wat | Voorbeeld |
|---|---|---|
| classifier | tekst kleuren | syntax-kleuren |
| adornment layer | iets over of onder de tekst tekenen, zonder dat de tekst opschuift | de kronkellijn onder een fout |
| intra-text adornment | een WPF-element *tussen* de tekens, de tekst schuift op | de kleurvakjes, inlay hints |

Voor de laatste geef je de editor `IntraTextAdornmentTag`s via een tagger. Een tag met een lengte van nul op de plek waar de waarde begint, zet het vakje vóór de waarde. `PositionAffinity.Successor` zegt dat het vakje bij de tekst erna hoort: typ je ervoor, dan blijft het bij de waarde staan.

| Klasse | Rol |
|---|---|
| `ColorSwatchTaggerProvider` | MEF-export, `IViewTaggerProvider` met `[TagType(typeof(IntraTextAdornmentTag))]`, voor `XAML` en `XML` (een .xaml-bestand kan ook in de XML-editor openen) |
| `ColorSwatchTagger` | `ITagger<IntraTextAdornmentTag>`: `GetTags` krijgt de zichtbare stukken tekst en geeft per kleur een tag met een `Border` |
| `ColorSwatchFinder` | het tekstwerk en het opzoeken van de kleur, zonder VS-code, dus getest |

Waarom een *view*-tagger? Een adornment hoort bij één editorvenster. Open je hetzelfde bestand in twee vensters, dan krijgt elk venster zijn eigen tagger. `textView.Properties.GetOrCreateSingletonProperty` zorgt dat er per venster maar één is, ook als VS het twee keer vraagt.

**Welke waarden krijgen een vakje?** `ColorSwatchFinder.Find` werkt per regel, net als de andere finders:

- een attribuut waarvan de property een brush of kleur is. Dat bepaalt dezelfde code als bij "Naar resource verplaatsen" (sectie 22): `ExtractPlanner.ResourceTypeFor(naam, "White")` geeft `SolidColorBrush` of `Color`. Zo krijgt `Text="Red"` geen vakje;
- `Value="..."` in een `<Setter>`: de property staat in `Property="..."` van dezelfde tag;
- de inhoud van `<Color>...</Color>`;
- commentaar wordt eerst leeggemaakt, met spaties, zodat de posities blijven kloppen.

**Een key opzoeken zonder de editor te vertragen.** `GetTags` draait op de UI-thread, elke keer als de editor tekent. Daar mag de index niet aan het werk, want de eerste keer leest die alle .xaml-bestanden. Daarom:

1. Een letterlijke kleur (`White`) is meteen bekend.
2. Voor een key kijkt de tagger in zijn eigen tabel. Staat hij er niet in, dan zet de tagger de key in een wachtrij en tekent nog geen vakje.
3. Een achtergrondtaak zoekt de keys in de wachtrij op met `ColorSwatchFinder.Resolve`: dezelfde opzoekvolgorde als de tooltip (sectie 15), en een `SolidColorBrush` met `Color="{StaticResource Accent}"` wordt gevolgd tot de kleur.
4. Daarna meldt de tagger `TagsChanged`, en de editor vraagt de tags opnieuw. Nu staat de kleur in de tabel.

Een kleur kan veranderen: je past de definitie aan in dit bestand (`ITextBuffer.Changed`) of in een ander bestand (`ResourceIndex.FilesChanged`). Dan markeert de tagger alle keys als verouderd, en zoekt ze opnieuw op zodra ze zichtbaar zijn. Bij typen gebeurt dat pas na een halve seconde stilte. Het oude vakje blijft tot het nieuwe er is, zodat er niets knippert.

**Het vakje zelf.** Een `Border` met een grijze rand, leesbaar in een licht en een donker thema. Een half doorzichtige kleur staat op een schaakbord (een `DrawingBrush` met `TileMode.Tile`), anders zie je het verschil met een volle kleur niet. Een tooltip toont de kleurcode. Meeschalen met de zoom hoeft niet: de editor zoomt met een transform op de hele view, adornments inbegrepen.

Een eerste versie zette de grootte op basis van `ITextView.LineHeight`. Dat gaf een `NullReferenceException` bij het openen van een solution: de tagger wordt al gevraagd voordat de view zijn eerste layout heeft gedaan, en `LineHeight` leest dan iets wat nog niet bestaat. Les: lees in `GetTags` zo weinig mogelijk van de view, en zeker geen layout-eigenschappen.

Geen vakje voor een `LinearGradientBrush` of een brush met `Opacity`: één vlak zou dan de verkeerde kleur tonen.

**Visual Studio doet het zelf ook.** De XAML-editor van VS heeft een eigen optie: **Languages > XAML > Advanced > Show inline color previews**. Staan beide aan, dan zie je twee vakjes per kleur: dat van VS vóór de aanhalingstekens, het onze erna. Dat bleek pas bij de screenshots, toen de Experimental Instance (waar alleen onze extensie in stond) toch twee vakjes toonde. De gebruiker kiest welke hij uitzet; de README zegt het.

Een nieuwe instelling, **Kleurvakjes in de editor tonen** (`showColorSwatches`), zet het uit. De tagger luistert naar `SettingsService.Changed` en meldt `TagsChanged` voor het hele bestand, zodat de vakjes direct verdwijnen.

### 25. Het venster XAML Resources

**View > Other Windows > XAML Resources** toont alle resources van de solution, of alleen wat het actieve .xaml-bestand kan gebruiken. Per bestand of per type, met zoeken, een preview als tooltip, een contextmenu en slepen naar de editor.

**Een tool window met een eigen menu-item.** Het venster van sectie 19 (verwijzingen) werd alleen geopend door een command in het contextmenu. Dit venster heeft een vaste plek in het View-menu:

| Onderdeel | Waar |
|---|---|
| `ResourcesWindow : ToolWindowPane` met een eigen `[Guid]` | het venster |
| `[ProvideToolWindow(typeof(ResourcesWindow), Window = "3AE79031-...")]` | registratie; die GUID is de Solution Explorer, dus het venster opent als tabblad daarnaast |
| een `Button` met parent `IDG_VS_WNDO_OTRWNDWS1` in de .vsct | het menu-item in View > Other Windows; zonder `DynamicVisibility`, zodat het er altijd staat |
| `InitializeCommandAsync` | koppelt het menu-item aan `ShowToolWindowAsync` |

Een command dat altijd zichtbaar is, laadt het package als je erop klikt. Daarom hoeft er geen extra `ProvideAutoLoad` bij.

**`Initialize()` in plaats van de constructor.** VS maakt het venster zelf aan: bij het eerste openen, maar ook bij het starten als het venster de vorige keer open stond. Er is dan geen command dat iets kan doorgeven. In de constructor is het package nog niet bekend; in `Initialize()` wel (`Package`). Daar haalt het venster zijn services op en begint het met laden.

**Het actieve document volgen.** `IVsMonitorSelection.AdviseSelectionEvents` meldt wijzigingen in de selectie van VS. Het venster implementeert `IVsSelectionEvents` en kijkt naar `SEID_DocumentFrame`: het actieve documentvenster. Uit dat `IVsWindowFrame` komt het pad via `VSFPROPID_pszMkDocument`. Wordt een niet-.xaml-bestand actief, dan blijft het laatste .xaml-bestand staan; anders zou de lijst leeg worden zodra je een .cs-bestand opent. Bij `Dispose` volgt `UnadviseSelectionEvents`, anders blijft VS het gesloten venster aanroepen.

**Wat erin staat: `ResourceCatalog`.** Net als bij de andere features zit de logica in een klasse zonder VS-code:

| Methode | Wat |
|---|---|
| `Build` | alle resources in de hoofd-dictionary van elk bestand (niet die in `Grid.Resources` of `Style.Resources`), of met een actief bestand: één definitie per key, langs de opzoekvolgorde van sectie 15 |
| `GroupByFile` | eerst de bestanden in de volgorde waarin WPF zoekt vanuit `App.xaml` (de laatst gemergde eerst), dan de rest op naam |
| `GroupByType` | brushes, kleuren, afbeeldingen en geometrieën, stijlen, templates, waarden; op elementnaam (`...Brush`, `...Template`, `...Geometry`) |
| `Filter` | key bevat de zoektekst, hoofdletterongevoelig |

De notities komen van de scanners die de Error List al gebruikt (secties 15 en 20): `OverriddenKeyScanner`, `UnusedResourceScanner` en `MergeGraph.IsLoaded`. Het venster toont dus hetzelfde als de Error List, ook als je die meldingen in de instellingen uit hebt gezet.

**Laden op de achtergrond, tekenen op de UI-thread.** Het lezen en scannen gebeurt met `await TaskScheduler.Default`. Een nieuwe lading annuleert de vorige via een `CancellationTokenSource`; de oude stopt met een `OperationCanceledException` die het venster stil opvangt. Zoeken en hergroeperen gebruiken de geladen lijst opnieuw. Dat is goedkoop genoeg om bij elke toetsaanslag te doen.

**De preview pas bij het openen van de tooltip.** Honderden previews vooraf bouwen kost te veel tijd. Elk item krijgt een lege `ToolTip`; in `ToolTipOpening` komt de inhoud erin, met dezelfde `ResourcePreviewData` en `PreviewRenderer` als de tooltip in de editor. Het kleine icoon voor de key komt van `CompletionIconFactory`, met zijn cache; die was eerst voor IntelliSense gemaakt (sectie 17).

**Slepen naar de editor.** WPF-slepen begint met `DragDrop.DoDragDrop` en een `DataObject`. Het venster zet daar de tekst `{StaticResource Key}` in als `UnicodeText`. De editor van VS accepteert tekst die erop valt en zet hem op de plek waar je loslaat; daar is geen eigen code voor nodig. Slepen begint pas als de muis met ingedrukte knop een paar pixels verschuift (`SystemParameters.MinimumHorizontalDragDistance`), anders wordt elke klik een sleepactie.

**Een gevangen exceptie is ook een probleem.** De eerste test in VS liep vast op `CaseStyle` uit `Broken\ReferenceProblems.xaml`: hover in het venster gaf een `XamlParseException` over `accentBrush`. Die exceptie werd wel gevangen, en de tooltip toonde netjes een melding. Maar een debugger die stopt bij elke gegooide exceptie, stopt daar toch. In de editor viel het nooit op, omdat je zelden over zo'n kapotte stijl hovert; het venster toont alles, dus daar wel.

De oplossing: niet proberen. `PreviewXamlBuilder` weet al welke keys ontbreken (`MissingKeys`). Is die lijst niet leeg, dan slaat `PreviewRenderer` `XamlReader.Parse` over en toont direct "Niet gevonden in de solution". De test die controleert dat geen enkele SampleApp-resource een exceptie gooit (ook geen gevangen, via `AppDomain.FirstChanceException`), loopt nu ook de bestanden in `Broken\` langs.

**Bijwerken zonder opslaan.** De eerste versie laadde opnieuw bij `ResourceIndex.FilesChanged`, en dat komt van een `FileSystemWatcher`: alleen bij opslaan. Maak je met "Naar resource verplaatsen" een resource in een bestand dat open staat, dan blijft dat bestand onopgeslagen (sectie 22) en zag het venster hem niet. Daarom nu:

- `LiveTextTracker`, een `IWpfTextViewCreationListener` voor .xaml-editors. Na een wijziging en een halve seconde stilte gaat de tekst naar `ResourceIndex.SetLiveText`, op een achtergrondthread. Sluit de editor, dan telt het bestand op schijf weer (`ClearLiveText`), tenzij er nog een tweede venster op hetzelfde bestand open is.
- `SetLiveText` slaat tekst over die hij al kent. Quick Info en de kleurvakjes geven vaak dezelfde tekst door; die hoeft niet opnieuw geparsed te worden.
- Is de tekst nieuw, dan meldt de index `LiveTextChanged`. Het venster luistert daarnaar, en naar `FilesChanged`, met een pauze van 0,7 seconde: tien wijzigingen achter elkaar geven één keer laden.
- Een venster op een verborgen tabblad laadt niet bij elke wijziging. Het onthoudt dat er iets veranderd is en laadt opnieuw zodra het zichtbaar wordt (`IsVisibleChanged`).

**Geselecteerde tekst in een donker thema.** De tekst in de boom had een vaste kleur: `EnvironmentColors.ToolWindowTextBrushKey`, wit in een donker thema. De themed TreeViewItem-stijl kleurt een geselecteerd item licht, en verwacht dat de tekst zijn eigen voorgrondkleur volgt. Met een vaste kleur werd het wit op wit. Nu krijgen de `TextBlock`s geen eigen kleur en erven ze die van het `TreeViewItem`. Hetzelfde gold voor het venster met verwijzingen.

**Een icoon in het menu.** VS heeft een catalogus met duizenden iconen, de image monikers. In de .vsct haal je ze binnen met `<Include href="KnownImageIds.vsct" />`, en een knop krijgt er een met `<Icon guid="ImageCatalogGuid" id="ResourceView" />` plus `<CommandFlag>IconIsMoniker</CommandFlag>`. Het tabblad van het venster gebruikt hetzelfde icoon via `BitmapImageMoniker = KnownMonikers.ResourceView`. Welke namen er zijn, staat in `KnownImageIds.vsct` in de VSSDK-map van je VS-installatie. Menuversie 8.

**Het contextmenu hergebruikt de commands.** Find Resource References en Rename Resource Key werkten vanaf de cursor in de editor. Ze kregen elk een ingang die met een definitie of key werkt (`FindFor(entry)`, `Rename(file, key)`), en een statische `Instance` zodat het venster ze kan vinden.

### 26. Een review: valkuilen die tests niet vinden

Na zeven nieuwe features volgde een review van de hele code. De logica was goed getest; de valkuilen zaten in wat tests niet zien: beveiliging, threads, geheugen en snelheid in grote solutions.

**1. XAML kan code uitvoeren.** `XamlReader` maakt objecten, en sommige WPF-objecten doen iets zodra ze bestaan. `ObjectDataProvider` roept een methode aan, elke methode:

```xml
<ObjectDataProvider x:Key="Evil" ObjectType="{x:Type diag:Process}" MethodName="Start">
    <ObjectDataProvider.MethodParameters><sys:String>calc.exe</sys:String></ObjectDataProvider.MethodParameters>
</ObjectDataProvider>
```

De oude controle liet namespaces door als VS die assembly al geladen had, zoals `System` met `System.Diagnostics.Process`. Hoveren was genoeg, en sinds het venster XAML Resources zelfs dat niet: een `DrawingImage` die naar `Evil` verwijst krijgt een icoon, en het icoon laadt zijn afhankelijkheden mee. Een gekloonde repo openen kon dus code uitvoeren.

Nu weigert `PreviewXamlBuilder` vier types altijd (`ObjectDataProvider`, `XmlDataProvider`, `Frame`, `WebBrowser`), ook diep in een stijl of als afhankelijkheid, en staat hij van `clr-namespace` alleen nog `System` (voor `sys:Double`) en `System.Windows.*` uit de WPF-assemblies toe. De test bewijst het: een provider die `Environment.SetEnvironmentVariable` zou aanroepen, gaat door de tooltip en het icoon van het venster XAML Resources, en de variabele blijft leeg.

Les: alles wat gebruikersbestanden met `XamlReader`, `BinaryFormatter` of een andere "maak objecten uit tekst"-API laadt, is een ingang voor code. Werk met een lijst van wat mag, niet met een lijst van wat niet mag.

**2. Een tweede watcher.** Na een buffer-overflow van de `FileSystemWatcher` (een grote `git checkout`) scant de index opnieuw en start een nieuwe watcher, maar de oude bleef draaien. `StartWatching` stopt nu eerst de oude.

**3. Snel genoeg, ook met tienduizend bestanden.** Elke verversing van het venster zocht voor "ongebruikt" de hele mappenboom af naar .cs- en .vb-bestanden. `CodeStrings` bewaart die lijst nu per solution, met een eigen watcher die hem alleen leegmaakt als er een codebestand of map bijkomt, verdwijnt of hernoemd wordt. Een versienummer voorkomt dat een lijst die tijdens zo'n wijziging gelezen werd, toch bewaard blijft.

**4. Niet parsen op de UI-thread.** IntelliSense las bij elke lijst de hele editortekst in de index, op de UI-thread. Sinds `LiveTextTracker` (sectie 25) dat op de achtergrond doet, is die regel weg.

**5 en 6. Opruimen bij het sluiten van de solution.** Indexen leefden de hele VS-sessie, elk met een watcher. `ResourceIndex.ReleaseAll` ruimt ze op als de solution sluit, en het venster XAML Resources maakt zijn lijst leeg en laadt opnieuw als er een solution opent.

**7. Error List en venster gelijk.** De Error List luistert nu ook naar `LiveTextChanged`, zodat een nieuwe resource zonder opslaan ook daar meetelt.

**8. Opslaan kan mislukken.** `BufferEditor` slaat een gesloten bestand stil op. Bij een alleen-lezen bestand mislukte dat zonder melding, en de wijziging verdween met de onzichtbare editor. Nu opent hij het bestand: de editor toont dezelfde buffer, gewijzigd en niet opgeslagen. En hij meldt waarom.

### 27. Een release maken

**Versie 1.5.0.** Na zeven nieuwe features is dit meer dan een kleine update, dus de versie springt van 1.0.0 naar 1.5.0. Het nummer staat op één plek: `Identity Version` in `source.extension.vsixmanifest`. De release-workflow (`.github/workflows/release.yml`) zet bij het bouwen de versie uit de tag of de invoer in het manifest; in de repository staat hij ook op 1.5.0, zodat een lokale build hetzelfde nummer heeft.

**De beschrijving en de tags** in het manifest zijn wat de Marketplace in de zoekresultaten toont. De README is de pagina zelf (`"overview": "README.md"` in `publishManifest.json`). De afbeeldingen in de README staan met een volledige `raw.githubusercontent.com`-URL, omdat de Marketplace relatieve paden niet altijd goed toont; `assetFiles` in `publishManifest.json` uploadt ze daarnaast mee.

**De changelog.** `CHANGELOG.md` heeft per versie een kop `## 1.5.0`. De workflow knipt die sectie eruit en geeft hem aan `gh release create --notes-file`. Is er geen sectie, dan maakt GitHub zelf notities uit de commits (`--generate-notes`).

**Screenshots maken met een script.** De afbeeldingen in de README zijn gemaakt zonder iets met de hand aan te klikken:

| Stap | Hoe |
|---|---|
| VS starten | `devenv.exe /rootsuffix Exp SampleApp.sln` |
| VS besturen | het DTE-object uit de Running Object Table (`!VisualStudio.DTE.18.0:<pid>`): bestanden openen, de cursor plaatsen, commands uitvoeren zoals `View.XamlResources` en `ResourcePreview.FindMatchingResource` |
| knoppen en keuzelijsten | Windows UI Automation (`System.Windows.Automation`): het element zoeken op naam of type en `SelectionItemPattern` of `TogglePattern` gebruiken |
| tooltip en lampje | met de focus in de editor `Ctrl+K, Ctrl+I` (Quick Info) en `Ctrl+.` sturen met `SendKeys` |
| vastleggen | `Graphics.CopyFromScreen`, na `SetProcessDPIAware`, zodat de pixels kloppen op een scherm met schaling |

Valkuilen: een DTE-command is "niet beschikbaar" zolang de editor geen toetsenbordfocus heeft; één klik in de editor lost dat op. En wie tijdens het script typt, typt in VS: zo kwam er een stukje chattekst in `Brushes.xaml` terecht (niet opgeslagen).

### 28. Keys uit een klasse (x:Static)

**De vraag.** Een gebruiker schreef na versie 1.5.0 dat zijn templates geen preview kregen. Hij zet de keys in een klasse, zodat zijn code en de XAML dezelfde naam gebruiken:

```xml
<DataTemplate x:Key="{x:Static res:TemplateKeys.ValueEditor}"> ... </DataTemplate>
<ContentControl ContentTemplate="{StaticResource {x:Static res:TemplateKeys.ValueEditor}}" />
```

De index sloeg elke key over die met `{` begint. Zo'n resource bestond voor de extensie dus niet.

**Het probleem: wat is de key?** WPF gebruikt als key de *waarde* van `TemplateKeys.ValueEditor`. Die waarde staat in een assembly die we niet laden (zie de veilige preview in sectie 26). We kunnen de waarde dus niet lezen. Wat we wel weten: twee keys zijn hetzelfde als ze dezelfde klasse en hetzelfde member noemen. De prefix tellen we niet mee, want het ene bestand kan `res:` gebruiken en het andere `keys:` voor dezelfde namespace.

**Eén plek die keys leest.** `ResourceKeys.Normalize` maakt van de tekst de key die de index gebruikt:

| In de XAML | Key in de index |
|---|---|
| `AccentBrush` | `AccentBrush` (ongewijzigd, ook met spaties) |
| `{x:Static res:TemplateKeys.ValueEditor}` | `{x:Static TemplateKeys.ValueEditor}` |
| `{x:Static Member=keys:TemplateKeys.ValueEditor}` | `{x:Static TemplateKeys.ValueEditor}` |
| `{x:Type Button}` | `null`: niet ondersteund, overslaan |

De accolade aan het begin zorgt dat een statische key nooit gelijk is aan een gewone key. Alle regexen die een key lezen (de index, de hover, de preview, de stijlen, de kleurvakjes) gebruiken nu hetzelfde stukje patroon, `ResourceKeys.KeyPattern`, en roepen daarna `Normalize` aan. Daardoor werkten hover, Go To Definition, Find References en de Error List in één keer, zonder dat we die code aanpasten.

**Twee keer de key.** `ResourceEntry` heeft nu `Key` (voor vergelijken) en `KeyText` (zoals hij in het bestand staat, met prefix). Overal waar we tekst invoegen, zoals slepen uit het venster XAML Resources, Find Matching Resource en `BasedOn` bij Extract to Style, gebruiken we `KeyText`. Anders zou er `{StaticResource {x:Static TemplateKeys.ValueEditor}}` zonder prefix in je XAML komen, en dat compileert niet.

**De preview.** `XamlReader` kan `x:Key="{x:Static res:...}"` niet lezen, want daarvoor moet hij het type laden. `PreviewXamlBuilder` maakt er daarom in de losse preview-dictionary een gewone key van: `xStatic.TemplateKeys.ValueEditor`. Verwijzingen naar die key binnen de preview krijgen dezelfde tekst. Een verwijzing naar een statische key die we niet vinden, zoals `{x:Static SystemColors.ControlBrushKey}`, blijft staan: die levert WPF zelf. De controle op eigen types draait nu op de aangepaste kopie, anders zou de oude `res:` in de key de preview alsnog blokkeren.

**Geen valse meldingen.** Drie keuzes:

- Een ontbrekende statische key melden we alleen als dezelfde klasse elders in XAML keys heeft. `SystemColors.ControlBrushKey` krijgt dus geen waarschuwing, `TemplateKeys.NumberEditor` (typfout, terwijl `TemplateKeys.ValueEditor` wel bestaat) wel.
- Statische keys krijgen nooit "ongebruikt". Ze bestaan juist om vanuit code gebruikt te worden, via het member en niet als tekst. Dat kunnen we niet volgen.
- Rename Resource Key verschijnt niet bij een statische key. De key is de naam van een member in C#; hernoemen hoort bij de C#-refactoring van VS.

**De les.** Toen de keys op tien plekken met een eigen regex gelezen werden, betekende een nieuwe vorm van key tien aanpassingen. Nu is het er één. Zoek bij een nieuwe feature eerst waar dezelfde tekst al gelezen wordt, en maak er één functie van voordat je hem uitbreidt.

### 29. Een DataTemplate renderen met voorbeelddata

**De vraag.** Dezelfde gebruiker als in sectie 28 wilde de layout van zijn templates zien (controls, afstanden, uitlijning) zonder de app te starten of een tijdelijke UserControl te maken. Tot nu toe toonden we bij een DataTemplate alleen de boom, omdat bindings zonder data leeg blijven.

**Drie keuzes,** samen met jou gemaakt:

| Vraag | Keuze |
|---|---|
| Waar komen de waarden voor bindings vandaan? | Automatisch, en `d:Text="120"` voor een eigen waarde |
| Wat gebeurt er met eigen controls en converters? | Een eigen control wordt een gestreept vak, een eigen converter valt weg |
| Welke templates? | DataTemplate en ItemsPanelTemplate; HierarchicalDataTemplate houdt alleen de boom |

**Twee stappen, twee klassen.** Net als bij de rest van de extensie staat het werk met tekst en XML los van het werk met WPF:

1. `TemplateSampleBuilder` (in `Resources`, alleen XML) maakt een kopie van de template die kan laden. Dat draait op een achtergrondthread, samen met de rest van `ResourcePreviewData.Create`.
2. `TemplateSampleRenderer` (in `Preview`, WPF) zet die template op het scherm met voorbeelddata. Dat draait op de UI-thread.

**Stap 1: de kopie schoonmaken.** Per element en attribuut:

| In de template | Wordt |
|---|---|
| `<local:Rating Grid.Column="1" Margin="4" />` | een `Grid` met een gestreepte `Rectangle` en de tekst `local:Rating`, met dezelfde `Grid.Column` en `Margin` |
| `{Binding Price, Converter={StaticResource PriceConverter}}` | `{Binding Price}` als de converter een eigen type is |
| `Click="OnOpen"`, `Loaded="OnLoaded"` | weg: `XamlReader` kan een event niet koppelen zonder code-behind |
| `Command="{x:Static local:Commands.Open}"`, `local:Help.Text="..."` | weg |
| `DataType="{x:Type local:Book}"` | weg |
| `d:Text="120"` | `Text="120"`, zoals de XAML-designer doet |
| `<Setter TargetName="Stars" ...>` op een element dat een vak werd | weg, anders faalt het laden |

Om een converter uit een binding te halen moet je de markup kunnen splitsen. Een komma scheidt de delen, maar niet binnen accolades of aanhalingstekens: in `{Binding Price, StringFormat='{}{0}, net'}` zit een komma die bij de StringFormat hoort. `SplitMarkup` telt daarom de diepte van de accolades en onthoudt of hij binnen quotes zit.

Of iets een event is, vraagt de builder aan WPF zelf: `typeof(Button).GetEvent("Click")`. Dat is gewone reflectie op WPF-types die VS al geladen heeft, dus dat mag op een achtergrondthread.

**Een valkuil.** De eerste versie zette de typenaam in het vak als `Text="local:Rating"`. De veiligheidscontrole uit sectie 26 leest alle attributen en zag daar een verwijzing naar een eigen type. Het vak blokkeerde zo zijn eigen preview. Nu staat de naam als inhoud: `<TextBlock>local:Rating</TextBlock>`.

**Stap 2: voorbeelddata.** De builder geeft ook een lijst van bindings mee: het pad, het element en de property. Per binding kiest de renderer een waarde:

| Property | Waarde |
|---|---|
| tekst (`string` of `object`, zoals `Text`, `Content`, `ToolTip`) | de naam van het pad: `{Binding Title}` toont "Title" |
| een lijst (`ItemsSource`) | drie items: "Chapters 1", "Chapters 2", "Chapters 3" |
| iets anders (`IsReadOnly`, `FontSize`) | de standaardwaarde van die property, zodat het eruitziet alsof er geen binding is |

`Author.Name` maakt een genest object. Wordt één pad voor tekst en voor iets anders gebruikt, dan wint de tekst.

**Waarom geen ExpandoObject.** WPF kan binden aan een `ExpandoObject`, maar gaat daarvoor via de DLR. Die gooit en vangt intern een exceptie voor elk member dat hij opzoekt. De test die alle SampleApp-resources rendert, staat geen enkele exceptie toe (ook geen opgevangen), omdat een debugger met "break when thrown" er anders op stopt. `SampleObject` implementeert daarom `ICustomTypeDescriptor`: WPF vraagt de properties op via `TypeDescriptor`, net als bij een `DataRowView` uit een `DataTable`. Geen DLR, geen excepties.

**ItemsPanelTemplate.** Een `ItemsControl` met de template als `ItemsPanel` en zes omrande items, 260 pixels breed. Zo zie je of een `WrapPanel` ze over regels verdeelt.

**Testen.** `TemplateSampleTests` controleert de kopie (vakken, converters, events, `d:`-waarden, triggers) en het renderen: de `TextBox` uit het voorbeeld van de gebruiker toont "Value" en is niet read-only. De SampleApp kreeg `PropertyRowTemplate` met een eigen converter, `FancyControl` en `d:Text`. De bestaande test die elke resource rendert, doet nu ook `Measure` en `Arrange`, zoals de tooltip. Zo vallen ook fouten op die pas optreden als WPF de template toepast.

## Hoe het zoeken werkt

VS heeft geen publieke API om te vragen waar een resource gedefinieerd is. `ResourceIndex` bouwt dat zelf op:

1. Zoek de solution-map: de eerste map boven het bestand met een `.sln` of `.slnx`. Geen gevonden, dan de root van de git-repository.
2. Lees alle `.xaml`-bestanden daaronder (behalve `bin`, `obj`, `.vs`, `.git`, `node_modules`) en onthoud elk element met een `x:Key`, plus de `MergedDictionaries` van elk bestand.
3. Een `FileSystemWatcher` houdt bij welke bestanden daarna wijzigen. Die worden bij de volgende hover opnieuw gelezen.
4. Het bestand dat open staat in de editor telt mee inclusief niet-opgeslagen wijzigingen.
5. Bij meerdere definities bepaalt `MergeGraph` de volgorde, zoals WPF dat doet (sectie 15).

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

`tests\ResourcePreview.Tests` bevat 683 tests die zonder Visual Studio draaien. Open Test Explorer (Test > Test Explorer) en klik op Run All. Dat duurt een paar seconden.

| Bestand | Wat het test |
|---|---|
| `ResourceReferenceFinderTests` | welke key onder de muis staat: `{StaticResource X}`, `ResourceKey=`, element-syntax, `x:Key`, nesting, net ernaast, en `TryFindReference` dat definities overslaat |
| `ResourceIndexTests` | parsen, regel en kolom, ongeldige XML, de solution-map vinden, zoeken over bestanden, `bin`/`obj` overslaan, live tekst uit de editor, wijzigingen op schijf |
| `PreviewXamlBuilderTests` | volgorde van afhankelijkheden, kringverwijzingen, ontbrekende keys, `DynamicResource` → `StaticResource`, pack-URI's, relatieve paden |
| `EndToEndTests` | de iconen uit `samples\SampleApp` door de hele keten tot en met `XamlReader`, en de renderer: tegels, grootte, kleuren, foutmeldingen |
| `ValuePreviewTests` | fonts (geïnstalleerd, ontbrekend, in een map), `Thickness` en `CornerRadius` met schalen, losse waarden met Nederlandse regio-instellingen, effecten, font-paden in alle schrijfwijzen, `System.Runtime` → `mscorlib` |
| `TemplateTests` | de boom (bindings, property-elementen, prefixen, maximum aan regels en diepte), het live voorbeeld bij Style en ControlTemplate, eigen types, welke controls we kunnen maken, `FillContent` per control |
| `MergeGraphTests` | `MergedDictionaries` lezen, `Source` in alle schrijfwijzen, de opzoekvolgorde (laatste merge wint, eigen keys eerst, geneste merges, kringen), niet-gemergde bestanden, de Error List-scan, en `InfoBrush` en `Check` uit de SampleApp |
| `StateSimulatorTests` | Muis erover en Ingedrukt: setters met `TargetName`, de volgorde van triggers, `MultiTrigger` met andere condities, `BasedOn`, `DataTrigger` op `IsMouseOver`, de `VisualStateManager` |
| `IntelliSenseTests` | wanneer de cursor op een key-plek staat, en de iconen van `CompletionIconFactory` (nu voor het venster XAML Resources): welke types er een krijgen, iconen uit de SampleApp en de cache |
| `ReferenceCheckerTests` | verwijzingen vinden (ook in commentaar en element-syntax), ontbrekende keys met hoofdlettersuggestie, keys die verderop staan, keys in een niet-geladen bestand, geen meldingen bij externe dictionaries, zonder App.xaml of in een UserControl, en precies de bekende problemen in de SampleApp |
| `UsageFinderTests` | alle verwijzingen naar een key, welke definitie elke verwijzing krijgt, een key zonder definities, en `InfoBrush` uit de SampleApp |
| `UnusedResourceTests` | ongebruikte keys, gebruik vanuit code, keys in Window.Resources, geen meldingen in niet-gemergde dictionaries, themabestanden, ThemeDictionaries en zonder App.xaml, en alleen `UnusedBrush` in de SampleApp |
| `KeyRenamerTests` | alle vormen van definitie en verwijzing hernoemen, andere keys, gewone tekst en commentaar ongemoeid laten, keys met punten, welke bestanden veranderen, en welke namen geweigerd worden |
| `ExtractPlannerTests` | welke waarden een lampje krijgen en welk type ze worden, de XAML van de resource, invoegen in een dictionary en in App.xaml, `xmlns:sys` toevoegen of hergebruiken, invoegen boven het gebruik in hetzelfde bestand, en de doelbestanden in de SampleApp |
| `StylePlannerTests` | geselecteerde attributen vinden (ook over meerdere regels), events en namen overslaan, de nieuwe stijl en het aangepaste element, `BasedOn` bij een bestaande stijl, setters toevoegen na de laatste setter, bestaande vervangen en een lege stijl openmaken |
| `ResourceMatcherTests` | stijlen die precies of deels passen, stijlen die meer zetten of andere waarden hebben, `TargetType` met overerving, `BasedOn` en triggers, setters met een verwijzing, attached properties, losse waarden in andere spellingen, de volgorde, het attribuut onder de cursor en welke resources een element ziet |
| `ColorSwatchTests` | welke waarden een kleurvakje krijgen (attributen, setters, `<Color>`, verwijzingen) en welke niet (tekst, bindings, commentaar), en de kleur van een key: via een `Color`-resource, met `Opacity`, een gradient, een kring |
| `ResourceCatalogTests` | welke resources het venster toont (hele solution of wat één bestand ziet), de notities overschreven, niet geladen en ongebruikt, de volgorde per bestand en per type, zoeken, en de bekende notities in de SampleApp |
| `NoExceptionTests` | welke types VS niet kan laden, in elementen, attributen en waarden, ook via afhankelijkheden; elke resource uit de SampleApp zonder één exceptie; `ColorParser` tegen alle WPF-kleurnamen |
| `StyleTests` | `TargetType` in alle schrijfwijzen, de `BasedOn`-keten met overschreven setters, de soorten waarden, triggers en binding-paden, en de weergave van de tabel |
| `SettingsAndLanguageTests` | kleuren en getallen, taalcodes van VS, de converters van de Opties-pagina, `Localizer` |
| `StaticKeyTests` | keys als `{x:Static ...}`: normaliseren met en zonder prefix, de index met `KeyText`, verwijzingen en hover, Find References met een andere prefix, geen meldingen voor `SystemColors`, wel voor een typfout in een bekende klasse, nooit "ongebruikt", de preview die laadt, en `BasedOn` met de tekst zoals geschreven |
| `TemplateSampleTests` | de kopie voor de gerenderde DataTemplate: eigen controls als vak op dezelfde plek, eigen converters weg en WPF-converters niet, events, `x:Static` en `DataType` weg, `d:Text`, triggers op een vak, welke bindings meetellen, `SplitMarkup`; en het renderen: tekst, geneste paden, lijsten, standaardwaarden, een `WrapPanel` met zes items, en de templates uit de SampleApp |
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
6. Hover over `SearchBox`, `RoundButtonTemplate`, `BookTemplate`, `FancyTemplate`, `FancyStyle` en `WrapPanelTemplate` onderaan `MainWindow.xaml`. `SearchBox` en `RoundButtonTemplate` tonen een echt control, normaal en uitgeschakeld, en die zien er verschillend uit. `DangerButton` toont er drie: Normaal, Muis erover en Ingedrukt, met een steeds lagere doorzichtigheid (1, 0,8 en 0,6). Uitgeschakeld ontbreekt: die stijl heeft geen trigger op `IsEnabled`. `BookTemplate` toont de boom met bindings. `FancyTemplate` en `FancyStyle` tonen de melding dat VS `local:FancyControl` niet kan laden.
7. Klik op de bestandsnaam en op het plaatje: VS opent het bestand met de key geselecteerd, ook als het al open stond.
   Rechtsklik op `{StaticResource PrimaryButton}`: **Go To Resource Definition** staat in het menu en springt naar `Styles.xaml`. Op een regel zonder verwijzing staat het item er niet. Ctrl+Alt+F12 doet hetzelfde, en opent geen "Find Symbol Results".
   Rechtsklik op `x:Key="InfoBrush"` in `Brushes.xaml` en kies Find Resource References (of Shift+Alt+F12): het venster toont twee definities en één verwijzing in `MainWindow.xaml`, met "gebruikt de definitie in Values.xaml". Dubbelklik op de verwijzing opent `MainWindow.xaml` op die regel.
   In de Error List (met Messages aan) staat ook een bericht voor `UnusedBrush` in `Brushes.xaml`, en niet voor `CodeOnlyBrush`.
   Rechtsklik op `InfoBrush` in `MainWindow.xaml` en kies Rename Resource Key...: de dialoog noemt 2 definities en 1 verwijzing in 3 bestanden. Probeer `AccentBrush` (bestaat al) en `Info Brush` (spatie): de knop blijft uit. Hernoem naar `NoticeBrush`, controleer de drie bestanden, en draai het terug (Ctrl+Z in de open bestanden, versiebeheer voor de rest).
   Zet de cursor in een vaste kleur of marge in `MainWindow.xaml` en druk Ctrl+.: kies Naar resource verplaatsen..., kies `Brushes.xaml` en controleer beide bestanden. Draai het daarna terug, ook in de bestanden die niet open stonden.
   Selecteer in `MainWindow.xaml` bij een `Path` de attributen `Fill` tot en met `Margin` en kies Naar stijl verplaatsen...; controleer de nieuwe stijl. Selecteer daarna `Padding="0"` op een element met een stijl en kies Toevoegen aan stijl. Zet alles daarna terug, ook in bestanden die niet open stonden.
   Selecteer bij de knop "Plain" onderaan `MainWindow.xaml` de attributen `Padding` tot en met `Background` en kies Passende resource zoeken...: `BaseButton` staat bovenaan en neemt `Padding`, `FontSize` en `Background` over; daaronder `AccentBrush` voor `Background`. Kies `BaseButton` en controleer dat de drie attributen vervangen zijn door `Style="{StaticResource BaseButton}"`. Zet het terug.
   Open `Brushes.xaml` en `MainWindow.xaml`: voor elke kleur en elke verwijzing naar een kleur-brush staat een vakje. Verander de kleur van `AccentBrush` in `Brushes.xaml` en sla op: het vakje bij `{StaticResource AccentBrush}` in `Styles.xaml` past zich aan. Zet de instelling Kleurvakjes uit: de vakjes verdwijnen meteen.
   Open View > Other Windows > XAML Resources. Per bestand staat `Values.xaml` boven `Brushes.xaml`; `InfoBrush` in `Brushes.xaml` heeft "overschreven door Values.xaml", `UnusedBrush` "ongebruikt" en `IconsLegacy.xaml` "in geen enkele MergedDictionaries". Zoek op `brush`, schakel naar Per type en zet Alleen wat het actieve bestand kan gebruiken aan. Hover voor de preview, dubbelklik om te openen, en sleep `AccentBrush` naar een attribuut in `MainWindow.xaml`.
   Hover over `InfoBrush` in `MainWindow.xaml`: bovenaan `Values.xaml` met "WPF gebruikt hier deze definitie.", eronder `Brushes.xaml` met "overschreven door Values.xaml". Bij `Check` staat achter `IconsLegacy.xaml` "in geen enkele MergedDictionaries".
   Open de Error List: één waarschuwing voor `InfoBrush` in `Brushes.xaml`. Dubbelklik springt naar de definitie. Haal `InfoBrush` weg uit `Values.xaml` en sla op: na een paar seconden is de waarschuwing weg. Zet hem daarna terug.
8. Typ in `Icons.xaml` een nieuwe `<Geometry x:Key="Nieuw">` zonder op te slaan, en hover erover in hetzelfde bestand: de preview werkt al.
   Open `Broken\ReferenceProblems.xaml` en de Error List: vier meldingen uit dat bestand (`LateBrush`, `accentBrush` met "Bedoel je 'AccentBrush'?", `LegacyArrow`, en `ThemeBackgroundFromCode` als bericht) plus `DoesNotExist` uit `MainWindow.xaml`. Hover over `LateBrush`: de melding staat ook in de tooltip.
9. Nieuw Opties-venster > XAML Resource Preview: er staat maar één categorie, met General en Appearance, en de labels zijn tekst (geen `@...`).
10. Zet Tegels op "Dark only" en tegelgrootte op 32, en hover: één kleine donkere tegel. De kleurvelden van de lichte tegel zijn grijs.
11. Legacy-Opties-venster: dezelfde waarden als in het nieuwe venster. Wijzig daar de taal naar Deutsch, klik OK en hover: "Zeile" in plaats van "line".
12. Zet de taal terug op Automatisch.

## Beperkingen

- **Eigen types.** Een resource die zelf een type uit je project is (`<local:IconDefinition x:Key=... />`) of een eigen markup extension bevat, kan niet laden. VS draait op .NET Framework 4.8 en kent je assembly niet. De tooltip toont dan de foutmelding.
- **Keys buiten de solution.** Resources uit een NuGet-pakket of een theme-DLL worden niet gevonden.
- **Scopes binnen een bestand.** Het hele huidige bestand telt als één scope. Een key in `Grid.Resources` wint dus van `App.xaml`, ook voor elementen buiten die grid.
- **Resources uit code** (`Application.Current.Resources.MergedDictionaries.Add(...)`) volgen we niet. Zo'n bestand krijgt "in geen enkele MergedDictionaries".
- **Een UserControl** ziet tijdens runtime ook de resources van het venster waar hij in staat. Dat venster kennen we niet; we volgen alleen de UserControl zelf en `App.xaml`.
- **Excepties die blijven.** Twee situaties gooien nog een exceptie die we zelf opvangen: een XAML-bestand dat tijdens het typen even geen geldige XML is (`XmlException` in `ResourceIndex`), en een template die wel laadt maar pas bij het tekenen faalt (in `LiveSampleRenderer`). Het eerste valt niet vooraf te controleren zonder een eigen XML-parser. Zie je ze in de debugger, dan is dat geen fout.
- **Andere markup als key**, zoals `x:Key="{x:Type Button}"` of `{ComponentResourceKey ...}`, slaan we over. Alleen `{x:Static ...}` wordt ondersteund (sectie 28).
- **Verwijzingen over meerdere regels** worden niet herkend. De finder kijkt per regel.
- **Keys die in code worden samengesteld** (`$"{naam}Brush"`) ziet de extensie niet. Zo'n resource krijgt ten onrechte "ongebruikt"; dat is een bericht, geen waarschuwing.
- **Afbeeldingen met een http-adres** (`BitmapImage UriSource="https://..."`) worden voor de preview gedownload.
- **Twee threads met verschillende tekst** voor `SetLiveText` tegelijk: de oudere kan winnen. De volgende wijziging herstelt het.

## Ideeën voor later

- **Find Elements That Could Use This Style**: de omgekeerde richting van sectie 23. Rechtsklik op een stijl en zie de elementen die precies zijn setters als losse attributen hebben; jij kiest welke je omzet.
- **HierarchicalDataTemplate renderen**, net als een DataTemplate in sectie 29, met een paar kinderen uit `ItemsSource`.
- **Een nieuwe extensie: overlappende extensies vinden.** Vergelijk wat geïnstalleerde extensies registreren per content type (taggers, Quick Info-bronnen, completion-bronnen, lampjes) en laat zien waar twee extensies hetzelfde doen, zoals Color Picker Tool, de eigen kleurvakjes van VS en de onze.
