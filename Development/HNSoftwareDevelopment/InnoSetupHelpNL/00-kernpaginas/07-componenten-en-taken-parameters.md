# Componenten en taken parameters

Twee parameters bepalen of Inno Setup een item verwerkt op basis van wat de gebruiker tijdens de installatie heeft aangevinkt.

## Components

De Components-parameter werkt in alle secties behalve [Types] en [Components] zelf. Je geeft een of meer componentnamen op, gescheiden door spaties. Heeft een item geen Components-parameter, dan wordt het altijd verwerkt, ongeacht welke componenten de gebruiker koos.

Voorbeeld: `Components: main` zorgt ervoor dat een bestand alleen meegaat als de gebruiker de component "main" heeft geselecteerd.

## Tasks

De Tasks-parameter werkt in alle secties behalve [Types], [Components] en [Tasks] zelf. Ook hier geldt: zonder deze parameter wordt het item altijd verwerkt. Let op bij Icons-items: de Tasks-parameter houdt geen rekening met het vinkje "Geen Startmenu-map aanmaken" dat de gebruiker eventueel heeft gezet.

## Combineren met logica

Beide parameters accepteren booleaanse expressies, met `not` voor ontkenning, `and` voor "en allebei", `or` voor "een van beide" en haakjes om onderdelen te groeperen.

```
Components: main help
Components: a or b
Components: not (a or b)
```

Inno Setup verwerkt een item alleen als de component- en taakselectie van de gebruiker overeenkomt met wat je in deze parameters hebt opgegeven.
