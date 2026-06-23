# TabControl

## Wat is het?

Een `TabControl` toont inhoud verdeeld over tabbladen.

## Wanneer gebruik je het?

Gebruik een `TabControl` wanneer verwante inhoud in overzichtelijke tabs kan worden verdeeld.

## Basisvoorbeeld

```xaml
<TabControl>
    <TabItem Header="Algemeen">
        <TextBlock Text="Inhoud" />
    </TabItem>
</TabControl>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Items` | De tabs. | `<TabItem Header="Algemeen" />` |
| `SelectedIndex` | Index van de geselecteerde tab. | `<TabControl SelectedIndex="0" />` |
| `SelectedItem` | Geselecteerde tab. | `<TabControl SelectedItem="{Binding SelectedTab}" />` |

## Uitgebreid besproken properties

### TabItem.Header

Met `Header` bepaal je de tekst of inhoud van het tabblad.

## Wat kan er binnen dit component?

Meestal `TabItem` elementen.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Te veel tabs gebruiken. | Navigatie wordt onoverzichtelijk. | Groepeer of splits schermen beter. |

## Praktijkvoorbeeld

```xaml
<TabControl>
    <TabItem Header="Details" />
    <TabItem Header="Historie" />
</TabControl>
```

