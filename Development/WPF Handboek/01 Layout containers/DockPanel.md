# DockPanel

## Wat is het?

Een `DockPanel` plaatst child elements tegen een zijde: boven, onder, links of rechts.

## Wanneer gebruik je het?

Gebruik een `DockPanel` voor schermen met vaste zones, zoals een menu bovenaan en inhoud in het midden.

## Basisvoorbeeld

```xaml
<DockPanel>
    <Menu DockPanel.Dock="Top" />
    <StatusBar DockPanel.Dock="Bottom" />
    <Grid />
</DockPanel>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `LastChildFill` | Laat het laatste child element de resterende ruimte vullen. | `<DockPanel LastChildFill="True">` |
| `DockPanel.Dock` | Attached property voor child elements. | `<Menu DockPanel.Dock="Top" />` |

## Uitgebreid besproken properties

### LastChildFill

Als `LastChildFill` op `True` staat, vult het laatste child element automatisch de resterende ruimte.

## Wat kan er binnen dit component?

Meestal plaats je menu's, statusbalken, sidebars en een hoofdcontainer binnen een `DockPanel`.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Vergeten dat het laatste child standaard vult. | Layout lijkt niet te luisteren naar `DockPanel.Dock`. | Controleer `LastChildFill`. |

## Praktijkvoorbeeld

```xaml
<DockPanel>
    <TextBlock DockPanel.Dock="Top" Text="Titel" />
    <Button DockPanel.Dock="Bottom" Content="Sluiten" />
    <Grid Background="White" />
</DockPanel>
```

