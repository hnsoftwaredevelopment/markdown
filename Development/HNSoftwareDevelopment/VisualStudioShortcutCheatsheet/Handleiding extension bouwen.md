# Shortcut Cheatsheet: handleiding

Leerdocument bij de extensie Shortcut Cheatsheet. Per stap: wat er gebouwd is, hoe het werkt en waarom. Het onderzoek vooraf staat in [[Haalbaarheid en voorstel v1]].

## Mappen

```
VisualStudioShortcutCheatsheet/
├─ ShortcutCheatsheet.sln
├─ Directory.Build.props                ← output naar Builds\<project>\
├─ external/ExtensionCommon/            ← gedeelde code, git-submodule
├─ src/ShortcutCheatsheet/
│  ├─ source.extension.vsixmanifest     ← wat zit erin, voor welke VS-versies
│  ├─ ShortcutCheatsheetPackage.cs      ← AsyncPackage: menu-command en tool window
│  ├─ ShortcutCheatsheetPackage.vsct    ← het menu-item View > Other Windows > Shortcut Cheatsheet
│  └─ ToolWindow/CheatsheetWindow.cs    ← het venster (nu nog leeg)
├─ tests/ShortcutCheatsheet.Tests/      ← MSTest, net48
└─ tools/build-and-test.ps1
```

## Stap 1: de opzet

### Twee repo's en een branch

`main` heeft één commit: de licentie en `.gitignore`. Al het werk gebeurt op `feature/v1`. Pas als jij de versie goedkeurt, gaat hij naar `main` en verdwijnt de branch. Zo blijft `main` altijd iets dat je kunt bouwen en installeren.

### Gedeelde code: Shared Project als submodule

`InstalledExtensions.cs` (welke extensies zijn ingeschakeld en waar staan ze) is nodig in ExtensionOverlap en in deze extensie. Eén bron, in de repo `ExtensionCommon`.

**Waarom een Shared Project.** Een gewone class library levert `ExtensionCommon.dll`. Installeer je twee extensies die elk hun eigen versie meebrengen, dan laadt VS die DLL één keer, in één proces. De tweede extensie krijgt de versie van de eerste, of een fout. Een Shared Project (`.shproj`) heeft geen eigen uitvoer: de `.cs`-bestanden worden meegecompileerd in `ShortcutCheatsheet.dll`. Elke extensie heeft dan zijn eigen kopie, in zijn eigen assembly.

Daarom zijn alle klassen in ExtensionCommon `internal`. Een `public` klasse `ExtensionCommon.VisualStudio.InstalledExtensions` in twee assemblies zou botsen zodra iemand beide refereert.

**Hoe het werkt.** Een Shared Project bestaat uit twee bestanden:

| Bestand | Wat het doet |
|---|---|
| `ExtensionCommon.projitems` | de lijst met `.cs`-bestanden; dit importeert de extensie |
| `ExtensionCommon.shproj` | alleen voor Solution Explorer, zodat je de bestanden ziet en kunt bewerken |

In `ShortcutCheatsheet.csproj`, vóór `Microsoft.CSharp.targets`:

```xml
<Import Project="..\..\external\ExtensionCommon\ExtensionCommon.projitems" Label="Shared" />
```

MSBuild voegt de `<Compile>`-regels uit `.projitems` toe aan het project, alsof ze er zelf in stonden.

In de `.sln` staat de sectie `SharedMSBuildProjectFiles`. Die vertelt VS welk project de gedeelde bestanden importeert, zodat IntelliSense in een gedeeld bestand de juiste context heeft. Voor de build doet die sectie niets.

**Waarom een submodule.** De repo's staan los op GitHub. Een map naast de repo (`..\ExtensionCommon`) werkt lokaal, maar in GitHub Actions bestaat die map niet. Een submodule is een verwijzing naar één commit van een andere repo, opgeslagen in de eigen repo:

```
git submodule add https://github.com/hnsoftwaredevelopment/ExtensionCommon.git external/ExtensionCommon
```

Dat maakt `.gitmodules` (de URL) en een speciale regel `external/ExtensionCommon` met de commit-hash (in `git status` zie je mode `160000`). De bestanden zelf staan niet in deze repo.

Gevolgen in de praktijk:

