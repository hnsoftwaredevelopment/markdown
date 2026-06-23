# Resources

## Wat is het?

Resources zijn herbruikbare objecten zoals brushes, styles, templates en converters.

## Voorbeeld

```xaml
<Grid.Resources>
    <SolidColorBrush x:Key="AccentBrush" Color="SteelBlue" />
</Grid.Resources>
```

## Gebruik

```xaml
<TextBlock Foreground="{StaticResource AccentBrush}" />
```

