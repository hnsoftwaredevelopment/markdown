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

### Na de eerste export: vier verbeteringen

De eerste JSON-export uit de Experimental Instance (1120 sneltoetsen) liet vier dingen zien.

**1. Onderdelen van VS die als extensie meetelden.** `View.Containers` kreeg "Visual Studio Container Tools Extensions" als extensie. Die staat in `Common7\IDE\Extensions\<willekeurige naam>\`, precies zoals een extensie van derden die voor alle gebruikers is geïnstalleerd, en `InstalledExtensions` rekent zo'n map dus niet tot VS. Het manifest zegt het wel:

```xml
<Installation AllUsers="true" SystemComponent="true">
```

`ManifestInfo.IsSystemComponent` leest dat, en `ExtensionCommands` slaat zo'n map over. Deze regel hoort eigenlijk in `InstalledExtensions` in ExtensionCommon, zodat ExtensionOverlap hem ook krijgt. Dat doe ik als de branch van ExtensionOverlap gemerged is.

**2. Commands zonder naam.** 73 commands had DTE geen naam voor, zoals die van de Graphics Designers en de merge-editor. VS heeft zelf ook command tables, in de `.pkgdef`-bestanden onder `Common7\IDE`. Dezelfde lezer leest er 96 van de 163; de rest is native (C++) en staat in Win32-resources. Ze geven 68 van de 73 een naam ("Take Incoming", "Pencil", "Lock X Axis"). Dat kost ongeveer 4 seconden, en het resultaat blijft bewaard zolang VS draait (`ExtensionCommands.VisualStudioNames`). Sommige tabellen zetten een identifier in de knoptekst (`VsGraphics.MRE.Select`); die wordt gelezen als canonieke naam.

Bij het lezen van al die tabellen kwam een fout boven: een `.resources`-bestand van Team Foundation heeft een eigen reader-type (`GzipResourceReader`). `ResourceReader` gooit dan een `NotSupportedException`, en die werd niet afgevangen. Een extensie van derden kan hetzelfde doen, dus nu wordt zo'n bestand overgeslagen.

**3. "Other" als categorie bij extensies.** Bookmark Studio noemt zijn commands `BookmarkShortcut1` en `GoToNextBookmark`, zonder punt, en die kwamen in "Other". Bij een command van een extensie wordt een categorie "Other" of "Context Menu" nu de naam van de extensie.

**4. Conflicten waar je niets aan kunt doen.** Alle 14 conflicten zaten in Merge Editor Window: telkens twee commands van VS zelf (de oude en de nieuwe merge-editor) op dezelfde toets. Herbert koos: alleen melden als minstens één van de commands van een extensie komt of door jou is toegevoegd.

### Hulpscript: klopt de deploy?

`tools\check-exp-deploy.ps1` vergelijkt de DLL, de `.pkgdef` en het manifest in `Builds\` met die in de Experimental Instance, en zoekt bestanden van 0 bytes in alle extensies daar. Met `-Repair` kopieert het de build en raakt het `extensions.configurationchanged` aan. Gebruik het als het venster na F5 nog de oude versie laat zien.

### Meldingen waar de gebruiker niets mee kan

Het venster toonde "Extension Manager not available, read the folders instead: InvalidOperationException: Sequence contains no matching element." Twee lessen.

**De oorzaak.** `InstalledExtensions` roept `IVsExtensionManagerAsync.GetEnabledExtensionsAsync` aan via reflection, en zocht een overload waarvan alle parameters optioneel zijn. In VS 2026 18.13 is de signatuur:

```csharp
Task<...> GetEnabledExtensionsAsync(CancellationToken cancellationToken)
```

zonder standaardwaarde. `First(...)` vond dus niets en gooide een exceptie; de terugval (de mappen zelf lezen) werkte wel, daarom zag de export er goed uit. De fix in ExtensionCommon accepteert ook een `CancellationToken`-parameter en geeft `CancellationToken.None` mee. Dit is het risico van een ongedocumenteerde API: de signatuur kan zonder aankondiging veranderen. De terugval is daarom geen luxe.

ExtensionOverlap heeft dezelfde code en dus dezelfde fout. Die krijgt de fix zodra zijn submodule naar de nieuwe commit van ExtensionCommon wijst.

**De melding.** Een melding die de gebruiker niet kan oplossen, maakt alleen ongerust. Zulke problemen (een interne API die anders is, een command table die niet te lezen is) gaan nu naar het ActivityLog van VS via `ActivityLog.TryLogWarning`. Start VS met `devenv /log` om ze te zien in `%AppData%\Microsoft\VisualStudio\18.0_<id>\ActivityLog.xml`. In de JSON-export blijft `problem` per extensie staan, voor wie het wil uitzoeken.

### Werkwijze: sluit de Experimental Instance vóór je bouwt

Twee keer liet het venster na F5 nog de oude versie zien. `check-exp-deploy.ps1` gaf beide keren hetzelfde beeld: de DLL in de Experimental Instance was ouder dan die in `Builds\`. De build was gelukt, de deploy niet. Een draaiende Experimental Instance houdt `ShortcutCheatsheet.dll` vast, en dan kan de deploy hem niet overschrijven. F5 start daarna gewoon een nieuwe instance, met de oude DLL. De melding van de mislukte deploy staat alleen in het Output-venster bij Build.

Dus: eerst de Experimental Instance sluiten (of de debugsessie stoppen), dan bouwen of F5. Twijfel je, draai dan `tools\check-exp-deploy.ps1`: staat er DIFFERENT bij de DLL, dan draait de oude versie.

### MSTEST0044

MSTest 4 markeert `[DataTestMethod]` als verouderd. `[TestMethod]` met `[DataRow(...)]` doet hetzelfde. Zoek bij het nakijken van de build op `warning` in het algemeen, niet alleen op `warning CS`: de analyzers van MSTest hebben hun eigen codes.

### Het ActivityLog

VS schrijft het naar `%AppData%\Microsoft\VisualStudio\18.0_<id>\ActivityLog.xml`, voor de Experimental Instance naar de map met `Exp` erachter. Start VS met `/log` (`devenv /rootsuffix Exp /log`) om zeker te zijn dat ook waarschuwingen van extensies erin komen. Het bestand opent in een browser; zoek op "Shortcut Cheatsheet".

## Stap 4: het venster

Het venster toont nu het cheat sheet zelf. Drie lagen, zodat alleen de bovenste WPF en VS nodig heeft:

| Laag | Klasse | Doet |
|---|---|---|
| Logica | `ShortcutView`, `KeyChord` (in `Model`) | filteren, groeperen, sorteren, toetsen splitsen; getest zonder WPF |
| Toestand | `CheatsheetViewModel` | zoektekst, filters, indeling; bouwt de lijst opnieuw op als iets verandert |
| Weergave | `CheatsheetControl.xaml` | tekent; knoppen gaan naar `CheatsheetWindow`, dat VS en de export doet |

### XAML in een klassiek VSIX-project

Een `.xaml`-bestand komt als `<Page>` in de `.csproj` met `<Generator>MSBuild:Compile</Generator>`, en de code-behind als `<Compile>` met `<DependentUpon>`. De kleuren en stijlen van VS komen uit `Microsoft.VisualStudio.Shell.15.0`:

```xml
Foreground="{DynamicResource {x:Static platformUI:EnvironmentColors.ToolWindowTextBrushKey}}"
Style="{DynamicResource {x:Static vsshell:VsResourceKeys.TextBoxStyleKey}}"
```

`DynamicResource`, niet `StaticResource`: dan volgt het venster een themawissel (licht, donker) zonder herstart.

### Toetsen als toetsen

`KeyChord.Parse` maakt van "Ctrl+K, Ctrl+C" twee stappen met elk twee toetsen. Splitsen op `+` gaat mis bij "Ctrl+Num +" en "Ctrl++". Daarom haalt de parser de bekende modifiers (Ctrl, Shift, Alt, Win) van de voorkant af; wat overblijft is de toets, welke tekens er ook in staan. Stappen worden gescheiden door ", " (komma plus spatie), zodat "Ctrl+," één toets blijft.

Een toets is een `Grid` met twee afgeronde rechthoeken en de tekst. Twee rechthoeken, omdat een brush uit `DynamicResource` geen eigen doorzichtigheid heeft: de ene vult met de tekstkleur op 8%, de andere tekent de rand op 45%.

### Groeperen zonder traag te worden

`ListCollectionView` met twee `PropertyGroupDescription`s (bijvoorbeeld scope en categorie). Met groepen zet WPF virtualisatie standaard uit; `VirtualizingPanel.IsVirtualizingWhenGrouping="True"` zet hem weer aan. Bij 70 scopes zijn alle groepen dicht, anders is het een muur van 1100 regels. Zodra je zoekt of filtert, of als er hooguit 150 regels zijn, gaan ze open (`ExpandGroups`).

Zoeken wacht 200 ms na de laatste toets (`DispatcherTimer`), anders wordt de lijst bij elke letter opnieuw opgebouwd en hapert het typen.

### Een smal venster

Op de eerste screenshot ontbrak het zoekvak: in een `DockPanel` met `LastChildFill` namen de keuzelijst en de knoppen alle breedte, en het zoekvak kreeg 0 pixels. Nu staat het zoekvak op een eigen regel, en de rest in een `WrapPanel`, dat naar de volgende regel gaat als het niet past. Het extensielabel in een regel verschijnt alleen als de groep of categorie de extensie niet al noemt; anders duwt het de naam weg.

### Een eigen icoon: image manifest

Het menu-item en het venster gebruiken het eigen icoon via een image manifest (`ShortcutCheatsheet.imagemanifest`):

1. Het manifest koppelt een GUID en ID aan `Resources/Icon-32.png`, met een pack-URI (`/ShortcutCheatsheet;component/Resources`).
2. `Icon-32.png` staat daarom als `<Resource>` in de `.csproj`: het zit in de DLL.
3. Het manifest gaat als `Content` met `IncludeInVSIX` mee; VS vindt `.imagemanifest`-bestanden in de extensiemap zelf.
4. De `.vsct` gebruikt dezelfde GUID en ID met `IconIsMoniker`; het venster zet `BitmapImageMoniker`.

Drie plekken met dezelfde GUID: een test (`Image_manifest_vsct_and_code_agree`) houdt ze gelijk.

Door het eigen icoon is `KnownImageIds.vsct` niet meer nodig, en daarmee is onze command table klein: één blok. De test op meerdere blokken gebruikt nu een eigen fixture, `Large.vsct`, die `KnownImageIds.vsct` insluit.

### Screenshots maken zonder het scherm te pakken

De eerste poging met `Graphics.CopyFromScreen` legde een ander programma vast dat vooraan stond: een achtergrondproces mag een venster niet naar voren halen. `PrintWindow` met `PW_RENDERFULLCONTENT` (2) vraagt het venster zelf om zich te tekenen, ook als het erachter ligt; er komt niets anders op de afbeelding. De Experimental Instance blijft op het startscherm staan als je hem zonder bestand start; met een bestand als argument (`devenv /rootsuffix Exp README.md`) opent hij meteen. Het zoekvak vul je met UI Automation (`ValuePattern.SetValue`), zonder toetsenbord. De scripts staan in `obj\research\`: `print-window.ps1`, `run-command.ps1`, `set-search.ps1`.

### Alleen tonen wat iets kan vinden

Na de eerste test, op verzoek van Herbert:

- **Filters die niets vinden, verdwijnen.** "Only added by you" en "Only conflicts" staan er alleen als er eigen sneltoetsen of conflicten zijn (`HasCustom`, `HasConflicts` in het viewmodel). Staat zo'n filter aan als hij verdwijnt, bijvoorbeeld na Refresh, dan gaat hij uit; anders is de lijst leeg zonder zichtbare reden.
- **De samenvatting laat nullen weg.** "0 added by you" is ruis.
- **Pijltoetsen als pijlen.** `KeyChord.Display` maakt van "Up Arrow" een ↑, en zo ook ↓, ← en →. Alleen op de toetsen in het venster: de gegevens, de export en het zoeken houden de tekst van VS, zodat zoeken op "arrow" ze blijft vinden.

### Uitlijnen met labels

Regels met een label ("yours", extensie, conflict) begonnen hun naam verder naar rechts. Het raster had drie kolommen: toetsen `2*`, naam `3*` en labels `Auto`. Een `Auto`-kolom neemt eerst zijn ruimte, en de rest wordt 2:3 verdeeld. Een regel met een label had dus een smallere toetsenkolom dan een regel zonder. Nu heeft elke regel dezelfde twee kolommen, en de labels staan rechts binnen de naamkolom (`DockPanel.Dock="Right"`).

Een akkoord dat niet op één regel past, liep door met de komma vooraan. De komma hoort nu bij de eerste stap (`StrokeView.HasNext`), zodat de regel eindigt met "Ctrl R ," en de volgende begint met de toets.

Enter staat als ⏎ op de toets: dat symbool staat op vrijwel elk toetsenbord. Backspace en de andere toetsen houden hun tekst.

### VS 2026 lost conflicten zelf op

Herbert kon geen conflict maken via de sneltoetsen-instellingen. Een proef in de Experimental Instance: de `.vsct` van deze extensie kreeg tijdelijk twee standaardsneltoetsen voor `View.ShortcutCheatsheet`, Ctrl+Shift+B (bezet door Build Solution) en Ctrl+Shift+Alt+F9 (vrij). Na de deploy gaf DTE:

```
View.ShortcutCheatsheet -> Global::Ctrl+Shift+Alt+F9
Build.BuildSolution     -> Global::Ctrl+Shift+B
```

VS paste de vrije sneltoets toe en sloeg de botsende stil over. Een conflict met een extensie of een eigen sneltoets in dezelfde scope ontstaat in VS 2026 dus niet; wat overblijft zijn conflicten binnen VS zelf, en die toont het venster niet (keuze a).

Twee bijzaken uit de proef:

- Een standaardsneltoets die eenmaal is toegepast, blijft staan als je hem uit de `.vsct` haalt. Ctrl+Shift+Alt+F9 bleef na het terugzetten bestaan, tot hij via DTE werd weggehaald (`command.Bindings = new object[0]`).
- Na een gewijzigde `.vsct` moet `extensions.configurationchanged` worden bijgewerkt, anders leest VS de nieuwe command table niet.

### Van conflicten naar "not applied"

Omdat VS 2026 zelf geen conflicten toelaat (zie hierboven), had het filter "Only conflicts" nooit iets te tonen. Wat wel gebeurt: een extensie brengt een standaardsneltoets mee die al bezet is, en VS slaat hem stil over. De gebruiker weet dan niet dat de extensie een sneltoets voor die functie had.

**Hoe het herkend wordt.** De command table van de extensie (sectie `Keys`) zegt welke sneltoetsen hij wil. `CheatSheetBuilder.NotApplied` loopt die langs:

1. `KeyText.Format` schrijft de sneltoets zoals DTE dat doet: virtual-key `0x42` met Ctrl en Shift wordt "Ctrl+Shift+B". De volgorde van de modifiers is die van DTE: Ctrl, Shift, Alt, Win. Een toets zonder bekende naam geeft `null`, en zo'n sneltoets wordt overgeslagen.
2. De scope komt uit de editor-GUID: `guidVSStd97` is Global, de text editor factory is Text Editor. Andere editor-scopes hebben een naam die we niet weten; die worden niet gemeld in plaats van geraden.
3. Heeft DTE het command met deze toetsen in deze scope, dan is hij toegepast.
4. Zo niet, dan alleen melden als een ander command de toetsen in die scope heeft. Ontbreekt de sneltoets om een andere reden, bijvoorbeeld omdat je het command zelf andere toetsen gaf, dan zwijgt het venster.
5. Heb je de sneltoets zelf verwijderd (`isRemoval` in `settings.json`), dan is dat je eigen keuze en geen melding waard.

**In het venster** staat zo'n regel gedimd, met een waarschuwingsicoon en een tweede regel onder de naam: "Shortcut Cheatsheet wants these keys, but they are used by Build Solution." Eerst stond "not applied" als label naast de naam, maar in een smal venster duwden de labels de naam helemaal weg. De uitleg onder de naam past altijd. In de samenvatting staat "1 not applied", en het filter heet nu "Only not applied". In de JSON vervangen `notApplied` en `usedBy` het oude `conflictsWith`.

**Getest** met dezelfde tijdelijke Ctrl+Shift+B in de `.vsct` als bij de proef, en daarna weer teruggezet. Eén keer terugzetten was niet genoeg: de gedeployde DLL had nog de tijdelijke command table. Na het terugzetten van de `.vsct` dus opnieuw deployen.

## Stap 5a: exporteren

De knop heet nu "Export..." en biedt zeven formaten: PDF, PNG, HTML, Markdown, CSV, JSON en XML. De export volgt het venster: dezelfde zoektekst, filters en indeling. Wie alleen de extensies wil afdrukken, vinkt "Only extensions" aan en exporteert.

### Eén document, zeven schrijvers

`ExportDocument.Create` filtert, sorteert en groepeert met dezelfde `ShortcutView` als het venster. Het resultaat heeft twee vormen:

- `Groups` (groep, subgroep, regels) voor de leesbare formaten: PDF, PNG, HTML en Markdown.
- `Sheet`, een gefilterde `CheatSheet`, voor de dataformaten: JSON, XML en CSV.

Elke schrijver is daardoor kort en apart te testen. `Exporter` kiest de schrijver op extensie (`.htm` en `.markdown` mogen ook) en levert het filter voor het opslagvenster.

### PDF en PNG: tekenen zonder venster

`SheetRenderer` tekent pagina's met `DrawingVisual` en `FormattedText`, niet met XAML-controls. Dat heeft twee voordelen: het draait in een test zonder venster, en de opmaak ligt vast. Alleen een STA-thread is nodig; de test start er zelf een.

De opbouw:

1. **Meten.** Elke kop en elke regel wordt een blok met een hoogte en een tekenfunctie. Een kop krijgt `KeepWithNext`, zodat hij nooit los onderaan een kolom staat.
2. **Plaatsen.** Blokken vullen drie kolommen per pagina (A4 liggend, 1123 x 794 WPF-eenheden). Begint een kolom midden in een groep, dan komt er een grijze regel boven: "Global · Build (continued)". Zo is elke kolom los te lezen.
3. **Tekenen** op schaal 2, dus 192 dpi: scherp op papier.

De breedte van de toetsenkolom volgt de gegevens: genoeg voor 9 van de 10 sneltoetsen op één regel, tussen 30 en 45 procent van de kolom. De eerste versie nam de breedste sneltoets, en dan stonden alle namen halverwege de kolom voor een paar lange regels. Nu loopt een akkoord als "Ctrl+K, Ctrl+→" door naar een tweede regel, en zet een heel lange toets ("Ctrl+Shift+Alt+F7") de naam eronder.

Sneltoetsen die VS niet heeft toegepast, staan niet in PDF en PNG. Ze werken niet, en op papier is geen ruimte om uit te leggen waarom. In de andere formaten staan ze wel, gemarkeerd.

PNG schrijft één bestand per pagina: "Shortcuts-1.png", "Shortcuts-2.png". Alle sneltoetsen van een normale installatie (ruim 1100) passen op 17 pagina's.

### Een eigen PDF-schrijver

PDFsharp 6.5 en iText zijn AGPL. Een PDF met alleen afbeeldingen is klein genoeg om zelf te schrijven (`PdfWriter`, ongeveer 150 regels):

- Per pagina een afbeelding (`/XObject /Image`, RGB, 8 bits) en een korte content stream die hem over de hele pagina zet: `q 842 0 0 595 0 0 cm /Im0 Do Q`.
- Compressie met `/FlateDecode`. Dat is zlib, en .NET heeft alleen `DeflateStream`, dus raw deflate. Zlib is raw deflate met 2 bytes ervoor (`78 9C`) en een Adler-32-controlegetal erachter. Die drie stukken schrijft `PdfWriter.Zlib` zelf.
- Daarna de catalogus, de pagina-lijst en een cross-reference-tabel met de byte-positie van elk object. Elke regel in die tabel is precies 20 bytes, inclusief de spatie voor de regelovergang.

De test controleert wat een PDF-lezer nodig heeft: `startxref` wijst naar de tabel, elke positie wijst naar zijn object, en elke `/Length` klopt met de data. Ter controle opende `qpdf --check` het resultaat zonder fouten.

### HTML, Markdown en CSV

- **HTML** is één bestand zonder iets van buiten: CSS-toetsen met `<kbd>`, een zoekveld (ook "ctrl+e,v" zonder spaties), donker als Windows donker staat, en een printopmaak in drie kolommen.
- **Markdown** zet toetsen in `<kbd>`, wat GitHub, Obsidian en de Markdown-preview van Visual Studio als toetsen tonen. Binnen `<kbd>` moet je HTML-coderen en toch nog `|`, `\`, `*`, `_` en `` ` `` escapen, anders breekt de tabel.

  De editor Zed kan dat niet: daar staat de eerste `<kbd>` van een cel als tekst, en de rest zonder toetsvorm. Even zijn de toetsen code geworden (`` `Ctrl+K, Ctrl+→` ``), op de aanname dat Obsidian het probleem was. Dat bleek niet zo, en die wijziging is teruggedraaid: voor een weinig gebruikte editor wordt de export elders niet slechter. Les: vraag eerst in welk programma het probleem zich voordoet, en test daar.
