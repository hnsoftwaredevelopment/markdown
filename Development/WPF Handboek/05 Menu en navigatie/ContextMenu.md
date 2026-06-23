# ContextMenu

## Wat is het?

Een `ContextMenu` is een menu dat meestal verschijnt via de rechtermuisknop.

## Wanneer gebruik je het?

Gebruik een `ContextMenu` voor acties die bij een specifiek element horen.

## Basisvoorbeeld

```xaml
<TextBox>
    <TextBox.ContextMenu>
        <ContextMenu>
            <MenuItem Header="Kopieren" />
        </ContextMenu>
    </TextBox.ContextMenu>
</TextBox>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Items` | Menu-items in het contextmenu. | `<MenuItem Header="Verwijderen" />` |
| `PlacementTarget` | Element waar het menu bij hoort. | Meestal automatisch ingesteld. |

## Uitgebreid besproken properties

### Items

Een `ContextMenu` bevat meestal `MenuItem` elementen.

## Wat kan er binnen dit component?

`MenuItem`, `Separator` en andere menu-gerelateerde elementen.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Binding-context verwachten alsof het menu direct in dezelfde visual tree zit. | Bindings kunnen onverwacht falen. | Let op `DataContext` bij `ContextMenu`. |

## Praktijkvoorbeeld

```xaml
<Button Content="Opties">
    <Button.ContextMenu>
        <ContextMenu>
            <MenuItem Header="Wijzigen" />
            <MenuItem Header="Verwijderen" />
        </ContextMenu>
    </Button.ContextMenu>
</Button>
```

