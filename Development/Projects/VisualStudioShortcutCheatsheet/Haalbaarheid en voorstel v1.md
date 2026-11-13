# Visual Studio Shortcut Cheatsheet: haalbaarheid en voorstel v1

Onderzoek op 13 november 2026, op nb1164, in VS 2026 Insiders 18.13 (Community). Nog geen code voor de extensie. Wel een paar PowerShell-scripts om de aannames te testen; die staan in `C:\DevOps\hnsoftwaredevelopment\Visual Studio Shortcut Cheatsheet\obj\research\` en worden niet gecommit.

## Kort antwoord

| Vraag | Antwoord |
|---|---|
| Alle sneltoetsen ophalen? | Ja. `DTE.Commands` geeft per command de `Bindings` als `"Scope::Toetsen"`. Gemeten: 5.912 commands, 1.024 sneltoetsen. |
| Groeperen op waar een toets werkt? | Ja. De scope (`Global`, `Text Editor`, `Solution Explorer`, ...) is precies dat. Op deze laptop: 67 scopes. Tweede indeling: de categorie uit de commandnaam (`Edit`, `Debug`, `View`). |
| Herkomst per sneltoets (welke extensie)? | Ja, via een ongedocumenteerd formaat. De gecompileerde command table (`.cto`) van een extensie is te lezen en noemt welke commands en standaardsneltoetsen die extensie levert. Bij CodeMaid klopt het tot op de laatste sneltoets. |
| Zien wat de gebruiker zelf heeft aangepast? | Ja. VS 2026 bewaart aanpassingen in Unified Settings (`environment.keyboardShortcuts.customizations`), te lezen met de API die ResourcePreview al gebruikt. |
| Exporteren naar JSON, XML, PNG, PDF? | JSON, XML en PNG zonder extra pakketten. PDF ook, maar niet met PDFsharp: de huidige versie is AGPL. Voorstel: een kleine eigen PDF-schrijver. |

## 1. De sneltoetsen ophalen

### DTE.Commands

Het oude automation-model van VS (`EnvDTE`) heeft `DTE.Commands`. Elk `Command` heeft `Name` (canonieke naam, zoals `Edit.Duplicate`), `LocalizedName`, `Guid`, `ID` en `Bindings`: een array met tekst als `"Text Editor::Ctrl+E, V"`.

Getest op je gewone VS (pid 22844) via de Running Object Table, net als de screenshot-scripts van ResourcePreview:

| Meting | Waarde |
|---|---|
| Commands | 5.912 |
| Sneltoetsen (scope + toets) | 1.024 |
| Daarvan akkoorden (twee stappen, `Ctrl+K, Ctrl+C`) | 316 |
| Command sets (verschillende GUID's) met een sneltoets | 95 |
| Sneltoetsen zonder canonieke naam | 82 |
| Tijd, vanuit een ander proces | 5,6 seconde |

Vanuit een ander proces gaat elke aanroep via COM tussen processen. In de extensie draait het in hetzelfde proces en is het naar verwachting veel sneller; dat meet ik in de eerste bouwstap. `DTE` moet op de UI-thread, dus het ophalen gebeurt daar, en het verwerken op de achtergrond.

De 82 sneltoetsen zonder naam horen bij commands die VS alleen kent als `{guid}:id`, bijvoorbeeld van SQL Server Data Tools (`F6` in de T-SQL Editor) en de Graphics Designers. Die krijgen een naam uit de command table (zie sectie 3), anders de GUID en het nummer.

### Wat VS 2026 nieuw heeft

In `Microsoft.Internal.VisualStudio.Interop.dll` zit de interface `IVsUnifiedSettingsKeyboardPrivate` (service `SVsUnifiedSettingsKeyboardPrivate`). Dat is de achterkant van het nieuwe sneltoetsenscherm in VS 2026:

```csharp
void GetAllKeyBindings(UnifiedSettingsKeyBindingLayer layer,
    out string[] keys, out string[] commands, out string[] scopes,
    out bool[] isRemovals, out string[] localizedKeys);
