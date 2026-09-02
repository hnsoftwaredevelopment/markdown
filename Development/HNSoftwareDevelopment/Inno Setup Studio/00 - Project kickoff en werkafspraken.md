# Project kickoff en werkafspraken: Inno Setup Studio

Datum: 2 september 2026
Repo: hnsoftwaredevelopment/InnoSetupStudio (nu leeg, alleen README)

## Beoordeling

Het idee is goed en het gat is reëel. Inno Setup zelf heeft geen GUI, alleen een teksteditor met syntax highlighting. Iedereen die een .iss bestand onderhoudt moet de sectienamen en property namen uit het hoofd kennen of steeds de help erbij pakken. Een tool die de structuur van een .iss bestand vertaalt naar aparte, herkenbare schermen lost een concreet probleem op, ook voor jezelf bij toekomstige installers.

Twee onderdelen zijn duidelijk het grootste risico, de rest is degelijk handwerk:

1. De live preview van wizardschermen. Inno Setup rendert zijn schermen zelf, er is geen API om dat te hergebruiken. De preview moet dus een eigen WPF nabootsing worden van elk standaardscherm (Welcome, License, Select Destination, Ready, Installing, Finished, en de rest), gestuurd door hetzelfde datamodel dat ook de .iss genereert. Dat is goed te bouwen, maar het blijft een gelijkende kopie, geen live render van de echte setup.exe. Dat onderscheid moet je gebruikers (of jijzelf over een jaar) helder blijven, anders verwacht men pixel perfect gedrag.
2. Pascal Scripting. Een volwaardige editor met foutcontrole en autocomplete voor Pascal Script bouwen is een project op zich. Realistisch scope voor nu: een code editor met syntax highlighting (AvalonEdit leent zich hiervoor) voor de [Code] sectie, met snippets voor de bekende event functies (InitializeSetup, CurStepChanged, NextButtonClick, en zo verder). De echte validatie laat je aan ISCC.exe zelf over bij het compileren, die geeft compilerfouten met regelnummer terug.

De rest, projectinstellingen, sectiekeuze met checkboxen, property editors per element, thema's, taalkeuze, versienummering, is standaard WPF werk waar je met MVVM en DynamicResource al ver mee komt.

## Wat ik al gezien heb

Ik heb de mapstructuur bekeken voor ik dit schreef:

- De GitHub repo is leeg (1 commit, alleen README).
- De projectfolder bevat nu de Inno Setup 7 handleiding (Vraagbaak 2.1, 556 KB) en syncfusionlicense.txt.
- HNSoftwareInstallerFramework is een bestaand PowerShell + modulaire .iss opzet (Base.iss, Architecture.iss, Files.iss, Shortcuts.iss). Die sectie indeling is een goed startpunt voor het datamodel.
- InnoSetup Examples bevat de officiële voorbeelden, inclusief een aantal Pascal Script voorbeelden (CodeDlg.iss, CodeClasses.iss, CodeDependencies.iss) die precies laten zien wat de meest gebruikte patronen zijn.
- In Obsidian staan al eigen projecten die rechtstreeks herbruikbaar zijn: CreateVectorResourceDictionary (vector iconen, sluit aan op je icons.xaml wens), SVGViewer, SVGConverter en FontManager. Die wil ik bekijken voor ik het thema en icon systeem opnieuw uitvind.
- Development\HNSoftwareDevelopment\Inno Setup Studio\ bestaat al in Obsidian maar is nog leeg. Dat is de map waar dit document naartoe gemirrord is.

Let op: de algemene Cowork instructie noemt Development\Projects\<ProjectName> als mirror locatie, jouw instructie in dit project noemt Development\HNSoftwareDevelopment\Inno Setup Studio\. Ik gebruik de laatste, die map bestond al en past bij de andere projecten die daar staan. Zeg het als dat niet de bedoeling is.

## Voorgestelde architectuur

Solution met een paar duidelijk gescheiden projecten:

