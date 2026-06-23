# Styles

## Wat is het?

Een `Style` groepeert property-instellingen zodat je dezelfde opmaak op meerdere controls kunt toepassen.

## Basisvoorbeeld

```xaml
<Style x:Key="PrimaryButtonStyle" TargetType="Button">
    <Setter Property="Padding" Value="10,6" />
    <Setter Property="FontWeight" Value="Bold" />
</Style>
```

## Gebruik

```xaml
<Button Content="Opslaan"
        Style="{StaticResource PrimaryButtonStyle}" />
```

