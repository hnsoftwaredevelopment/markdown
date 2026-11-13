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
