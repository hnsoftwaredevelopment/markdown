# HN Software Installer Framework

Herbruikbare starter voor betrouwbare Inno Setup-installers voor .NET-projecten. De basis houdt productkeuzes expliciet en automatiseert de voorspelbare releaseketen: publiceren, valideren, compileren, hashen en documenteren.

## Eerste gebruik

1. Pas [Installer/Product.iss](Installer/Product.iss) aan voor één applicatie; vooral `AppId`, `ProductName`, `MainExecutable` en `PrivilegesRequired` zijn verplicht te beoordelen.
2. Voer de build uit met een bestaand SDK-style project:

   ```powershell
   .\scripts\Build-Installer.ps1 -ProjectFile C:\Bron\MijnApp\MijnApp.csproj -InnoCompilerPath C:\Program Files\Inno Setup 7\ISCC.exe
   ```

3. Controleer `Builds\Release\release-manifest.json` en test de installer in een schone VM.

`Product.iss` is bewust geen geheimenbestand. Ondertekening blijft uitgeschakeld totdat een veilige signing-oplossing is gekozen.

Zie [docs/INSTALLER_FRAMEWORK_PLAN.md](docs/INSTALLER_FRAMEWORK_PLAN.md) voor het ontwerp en [docs/FRAMEWORK_USAGE.md](docs/FRAMEWORK_USAGE.md) voor parameters, uitvoer en veiligheidsgrenzen.