- InnoSetupStudio.Core: het datamodel van een .iss project (Setup sectie, Types, Components, Tasks, Files, Icons, Run, Code) plus de generator die daarvan tekst maakt en de parser die bestaande .iss bestanden terugleest.
- InnoSetupStudio.Wizard: de WPF UserControls die elk wizardscherm nabootsen, een control per scherm type (Welcome, License, SelectDir, Ready, en zo verder), elk met zijn eigen editable properties.
- InnoSetupStudio.App: de WPF shell, MVVM (CommunityToolkit.Mvvm ligt voor de hand), navigatie tussen projectinstellingen, schermkeuze en scherm editor.
- InnoSetupStudio.Localization: de 3 resx bestanden (nl, en, de) achter een LocalizationManager die INotifyPropertyChanged implementeert, zodat een taalwissel direct doorwerkt in alle open schermen zonder herstart. Directe resx binding in XAML doet dat niet vanzelf, dat moet je bewust bouwen.

Thema's: 9 ResourceDictionaries, een per thema, samengevoegd in Application.Resources bij het opstarten en gewisseld tijdens runtime. Alle XAML gebruikt DynamicResource, nooit StaticResource, voor kleuren en brushes, anders werkt live wisselen niet overal.

Versienummering (YYYY.MM.dd.xxx): een MSBuild target die voor de build een teller bijhoudt in een klein JSON bestand, ophoogt bij een nieuwe build op dezelfde dag, reset bij een nieuwe dag, en het resultaat in AssemblyInformationalVersion zet. Dat nummer komt dan ook op het splashscreen.

Syncfusion licentie: syncfusionlicense.txt verplaats ik naar buiten de repo, bijvoorbeeld %LocalAppData%\InnoSetupStudio\license\syncfusionlicense.txt. De app leest hem daar bij het opstarten. Een regel in .gitignore is een goede extra vangnet, maar niet de enige bescherming, een bestand dat nooit in de repo folder staat kan ook nooit per ongeluk meegecomit worden.

.NET versie: ik stel .NET 10 voor, niet .NET 8. .NET 8 en .NET 9 bereiken beide end of support op 10 november 2026, over ruim 2 maanden. .NET 10 is de nieuwe LTS release (uitgebracht november 2025, ondersteund tot november 2028) en Syncfusion heeft daar vanaf de release al ondersteuning voor. Voor een project dat nu start is dat de logische keuze.

## Roadmap, als feature branches

1. feature/solution-scaffolding: solution, projectstructuur, thema systeem met de 9 thema's, localization manager met de 3 resx bestanden, splashscreen met versienummer.
2. feature/project-settings: het scherm voor algemene projectinformatie (naam, ontwikkelaar, contactgegevens, bestandslocaties, icon).
3. feature/screen-selection: het overzicht met checkboxen en preview thumbnails om wizardschermen aan of uit te zetten.
4. feature/screen-editor: de schermeditor zelf, klikbare elementen, property panel, live doorwerken in de preview.
5. feature/iss-generation: de generator die het datamodel naar een werkend .iss bestand schrijft, en de parser voor bestaande bestanden.
6. feature/pascal-code-editor: de AvalonEdit gebaseerde editor voor de [Code] sectie met snippets.
7. feature/build-integration: ISCC.exe aanroepen vanuit de app, compileerlog tonen, installer direct kunnen starten.
8. feature/help-pdf: de handleiding per taal, te openen vanuit een help knop.

Elke fase wordt een los te reviewen PR, in de volgorde hierboven omdat elke fase op de vorige leunt.

## Werkafspraken

- Elke feature krijgt een eigen branch, na lokaal testen commit en push ik, bij een afgeronde en geteste feature maak ik een gewone (geen draft) PR aan zodat CodeRabbit die kan reviewen.
- Zinvolle suggesties van CodeRabbit verwerk ik, daarna merge naar main en de branch verwijderen.
- Tussentijds hou ik mijn toelichting kort. Aan het eind van een feature krijg je een volledig overzicht van wat er is aangepast en wat je zou moeten testen.
- Elk .md bestand dat ik maak of aanpas mirror ik naar Development\HNSoftwareDevelopment\Inno Setup Studio\ in Obsidian.

## Nog te bevestigen

- Start ik nu met de solution scaffolding (fase 1), of wil je dit document eerst laten bezinken.
- .NET 10 als target, akkoord.
- CreateVectorResourceDictionary, SVGViewer en FontManager mag ik bekijken als basis voor het icon en thema systeem, in plaats van dat opnieuw te bouwen.
