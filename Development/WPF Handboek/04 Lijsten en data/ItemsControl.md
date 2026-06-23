# ItemsControl

## Wat is het?

Een `ItemsControl` toont een collectie items zonder standaard selectiegedrag.

## Wanneer gebruik je het?

Gebruik een `ItemsControl` wanneer je herhalende data wilt tonen zonder selectie, zoals cards of labels.

## Basisvoorbeeld

```xaml
<ItemsControl ItemsSource="{Binding Tags}" />
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `ItemsSource` | De collectie met items. | `<ItemsControl ItemsSource="{Binding Tags}" />` |
| `ItemTemplate` | Template per item. | `<ItemsControl.ItemTemplate>` |
| `ItemsPanel` | Layoutpanel voor de items. | `<ItemsControl.ItemsPanel>` |

## Uitgebreid besproken properties

### ItemTemplate

Met `ItemTemplate` bepaal je hoe ieder item wordt weergegeven.

## Wat kan er binnen dit component?

Items, templates en een custom items panel.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| `ItemsControl` gebruiken wanneer selectie nodig is. | Selectie ontbreekt. | Gebruik `ListBox`, `ListView` of `DataGrid`. |

## Praktijkvoorbeeld

```xaml
<ItemsControl ItemsSource="{Binding Tags}">
    <ItemsControl.ItemTemplate>
        <DataTemplate>
            <TextBlock Text="{Binding}" />
        </DataTemplate>
    </ItemsControl.ItemTemplate>
</ItemsControl>
```

