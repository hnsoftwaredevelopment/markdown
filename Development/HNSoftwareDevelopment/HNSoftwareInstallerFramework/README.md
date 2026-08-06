# HN Software Installer Framework

Een neutrale, modulaire basis voor Inno Setup 7-installers van .NET-applicaties. Het template automatiseert publiceren, valideren, compileren, hashen en het genereren van releasegegevens, zonder product- of signinggeheimen op te slaan.

## Start met een nieuw project

1. Kopieer `Installer\Product.iss.example` naar `Installer\Product.iss`.
2. Vervang alle herkenbare `{{...}}`-tags door productwaarden.
3. Kies bewust `PrivilegesRequired`, architectuur en runtimebeleid.
4. Voer de build uit:

   ```powershell
   .\scripts\Build-Installer.ps1 -ProjectFile C:\Bron\MijnApp\MijnApp.csproj -InnoCompilerPath 'C:\Program Files\Inno Setup 7\ISCC.exe'
   ```

Zie [docs/USAGE.md](docs/USAGE.md) voor de volledige uitleg en teststappen.
