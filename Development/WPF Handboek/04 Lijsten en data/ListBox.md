# ListBox

## Wat is het?

Een `ListBox` toont een lijst waaruit de gebruiker een of meer items kan selecteren.

## Wanneer gebruik je het?

Gebruik een `ListBox` wanneer meerdere items tegelijk zichtbaar mogen zijn.

## Basisvoorbeeld

```xaml
<ListBox ItemsSource="{Binding Customers}"
         SelectedItem="{Binding SelectedCustomer}" />
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `ItemsSource` | De collectie met items. | `<ListBox ItemsSource="{Binding Customers}" />` |
| `SelectedItem` | Het geselecteerde item. | `<ListBox SelectedItem="{Binding SelectedCustomer}" />` |
| `SelectionMode` | Een of meerdere selecties. | `<ListBox SelectionMode="Extended" />` |

## Uitgebreid besproken properties

### SelectionMode

Met `SelectionMode` bepaal je of de gebruiker een of meerdere items kan selecteren.

## Wat kan er binnen dit component?

Items kunnen direct in XAML staan of via `ItemsSource` worden gebonden.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Te veel informatie in een simpele `ListBox` tonen. | Lijst wordt onoverzichtelijk. | Gebruik eventueel `ListView` of `DataGrid`. |

## Praktijkvoorbeeld

```xaml
<ListBox ItemsSource="{Binding Products}"
         DisplayMemberPath="Name" />
```