| Situatie | Wat je doet |
|---|---|
| Nieuwe clone | `git clone --recurse-submodules ...`, of daarna `git submodule update --init` |
| GitHub Actions | `actions/checkout` met `submodules: true` |
| ExtensionCommon wijzigen | in `external\ExtensionCommon` committen en pushen (dat is de andere repo), daarna in deze repo de nieuwe commit vastleggen met `git add external/ExtensionCommon` |
| Nieuwe versie van ExtensionCommon ophalen | `git submodule update --remote`, dan committen |

Een extensie gebruikt dus altijd een vaste versie van de gedeelde code. Wijzigt ExtensionCommon voor de ene extensie, dan merkt de andere dat pas als je hem bewust bijwerkt.

`build-and-test.ps1` controleert of `external\ExtensionCommon\ExtensionCommon.projitems` bestaat. Zonder die controle krijg je bij een clone zonder submodule een onduidelijke MSBuild-fout over een ontbrekende import.

### Het package en het menu

Zelfde opbouw als ExtensionOverlap:

- `ShortcutCheatsheetPackage` is een `AsyncPackage` met `[ProvideMenuResource]` en `[ProvideToolWindow]`.
- `ShortcutCheatsheetPackage.vsct` zet een knop in de groep `IDG_VS_WNDO_OTRWNDWS1`: het menu View > Other Windows.
- Het manifest heeft alleen een `VsPackage`-asset. Er zijn (nog) geen MEF-onderdelen, dus de `MefComponent`-asset is weggelaten.
- `InstallationTarget Version="[18.0,19.0)"`: alleen VS 2026.

Na de build staat in `Builds\ShortcutCheatsheet\Debug\ShortcutCheatsheet.pkgdef`:

```
[$RootKey$\Menus]
"{acf2e531-e047-4046-9f60-a0765ab33ef5}"=", Menus.ctmenu, 1"
```

Dat is dezelfde regel waarmee deze extensie straks bij andere extensies de command table vindt (sectie 3c van het voorstel). Onze eigen `Menus.ctmenu` wordt daarmee ook testmateriaal.

### Tests

`ConsistencyTests` controleert twee dingen die op twee plekken staan:

- De GUID's en het command-ID in de `.vsct` zijn gelijk aan de constanten in `ShortcutCheatsheetPackage`. Wijkt dat af, dan staat het menu-item er wel, maar doet een klik niets.
- De gedeelde code zit in de assembly. Die test compileert niet eens als de submodule ontbreekt.

