# Gebruik van het template

## Productconfiguratie

Maak eerst `Installer\Product.iss` op basis van `Product.iss.example`. Vervang alle `{{...}}`-tags. Belangrijke keuzes:

- `AppId`: één unieke GUID per product; nooit wijzigen voor upgrades.
- `PrivilegesRequired`: `lowest` voor per-gebruikerinstallaties, `admin` voor machinebrede wijzigingen.
- `TargetArchitecture`: `x64` of `arm64`, gelijk aan de gekozen publish-RID.
- `MainExecutable`: het hoofdprogramma in de publishmap.

## Build en release

De build schrijft alleen onder `Builds`. Hij publiceert de applicatie, valideert het hoofdprogramma, compileert `Main.iss` met Inno Setup 7 en maakt een SHA-256-bestand plus `release-manifest.json`.

Gebruik signing en prerequisitemodules pas nadat je ze per product expliciet hebt ingericht. Sla geen certificaten, wachtwoorden of tokens op in de repository.
