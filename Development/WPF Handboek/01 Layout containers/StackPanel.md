# StackPanel

## Wat is het?

Een `StackPanel` plaatst child elements achter elkaar, horizontaal of verticaal.

## Wanneer gebruik je het?

Gebruik een `StackPanel` wanneer elementen simpelweg onder elkaar of naast elkaar moeten staan.

## Basisvoorbeeld

```xaml
<StackPanel Orientation="Vertical">
    <TextBlock Text="Naam" />
    <TextBox />
</StackPanel>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Orientation` | Bepaalt of children horizontaal of verticaal worden geplaatst. | `<StackPanel Orientation="Horizontal">` |
| `Margin` | Ruimte buiten het panel. | `<StackPanel Margin="10">` |
| `Background` | Achtergrondkleur of brush. | `<StackPanel Background="White">` |

## Uitgebreid besproken properties

### Orientation

Gebruik `Vertical` voor onder elkaar plaatsen en `Horizontal` voor naast elkaar plaatsen.

## Wat kan er binnen dit component?

Alle zichtbare WPF-controls en andere layoutcontainers kunnen child element zijn.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Een `StackPanel` gebruiken waar schaalbare kolommen nodig zijn. | Elementen schalen minder voorspelbaar. | Gebruik dan vaak een `Grid`. |

## Praktijkvoorbeeld

```xaml
<StackPanel Margin="10">
    <TextBlock Text="Gebruikersnaam" />
    <TextBox />
    <Button Content="Inloggen" />
</StackPanel>
```

