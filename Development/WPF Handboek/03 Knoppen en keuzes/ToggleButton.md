# ToggleButton

## Wat is het?

Een `ToggleButton` is een knop met een aan/uit-status.

## Wanneer gebruik je het?

Gebruik een `ToggleButton` wanneer een actie of modus ingeschakeld en uitgeschakeld kan worden.

## Basisvoorbeeld

```xaml
<ToggleButton Content="Bewerken" IsChecked="{Binding IsEditMode}" />
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Content` | Inhoud van de knop. | `<ToggleButton Content="Aan" />` |
| `IsChecked` | Aan/uit-status. | `<ToggleButton IsChecked="True" />` |
| `IsThreeState` | Staat ook een onbepaalde status toe. | `<ToggleButton IsThreeState="True" />` |

## Uitgebreid besproken properties

### IsChecked

`IsChecked` bepaalt of de knop actief is.

## Wat kan er binnen dit component?

Een `ToggleButton` is een content control.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Een gewone `Button` gebruiken voor een blijvende status. | De status is niet zichtbaar of bindbaar. | Gebruik `ToggleButton`. |

## Praktijkvoorbeeld

```xaml
<ToggleButton Content="Filter actief"
              IsChecked="{Binding IsFilterEnabled}" />
```

