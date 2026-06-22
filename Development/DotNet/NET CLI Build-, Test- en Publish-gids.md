## Inleiding

Tot nu toe worden builds uitgevoerd vanuit Visual Studio. Hoewel dit prima werkt, heeft dit enkele nadelen:

*   Visual Studio past soms automatisch het `.csproj`\-bestand aan.
*   Er ontstaat extra "ruis" in Git.
*   Buildprocessen zijn minder reproduceerbaar.
*   Automatiseren (CI/CD) wordt lastiger.

Een betere aanpak is om Visual Studio uitsluitend als IDE te gebruiken en alle builds via de `.NET CLI` (`dotnet`) uit te voeren.

---

# Basis

Open een terminal (PowerShell, Command Prompt of Windows Terminal) en ga naar de map waar de solution staat.

```powershell
cd C:\Users\<gebruikersnaam>\OneDrive\DevOps\<projectnaam>
```

---

# Solution build

Build de volledige solution.

```powershell
dotnet build
```

Of expliciet:

```powershell
dotnet build Amusing.sln
```

Release build:

```powershell
dotnet build Amusing.sln -c Release
```

---

# Specifiek project builden

Build één project.

```powershell
dotnet build Amusing\Amusing.csproj
```

Release:

```powershell
dotnet build Amusing\Amusing.csproj -c Release
```

Release naar specifieke output folder:

```powershell
dotnet build Modelbouwer\Modelbouwer.csproj -c Release -o .\Builds\Demo
```

---

# Clean

Verwijder alle build-artifacts.

```powershell
dotnet clean
```

Of expliciet:

```powershell
dotnet clean Amusing.sln
```

---

# Rebuild

De .NET CLI kent geen aparte `rebuild`.

Voer achter elkaar uit:

```powershell
dotnet clean

dotnet build -c Release
```

---

# Unit tests uitvoeren

Alle tests:

```powershell
dotnet test
```

Release:

```powershell
dotnet test -c Release
```

Specifiek testproject:

```powershell
dotnet test Amusing.Tests.csproj
```

---

# Publish voor Windows x64

Framework-dependent:

```powershell
dotnet publish -c Release -r win-x64
```

Self-contained:

```powershell
dotnet publish -c Release -r win-x64 --self-contained true

```

Met een eigen outputmap:

```powershell
dotnet publish -c Release -r win-x64 -o .\publish
```

---

# Publish voor Windows ARM64

Framework-dependent:

```powershell
dotnet publish -c Release -r win-arm64
```

Self-contained:

```powershell
dotnet publish -c Release -r win-arm64 --self-contained true
```

---

# Publish voor Linux (Debian VPS)

Framework-dependent:

```powershell
dotnet publish -c Release -r linux-x64
```

Self-contained:

```powershell
dotnet publish -c Release -r linux-x64 --self-contained true
```

Met outputmap:

```powershell
dotnet publish -c Release -r linux-x64 -o .\publish\linux
```

---

# Publish voor Raspberry Pi (ARM64)

Framework-dependent:

```powershell
dotnet publish -c Release -r linux-arm64
```

Self-contained:

```powershell
dotnet publish -c Release -r linux-arm64 --self-contained true
```

---

# Single-file executable

Windows:

```powershell
dotnet publish -c Release -r win-x64 --self-contained true /p:PublishSingleFile=true
```

Linux:

```powershell
dotnet publish -c Release -r linux-x64 --self-contained true /p:PublishSingleFile=true
```

---

# Native AOT

Niet ieder project ondersteunt dit.

```powershell
dotnet publish -c Release -r win-x64 /p:PublishAot=true
```

Voor Blazor Server wordt dit momenteel niet aanbevolen.

---

# Handige extra commando's

## Verbose logging

```powershell
dotnet build -v quit
dotnet build -v minimal
dotnet build -v normal
dotnet build -v detailed
dotnet build -v diagnostic
```

## Or short Verbose logging parameters, same order as above

```powershell
dotnet build -v q
dotnet build -v m
dotnet build -v n
dotnet build -v d
dotnet build -v diag
```

## Dependencies herstellen

```powershell
dotnet restore
```

## Geforceerd dependencies vernieuwen

```powershell
dotnet restore --force
```

## SDK-informatie

```powershell
dotnet --info
```

## Geïnstalleerde SDK's

```powershell
dotnet --list-sdks
```

---

# Aanbevolen workflow voor Blazor Server (Amusing)

```powershell
dotnet restore

dotnet clean

dotnet build -c Release

dotnet test

dotnet publish -c Release -r linux-x64 -o .\publish\linux
```

---

# Aanbevolen workflow voor WPF (Modelbouwer)

```powershell
dotnet restore

dotnet clean

dotnet build -c Release

dotnet publish -c Release -r win-x64 -o .\publish\windows
```

---

# Automatiseren met batch-bestanden

## publish-linux.bat

```powershell
@echo off

dotnet restore

dotnet clean

dotnet build -c Release

dotnet publish -c Release -r linux-x64 -o .\publish\linux

pause
```

## publish-windows.bat

```powershell
@echo off

dotnet restore

dotnet clean

dotnet build -c Release

dotnet publish -c Release -r win-x64 -o .\publish\windows

pause
```

---

# Advies

Voor projecten zoals:

*   Blazor Server + Debian VPS
*   WPF desktopapplicaties
*   GitHub repositories
*   Automatische deployments

is het verstandig om Visual Studio uitsluitend als IDE te gebruiken en alle builds, tests en deployments via de .NET CLI uit te voeren.

Dit maakt het ontwikkelproces:

*   voorspelbaar
*   reproduceerbaar
*   beter automatiseerbaar
*   CI/CD-vriendelijk
*   minder afhankelijk van Visual Studio
*   overzichtelijker voor versiebeheer (Git)