---
tags: [modelbouwwerkbank, analyse]
datum: 2026-11-23
repo: https://github.com/hnsoftwaredevelopment/ModelbouwWerkbank
jira: https://hnsoftwaredevelopment.atlassian.net/jira/software/projects/KAN/boards/1
---
# ModelbouwWerkbank: statusanalyse 23-11-2026

## Waar je bent gebleven
- Laatste commit: 19-06-2026 `f759542` "Improved formattig of the code" op `master`.
- Werkmap schoon, `master` gelijk aan `origin/master`. Er staat geen half werk lokaal.
- Laatste functionele werk (mei 2026): MAUI-app voor de Android-tablet (PR #44), timer in de mobiele app, bulk voorraadontvangst, stabiliteit van async laden.
- Open GitHub issues: #45 (voorraadhistorie per product) en #46 (orderhistorie per leverancier). Beide met label `[zube]: Backlog`: je gebruikte toen Zube als planbord.
- Build desktop: geslaagd, 0 warnings. Unit tests: 345 van 345 geslaagd.

## Oplossing
| Project | Techniek | Inhoud |
|---|---|---|
| `Modelbouwer` | WPF, .NET 10, CommunityToolkit.Mvvm, Syncfusion 32.1, MySql.Data 9.5, ClosedXML | Desktopapplicatie, versie 26.5.27 |
| `Modelbouwer.Mobile` | .NET MAUI 10 (Android, ook Windows/MacCatalyst targets) | Tablet-app, versie 26.5.25 |
| `Modelbouwer.UnitTests` | xUnit | 345 tests: services, viewmodels, XAML-wiring |
| `Modelbouwer.Tests` | 1 testbestand | Staat niet in de solution |
| `Installer` | Inno Setup | `Modelbuilder.iss` + buildscript |
| `Database` | SQL-scripts | Tabellen, views, procedures, dumps |

Architectuur desktop: MVVM met DI (Microsoft.Extensions.Hosting). Per entiteit een Service + Interface, generieke `GenericDataService` en `EntityPageViewModel` als basis voor CRUD-schermen. Teksten via `Language.resx` (NL, EN-US, DE).

## Functionaliteit desktop
| Onderdeel | Schermen | Stand |
|---|---|---|
| Urenregistratie | `TimeRegistrationView` (uren en materiaal per project), `ProjectView` | Werkt. Projecten met verwachte bouwtijd en berekende resterende werkdagen |
| Rapportages | `ProjectReportsView` | Werkt. Uren per weekdag/maand/jaar/werksoort, kostenverdeling, kostendeclaraties, optie uren meenemen tegen uurtarief |
| Voorraadbeheer | `StockManagementView`, `StorageLocationView` | Werkt. Voorraad per product en opslaglocatie (boomstructuur) |
| Inkoop | `StockOrderView`, `StockReceiptView` + dialogen | Werkt. Orders met regels, ontvangsten registreren (ook bulk), voorraadcorrectie |
| Bestel advies | geen | **Niet gevonden.** Wel `MinimalStock` op product, procedure `GetProductsBySupplier` met kolom `InventoryOrder` en ongebruikte constanten `ProductInventoryOrderProcedure*` in `DBNames.cs` |
| Stambestanden | Product, Leverancier (+contacten), Merk, Categorie, Eenheid, Werksoort, Land, Valuta, Contacttype | Werkt. Tabbladen Voorraadhistorie (product) en Orderhistorie (leverancier) zijn leeg: zie GitHub #45 en #46 |
| Instellingen | `SettingsView` | Regio, taal, uurtarief. Opgeslagen in tabel `settings` |
| Over | `AboutView` | Releasehistorie via GitHub API |
| Import/export | `CsvImportService`, `CsvExportService`, `ExcelExportService` | Aanwezig, o.a. Cornwall-deuvelimport (zie `docs/`) |

## Functionaliteit mobiele app
Vier tabbladen: **Tijd** (uren boeken, timer starten/stoppen), **Materiaal** (verbruik boeken), **Producten** (toevoegen/wijzigen), **Projecten** (toevoegen/wijzigen).
- Verbindt rechtstreeks met MySQL (`MySqlMobileWorkspaceService`), geen API ertussen.
- Een lopende timer staat in `Preferences` op het toestel, niet in de database. Een timer gestart op de tablet is dus niet zichtbaar op de desktop.
- `tmp/tablet-crash-logcat.txt` wijst op een crash op de tablet die is onderzocht. Of die is opgelost, is niet duidelijk.

## Database
- Schema `modelbuilder`, 22 tabellen: brand, category, contacttype, country, currency, months, product, productinventoryold, productsupplier, productusage, project, settings, stock, stocklog, storage, supplier, suppliercontact, supplyorder, supplyorderline, time, unit, flyway_schema_history.
- Circa 25 views en circa 20 stored procedures/functies (scripts in `Database/`).
- Flyway alleen als baseline (07-01-2026). Er zijn geen migratiescripts; schemawijzigingen gaan nu handmatig.
- Serveradres staat gecodeerd in `Resources/Config/modelbouwer.config` (`.local` = 127.0.0.1, `.external` = een publiek IP-adres). De mobiele app gebruikt standaard dat publieke adres, met `SslMode=Disabled`.
- Lokale verbinding met het wachtwoord uit de code lukte niet (access denied voor root). Het lokale wachtwoord wijkt dus af van wat in de code staat.

## Bevindingen
### Kritiek: databasewachtwoord in publieke repo
De repository is **publiek**. Het MySQL root-wachtwoord staat leesbaar in `Modelbouwer/Helpers/DBConnect.cs` en `Modelbouwer.Mobile/Services/MobileDbConnectionSettings.cs`, en dus ook in de git-historie. Het IP-"versleutelen" in de config is een eenvoudige rekensom en geen beveiliging. Als poort 3306 van de NAS vanaf internet bereikbaar is, kan iedereen met deze repo inloggen als root. Jira: [[KAN-78]].

### Overig
- Code-analyse mei 2026 (`docs/superpowers/plans/2026-05-01-code-analysis-*`): 579 analyzer-meldingen, 6 concepttickets. Een deel lijkt al uitgevoerd: `IStockOrderService` en `ITimeRegistrationService` hebben al `CancellationToken`-overloads. Status per ticket nog vaststellen.
- Coverage-backlog (`2026-04-30-coverage-backlog.md`): veel genoemde tests bestaan inmiddels.
- Verouderde remote branches: `CreateProductView`, `TimeReports`, `RefactorSupplierPageViewModel`, `coderabbitai/utg/4ca878e`.
- `Database/` bevat elke view dubbel (`view-*.sql` en `view_*.sql`) en dumps van 4 tot 13 MB in git.
- `language.csv`, `TableKeys.xlsx`, `favorites.json` in de root: doel onbekend.
- Syncfusion is commerciële software (community-licentie?). Controleren of dat past bij je eis voor open source.
- Hoofdbranch heet `master`, niet `main`.
- GitHub-bots: CodeRabbit is actief op PR's.

## Jira (KAN)
| Epic | Label | Key |
|---|---|---|
| ModelbouwWerkbank (overkoepelend) | `modelbouwwerkbank` | KAN-72 |
| Urenregistratie | `ModelbouwWerkbank.Hourregistration` | KAN-73 |
| Voorraadbeheer | `ModelbouwWerkbank.StorageManagement` | KAN-74 |
| Stambestanden | `ModelbouwWerkbank.MasterData` | KAN-75 |
| Rapportages | `ModelbouwWerkbank.Reports` | KAN-76 |
| Mobiele app | `ModelbouwWerkbank.Mobile` | KAN-77 |

Stories: KAN-78 (wachtwoord uit code, prioriteit High), KAN-79 (repo opschonen), KAN-80 (voorraadhistorie, GitHub #45), KAN-81 (orderhistorie leverancier, GitHub #46), KAN-82 (bestel advies).

## Werkwijze
Feature branch per User Story (`feature/KAN-xx-korte-naam`). Herbert test, daarna commit en push. Story klaar en goedgekeurd: PR naar `master`, botmeldingen beoordelen en afhandelen, merge, branch verwijderen. Jira-status bijwerken bij elke stap met link naar commit of PR.

## Stand van docs/superpowers (Zube-backlog)
Gecontroleerd tegen de code op 23-11-2026. De checkboxen in de plannen zijn nooit afgevinkt, dus die zeggen niets over de werkelijke stand.

| Document | Onderdeel | Stand |
|---|---|---|
| stock-order-design + implementation | Inkooporders (8 taken) | Gebouwd, PR #27. Supplier-filter (bonus) niet gecontroleerd |
| cornwall-dowel-import | Eenmalige import Cornwall-deuvels | Uitgevoerd en code verwijderd; `ImportCleanupTests` bewaakt dat |
| coverage-backlog CB-01 | UnitService tests | Klaar |
| CB-02 t/m CB-06 | Tests Country-, Category-, StorageLocation-, WorkType-, CurrencyService | **Open**, geen testbestanden |
| CB-07 t/m CB-11 | Tests Project-, StockManagement-, Category-, StorageLocation-, WorkType-PageViewModel | Deels: bestanden bestaan (60 tot 110 regels), dekken niet alle criteria |
| CB-12 t/m CB-14 | Product-, Supplier-, StockOrder-ViewModel uitbreiden | Grotendeels klaar (580 tot 1080 regels). "Heropen order" bestaat nog niet |
| CB-15 | CsvImportService tests | Klaar |
| CB-16, CB-17 | CsvExport- en ExcelExportService tests | **Open** |
| Analyse-ticket 1 | CancellationToken in basisinfrastructuur | Deels: `GenericDataService` klaar, `App` start/stop nog zonder token |
| Analyse-ticket 2 | CancellationToken in CRUD-interfaces en validators | **Open** |
| Analyse-ticket 3 | StockOrder analyzer-meldingen | Klaar |
| Analyse-ticket 4 | ConfigureAwait expliciet maken | **Vervallen** (besluit 23-11-2026): in WPF-viewmodels breekt `ConfigureAwait(false)` de UI-thread, in de servicelaag levert het weinig op |
| Analyse-ticket 5 | Naamgeving Worktype/WorkType, DBNames-spelling | **Open**: klassen heten nog `Worktype*` in `WorkType*`-bestanden, 19 spelfouten in `DBNames.cs` |
| Analyse-ticket 6 | Kleine analyzer-meldingen | Open, niet per melding gecontroleerd |

Overgenomen in Jira: KAN-88 testdekking (subtaken KAN-89 services, KAN-90 viewmodels, KAN-91 export), KAN-92 CancellationToken (tickets 1 en 2), KAN-93 naamgeving (ticket 5), KAN-94 kleine meldingen (ticket 6), KAN-95 gesloten inkooporder heropenen. Alle met prioriteit Low, KAN-94 Lowest.

## Stand einde dag 23-11-2026
| Ticket | Onderwerp | Stand |
|---|---|---|
| KAN-78 | Wachtwoord en Syncfusion-sleutel uit de code | Gemerged (PR #47). Open: KAN-86, wachtwoord NAS wijzigen. Let op `root@%` als definer, zie KAN-86 |
| KAN-100 | Voorraad dubbel geteld bij inkooporders | Gereed (PR #48). Open: opruimscript `Database/KAN-100-cleanup-order-stock-corrections.sql` op de NAS draaien na back-up |
| KAN-102 | Ontvangstscherm vereenvoudigen (lost KAN-101 op) | Functioneel akkoord, gecommit op `feature/KAN-102-ontvangstscherm` (867a095). Volgende stap: orderkeuze als herbruikbare dropdown (subtaak), dan PR |
| KAN-103 | Bestelscherm vereenvoudigen | Nog doen. Gebruikt de dropdown uit KAN-102 en de popup `SupplierProductDialog` |
| KAN-82 | Bestel advies | Komt in het bestelscherm (filter "alleen tekort", knop "tekorten toevoegen") |

Lokale database: views en procedures met definer `root@%` omgezet naar `SQL SECURITY INVOKER` (die gebruiker bestaat lokaal niet).
