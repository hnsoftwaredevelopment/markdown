# Viewbox

## Wat is het?

Een `Viewbox` schaalt een enkel child element.

## Wanneer gebruik je het?

Gebruik een `Viewbox` wanneer een stuk UI proportioneel moet meeschalen.

## Basisvoorbeeld

```xaml
<Viewbox>
    <TextBlock Text="Grote tekst" />
</Viewbox>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Stretch` | Schaalgedrag. | `<Viewbox Stretch="Uniform" />` |
| `StretchDirection` | Richting waarin geschaald mag worden. | `<Viewbox StretchDirection="UpOnly" />` |

## Uitgebreid besproken properties

### Stretch

`Stretch` bepaalt hoe het child element wordt geschaald.

## Wat kan er binnen dit component?

Een `Viewbox` heeft meestal een enkel child element.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Een volledig complex scherm in een `Viewbox` stoppen. | Tekst en controls schalen onnatuurlijk. | Gebruik `Viewbox` gericht en spaarzaam. |

## Praktijkvoorbeeld

```xaml
<Viewbox Stretch="Uniform">
    <TextBlock Text="42" FontWeight="Bold" />
</Viewbox>
```

