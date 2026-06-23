# ToolBar

## Wat is het?

Een `ToolBar` groepeert veelgebruikte acties in een werkbalk.

## Wanneer gebruik je het?

Gebruik een `ToolBar` voor snelle acties zoals nieuw, openen, opslaan of vernieuwen.

## Basisvoorbeeld

```xaml
<ToolBar>
    <Button Content="Nieuw" />
    <Button Content="Opslaan" />
</ToolBar>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Items` | De inhoud van de werkbalk. | `<Button Content="Opslaan" />` |

## Uitgebreid besproken properties

### Items

Een `ToolBar` bevat meestal knoppen, separators en andere compacte controls.

## Wat kan er binnen dit component?

Knoppen, toggles, separators en soms combo boxes.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Te veel acties in een toolbar stoppen. | De interface wordt druk. | Toon alleen veelgebruikte acties. |

## Praktijkvoorbeeld

```xaml
<ToolBar>
    <Button Content="Openen" Command="{Binding OpenCommand}" />
    <Button Content="Opslaan" Command="{Binding SaveCommand}" />
</ToolBar>
```

