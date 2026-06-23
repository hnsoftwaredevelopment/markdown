# CheckBox

## Wat is het?

Een `CheckBox` laat de gebruiker een optie aan- of uitzetten.

## Wanneer gebruik je het?

Gebruik een `CheckBox` voor onafhankelijke ja/nee-keuzes.

## Basisvoorbeeld

```xaml
<CheckBox Content="Actief" IsChecked="{Binding IsActive}" />
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Content` | Tekst of inhoud naast het vakje. | `<CheckBox Content="Actief" />` |
| `IsChecked` | De geselecteerde waarde. | `<CheckBox IsChecked="{Binding IsActive}" />` |
| `IsThreeState` | Staat ook een onbepaalde waarde toe. | `<CheckBox IsThreeState="True" />` |

## Uitgebreid besproken properties

### IsChecked

`IsChecked` bevat meestal `True` of `False`. Bij `IsThreeState` kan ook `null` voorkomen.

## Wat kan er binnen dit component?

Een `CheckBox` is een content control en kan tekst of andere content bevatten.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| `CheckBox` gebruiken voor keuzes waarvan maar een optie tegelijk mag gelden. | Gebruiker kan meerdere opties selecteren. | Gebruik dan `RadioButton`. |

## Praktijkvoorbeeld

```xaml
<CheckBox Content="Nieuwsbrief ontvangen"
          IsChecked="{Binding WantsNewsletter}" />
```

