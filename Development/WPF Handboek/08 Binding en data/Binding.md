# Binding

## Wat is het?

Binding koppelt een property van een WPF-element aan data.

## Wanneer gebruik je het?

Gebruik binding om UI en data gescheiden te houden, vooral in MVVM.

## Basisvoorbeeld

```xaml
<TextBlock Text="{Binding Name}" />
```

## Belangrijkste properties

| Onderdeel | Doel | Voorbeeld |
|---|---|---|
| `Path` | Welke property wordt gelezen. | `{Binding Name}` |
| `Mode` | Richting van binding. | `{Binding Name, Mode=TwoWay}` |
| `UpdateSourceTrigger` | Wanneer de bron wordt bijgewerkt. | `{Binding Name, UpdateSourceTrigger=PropertyChanged}` |
| `Converter` | Waarde omzetten. | `{Binding Price, Converter={StaticResource PriceConverter}}` |

## Uitgebreid besproken properties

### Mode

`Mode` bepaalt of data een kant op of twee kanten op loopt.

## Wat kan er binnen dit component?

Binding wordt meestal als markup extension gebruikt binnen een propertywaarde.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Geen goede `DataContext`. | Binding toont niets. | Controleer de binding-context. |

## Praktijkvoorbeeld

```xaml
<TextBox Text="{Binding CustomerName, Mode=TwoWay, UpdateSourceTrigger=PropertyChanged}" />
```

