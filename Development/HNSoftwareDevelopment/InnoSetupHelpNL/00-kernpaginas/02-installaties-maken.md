# Installaties maken

Alles wat een Inno Setup-installatie doet, staat in een tekstbestand met de extensie .iss. Dat bestand heeft een INI-achtige opbouw: je zet informatie over je applicatie, de bestanden die mee moeten, de snelkoppelingen die je wilt en nog veel meer in secties.

## De Compiler IDE

Je schrijft en bewerkt je script in de Compiler IDE, de ontwikkelomgeving die met Inno Setup meekomt. Zodra je script klaar is, kies je in het menu voor Compile. De compiler leest je script en bouwt er een compleet, uitvoerbaar installatieprogramma van.

## Waar het resultaat terechtkomt

Standaard zet Inno Setup het gecompileerde installatieprogramma in een map genaamd Output, direct naast je scriptbestand. Wil je een andere locatie, dan stel je dat in via de Output-directive in de [Setup]-sectie van je script.

## Een startpunt vinden

Begin niet met een leeg scherm. In de submap Examples van je Inno Setup-installatie vind je kant-en-klare voorbeeldscripts. Pak er een die in de buurt komt van wat jij nodig hebt, pas de namen en paden aan naar jouw project en werk van daaruit verder. Dat scheelt je een hoop uitzoekwerk over hoe de basisstructuur van een script eruitziet.