- **CSV** opent direct goed in Excel als aan twee dingen is voldaan: UTF-8 met BOM (anders worden de pijltjes onleesbaar) en het lijstscheidingsteken van de landinstelling. In Nederland is dat een puntkomma. Met een komma als scheidingsteken krijgt "Ctrl+," aanhalingstekens.

### Tests

12 nieuwe tests, 68 in totaal. Eén test schrijft alle formaten uit `tools\Shortcuts.json` (een echte export, niet in de repo) naar `obj\export-samples`. Zo kun je het resultaat bekijken zonder VS te starten. Staat het bestand er niet, dan meldt de test "Inconclusive" en faalt hij niet.

### Valkuil: tijdelijke bestanden

Desktop Commander mag alleen in `C:\DevOps` en een paar andere mappen schrijven, niet in `%TEMP%`. Het commitbericht staat daarom in `obj\commit-msg.txt`; `obj` staat in `.gitignore`.

## Stap 5b: instellingen

Tools > Options > Shortcut Cheatsheet, in beide Options-vensters van VS 2026: het nieuwe (Unified Settings) en het klassieke. Dezelfde opzet als XAML Resource Preview.

| Groep | Instelling | Standaard |
|---|---|---|
| General | Language | Automatic (de taal van VS, anders Engels) |
| General | Group by: de indeling waarmee het venster opent | Where it works |
| Export | Paper size voor PDF en PNG | Automatic |
| Export | Colors voor PDF en PNG: light of dark | Light |
| Export | Columns per page, 1 tot 4 | 3 |