**Valkuil: waar staat de repo?** De eerste versie zocht `ShortcutCheatsheet.sln` vanaf `AppDomain.CurrentDomain.BaseDirectory` naar boven. Dat faalde: vstest draait de test-DLL niet altijd vanuit de build-map. De oplossing is `[CallerFilePath]`: de compiler vult het pad van het bronbestand in. Vanaf `tests\ShortcutCheatsheet.Tests\` naar boven zoeken vindt de repo altijd, ook in GitHub Actions, omdat daar op dezelfde machine gebouwd en getest wordt.

### Werken via Desktop Commander

Desktop Commander weigert opdrachten met bepaalde woorden, waaronder `init`. `git init` kon dus niet. De omweg: de lege GitHub-repo klonen naar een tijdelijke map en de map `.git` verplaatsen naar de projectmap. Het resultaat is hetzelfde als `git init` plus `git remote add origin`.

### Bekend probleem: het menu-item verschijnt niet

Na F5 stond Shortcut Cheatsheet niet onder View > Other Windows. De extensie was nooit in de Experimental Instance gezet: in `%LocalAppData%\Microsoft\VisualStudio\18.0_3fdcf796Exp\Extensions\` ontbrak de map.

De oorzaak zat bij een andere extensie. Bij het deployen leest de VSSDK eerst de manifesten van alle extensies die al in de Experimental Instance staan (taak `FindInstalledExtension`). In de map van XAML Resource Preview waren `extension.vsixmanifest`, `catalog.json` en `manifest.json` 0 bytes groot. Die waren om 11:27:42 opnieuw geschreven, terwijl de Experimental Instance draaide en de DLL van ResourcePreview in gebruik was. Die deploy is halverwege gestopt. Daarna faalt elke deploy met:

```
error MSB4018: The "FindInstalledExtension" task failed unexpectedly.
InvalidExtensionManifestException: This VSIX does not apply to any product installed on this machine.
```

Het lastige is dat de melding de schuld bij je eigen VSIX legt, terwijl een ander manifest kapot is. In Visual Studio zie je hem alleen in het Output-venster bij Build; de Experimental Instance start gewoon, zonder je extensie.

Opgelost door de drie bestanden opnieuw uit `ResourcePreview.vsix` te halen (een VSIX is een zip-bestand). Daarna lukte de deploy.

Lessen:

- Deploy niet vanuit twee solutions tegelijk naar dezelfde Experimental Instance, en niet terwijl die draait.
- Staat je menu-item er niet, kijk dan eerst of de map van je extensie in `...Exp\Extensions\` staat. Zo niet, dan zit het probleem in de deploy en niet in je `.vsct`.
- Zoek in die map naar bestanden van 0 bytes: `Get-ChildItem -Recurse -File | Where-Object Length -eq 0`.

**Een tweede oorzaak, direct daarna.** Na het herstel stond de map er wel, en Manage Extensions noemde de extensie actief. Toch ontbrak het menu-item. Via DTE bleek dat de Experimental Instance het command `View.ShortcutCheatsheet` niet kende: de `.pkgdef` was niet ingelezen.

VS leest de `.pkgdef`-bestanden niet bij elke start. Het houdt een samengevoegde configuratie bij en bouwt die alleen opnieuw op als het bestand `Extensions\extensions.configurationchanged` nieuwer is dan de vorige keer. De deploy raakt dat bestand aan in de laatste stap, en juist die stap was mislukt (VSSDK1031). Na het bijwerken van de datum van dat bestand en een herstart stond het menu-item er.

Zelf doen: `(Get-Item "$env:LOCALAPPDATA\Microsoft\VisualStudio\18.0_<id>Exp\Extensions\extensions.configurationchanged").LastWriteTime = Get-Date`, of `devenv /rootsuffix Exp /updateconfiguration`.

## Stap 2: de command table van een extensie lezen

Doel: per command weten welke extensie hem levert, en welke sneltoetsen die extensie standaard meebrengt. Die informatie staat in de gecompileerde command table van het package. De code staat in `src\ShortcutCheatsheet\CommandTables\` en heeft geen Visual Studio nodig.

### Waar de tabel staat

1. In de `.pkgdef` van de extensie staat welk package een command table heeft, en onder welke naam:

   ```
   [$RootKey$\Menus]
   "{4c82e17d-927e-42d2-8460-b473ac7df316}"=", Menus.ctmenu, 1"
   ```

   De waarde is "satellite-DLL, resourcenaam, versie". Bijna altijd is de naam `Menus.ctmenu`; Advanced Installer gebruikt `1000`. `PkgdefMenus` leest dit.
2. De tabel is een byte-array in een `.resources`-bestand, en dat zit als resource in de DLL. Bij de meeste extensies in de DLL zelf (`VSPackage.resources`), bij CodeMaid in `en-US\SteveCadwallader.CodeMaid.VS2022.resources.dll` (`VSPackage.en-US.resources`). `CommandTableResource` zoekt in die volgorde: de DLL, de en-US-satellite, de andere satellites.

**Lezen zonder te laden.** `PEReader` (uit `System.Reflection.Metadata`) leest de DLL als bytes. Een embedded resource staat op "resources-directory plus offset", met eerst 4 bytes lengte. `ResourceReader.GetResourceData` geeft daarna de ruwe bytes van één resource, zonder objecten te maken. Er draait dus geen code van de extensie, net als in ExtensionOverlap. Een byte-array krijgt van `ResourceReader` nog 4 bytes lengte vooraan; die halen we eraf.

### Het formaat

Niet gedocumenteerd. Uitgezocht met een eigen testtabel en met VSCT zelf:

- **VSCT kan terugvertalen.** `VSCT.exe Menus.cto uit.vsct` maakt van een gecompileerde tabel weer XML. Dat is wat VS zelf in de tabel ziet, en dus het antwoordmodel voor de tests.
- **Een eigen fixture.** `tests\Fixtures\CommandTables\Fixture.vsct` heeft vier commands in twee command sets, een command van VS (Cut) dat alleen in een menu geplaatst wordt, en vier sneltoetsen: een gewone, een akkoord in de Text Editor, een met Alt, en een voor Cut. `tools\build-fixtures.ps1` compileert hem met de VSCT uit de NuGet-cache en vertaalt hem meteen terug.

Gecomprimeerd:

| Deel | Inhoud |
|---|---|
| 20 bytes kop | `CFCT`, versie 5, totale grootte na uitpakken, 20, 0 |
| per blok | 16 bytes kop (4 bytes, grootte uitgepakt, 4 bytes, grootte gecomprimeerd), dan de data |

Een blok is maximaal 64 KB. Onze eigen tabel is 137 KB uitgepakt, omdat hij `KnownImageIds.vsct` insluit voor het icoon, en heeft dus drie blokken. De eerste versie van `CtoDecompressor` ging uit van één blok: de fixture en CodeMaid (40 KB) werkten, onze eigen tabel gaf fout `0xC0000242` (STATUS_BAD_COMPRESSION_BUFFER). De test die onze eigen DLL leest, vond dat.

Elk blok is Xpress Huffman. Windows pakt dat zelf uit: `RtlDecompressBufferEx` in `ntdll.dll`, formaat 4.

Uitgepakt:

| Deel | Inhoud |
|---|---|
| kop | `CFCT`, versie 5, 0, offset van de GUID-tabel, 0 |
| `Symb` | per GUID de naam uit de `.vsct` en de namen van zijn ID's |
| GUID-tabel | alle GUID's achter elkaar; de rest van het bestand verwijst ernaar met een index die bij 1 begint |
| `Menu`, `Grup` | menu's en groepen |
| `Cmmd` | de commands die deze tabel definieert, met knoptekst en canonieke naam |
| `Bimp` | iconen |
| `Plac` | commands die alleen in een menu geplaatst worden, ook die van VS |
| `Keys` | de standaardsneltoetsen |

Een `Cmmd`-regel: GUID-index, parent-index, ID, parent-ID, 16 bytes prioriteit, icoon en vlaggen, type, lengte van de teksten, en dan zes teksten (knoptekst, menutekst, tooltip, command-well-tekst, canonieke naam, gelokaliseerde canonieke naam), elk afgesloten met een 0-teken.

Een `Keys`-regel is 16 bytes: command-GUID, emulatie-GUID, command-ID, editor-GUID (de scope: `guidVSStd97` is Global), 2 bytes, en dan toets 1, modifiers 1, toets 2, modifiers 2. De toetsen zijn Windows virtual-key-codes (`0x70` is F1). De modifiers zijn bits: Alt 1, Shift 2, Ctrl 4.

**Het belangrijkste verschil voor de herkomst.** CodeMaid noemt GUID's van VS (XAML Designer, JSON Editor, HTML) omdat het zich aan die menu's hangt. Die staan in `Symb` en in `Plac`, maar nooit in `Cmmd`. Alle 30 commands in `Cmmd` van CodeMaid hebben CodeMaids eigen command set. Daarmee is het probleem van de GUID-zoekmethode uit het voorstel opgelost.

### Secties vinden zonder lengte

Een sectie heeft een naam en een aantal, maar geen lengte in bytes, en de regels zijn per sectie anders. Een onbekende sectie kun je dus niet overslaan. `Bimp` bevat zelfs de pixels van de iconen.

Daarom leest `CommandTableReader` `Symb` direct (die staat altijd op byte 20), en zoekt hij `Cmmd` en `Keys` op hun naam. Een treffer telt alleen als elke regel klopt (geldige GUID-indexen, een lengte die past) en de sectie precies eindigt waar de volgende naam begint of waar de data ophoudt. Een toevallige reeks `Keys` in de pixels van een icoon haalt die controle niet.

### Tests

| Test | Wat |
|---|---|
| `Reads_the_commands_the_table_defines` | de vier commands, met knoptekst, symboolnaam en canonieke naam |
| `A_command_that_is_only_placed_is_not_defined` | Cut staat in `Plac` en heeft een sneltoets, maar is van VS |
| `Reads_key_bindings_with_scope_and_chords` | Ctrl+Shift+F1, het akkoord Ctrl+K, Ctrl+Q in de Text Editor, Alt+D |
| `Matches_what_VSCT_decompiles` | voor elke fixture: dezelfde commands en sneltoetsen als VSCT terugvertaalt |
| `Reads_the_table_of_this_extension_from_its_dll` | de hele keten op onze eigen DLL: resource, drie blokken, tabel |
| `Reads_CodeMaid_from_its_satellite_when_installed` | een echte extensie met de tabel in een satellite; slaat over als CodeMaid er niet is |
| `Every_installed_command_table_can_be_read` | alle geïnstalleerde extensies van VS 2026 op deze machine: 125 tabellen, 188 sneltoetsen, ongeveer een seconde |
| `Rejects_data_that_is_not_a_command_table` | geen CFCT, afgekapt, andere versie: altijd `FormatException` |

De test over alle geïnstalleerde extensies vond de tabel met de naam `1000` van Advanced Installer. Zonder `PkgdefMenus` was die gemist.

### Valkuilen

- **VSCT schrijft bij terugvertalen een `.h` in de huidige map.** De eerste keer stonden er twee losse bestanden in de root van de repo. `build-fixtures.ps1` draait VSCT nu vanuit de fixturemap.
- **Een test buiten vstest.** Een PowerShell-script dat de reader via reflection aanriep, vond in geen enkele extensie een tabel; de echte test vond ze allemaal. Waarschijnlijk laadt PowerShell 5.1 een andere `System.Reflection.Metadata`. Controleer zoiets dus in een test, niet in een los script.
- **Automatic Versions.** Bij bouwen in VS zet die extensie de versie in `AssemblyInfo.cs` en in de `.csproj` van de tests op de datum (`2026.11.13.2`). Dat komt mee in de commits.

## Stap 3: alle sneltoetsen verzamelen, met herkomst

Het resultaat is een `CheatSheet`: een lijst `Shortcut`-objecten plus een regel per extensie. Het venster toont voorlopig alleen een samenvatting en een knop Export to JSON, zodat je de gegevens kunt controleren voordat de echte weergave er is (stap 4).

### De keten

| Stap | Klasse | Thread | Doet |
|---|---|---|---|
| 1 | `DteBindingReader` | UI | elk command uit `DTE.Commands` met zijn `Bindings` ("Text Editor::Ctrl+E, V") |
| 2 | `InstalledExtensions` (ExtensionCommon) | UI, dan achtergrond | de mappen van de ingeschakelde extensies |
| 3 | `ExtensionCommands` | achtergrond | per extensie de `.pkgdef`, de DLL van het package en de command table |
| 4 | `Customizations` | achtergrond | jouw eigen sneltoetsen uit `settings.json` |
| 5 | `CheatSheetBuilder` | achtergrond | naam, categorie, extensie, conflicten, sortering |

`CheatSheetCollector` zet deze stappen achter elkaar. Alleen stap 1 heeft DTE nodig; stap 3 tot en met 5 hebben geen VS nodig en zijn daarom direct getest.

**DTE en de threading-analyzer.** `DTE` is COM en hoort op de UI-thread. Elke property van een `Command` kan een `COMException` geven. De eerste versie ving dat af met een hulpfunctie die een lambda kreeg (`SafeGet(() => command.Name)`). De analyzer VSTHRD010 kan niet zien dat die lambda op de UI-thread draait, en gaf drie waarschuwingen. Nu is er per property een kleine methode met `ThreadHelper.ThrowIfNotOnUIThread()`. Hetzelfde bij de knop: `_export.Click += (s, e) => { ThreadHelper.ThrowIfNotOnUIThread(); Export(); };`.

**Een await naar de achtergrond.** `await TaskScheduler.Default;` werkt alleen met `using Microsoft.VisualStudio.Threading;`. Zonder die regel zoekt de compiler een `GetAwaiter` en vindt hij alleen die voor `IVsTask` (fout CS1929). De melding wijst niet naar de ontbrekende `using`.

### Welk DLL hoort bij een package

In de `.pkgdef` staat per package:

```
[$RootKey$\Packages\{acf2e531-...}]
"Assembly"="ShortcutCheatsheet, Version=..., Culture=neutral, PublicKeyToken=null"
"CodeBase"="$PackageFolder$\ShortcutCheatsheet.dll"
```

`PkgdefPackages` neemt `CodeBase` als die er is (dat is het exacte bestand), anders de naam uit `Assembly` plus `.dll`. Ontbreken beide, dan de DLL met dezelfde naam als de `.pkgdef`. Een pad met een ander token dan `$PackageFolder$`, zoals `$RootFolder$`, wijst buiten de extensie en wordt overgeslagen.

Een command dat in geen enkele command table van een extensie staat, telt als Visual Studio. Daarmee krijgen ook ingebouwde onderdelen zoals GitHub Copilot en SQL Server Data Tools geen extensienaam, zoals afgesproken.

### Jouw eigen sneltoetsen

VS 2026 bewaart ze in `%LocalAppData%\Microsoft\VisualStudio\18.0_<id>\settings.json`, onder `environment.keyboardShortcuts.customizations`:

```json
{ "scheme": "default", "command": "Debug.Autos.Search", "shortcut": "Ctrl+E",
  "scope": "Autos Window", "scopeId": "{F2E84780-...}", "isRemoval": true }