string GetActiveKeyboardScheme();
string[] GetAllKeyBindingScopes();
```

`UnifiedSettingsKeyBindingLayer` heeft de waarden `Default`, `Scheme`, `Profile`, `User` en `All`. Daarmee zie je per sneltoets of hij standaard is, uit het gekozen schema komt of door jou is toegevoegd of verwijderd.

Het woord `Private` en de namespace `Microsoft.Internal` zeggen genoeg: niet bedoeld voor extensies, kan in elke update veranderen. Voorstel: niet als hoofdbron, wel als extra via reflection, met `DTE.Commands` als basis. Werkt hij niet, dan ontbreekt alleen de laag-informatie.

### Wat jij zelf hebt aangepast: de publieke weg

`CommonExtensions\Platform\Shell\Shell.registration.json` definieert twee instellingen in Unified Settings:

| Moniker | Inhoud |
|---|---|
| `environment.keyboardShortcuts.activeScheme` | het actieve schema; leeg is het standaardschema |
| `environment.keyboardShortcuts.customizations` | jouw aanpassingen; het command is een canonieke naam of `{guid},id` |

Die categorie is alleen zichtbaar als de feature `VS.Core.UsxKeyboardShortcuts` aan staat. Lezen gaat met `ISettingsManager`, dezelfde API als in ResourcePreview (sectie 10 van de handleiding). Staat de feature uit, dan staan de aanpassingen nog in de oude vorm in `CurrentSettings.vssettings` onder `<UserShortcuts>` (`<Shortcut>` en `<RemoveShortcut>`).

## 2. Groeperen

### Op scope: waar werkt de toets?

De scope is het deel vóór `::`. De grootste op deze laptop:

| Scope | Sneltoetsen |
|---|---|
| Global | 370 |
| Text Editor | 144 |
| Graphics Designers | 49 |
| Workflow Designer | 43 |
| VC Image Editor | 37 |
| VC Dialog Editor | 29 |
| Windows Forms Designer | 25 |
| ... | (67 in totaal) |

Een scope van een extensie staat er gewoon tussen: `Object Explorer for MySQL` (3) en `MySQL Query Editor` (3) zijn van jouw eigen extensie, `MarkdownEditorV2` (6) van Markdown Editor v2.

Een sneltoets in een specifieke scope wint van dezelfde toets in `Global`, zolang je in dat venster werkt. Dat is nuttig om te tonen: "in de Text Editor doet `Ctrl+D` iets anders dan globaal".

### Op categorie: wat doet de toets?

Het eerste deel van de canonieke naam: `Edit` (247), `TestExplorer` (61), `Debug` (61), `View` (60), `Window` (51), `CodeMaid` (24).

Een valkuil: veel namen beginnen met het pad van een contextmenu, zoals `EditorContextMenus.CodeWindow.VisualchatGPTStudio.Complete` (47 keer `EditorContextMenus`, 40 keer `OtherContextMenus`). Dat zegt waar het menu-item staat, niet wat het doet. Voor de weergave knip ik dat pad eraf en gebruik ik de knoptekst uit de command table of `LocalizedName`.

### Conflicten

Twee commands met dezelfde toets in dezelfde scope komen voor, bijvoorbeeld `F10`, `F11`, `Alt+1` en `Shift+F8` in Merge Editor Window, en `Ctrl+=` in GitHub Copilot Chat. Soms is dat bedoeld (het ene command is alleen actief als het andere het niet is), soms niet. De cheat sheet kan ze markeren.

## 3. Herkomst: welke extensie levert de sneltoets?

Drie manieren geprobeerd.

### a. De GUID als tekst zoeken in de DLL's van extensies (afgewezen)

Een extensie die een command afhandelt, heeft de GUID van de command set in zijn code staan, meestal als string. Alle 110 extensiemappen doorzocht in 37 seconden. Voor de eigen commands van extensies klopt het: CodeMaid, Font Sizer, Insert Guid, Rainbow Braces, XAML Resource Preview.

Maar extensies noemen ook GUID's van VS zelf, om zich aan bestaande commands of menu's te hangen:

| Gevonden in | Command set | Is eigenlijk van |
|---|---|---|
| CodeMaid | `MoveLeftEdgetotheleft` (XAML Designer), `ReloadSchemas` (JSON Editor), HTML-commands | VS |
| Bookmark Studio | `Edit.Duplicate`, `Edit.PeekDifference`, `ResetZoom` | VS |
| File Differ | `Diff.SwitchBetweenLeftAndRight`, `Team.Git.Commit` | VS |
| drie extensies | `5EFC7975-...` (VSStd97, de standaard-commands) | VS |

Te veel valse meldingen. VS zelf erbij doorzoeken om die uit te sluiten kost te veel: 10.172 bestanden, 2,7 GB.

### b. De GUID binair zoeken in de DLL (werkt niet)

De command table zit gecomprimeerd in de DLL. Binair zoeken vindt de GUID van CodeMaid niet.

### c. De command table zelf lezen (voorstel)

Elk VSIX-package met menu's heeft in zijn `.pkgdef`:

```
[$RootKey$\Menus]
"{4c82e17d-927e-42d2-8460-b473ac7df316}"=", Menus.ctmenu, 1"
```

`Menus.ctmenu` is de gecompileerde `.vsct`, als resource in `VSPackage.resources`. Bij CodeMaid staat hij in de satellite-DLL `en-US\SteveCadwallader.CodeMaid.VS2022.resources.dll`, dus ook die moeten mee.

De opbouw, uitgezocht met CodeMaid:

| Bytes | Betekenis |
|---|---|
| `43 46 43 54` | `CFCT`, de herkenning |
| `05 00 00 00` | versie 5 |
| `F0 9E 00 00` | grootte na uitpakken: 40.688 bytes |
| vanaf byte 36 | gecomprimeerd met **Xpress Huffman** |

Windows kan dat zelf uitpakken: `RtlDecompressBufferEx` in `ntdll.dll` met formaat 4 (`COMPRESSION_FORMAT_XPRESS_HUFF`). Geen eigen decompressor nodig. Het resultaat heeft secties met een naam van vier letters:

| Sectie | Inhoud |
|---|---|
| `Symb` | de GUID's met hun naam uit de `.vsct`, zoals `guidCodeMaidToolWindowBuildProgress` |
| `Cmmd` | de commands die deze extensie definieert, met de knoptekst (`About CodeMaid...`) |
| `Keys` | de standaardsneltoetsen van deze extensie |
| `Menu`, `Grup`, `Plac`, `Bimp` | menu's, groepen, plaatsing en iconen |

De proef: `Keys` van CodeMaid heeft 27 regels. `DTE.Commands` toont voor CodeMaid precies 27 sneltoetsen. De eerste regel is `M` met Ctrl, dan Spatie zonder modifier: `Ctrl+M, Space` voor `CodeMaid.CleanupActiveDocument`.

De velden in `Keys` lijken te passen op de structs `KeyBindingId` en `KeyBindingData` uit `Microsoft.Internal.VisualStudio.Interop.dll`: een index in de GUID-tabel plus een ID voor het command, een index voor de scope, en twee keer toets plus modifier. Met de GUID-tabel uit `Symb` wordt dat weer een echte GUID. De precieze indeling van elke sectie zoek ik uit in bouwstap 2, met tests.

Wat dit oplevert:

- **Herkomst.** Een command hoort bij de extensie in wiens `Cmmd` het staat. In `Symb` van CodeMaid staan ook vier GUID's van VS (dezelfde valse treffers als bij manier a). Mijn verwachting is dat die alleen in `Plac` gebruikt worden en niet in `Cmmd`; dat is de eerste test in bouwstap 2.
- **Standaard of aangepast.** Staat de sneltoets in `Keys` van de extensie, dan is het de standaard van die extensie. Staat hij er niet in, dan heb jij hem toegevoegd.
- **Namen voor commands zonder canonieke naam**, uit de knoptekst in `Cmmd`.

Veiligheid: net als ExtensionOverlap niets laden. De resource lees je met `System.Reflection.Metadata` (`ManifestResource`) en `ResourceReader` op die bytes; er draait geen code van de extensie.

Risico: het formaat is niet gedocumenteerd. Versie 5 staat in de header; bij een andere versie slaat de lezer het bestand over en valt terug op manier a, alleen voor GUID's die in precies één extensie staan en niet in een vaste lijst van bekende VS-command sets (`VSConstants` heeft er een paar tientallen). Het label wordt dan "waarschijnlijk: CodeMaid".

### Welke extensies?

Hetzelfde als ExtensionOverlap: `IVsExtensionManagerAsync.GetEnabledExtensionsAsync()`, met terugval op de mappen. Die code (`InstalledExtensions.cs`) is herbruikbaar.

### Wat er overblijft

- **Extensies in het nieuwe VisualStudio.Extensibility-model** definiëren commands in code, zonder `.cto`. Die herken ik in v1 niet; ze krijgen "onbekende bron" als ze niet van VS lijken.
- **Ingebouwde onderdelen van Microsoft**, zoals SQL Server Data Tools en GitHub Copilot, tellen als VS. Jij wilde bij standaard-VS geen bron; dat geldt dan ook voor deze.

## 4. Exporteren

| Formaat | Hoe | Extra pakket |
|---|---|---|
| JSON | `DataContractJsonSerializer` of het `Newtonsoft.Json` dat VS al meebrengt | nee |
| XML | `XmlWriter` | nee |
| PNG | het cheat sheet als WPF-layout, `RenderTargetBitmap`, `PngBitmapEncoder` | nee |
| PDF | zie hieronder | nee |

### PDF

PDFsharp was jarenlang MIT. Versie 6.1.1 is nog MIT, de huidige 6.5.0 (oktober 2026) is **AGPL-3.0**. Dat past niet bij jouw eis van MIT- of GPL-compatibele software zonder voorwaarden voor gebruikers. Een oude MIT-versie vastpinnen kan, maar dan krijg je nooit meer fixes.

Voorstel: een eigen kleine PDF-schrijver die per pagina de gerenderde PNG als afbeelding opneemt, op A4 of Letter. Dat is ongeveer 150 regels, zonder pakket, en het werkt voor alle 15 talen (ook Japans en Chinees, waar een eenvoudige PDF met tekst een embedded font nodig heeft). Nadeel: je kunt de tekst in de PDF niet selecteren of doorzoeken. Daarvoor is HTML er (zie hieronder). Echte tekst in de PDF kan later.

### Extra formaten die weinig kosten

| Formaat | Waarom |
|---|---|
| HTML | doorzoekbaar, filterbaar met een paar regels JavaScript, en de browser drukt hem af of maakt er een PDF met echte tekst van |
| Markdown | voor een wiki of README |
| CSV | voor Excel |

## 5. Wat er al bestaat

Mads Kristensen heeft de extensie Show Keybindings: Tools > Export Keyboard Shortcuts..., naar HTML, VS Settings, tekst of JSON. Volgens de README zitten ook aangepaste sneltoetsen en sneltoetsen van extensies erin, maar er staat niet bij welke extensie ze levert.

Waar deze extensie anders is:

- per sneltoets de extensie die hem levert;
- of een sneltoets standaard is of door jou aangepast;
- conflicten in dezelfde scope;
- een afdrukbaar cheat sheet (PNG, PDF) met kolommen per scope, niet alleen een lijst;
- een venster in VS om te zoeken en te filteren, niet alleen een export.

## 6. Voorstel v1

### Wat erin zit

1. **Verzamelen.** `DTE.Commands` op de UI-thread; scope, toetsen, naam, GUID en ID. Daarna op de achtergrond verder.
2. **Herkomst.** Ingeschakelde extensies via de Extension Manager; per extensie de `.pkgdef` lezen, `Menus.ctmenu` uitpakken en `Symb`, `Cmmd` en `Keys` lezen. Cache per DLL op pad, grootte en datum. Terugval: GUID-tekst, alleen bij één extensie en niet in de VS-lijst.
3. **Aangepast door jou.** `environment.keyboardShortcuts.customizations` via `ISettingsManager`; anders `<UserShortcuts>` uit `CurrentSettings.vssettings`.
4. **Indeling.** Standaard op scope, met daarbinnen de categorie. Te kiezen: op categorie, op extensie, of plat op toets.
5. **Weergave.** Een tool window, **View > Other Windows > Shortcut Cheatsheet**:

```
Text Editor (144)
├─ Edit
│  ├─ Ctrl+E, V      Duplicate
│  └─ Ctrl+K, Ctrl+C Comment Selection
└─ CodeMaid
   └─ Ctrl+M, Space  Cleanup Active Document        CodeMaid
