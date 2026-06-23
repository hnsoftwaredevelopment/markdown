# Templates

## Wat is het?

Templates bepalen hoe een control visueel wordt opgebouwd.
Met een template kun je de structuur en weergave van een control vergaand aanpassen.

## Basisvoorbeeld

```xaml
<ControlTemplate TargetType="Button">
    <Border Background="{TemplateBinding Background}">
        <ContentPresenter HorizontalAlignment="Center"
                          VerticalAlignment="Center" />
    </Border>
</ControlTemplate>
```

