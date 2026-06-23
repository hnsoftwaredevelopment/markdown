# Canvas

## Wat is het?

Een `Canvas` plaatst elementen op absolute posities.

## Wanneer gebruik je het?

Gebruik een `Canvas` wanneer exacte coordinaten belangrijk zijn, bijvoorbeeld bij tekenen, diagrammen of eenvoudige visuele editors.

## Basisvoorbeeld

```xaml
<Canvas>
    <Button Canvas.Left="20" Canvas.Top="30" Content="Knop" />
</Canvas>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Canvas.Left` | X-positie vanaf links. | `Canvas.Left="20"` |
| `Canvas.Top` | Y-positie vanaf boven. | `Canvas.Top="30"` |
| `Canvas.Right` | Positie vanaf rechts. | `Canvas.Right="20"` |
| `Canvas.Bottom` | Positie vanaf onder. | `Canvas.Bottom="20"` |

## Uitgebreid besproken properties

### Canvas.Left en Canvas.Top

Deze attached properties bepalen waar een child element binnen de Canvas wordt geplaatst.

## Wat kan er binnen dit component?

Alle zichtbare controls, shapes en andere containers.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| `Canvas` gebruiken voor gewone schermlayout. | De interface schaalt slecht mee. | Gebruik voor standaard layout meestal `Grid`. |

## Praktijkvoorbeeld

```xaml
<Canvas Background="White">
    <TextBlock Canvas.Left="10" Canvas.Top="10" Text="Vrij geplaatst" />
</Canvas>
```

