# Start: extensie "Visual Studio Shortcut Cheatsheet" (werktitel)

## Doel

Ik wil een Visual Studio 2026-extensie bouwen die een overzicht kan genereren van alle shortcut keys die beschikbaar zijn in de VS Instance van de gebruiker.

Ik wil dat de Keys zoveel mogelijk worden gegroepeerd, bijvorbeeld op area, waar kun je deze key toepassen. Daarnaast wil ik kunnen zien waar de key vandaan komt (Extension bijvoorbeeld, bij standaard VS shortcuts hoeft dit niet genoemd te worden).

De gebruiker moet het cheat sheet kunnen exporteren als xml, json, png of pdf (misschien komen we gedurende het proces op nnog meer formats)

Misschien groeit de functionaliteit naarmate het project vorderd (bijvoorbeeld de gebruiker laten kiezen hoe te categoriseren)

## Eerste stap

Begin niet met code. Onderzoek eerst wat technisch haalbaar is, eventueel aanvullend voorstel voor functionaliteit en leg het me voor,
met een voorstel voor de eerste versie:

## Folders en repository

Ik geef je hierbij volledige toegang tot de volgende folders en repository:
Project folder: c:\DevOps\hnsoftwaredevelopment\Visual Studio Shortcut Cheatsheet\
Overal development folder: c:\DevOps\hnsoftwaredevelopment\
Repository: https://github.com/hnsoftwaredevelopment/VisualStudioShortcutCheatsheet

## Vorig project als referentie

Mijn vorige extensies zijn:
XAML Resource Preview (repo: https://github.com/hnsoftwaredevelopment/ResourcePreview)
Object Explorer for MySQL (repo: https://github.com/hnsoftwaredevelopment/ObjectExplorerForMySQL)
Extensions Overlap (in bewerking) (repo: https://github.com/hnsoftwaredevelopment/ExtensionOverlap)

- Leerdocument: C:\DevOps\hnsoftwaredevelopment\Obsidian\Development\Projects\Handleiding extension bouwen.md
  Lees die eerst, dit document is nu gebasseerd op ResourcePreview maar moet een algemene handleiding worden voor nieuwe extensions, dus werk het gerus bij gedurende het proces. Neem de opbouw, het buildscript, de workflow en de lessen over waar
  dat past.

## Afspraken over de opzet

- Repo onder de GitHub-organisatie hnsoftwaredevelopment (niet onder herbie68),
  lokaal in C:\DevOps\hnsoftwaredevelopment\<ProjectNaam>.
- Build-output in <repo>\Builds\<projectnaam>\ via Directory.Build.props, nooit bin\.
- VSIX-project op net48 (klassiek VSSDK), voor Visual Studio 2026.
- Unittests (MSTest, net48) die zonder Visual Studio draaien. Bouwen en testen met
  tools\build-and-test.ps1, net als in ResourcePreview: dat script kiest Enterprise,
  Professional of Community, niet BuildTools.
- Teksten in de UI via Strings.resx, in dezelfde 15 talen als ResourcePreview.
- Instellingen in beide Options-vensters, net als in ResourcePreview.
- GitHub Actions-workflow release.yml (build, tests, GitHub Release met de notes uit
  CHANGELOG.md, optioneel publiceren naar de Marketplace), plus publishManifest.json.
- Marketplace-publisher: hnsoftwaredevelopment.
- Maak zoveel mogelijk gebruik van lokale herbruikbare powershell scripts om credits/tokens te besparen.

## Documentatie

- README.md in het Engels, kort, met screenshots per functie (voor GitHub en de Marketplace).
- CHANGELOG.md in het Engels.
- Een Nederlandse handleiding "Handleiding extension bouwen.md" voor dit project, waarin
  je per stap uitlegt hoe het werkt en waarom. Dit is mijn leerdocument.
- Elk .md-bestand dat je maakt of wijzigt spiegel je ook naar
  C:\DevOps\hnsoftwaredevelopment\Obsidian\Development\Projects\<ProjectNaam>
  en naar dit Claude-project.
- md bestanden die puur bedoelt zijn voor het ontwikkelproces komen alleen in Obsidian andere bestanden die voor gebruikers relevante informatie bevatten (readme, changelog) komen ook in de repo

## Stijl

- Antwoorden in het Nederlands, direct en concreet. Geen " — " streepjes, geen modewoorden, geen herhaalde structuren.
- Commentaar in de code in het Engels, kort.
- Commits in het Engels: een korte eerste regel, daarna wat en waarom.

## Werkwijze met mijn computer

- Werk op mijn computer via de gekoppelde map; push vanaf mijn computer (de cloud-kloon
  krijgt een 403). Git staat in:
  C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe
- Na het overzetten van bestanden: controleer de MD5-hashes op mijn computer.
- Testen in VS doe ik in de Experimental Instance (devenv /rootsuffix Exp).
- Screenshots kun je zelf maken met de scripts in
  C:\DevOps\hnsoftwaredevelopment\ResourcePreview\obj (vs.ps1, shots2.ps1, shots3.ps1).
  Geef aan wanneer ik van de muis en toetsenbord af moet blijven.
- Ik wil gebruik maken van feature brances, zodat een aanvulling of wijziging op de applicatie niet direct de draaiende extensie beïnvloed. Als een feature voltooid is en door mij akkoord gegeven dan mag deze worden gemerged naar main, de featurebrance kan dan worden verwijderd
