# Parameters in secties

De meeste secties in een Inno Setup-script werken met parameters. Alleen [Setup], [Messages], [CustomMessages], [LangOptions] en de [Code]-sectie vallen hierbuiten, die hebben hun eigen opbouw.

## Syntax

Een parameter schrijf je als `Naam: Waarde`. Zet je er meerdere op één regel, scheid ze dan met een puntkomma. De volgorde waarin je ze zet maakt niet uit. Vergeet je een parameter, dan pakt Inno Setup gewoon de standaardwaarde, de meeste parameters zijn optioneel.

Een voorbeeld uit de [Files]-sectie:

```
Source: "mijnprogramma.exe"; DestDir: "{app}"; Flags: ignoreversion
```

Hier zie je twee parameters, Source en DestDir, gescheiden door een puntkomma.

## Aanhalingstekens gebruiken

Zet waarden, zeker zelfgekozen tekst zoals bestandsnamen, tussen dubbele aanhalingstekens. Verplicht is dat niet, maar zonder aanhalingstekens kun je geen spaties aan het begin of einde, puntkomma's of aanhalingstekens zelf in je waarde kwijt.

Wil je een dubbel aanhalingsteken binnen een waarde, typ het dan twee keer achter elkaar (`""`). Voor een enkel aanhalingsteken in je waarde heb je vier aanhalingstekens nodig (`""""`): twee voor de rand van de string, twee voor het teken zelf.