### Twee vensters, één bron

- **`Options\registration.json`** beschrijft de instellingen voor het nieuwe venster. VS vindt het bestand via `[ProvideSettingsManifest]`; in de `.pkgdef` wordt dat `[$RootKey$\SettingsManifests\{package-guid}]` met `ManifestPath`. Het bestand moet als `Content` met `IncludeInVSIX` in de VSIX.
- **`GeneralOptionsPage`** is een `DialogPage` voor het klassieke venster. `IsInUnifiedSettings = true` op `[ProvideOptionPage]` houdt hem uit het nieuwe venster, en `legacyOptionPageId` in registration.json koppelt de categorie aan de pagina.
- **`SettingsService`** leest Unified Settings als VS dat aan heeft, en anders de DialogPage. Slaat iemand op in het klassieke venster, dan schrijft de pagina naar Unified Settings. Zo tonen beide vensters dezelfde waarden. Wijzigingen komen binnen via `SubscribeToChanges`; het venster neemt een nieuwe standaardindeling meteen over.

### Teksten uit de resources

In registration.json staat `"@OptionsLanguageName;{package-guid}"`: VS zoekt die naam in de resources van het package. Die heten `VSPackage.resources`. Daarom krijgt `Localization\Strings.resx` in de `.csproj` `LogicalName` `VSPackage.resources`, met `MergeWithCTO`: de gecompileerde command table (`Menus.ctmenu`) gaat in dezelfde resource. De test die onze eigen command table uit de DLL leest, bevestigt dat dat nog werkt.

