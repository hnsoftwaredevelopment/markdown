# ComboBox

## Wat is het?

Een `ComboBox` laat de gebruiker een item kiezen uit een uitklapbare lijst.

## Wanneer gebruik je het?

Gebruik een `ComboBox` wanneer er meerdere opties zijn, maar niet alles tegelijk zichtbaar hoeft te zijn.

## Basisvoorbeeld

```xaml
<ComboBox ItemsSource="{Binding Countries}"
          SelectedItem="{Binding SelectedCountry}" />
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `ItemsSource` | De lijst met items. | `<ComboBox ItemsSource="{Binding Countries}" />` |
| `SelectedItem` | Het geselecteerde object. | `<ComboBox SelectedItem="{Binding SelectedCountry}" />` |
| `SelectedValue` | De geselecteerde waarde. | `<ComboBox SelectedValue="{Binding CountryId}" />` |
| `DisplayMemberPath` | Welke property getoond wordt. | `<ComboBox DisplayMemberPath="Name" />` |

## Uitgebreid besproken properties

### ItemsSource

Met `ItemsSource` bind je de `ComboBox` aan een collectie.

## Wat kan er binnen dit component?

Je kunt items direct in XAML plaatsen of via `ItemsSource` binden.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| `SelectedItem` en `SelectedValue` door elkaar gebruiken. | Binding werkt anders dan verwacht. | Kies bewust welke waarde je nodig hebt. |

## Praktijkvoorbeeld

```xaml
<ComboBox ItemsSource="{Binding Customers}"
          DisplayMemberPath="Name"
          SelectedItem="{Binding SelectedCustomer}" />
```

