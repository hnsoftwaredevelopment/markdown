# Scanprestaties meten

De drive-scan heeft twee strategieën die functioneel hetzelfde resultaat moeten
geven. De app gebruikt altijd **Optimized**: één ongesorteerde enumeratie per
map telt SVG-bestanden en verzamelt submappen tegelijk. **Legacy** is uitsluitend
aanwezig om de oude aanpak — afzonderlijk SVG's tellen en submappen sorteren —
eerlijk te kunnen vergelijken.

Meet op de daadwerkelijke schijf, bijvoorbeeld de werklaptop:

```powershell
.\build\Measure-ScanPerformance.ps1 -Path 'C:\' -Iterations 3
```

Het script start een kleine .NET 8-benchmarkhost, voert beide strategieën
afwisselend uit en rapporteert per run de verstreken tijd, het aantal gescande
mappen en mappen per seconde. Daardoor werkt het zowel vanuit Windows PowerShell
5.1 als PowerShell 7+.
Daarna geeft het gemiddelde en het relatieve verschil. Het wijzigt niets op de
gemeten schijf.

`-Iterations 1` is geschikt voor een snelle indicatie. Gebruik `-Iterations 3`
voor een betrouwbaarder gemiddelde; dit scant de doelmap zes keer en kan bij
430.000 mappen dus geruime tijd duren. Het afwisselen van de volgorde beperkt
het voordeel van een warme Windows-bestandssysteemcache, maar kan dat niet geheel
elimineren. Vergelijk daarom alleen metingen die op dezelfde machine, schijf en
zo rustig mogelijk moment zijn uitgevoerd.