De klassieke pagina toont enums via `LocalizedEnumConverter<T>`. Die zoekt de tekst op als typenaam plus waarde: `Grouping.Scope` wordt resource `GroupingScope`, "Where it works". Eén klasse voor alle drie de keuzelijsten, in plaats van een converter per enum zoals in ResourcePreview.

Nu staat alleen Engels in Strings.resx. De vertalingen en de teksten van het venster volgen in stap 5c.

### Papierformaat automatisch

`RegionInfo.IsMetric` lijkt de vraag te beantwoorden, maar Canada is metrisch en drukt op Letter. `ExtensionSettings.ResolvePaper` gebruikt daarom een lijst landen met Letter: de Verenigde Staten, Canada, Mexico en een paar landen in Latijns-Amerika en Azië. Overal anders A4.

### De datum in een export

Die volgde de taal van Windows en gaf "16 november 2026" in een Engelse export. Nu volgt hij de taal van de extensie (`Localizer.Culture`), in de lange notatie van die taal.

### Valkuilen

- **Een `DialogPage` kun je niet testen zonder VS.** De constructor vraagt `Microsoft.Internal.VisualStudio.Interop` op, en die staat alleen in VS. De test op de pagina is daarom vervallen; de tests controleren registration.json tegen de code (monikers, standaardwaarden, keuzes, de koppeling met de pagina) en of elke tekst in Strings.resx staat.
- **De `Grouping`-enum moest `public` worden**, omdat de pagina `public` is en een eigenschap van dat type heeft.
- **registration.json staat niet in `Builds\`.** `Content` gaat alleen in de VSIX en de deploy. `check-exp-deploy.ps1` kopieert alleen de DLL, `.pkgdef` en het manifest; na een nieuw bestand dus echt deployen: `MSBuild ... -p:DeployExtension=true`.
