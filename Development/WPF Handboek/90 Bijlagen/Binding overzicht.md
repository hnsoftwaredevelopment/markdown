# Binding overzicht

Binding wordt gebruikt om UI-elementen te koppelen aan data.

## Basisbinding

```xaml
<TextBlock Text="{Binding Name}" />
```

## TwoWay binding

```xaml
<TextBox Text="{Binding Name, Mode=TwoWay}" />
```

## Binding met converter

```xaml
<TextBlock Text="{Binding Price, Converter={StaticResource PriceConverter}}" />
```

## DataContext

`DataContext` bepaalt waar bindings standaard hun data vandaan halen.

```xaml
<Grid DataContext="{Binding Customer}">
    <TextBlock Text="{Binding Name}" />
</Grid>
```

