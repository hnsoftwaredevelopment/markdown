# CODEX-projectoverdracht — HN Software Development Platform

## Doel en afbakening

Deze map is op 16 juli 2026 geïnventariseerd als een lege Codex-projectmap. Hij bevat uitsluitend een lokale Git-repository; er zijn geen bronbestanden, documentatie, projectconfiguratie, `.codex`-map, `AGENTS.md`-bestand, commits of remote-repository aanwezig.

Het praktische doel is daarom een gelijkwaardige **lege, vertrouwde Codex-werkruimte** te herstellen. Dit document beschrijft de leesbare project- en gebruikersconfiguratie die tijdens de inventarisatie van invloed is op die ervaring. Het maakt geen aanspraak op herstel van persoonlijke sessies, geheimen of verborgen Codex-appmetadata.

## Benodigde bestanden, mappen en repositories

| Onderdeel | Huidige toestand | Nodig bij herstel |
| --- | --- | --- |
| Projectmap | `C:\Users\hnijk\OneDrive\Data\HN Software Development Platform` | Maak of kopieer een map met deze naam (of pas het pad consequent aan). |
| Git | Geïnitialiseerde repository op branch `main`; geen commits en geen remote | Voer `git init -b main` uit. Er hoeft geen repository gekloond of remote ingesteld te worden. |
| Projectbestanden | Geen | Geen vereist. Voeg pas broncode/configuratie toe wanneer dit platform een concreet project gaat bevatten. |
| Projectinstructies | Geen fysiek project-`AGENTS.md` en geen `.codex` aanwezig | Zie de verplichte algemene instructie hieronder. |
| Overdrachtsbestand | Dit bestand | Bewaar in de hoofdmap. |

De Git-repository heeft `core.filemode=false`, `core.symlinks=false`, `core.ignorecase=true` en `core.logallrefupdates=true`. Deze waarden zijn normale Windows-standaarden en niet uniek voor dit project. Er zijn geen Git-hooks, submodules, LFS-tracked bestanden of ignore-regels aangetroffen die herstel vereisen.

## Instructies die Codex altijd moet volgen

De enige aangetroffen toepasselijke instructie komt uit het globale `C:\Users\hnijk\.codex\AGENTS.md` (niet uit de projectmap):

> Bij het maken of wijzigen van een Markdown-bestand voor een HN Software Development-project moet Codex het bijgewerkte bestand ook kopiëren naar `C:\Data\Obsidian\markdown\Development\HNSoftwareDevelopment\<Projectnaam>`. Gebruik standaard de naam van de repositorymap als projectnaam en behoud waar praktisch de relatieve mapstructuur. Meld expliciet wanneer die kopie niet lukt.

Voor dit project is `<Projectnaam>` `HN Software Development Platform`. Dit document hoort dus gespiegeld te worden naar `C:\Data\Obsidian\markdown\Development\HNSoftwareDevelopment\HN Software Development Platform\CODEX-PROJECT-OVERDRACHT.md`.

Aanvullende algemene Codex-conventies die in de actieve desktopconfiguratie zichtbaar waren:

- maak Git-commits en pull requests in het Engels;
- vermeld bij commits wat en waarom er is gewijzigd, inclusief waarom een voor de hand liggend alternatief niet is gekozen wanneer dat relevant is;
- gebruik standaard branchnamen met voorvoegsel `codex/` bij het maken van een nieuwe branch;
- de interface is ingesteld op Nederlands (`nl-NL`) en Git wordt standaard in Visual Studio geopend.

Er zijn geen aanvullende projectconventies of terugkerende werkprocessen in bestanden, Git-geschiedenis of taken binnen deze map aantoonbaar.

## Skills, hulpmiddelen en plug-ins

Er zijn **geen projectgebonden skills** of lokale hulpmiddelen aangetroffen: er is geen `.codex`, `skills/`, script, package manifest of bronmap in deze repository.

De onderstaande voorzieningen zijn algemene, gebruikersbrede Codex-installaties. Herinstalleer of activeer ze alleen als een vergelijkbare algemene werkomgeving gewenst is; deze lege repository is er niet functioneel van afhankelijk.

| Herkomst | Ingeschakelde plug-ins / mogelijkheden |
| --- | --- |
| OpenAI curated | Superpowers, GitHub, Build Web Apps, Vercel, CodeRabbit, Teams, Notion, Gmail en Google Calendar. |
| OpenAI primary runtime | Documents, Spreadsheets, Presentations, PDF en Template Creator. |
| OpenAI bundled | Browser Use, Browser en Visualize. |
| Lokale algemene skills | Agents SDK, Cloudflare (inclusief One, Durable Objects, Wrangler en Workers-praktijken), Playwright, Sandbox SDK, Turnstile, web performance en enkele ModelbouwWerkbank-/Amusing-publicatieskills. Dit zijn geen skills van dit project. |

