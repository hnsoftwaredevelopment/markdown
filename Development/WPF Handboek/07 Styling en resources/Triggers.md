# Triggers

## Wat is het?

Triggers passen properties aan wanneer aan een voorwaarde wordt voldaan.

## Voorbeeld

```xaml
<Style TargetType="Button">
    <Style.Triggers>
        <Trigger Property="IsMouseOver" Value="True">
            <Setter Property="Background" Value="LightBlue" />
        </Trigger>
    </Style.Triggers>
</Style>
```

