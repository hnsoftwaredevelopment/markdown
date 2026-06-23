# WrapPanel

## Wat is het?

Een `WrapPanel` plaatst elementen naast elkaar en gaat automatisch verder op een nieuwe regel wanneer er geen ruimte meer is.

## Wanneer gebruik je het?

Gebruik een `WrapPanel` voor tags, knoppenreeksen, thumbnails of andere herhalende elementen.

## Basisvoorbeeld

```xaml
<WrapPanel>
    <Button Content="A" />
    <Button Content="B" />
    <Button Content="C" />
</WrapPanel>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Orientation` | Bepaalt de richting waarin elementen worden geplaatst. | `<WrapPanel Orientation="Horizontal">` |
| `ItemWidth` | Vaste breedte voor ieder item. | `<WrapPanel ItemWidth="120">` |
| `ItemHeight` | Vaste hoogte voor ieder item. | `<WrapPanel ItemHeight="40">` |

## Uitgebreid besproken properties

### ItemWidth en ItemHeight

Met `ItemWidth` en `ItemHeight` kun je alle child elements dezelfde basismaat geven.

## Wat kan er binnen dit component?

Meestal knoppen, labels, cards of kleine samengestelde controls.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| `WrapPanel` gebruiken voor formulierlayout. | Labels en invoervelden lijnen slecht uit. | Gebruik dan meestal `Grid`. |

## Praktijkvoorbeeld

```xaml
<WrapPanel Margin="10" ItemWidth="100">
    <Button Content="Nieuw" />
    <Button Content="Openen" />
    <Button Content="Opslaan" />
</WrapPanel>
```

