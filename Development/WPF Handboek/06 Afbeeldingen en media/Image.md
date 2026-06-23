# Image

## Wat is het?

Een `Image` toont een afbeelding in de interface.

## Wanneer gebruik je het?

Gebruik een `Image` voor pictogrammen, previews, illustraties of andere bitmap/vectorafbeeldingen.

## Basisvoorbeeld

```xaml
<Image Source="/Images/logo.png" />
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Source` | De afbeelding die wordt getoond. | `<Image Source="/Images/logo.png" />` |
| `Stretch` | Hoe de afbeelding schaalt. | `<Image Stretch="Uniform" />` |
| `Width` | Breedte. | `<Image Width="120" />` |
| `Height` | Hoogte. | `<Image Height="80" />` |

## Uitgebreid besproken properties

### Stretch

`Stretch` bepaalt hoe de afbeelding past binnen de beschikbare ruimte.

## Wat kan er binnen dit component?

Een `Image` bevat normaal geen child elements.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| `Fill` gebruiken voor foto's zonder verhouding te bewaken. | Afbeelding vervormt. | Gebruik vaak `Uniform`. |

## Praktijkvoorbeeld

```xaml
<Image Source="/Images/avatar.png"
       Width="64"
       Height="64"
       Stretch="UniformToFill" />
```

