# Property value syntax

WPF-properties kunnen op verschillende manieren worden ingesteld.

## Eenvoudige tekstwaarde

```xaml
<Button Content="Opslaan" />
```

## Getalwaarde

```xaml
<Grid MinHeight="40" />
```

## Meerdere waarden

```xaml
<Grid Margin="5,10,5,10" />
```

Bij `Margin` en `Padding` is de volgorde meestal:

```text
links, boven, rechts, onder
```

## Binding

```xaml
<TextBlock Text="{Binding Name}" />
```

## StaticResource

```xaml
<Grid Background="{StaticResource PageBackgroundBrush}" />
```

