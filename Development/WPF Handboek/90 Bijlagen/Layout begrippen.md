# Layout begrippen

## Device-independent pixels

WPF werkt met device-independent pixels.
Een waarde zoals `40` betekent dus niet altijd letterlijk 40 fysieke schermpixels.

## Auto

`Auto` betekent dat een rij, kolom of element de ruimte krijgt die de inhoud nodig heeft.

```xaml
<RowDefinition Height="Auto" />
```

## Ster-layout

Met `*` wordt resterende ruimte verdeeld.

```xaml
<ColumnDefinition Width="*" />
<ColumnDefinition Width="2*" />
```

In dit voorbeeld krijgt de tweede kolom twee keer zoveel resterende ruimte als de eerste kolom.

## Alignment

Alignment bepaalt hoe een element zich binnen de beschikbare ruimte plaatst.

Veelgebruikte waarden:

- `Left`
- `Right`
- `Top`
- `Bottom`
- `Center`
- `Stretch`

