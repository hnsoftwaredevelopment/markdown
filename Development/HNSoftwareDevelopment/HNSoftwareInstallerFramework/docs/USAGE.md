# Gebruik van het template

## Productconfiguratie

Maak eerst `Installer\Product.iss` op basis van `Product.iss.example`. Vervang alle `{{...}}`-tags. Belangrijke keuzes:

- `AppId`: één unieke GUID per product; nooit wijzigen voor upgrades.
- `PrivilegesRequired`: `lowest` voor per-gebruikerinstallaties, `admin` voor machinebrede wijzigingen.
- `TargetArchitecture`: `x64` of `arm64`, gelijk aan de gekozen publish-RID.
- `MainExecutable`: het hoofdprogramma in de publishmap.

## Upgrades en Windows-pins

Houd voor iedere release dezelfde `AppId`, de naam van `MainExecutable` en de
installatiemap aan. Het template hergebruikt daarom standaard de eerdere
installatiemap en werkt bestanden rechtstreeks bij. Voeg geen algemene
`[InstallDelete]`-regels voor `.exe`, `.dll` of andere programmabestanden toe:
het tijdelijk verwijderen van het uitvoerbare bestand kan pins in Start en de
taakbalk ongeldig maken. Verwijder uitsluitend expliciet benoemde,
daadwerkelijk vervallen bestanden.

## Build en release

De build schrijft alleen onder `Builds`. Hij publiceert de applicatie, valideert het hoofdprogramma, compileert `Main.iss` met Inno Setup 7 en maakt een SHA-256-bestand plus `release-manifest.json`.

Gebruik signing en prerequisitemodules pas nadat je ze per product expliciet hebt ingericht. Sla geen certificaten, wachtwoorden of tokens op in de repository.