```

Op deze laptop: 181 verwijderingen en 1 toevoeging. Een verwijderde sneltoets staat niet meer in DTE; het cheat sheet telt ze alleen (`removedByYou`).

Twee keuzes:

- **Het bestand lezen, niet `ISettingsManager`.** De waarde is een lijst van objecten. Hoe `ISettingsReader.GetValue<T>` zo'n lijst teruggeeft, is niet gedocumenteerd. Het bestand is gewone JSON. De map komt uit `ShellSettingsManager.GetApplicationDataFolder(ApplicationDataFolder.LocalSettings)`, zodat de Experimental Instance zijn eigen bestand leest. Wordt het formaat later anders, dan raakt dat alleen deze ene klasse.
- **Het begint met een commentaar.** De eerste regel is `/* Visual Studio Settings File */`. `ConvertFrom-Json` in PowerShell weigert dat; Newtonsoft leest het met `CommentHandling.Ignore`.

### Namen en categorieën

`CommandNames.Describe` maakt van de canonieke naam een categorie en een leesbare naam:

| Canonieke naam | Categorie | Naam |
|---|---|---|
| `Edit.CommentSelection` | Edit | Comment Selection |
| `EditorContextMenus.CodeWindow.Markdown.MakeBold` | Markdown | Make Bold |
| `OtherContextMenus.LeftMarginContextMenu.ToggleBookmark` | Context Menu | Toggle Bookmark |
| `CodeMaid.CleanupActiveDocument` (knoptekst `&Cleanup Active Document`) | CodeMaid | Cleanup Active Document |

Het pad van een contextmenu (`EditorContextMenus.CodeWindow`) zegt waar het item in een menu staat, niet wat het doet, dus dat valt weg. Bij een command van een extensie is de knoptekst uit de command table de naam; de `&` voor de sneltoetsletter en de `...` aan het eind gaan eraf.

### Conflicten

Twee verschillende commands met dezelfde toetsen in dezelfde scope. `Ctrl+E, V` en `Ctrl+E,V` tellen als dezelfde toetsen. Een toets in `Global` en dezelfde toets in bijvoorbeeld de Text Editor is geen conflict: in de Text Editor wint de specifieke. Hetzelfde command twee keer met dezelfde toets is ook geen conflict; die dubbele regel wordt weggelaten.

### JSON

`DataContractJsonSerializer` uit .NET Framework, dus geen extra pakket. De veldnamen staan in de `[DataMember]`-attributen op het model; `EmitDefaultValue = false` laat `extension`, `custom` en `conflictsWith` weg als ze leeg zijn. `formatVersion` staat erin, zodat een latere versie van de extensie oude exports kan herkennen. Dezelfde attributen dienen straks voor de XML-export.

### Het icoon

`src\ShortcutCheatsheet\Resources\` bevat de SVG en vier PNG-exports. In het manifest is `Icon-128.png` het icoon en `Icon-256.png` het voorbeeldplaatje; die twee gaan als `Content` met `IncludeInVSIX` mee in de VSIX. De rest staat als `None` in het project, zodat je ze in Solution Explorer ziet zonder dat ze in het pakket komen.

### Tests

`CheatSheetTests` (15 tests): scope en toetsen splitsen, namen en categorieën, `settings.json` met commentaar en ongeldige JSON, `CodeBase` en `Assembly` in een `.pkgdef`, conflicten alleen binnen een scope, sortering met Global eerst, jouw eigen sneltoetsen, en een JSON-export die weer ingelezen kan worden.

De herkomst wordt getest met de eigen build-uitvoer: `Builds\ShortcutCheatsheet\Debug\` heeft een manifest, een `.pkgdef` en de DLL, en is daarmee een complete extensiemap. Een sneltoets op `View.ShortcutCheatsheet` krijgt dan "Shortcut Cheatsheet" als extensie.
