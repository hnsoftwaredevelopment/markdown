# DataGrid

## Wat is het?

Een `DataGrid` toont data in rijen en kolommen en kan ook bewerken ondersteunen.

## Wanneer gebruik je het?

Gebruik een `DataGrid` voor tabellen, administratieve schermen en overzichtslijsten met kolommen.

## Basisvoorbeeld

```xaml
<DataGrid ItemsSource="{Binding Customers}"
          AutoGenerateColumns="False">
    <DataGrid.Columns>
        <DataGridTextColumn Header="Naam" Binding="{Binding Name}" />
    </DataGrid.Columns>
</DataGrid>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `ItemsSource` | De collectie met rijen. | `<DataGrid ItemsSource="{Binding Customers}" />` |
| `AutoGenerateColumns` | Kolommen automatisch genereren. | `<DataGrid AutoGenerateColumns="False" />` |
| `SelectedItem` | De geselecteerde rij. | `<DataGrid SelectedItem="{Binding SelectedCustomer}" />` |
| `CanUserAddRows` | Gebruiker mag nieuwe rij toevoegen. | `<DataGrid CanUserAddRows="False" />` |
| `IsReadOnly` | Alleen lezen. | `<DataGrid IsReadOnly="True" />` |

## Uitgebreid besproken properties

### AutoGenerateColumns

Voor beheersbare schermen staat `AutoGenerateColumns` vaak op `False`, zodat je kolommen zelf definieert.

## Wat kan er binnen dit component?

Meestal `DataGrid.Columns` met kolomdefinities.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| `AutoGenerateColumns=True` laten staan in productie-layout. | Kolommen zijn minder controleerbaar. | Definieer kolommen handmatig. |

## Praktijkvoorbeeld

```xaml
<DataGrid ItemsSource="{Binding Orders}"
          AutoGenerateColumns="False"
          IsReadOnly="True">
    <DataGrid.Columns>
        <DataGridTextColumn Header="Ordernummer" Binding="{Binding OrderNumber}" />
        <DataGridTextColumn Header="Klant" Binding="{Binding CustomerName}" />
    </DataGrid.Columns>
</DataGrid>
```