Global (370)
└─ ...
⚠ Merge Editor Window: F10 is gekoppeld aan 2 commands
```

   Bovenaan: zoeken (op naam en op toets, dus ook "wat doet Ctrl+D?"), filters (alleen extensies, alleen door mij aangepast, alleen conflicten, een scope), en de knop Exporteren.
6. **Exporteren.** JSON, XML, PNG, PDF, plus HTML. De export volgt de filters en indeling van het venster: wie alleen de Text Editor wil, krijgt een cheat sheet van één pagina.
7. **Instellingen** in beide Opties-vensters: taal, standaardindeling, VS-sneltoetsen tonen, papierformaat (A4, Letter), licht of donker thema voor PNG en PDF, akkoorden tonen.
8. **Strings.resx** in 15 talen, zoals ResourcePreview.

### Wat er niet in zit

- Sneltoetsen wijzigen. De extensie toont en exporteert; aanpassen doe je in VS zelf.
- Extensies in het VisualStudio.Extensibility-model herkennen.
- PDF met selecteerbare tekst.
- De lagen Default, Scheme en Profile via de private API. Eerst kijken of dat nodig is naast "aangepast door jou".

### Ideeën voor later

- Een sneltoets voorstellen voor commands die je vaak via het menu gebruikt. Dat vraagt meten wat je klikt; apart project.
- Twee exports vergelijken, bijvoorbeeld voor en na een VS-update of tussen twee laptops.
- Een cheat sheet van één venster: rechtsklik in Solution Explorer en alleen die scope plus Global afdrukken.

### Opbouw van de repo

Overgenomen van ResourcePreview en ExtensionOverlap:

```
VisualStudioShortcutCheatsheet/
├─ Directory.Build.props              ← output naar Builds\<project>\
├─ ShortcutCheatsheet.sln
├─ src/ShortcutCheatsheet/            ← VSIX, net48
│  ├─ Collecting/                     ← DTE en Unified Settings lezen
│  ├─ CommandTables/                  ← .cto uitpakken en lezen, geen VS nodig, getest
│  ├─ Origin/                         ← extensies vinden, sneltoets aan extensie koppelen
│  ├─ Model/                          ← Shortcut, Scope, CheatSheet; alleen data
│  ├─ Export/                         ← JSON, XML, HTML, PNG, PDF
│  ├─ ToolWindow/
│  ├─ Localization/                   ← Strings.resx + 14 vertalingen
│  └─ Options/                        ← registration.json + oude Opties-pagina
├─ tests/ShortcutCheatsheet.Tests/    ← MSTest, net48
├─ tests/Fixtures/                    ← een paar echte .ctmenu-bestanden als testdata
├─ tools/build-and-test.ps1
├─ publishManifest.json, README.md, CHANGELOG.md
└─ .github/workflows/release.yml
```

`CommandTables`, `Model` en `Export` hebben geen VS nodig. De tests lezen een `.ctmenu` van een kleine eigen test-extensie (een `.vsct` met twee commands en drie sneltoetsen) en controleren dat er precies dat uitkomt. Eén test leest CodeMaid als die op de machine staat, en slaat over als hij er niet is (zodat GitHub Actions blijft werken).

### Volgorde van bouwen

Op de branch `feature/v1`, met tussenstappen die je kunt testen:

1. Repo-opzet, buildscript, lege VSIX die laadt in de Experimental Instance.
2. `CommandTables` met tests: dit is het grootste risico, dus eerst.
3. Verzamelen en herkomst, met een export naar JSON om het resultaat te controleren.
4. Tool window met indeling, zoeken en filters.
5. De andere exports, instellingen, vertalingen.
6. README met screenshots, CHANGELOG, release-workflow.

## Beslissingen die ik van je nodig heb

1. **Naam.** De repo heet `VisualStudioShortcutCheatsheet`. Voorstel voor de weergavenaam: "Shortcut Cheatsheet", en `ShortcutCheatsheet` voor project en namespace. De lokale map heeft nu spaties (`Visual Studio Shortcut Cheatsheet`); bij ResourcePreview en ExtensionOverlap was de map gelijk aan de repo-naam.
2. **Minimum VS 2026** (`[18.0,19.0)`), net als ExtensionOverlap. Unified Settings voor sneltoetsen bestaat alleen in VS 2026.
3. **De command table lezen** (sectie 3c) als hoofdbron voor de herkomst, met het risico van een ongedocumenteerd formaat.
4. **PDF als afbeeldingen** met een eigen schrijver, plus HTML voor doorzoekbare tekst.
5. **Code delen met ExtensionOverlap.** `InstalledExtensions.cs` kopiëren (simpel, twee kopieën om bij te houden) of later een gedeeld project. Voorstel: kopiëren in v1.

## Besluiten (13 november 2026)

1. **Naam: Shortcut Cheatsheet.** `ShortcutCheatsheet` voor project, namespace en solution. De repo blijft `VisualStudioShortcutCheatsheet`.
2. **Minimum VS 2026**: `InstallationTarget Version="[18.0,19.0)"`.
3. **De command table is de hoofdbron voor de herkomst.** De GUID-tekst is alleen terugval.
4. **PDF als afbeeldingen**, met een eigen schrijver. De toetsen worden grafisch getekend als toetsen (een afgerond kader per toets, `Ctrl` `+` `K` en dan `Ctrl` `+` `C` voor een akkoord), in PNG en PDF. HTML komt erbij voor doorzoekbare tekst.
5. **Gedeelde code in een eigen repo.** Nieuwe repo `hnsoftwaredevelopment/ExtensionCommon` met een Shared Project (`.shproj`). ExtensionOverlap en Shortcut Cheatsheet nemen die op als git-submodule in `external\ExtensionCommon`. Eerste inhoud: `InstalledExtensions.cs` uit ExtensionOverlap. De release-workflow haalt de submodule mee met `submodules: true` in `actions/checkout`. Herbert maakt de lege GitHub-repo aan.

### Waarom een Shared Project en geen gewone DLL

Een Shared Project heeft geen eigen uitvoer. De bestanden worden meegecompileerd in elke extensie die hem gebruikt. Dat voorkomt twee problemen:

- Twee extensies met elk een eigen versie van `ExtensionCommon.dll` in hetzelfde VS-proces. VS laadt dan maar één van beide, en de andere extensie krijgt mogelijk de verkeerde versie.
- Een extra DLL in elke VSIX die ondertekend en meegeleverd moet worden.

Nadeel: de klassen moeten `internal` blijven, anders botsen ze met dezelfde klasse in een andere extensie. Dat is bij Shared Projects de gewoonte.
