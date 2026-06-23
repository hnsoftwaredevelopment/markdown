# UniformGrid

## Wat is het?

Een `UniformGrid` verdeelt beschikbare ruimte in even grote cellen.

## Wanneer gebruik je het?

Gebruik een `UniformGrid` wanneer alle items dezelfde grootte moeten krijgen. UniformGrid is dus niet zo geavanceerd als Grid, maar handig als je een evenredig verdeeld grid nodig hebt zonder poespas

## Basisvoorbeeld

```xaml
<UniformGrid Rows="2" Columns="2">
    <Button Content="1" />
    <Button Content="2" />
    <Button Content="3" />
    <Button Content="4" />
</UniformGrid>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Rows` | Aantal rijen. | `<UniformGrid Rows="2">` |
| `Columns` | Aantal kolommen. | `<UniformGrid Columns="3">` |
| `FirstColumn` | Startkolom voor het eerste item. | `<UniformGrid FirstColumn="1">` |

## Uitgebreid besproken properties

### Rows en Columns

Met `Rows` en `Columns` bepaal je hoeveel gelijke cellen worden gebruikt.

## Wat kan er binnen dit component?

Meestal herhalende controls zoals knoppen, tegels of simpele cards.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Verwachten dat kolommen verschillende breedtes kunnen hebben. | Dat kan niet met `UniformGrid`. | Gebruik `Grid` voor ongelijke kolommen. |

## Praktijkvoorbeeld

```xaml
<UniformGrid Columns="3">
    <Button Content="Ja" />
    <Button Content="Nee" />
    <Button Content="Annuleren" />
</UniformGrid>
```

