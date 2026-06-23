# Converters

## Wat is het?

Converters zetten bindingwaarden om tussen bron en doel.

## Wanneer gebruik je het?

Gebruik een converter wanneer de data niet direct geschikt is voor de UI-property.

## Basisvoorbeeld

```xaml
<TextBlock Visibility="{Binding IsActive, Converter={StaticResource BooleanToVisibilityConverter}}" />
```

## Belangrijkste onderdelen

| Onderdeel | Doel | Voorbeeld |
|---|---|---|
| `IValueConverter` | Een waarde omzetten. | Boolean naar Visibility |
| `IMultiValueConverter` | Meerdere waarden combineren. | Voor- en achternaam samenvoegen |
| `ConverterParameter` | Extra parameter meegeven. | `{Binding Value, ConverterParameter=Short}` |

## Uitgebreid besproken properties

### ConverterParameter

Met `ConverterParameter` geef je extra informatie mee aan een converter.

## Wat kan er binnen dit component?

Converters worden meestal als resource geregistreerd.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Te veel logica in converters stoppen. | UI-laag wordt moeilijk onderhoudbaar. | Houd converters klein en gericht. |

## Praktijkvoorbeeld

```xaml
<Window.Resources>
    <BooleanToVisibilityConverter x:Key="BooleanToVisibilityConverter" />
</Window.Resources>
```