Daarnaast is een lokale Node REPL MCP-server geconfigureerd, maar de bijbehorende feature staat uit. Hij is dus geen vereiste voor dit project. De standaard Codex-runtimes, modellen en plug-inversies zijn app-/installatiegebonden en mogen op de nieuwe laptop afwijken.

## Externe koppelingen, accounts en instellingen

Er is geen project-remote, cloudresource, API-sleutel, database, CI/CD-configuratie of omgevingsbestand gevonden.

De algemene Codex-configuratie heeft plug-ins voor GitHub, Teams, Notion, Gmail en Google Calendar ingeschakeld. Als deze op de nieuwe laptop gebruikt moeten worden, meld dan in Codex opnieuw aan bij de betreffende accounts en autoriseer de koppelingen. Er is geen bewijs dat dit project een van die koppelingen gebruikt.

Git is lokaal geconfigureerd met Git Credential Manager en Git LFS. Een persoonlijke Git-naam/e-mailadres en credentials zijn gebruikersgegevens: stel ze op de nieuwe laptop zelf in en kopieer geen `auth.json`, tokens, cookies, sessiedatabases of de volledige `.codex`-map.

## Belangrijke context buiten projectbestanden

- Deze map is vermoedelijk bedoeld als container voor het bredere HN Software Development Platform, maar die functie staat niet nader beschreven in de leesbare bestanden.
- De map is op de huidige laptop aangemerkt als `trusted` in de globale Codex-configuratie. Daardoor kan Codex er met ruimere lokale rechten werken. Dit is geen repositorybestand en moet op een nieuwe laptop bewust opnieuw worden vertrouwd.
- Er is geen taakgeschiedenis, commitgeschiedenis of documentatie in de repository waaruit besluiten kunnen worden gereconstrueerd. Daarom zijn er geen aantoonbare eerdere projectbesluiten om over te dragen.

## Opnieuw inrichten op een nieuwe laptop

1. Installeer Codex Desktop, Git en (optioneel) Git LFS.
2. Maak de projectmap, bij voorkeur onder een gesynchroniseerde OneDrive-locatie: `C:\Users\<gebruiker>\OneDrive\Data\HN Software Development Platform`.
3. Initialiseer de lege repository: `git init -b main`. Voeg alleen een remote toe als er later een echte centrale repository wordt gekozen.
4. Plaats dit overdrachtsbestand in de hoofdmap.
5. Maak `C:\Data\Obsidian\markdown\Development\HNSoftwareDevelopment\HN Software Development Platform` aan, of kies een equivalente lokale Obsidian-kluis. Leg dezelfde Markdown-spiegelregel vast in `C:\Users\<gebruiker>\.codex\AGENTS.md`.
6. Installeer/activeer naar behoefte de hierboven genoemde algemene Codex-plug-ins en meld opnieuw aan bij de benodigde externe diensten. Herstel geen auth- of sessiebestanden door te kopiëren.
7. Configureer Git-identiteit, Credential Manager en eventueel LFS voor de nieuwe gebruiker.
8. Open de map in Codex en markeer haar alleen als vertrouwd wanneer de lokale inhoud en herkomst zijn gecontroleerd.

## Korte controlelijst

- [ ] De projectmap opent in Codex en `git status --branch` meldt `main` zonder remote/commits.
- [ ] `CODEX-PROJECT-OVERDRACHT.md` staat in de projecthoofdmap.
- [ ] Een proefwijziging aan een Markdown-bestand wordt gespiegeld naar de Obsidian-map.
- [ ] De Markdown-spiegelinstructie is beschikbaar voor Codex (globaal of als project-`AGENTS.md`).
- [ ] Eventuele gewenste plug-ins zijn ingeschakeld en externe accounts zijn opnieuw geautoriseerd.
- [ ] Geen persoonlijke geheimen, tokens, sessies of volledige `.codex`-map zijn gekopieerd.

## Niet uitleesbare of bewust niet overgenomen informatie

Niet volledig uitleesbaar of niet veilig overdraagbaar waren: verborgen Codex Desktop-appinstellingen en projectmetadata, actieve/intern opgeslagen taakconversaties, accountautorisaties en tokens, browsercookies, secrets, lokale databases en persoonlijke herinneringen. Ook is niet vast te stellen welke externe accounts op de nieuwe laptop moeten worden gebruikt; in deze repository bestaat daar geen verwijzing naar.
