# Indeling van een Inno Setup-script

Een Inno Setup-script bestaat uit secties. Elke sectie regelt een ander onderdeel van de installatie en bevat de bijbehorende items. Je herkent een sectie aan de naam tussen vierkante haken, bijvoorbeeld [Setup] of [Files].

## Twee soorten secties

Er bestaan twee soorten secties, en dat verschil bepaalt hoe je regels erin opbouwt:

- **Directive-secties**, zoals [Setup]. Hier zet je losse naam-waarde paren, één per regel.
- **Parameter-secties**, zoals [Files]. Hier bouw je regels op uit meerdere parameters achter elkaar.

Je mag dezelfde sectienaam trouwens meerdere keren in één script gebruiken. Inno Setup voegt de inhoud dan gewoon samen.

## Commentaar

Zet een puntkomma aan het begin van een regel en de compiler negeert die regel volledig. Handig om uitleg in je script te zetten of om tijdelijk een regel uit te schakelen zonder hem te verwijderen.

## Bestanden insluiten

Met de directive `#include "bestandsnaam.txt"` haal je de inhoud van een ander bestand in je script. Zonder het voorvoegsel `compiler:` zoekt Inno Setup dat bestand in dezelfde map als je script.

## Preprocessor

Zet je op de eerste regel van je script een `#preproc`-directive, dan kies je zelf tussen de eenvoudige ingebouwde preprocessor of de uitgebreidere Inno Setup Preprocessor (ISPP). Heb je niets opgegeven en is ISPP beschikbaar, dan gebruikt Inno Setup die automatisch.

## Tekencodering

Werk je met Unicode-tekens in je script, sla het bestand dan op als UTF-8. Let bij taalbestanden (.isl) op: die mogen geen enkele directive bevatten, ze zijn puur bedoeld voor vertaalde teksten.
