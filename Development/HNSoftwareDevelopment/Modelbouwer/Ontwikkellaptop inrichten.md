---
tags: [modelbouwwerkbank, inrichting, beveiliging]
jira: KAN-78
---
# Ontwikkellaptop inrichten voor ModelbouwWerkbank

Sinds KAN-78 staan het databasewachtwoord en de Syncfusion-licentie niet meer in de repository. Op elke laptop waarop je ontwikkelt (Voortman-laptop en thuislaptop) richt je ze één keer zelf in.

## Wat de app leest
| Instelling | Waar | Verplicht | Standaard |
|---|---|---|---|
| `MODELBOUWER_DB_PASSWORD` | omgevingsvariabele (gebruiker) | ja | geen: app stopt met een melding |
| `MODELBOUWER_DB_USER` | omgevingsvariabele | nee | `root` |
| `MODELBOUWER_DB_SERVER` | omgevingsvariabele | nee | adres uit `Resources\Config\modelbouwer.config` |
| `MODELBOUWER_DB_PORT` | omgevingsvariabele | nee | `3306` |
| `MODELBOUWER_MOBILE_DB_SERVER` | omgevingsvariabele, alleen bij bouwen tablet-app | nee | adres uit `modelbouwer.config` |
| Syncfusion-licentie | `docs\SyncfusionLicense.txt` in de repo-map (staat in `.gitignore`) of variabele `MODELBOUWER_SYNCFUSION_LICENSE_KEY` | ja, anders trial-melding | |

De desktop-app leest de variabelen bij het starten. De tablet-app krijgt ze tijdens de build mee: het wachtwoord komt dan in de APK, niet in git.

## Let op: juiste Windows-account
Je terminal draait als `nb1164\local.admin`. Een variabele met bereik `User` die je daar zet, komt bij **local.admin** terecht en niet bij jouw eigen account. Visual Studio en de app draaien onder `herbert.nijkamp` en zien hem dan niet.

Zet de variabelen daarom op één van deze manieren:
- **Via Windows:** Start, typ "omgevingsvariabelen voor uw account", Nieuw. Dit venster werkt altijd voor het account waarmee je bent ingelogd.
- **Via PowerShell zonder beheerdersrechten**, gestart als jezelf (niet "Als administrator uitvoeren"):

```powershell
[Environment]::SetEnvironmentVariable('MODELBOUWER_DB_PASSWORD', 'jouw-wachtwoord', 'User')
# optioneel
[Environment]::SetEnvironmentVariable('MODELBOUWER_DB_USER', 'root', 'User')
[Environment]::SetEnvironmentVariable('MODELBOUWER_DB_SERVER', 'localhost', 'User')
[Environment]::SetEnvironmentVariable('MODELBOUWER_MOBILE_DB_SERVER', 'adres-van-de-nas', 'User')
```

Controleer met `whoami` dat je als `herbert.nijkamp` werkt. Gebruik geen enkel aanhalingsteken (`'`) en geen regelovergang in het wachtwoord: de build van de tablet-app kan daar niet mee overweg.

**Herstart Visual Studio** na het zetten van een variabele. VS geeft de variabelen bij het starten door aan builds. De desktop-app zelf leest ook direct de gebruikersvariabelen, dus die werkt zonder herstart.

## Syncfusion-licentiebestand
Dit project gebruikt Syncfusion 32.1. Je nieuwste licentiesleutel werkt daar niet mee, dus dit project heeft een eigen bestand met de oude sleutel.

Op een laptop waar het bestand nog niet staat, haal je de oude sleutel uit de git-historie (laatste commit vóór KAN-78):

```powershell
cd C:\DevOps\hnsoftwaredevelopment\ModelbouwWerkbank
$line = git show f759542:Modelbouwer/App.xaml.cs | Select-String 'RegisterLicense\( "([^"]+)"'
Set-Content docs\SyncfusionLicense.txt $line.Matches[0].Groups[1].Value -NoNewline
```

Bij de build wordt het bestand naast `Modelbouwer.exe` gezet, zodat de installer het meeneemt.

