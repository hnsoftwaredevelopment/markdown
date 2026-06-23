# TextBox

## Wat is het?

Een `TextBox` is een invoerveld waarin de gebruiker tekst kan typen.

## Wanneer gebruik je het?

Gebruik een `TextBox` voor tekstinvoer, formulieren en zoekvelden.

## Basisvoorbeeld

```xaml
<TextBox Text="{Binding Name}" />
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Text` | De ingevoerde tekst. | `<TextBox Text="{Binding Name}" />` |
| `MaxLength` | Maximum aantal tekens. | `<TextBox MaxLength="50" />` |
| `IsReadOnly` | Alleen lezen. | `<TextBox IsReadOnly="True" />` |
| `AcceptsReturn` | Meerdere regels toestaan. | `<TextBox AcceptsReturn="True" />` |
| `TextWrapping` | Tekst afbreken. | `<TextBox TextWrapping="Wrap" />` |

## Uitgebreid besproken properties

### IsReadOnly

Met `IsReadOnly` kan tekst wel geselecteerd en gekopieerd worden, maar niet aangepast.

## Wat kan er binnen dit component?

Een `TextBox` bevat normaal geen child elements; de inhoud staat in de property `Text`.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| `IsEnabled="False"` gebruiken voor alleen-lezen tekst. | De control wordt grijs en minder bruikbaar. | Gebruik `IsReadOnly="True"`. |

## Praktijkvoorbeeld

```xaml
<TextBox Text="{Binding Description}"
         AcceptsReturn="True"
         TextWrapping="Wrap"
         MinHeight="80" />
```

