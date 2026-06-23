# Menu

## Wat is het?

Een `Menu` toont een klassieke menubalk met menu-items.

## Wanneer gebruik je het?

Gebruik een `Menu` voor applicatiecommando's zoals Bestand, Bewerken en Help.

## Basisvoorbeeld

```xaml
<Menu>
    <MenuItem Header="_Bestand">
        <MenuItem Header="_Openen" />
    </MenuItem>
</Menu>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Items` | Menu-items. | `<MenuItem Header="Bestand" />` |
| `IsMainMenu` | Markeert het hoofdmenu. | `<Menu IsMainMenu="True" />` |

## Uitgebreid besproken properties

### MenuItem.Header

Met `Header` stel je de zichtbare tekst van een menu-item in.

## Wat kan er binnen dit component?

Vooral `MenuItem` elementen.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Commands niet gebruiken voor menu-acties. | Logica raakt verspreid. | Gebruik waar passend `Command`. |

## Praktijkvoorbeeld

```xaml
<Menu>
    <MenuItem Header="_Bestand">
        <MenuItem Header="_Afsluiten" Command="{Binding ExitCommand}" />
    </MenuItem>
</Menu>
```
