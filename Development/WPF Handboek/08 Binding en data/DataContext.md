# DataContext

## Wat is het?

`DataContext` bepaalt de standaard bron voor bindings binnen een element.

## Wanneer gebruik je het?

Gebruik `DataContext` om een scherm, container of control aan een viewmodel of object te koppelen.

## Basisvoorbeeld

```xaml
<Grid DataContext="{Binding Customer}">
    <TextBlock Text="{Binding Name}" />
</Grid>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `DataContext` | Binding-context voor element en children. | `<Grid DataContext="{Binding Customer}" />` |

## Uitgebreid besproken properties

### DataContext inheritance

Child elements erven meestal de `DataContext` van hun parent.

## Wat kan er binnen dit component?

`DataContext` is geen component maar een property die op veel WPF-elementen bestaat.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Niet weten waar de `DataContext` vandaan komt. | Binding-problemen zijn lastig te vinden. | Controleer parent containers en output window binding errors. |

## Praktijkvoorbeeld

```xaml
<StackPanel DataContext="{Binding SelectedCustomer}">
    <TextBlock Text="{Binding Name}" />
    <TextBlock Text="{Binding City}" />
</StackPanel>
```

