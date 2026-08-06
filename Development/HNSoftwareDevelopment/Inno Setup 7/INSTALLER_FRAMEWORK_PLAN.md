# HN Software Installer Framework — ontwerpstart

## Doel

Een herbruikbare, expliciete basis voor Inno Setup 7-projecten. Het framework automatiseert voorspelbare stappen — publiceren, valideren, compileren, testen en opleveren — zonder product-specifieke keuzes zoals installatierechten, runtime-strategie of signing te verbergen.

## Voorstel projectindeling

```text
<project>/
  Installer/
    Product.iss              # Productwaarden: naam, versie, uitvoerbaar bestand
    Main.iss                 # Compositiepunt
    Modules/
      Base.iss               # Gemeenschappelijke [Setup]-waarden
      Architecture.iss       # x86/x64/Arm64-keuze
      Files.iss              # Publish-output en uitzonderingen
      Tasks.iss              # Optionele snelkoppelingen en functies
      Prerequisites.iss      # Detectie en installatie van afhankelijkheden
      Signing.iss            # Alleen commandodefinitie; geen secrets
      Upgrade.iss            # Upgrade-/downgradebeleid
    Assets/
  scripts/
    Build-Installer.ps1      # Orkestreert de pipeline
    Test-Installer.ps1       # Basisvalidatie en logverzameling
  Builds/
    Publish/
    Installer/
    Release/
```

## Geautomatiseerde pipeline

1. Lees versie en productconfiguratie.
2. Maak een schone `Builds`-uitvoerstructuur.
3. Publiceer de .NET-applicatie met een expliciet publishprofiel.
4. Valideer dat het verwachte hoofdprogramma en vereiste bestanden bestaan.
5. Compileer `Installer\Main.iss` met `ISCC.exe` en gecontroleerde defines.
6. Onderteken alleen wanneer een expliciete signingconfiguratie beschikbaar is.
7. Verifieer handtekeningen en genereer SHA-256-hashes plus release-manifest.
8. Voer installatie- en upgradecontroles uit in een schone testomgeving; bewaar logs.

## Productconfiguratie

De eerste implementatie gebruikt één `Product.iss` met duidelijke waarden, bijvoorbeeld:

```iss
#define ProductName "Voorbeeldapplicatie"
#define ProductVersion "1.0.0"
#define ProductPublisher "HN Software Development"
#define MainExecutable "Voorbeeldapplicatie.exe"
#define PublishDir "..\Builds\Publish\win-x64"
```

Een JSON- of YAML-laag is pas zinvol wanneer meerdere projecten dezelfde generator gebruiken. Inno Setup-defines houden de eerste versie eenvoudig te beoordelen en rechtstreeks compileerbaar.

## Veiligheidsgrenzen

- Geen certificaatwachtwoorden, tokens of privé-certificaten in de repository.
- Geen stilzwijgende installatie met verhoogde rechten: `PrivilegesRequired` is productconfiguratie.
- Geen onbeperkte verwijderacties; verwijderpaden blijven onder expliciete applicatiemappen.
- Downloads gebruiken HTTPS en moeten integriteit controleren.
- Elke externe procesaanroep controleert exitcode en schrijft een diagnose naar het log.

## Eerste pilot

Kies één bestaande .NET/WPF-applicatie met een eenvoudige publishmap. Daarmee implementeren en testen we eerst `Product.iss`, `Main.iss`, `Base.iss`, `Files.iss` en `Build-Installer.ps1`; runtime-downloads, signing en upgrades volgen als optionele modules.

## Implementatiestatus

De starter is opgezet in de repository. Hij bevat de modulaire ISS-bestanden, de publicatie- en compileerstappen, uitvoervalidatie, een SHA-256-bestand en een JSON-release-manifest. De lokale computer heeft op dit moment een Inno Setup 6-compiler op de bekende standaardlocatie; voor de pilot wordt expliciet een Inno Setup 7-compilerpad verwacht, zodat de beoogde versie niet per ongeluk wordt vervangen.
