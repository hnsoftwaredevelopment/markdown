# Installer Framework — gebruik

## Bewuste keuzes vóór de eerste build

- Maak een unieke `AppId` voor het product en bewaar die voor alle toekomstige upgrades.
- Stel `MainExecutable` in wanneer de EXE-naam afwijkt van de projectbestandsnaam.
- Kies `PrivilegesRequired=lowest` voor een per-gebruikerinstallatie of `admin` voor werkelijk machinebrede wijzigingen.
- Kies dezelfde architectuur in `Product.iss` en in `-RuntimeIdentifier`.
- Gebruik geen signinggeheimen in dit project.

## Build

```powershell
.\scripts\Build-Installer.ps1 `
  -ProjectFile C:\Bron\MijnApp\MijnApp.csproj `
  -RuntimeIdentifier win-x64 `
  -InnoCompilerPath 'C:\Program Files\Inno Setup 7\ISCC.exe'
```

De build schrijft uitsluitend onder `Builds`:

| Map | Inhoud |
| --- | --- |
| `Builds\Publish\<RID>` | Gevalideerde `dotnet publish`-uitvoer |
| `Builds\Installer` | Rechtstreekse uitvoer van ISCC |
| `Builds\Release` | Installer, SHA-256-bestand en `release-manifest.json` |

Gebruik `-Clean` alleen wanneer je de bestaande builduitvoer wilt verwijderen. De parameter verwijdert uitsluitend de drie bekende submappen onder dit framework.

## Controles

```powershell
.\scripts\Test-Installer.ps1 -InstallerPath .\Builds\Release\MijnApplicatie-Setup.exe
```

Dit is een statische controle op bestand en hash. Voer voor elke release daarnaast handmatig een installatie, upgrade en uninstall uit in een schone virtuele machine. Voeg pas na die basis een signingmodule of downloadmodule toe.
