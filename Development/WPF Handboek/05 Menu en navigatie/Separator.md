# Separator

## Wat is het?

Een `Separator` is een visuele scheidingslijn tussen items.

## Wanneer gebruik je het?

Gebruik een `Separator` in menu's, contextmenu's of toolbars om groepen acties te scheiden.

## Basisvoorbeeld

```xaml
<MenuItem Header="Bestand">
    <MenuItem Header="Openen" />
    <Separator />
    <MenuItem Header="Afsluiten" />
</MenuItem>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Style` | Opmaak van de separator. | `<Separator Style="{StaticResource MySeparatorStyle}" />` |

## Uitgebreid besproken properties

### Style

Met `Style` kun je de weergave aanpassen.

## Wat kan er binnen dit component?

Een `Separator` bevat normaal geen child content.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Separators gebruiken als algemene layoutlijnen. | Semantiek en styling worden rommelig. | Gebruik voor layout liever `Border` of styling. |

## Praktijkvoorbeeld

```xaml
<ContextMenu>
    <MenuItem Header="Wijzigen" />
    <Separator />
    <MenuItem Header="Verwijderen" />
</ContextMenu>
```

