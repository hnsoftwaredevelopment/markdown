# ListView

## Wat is het?

Een `ListView` toont een lijst met items en kan met een view, zoals `GridView`, kolommen weergeven.

## Wanneer gebruik je het?

Gebruik een `ListView` wanneer een lijst meer structuur nodig heeft dan een `ListBox`.

## Basisvoorbeeld

```xaml
<ListView ItemsSource="{Binding Customers}">
    <ListView.View>
        <GridView>
            <GridViewColumn Header="Naam" DisplayMemberBinding="{Binding Name}" />
        </GridView>
    </ListView.View>
</ListView>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `ItemsSource` | De collectie met items. | `<ListView ItemsSource="{Binding Customers}" />` |
| `SelectedItem` | Het geselecteerde item. | `<ListView SelectedItem="{Binding SelectedCustomer}" />` |
| `View` | Bepaalt de weergave. | `<ListView.View>` |

## Uitgebreid besproken properties

### View

Met `View` kun je bijvoorbeeld een `GridView` gebruiken voor kolomweergave.

## Wat kan er binnen dit component?

Items, item templates en een `ListView.View`.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| `ListView` gebruiken waar bewerken in cellen nodig is. | Bewerken wordt omslachtig. | Gebruik dan vaak `DataGrid`. |

## Praktijkvoorbeeld

```xaml
<ListView ItemsSource="{Binding Orders}" />
```