## Wachtwoord wijzigen (eenmalig, KAN-86)
Het oude wachtwoord stond in de publieke repo en moet op de NAS als gelekt worden beschouwd.

Op de NAS (MySQL-console of je MySQL-beheertool):

```sql
SELECT user, host FROM mysql.user WHERE user = 'root';
-- voor elke host uit het resultaat:
ALTER USER 'root'@'%' IDENTIFIED BY 'nieuw-sterk-wachtwoord';
```

Aanbevolen vervolgstap: een eigen gebruiker voor de app, zodat root niet meer van buitenaf nodig is:

```sql
CREATE USER 'modelbouwer'@'%' IDENTIFIED BY 'nieuw-sterk-wachtwoord';
GRANT SELECT, INSERT, UPDATE, DELETE, EXECUTE, SHOW VIEW ON modelbuilder.* TO 'modelbouwer'@'%';
```

Zet daarna `MODELBOUWER_DB_USER` op `modelbouwer`. Test eerst of alle schermen werken; als de app ergens tabellen aanmaakt of wijzigt, zijn extra rechten nodig.

Lokaal op de Voortman-laptop gebruik je je eigen lokale root-wachtwoord. Dat wijkt al af van wat in de code stond.

## Controle
1. Start Modelbouwer. Krijg je de melding "Er is geen databasewachtwoord ingesteld", dan ziet de app de variabele niet: controleer het account.
2. Zie je een Syncfusion-licentiemelding, dan ontbreekt `docs\SyncfusionLicense.txt` of staat er een sleutel voor een andere versie in.
3. Tablet-app: bij het bouwen zonder `MODELBOUWER_DB_PASSWORD` geeft de build een waarschuwing en meldt de app op de tablet dat er geen wachtwoord is meegebouwd.

## Productiedata naar de lokale database halen (KAN-108)
Met `Tools\Sync-ProductionToLocal.ps1` vervang je de lokale database `modelbuilder` door een kopie van de productiedatabase op de NAS. Productie wordt alleen gelezen.

```powershell
cd C:\DevOps\hnsoftwaredevelopment\ModelbouwWerkbank
.\Tools\Sync-ProductionToLocal.ps1
```

Wat het script doet:
1. Controleert of productie en lokaal bereikbaar zijn. Vanaf het Voortman-netwerk is de NAS niet bereikbaar; draai het thuis.
2. Vraagt bevestiging (overslaan met `-Force`).
3. Maakt een back-up van de lokale database in `Documenten\ModelbouwWerkbank\db-backups` (de laatste 5 blijven bewaard, aan te passen met `-KeepBackups`).
4. Leest productie uit, inclusief views, procedures, functies en afbeeldingen.
5. Zet `DEFINER=root@%` om naar de lokale gebruiker met `SQL SECURITY INVOKER`. Zonder deze stap geven de views lokaal de fout "The user specified as a definer does not exist".
6. Vervangt de lokale database. Mislukt de import, dan zet het script de back-up automatisch terug.
7. Toont een telling van tabellen, views, procedures en de belangrijkste tabellen, voor productie en lokaal naast elkaar.

Wachtwoorden:
- Lokaal: dezelfde `MODELBOUWER_DB_PASSWORD` als de app.
- Productie: `MODELBOUWER_PROD_DB_PASSWORD` (en eventueel `MODELBOUWER_PROD_DB_USER`, standaard `root`). Staat die niet ingesteld, dan vraagt het script erom; het wachtwoord wordt dan nergens opgeslagen.
- Het productieadres komt uit `modelbouwer.config.external`. Een ander adres geef je op met `-ProdServer`.

Productie draait **MariaDB 10.3**, lokaal draait MySQL 26.x. Het script haalt daarom ook de SQL-modus `NO_AUTO_CREATE_USER` uit de procedures, want MySQL 8 en hoger kent die niet meer. Houd bij nieuwe SQL rekening met dit verschil: wat lokaal werkt, moet ook op MariaDB 10.3 draaien.

Let op: zolang het opruimscript van KAN-100 nog niet op de NAS is gedraaid, haal je ook de dubbele voorraadcorrecties weer binnen. Draai dat script eerst op de NAS.
