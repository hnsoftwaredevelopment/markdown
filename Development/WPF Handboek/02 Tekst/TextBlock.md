# TextBlock

## Wat is het?

Een `TextBlock` toont tekst die meestal niet door de gebruiker wordt aangepast.

## Wanneer gebruik je het?

Gebruik een `TextBlock` voor labels, titels, toelichtingen en gewone tekstweergave.

## Basisvoorbeeld

```xaml
<TextBlock Text="Voorbeeldtekst" />
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Text` | De weergegeven tekst. | `<TextBlock Text="Naam" />` |
| `FontSize` | Tekstgrootte. | `<TextBlock FontSize="16" />` |
| `FontWeight` | Tekstdikte. | `<TextBlock FontWeight="Bold" />` |
| `Foreground` | Tekstkleur. | `<TextBlock Foreground="DarkBlue" />` |
| `TextWrapping` | Tekst laten afbreken. | `<TextBlock TextWrapping="Wrap" />` |

## Uitgebreid besproken properties

### TextWrapping

Met `TextWrapping="Wrap"` kan tekst over meerdere regels lopen.

## Wat kan er binnen dit component?

Een `TextBlock` kan ook inline content bevatten zoals `Run`, `Bold`, `Italic` en `LineBreak`.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Een border direct op `TextBlock` verwachten. | `TextBlock` heeft geen `BorderBrush` of `BorderThickness`. | Plaats de `TextBlock` in een `Border`. |

## Praktijkvoorbeeld

```xaml
<Border BorderBrush="Gray" BorderThickness="1" Padding="6">
    <TextBlock Text="Tekst met rand" />
</Border>
```

