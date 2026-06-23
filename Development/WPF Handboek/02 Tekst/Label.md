# Label

## Wat is het?

Een `Label` is een tekstlabel dat vaak bij een invoerveld hoort.

## Wanneer gebruik je het?

Gebruik een `Label` wanneer je tekst expliciet aan een andere control wilt koppelen.

## Basisvoorbeeld

```xaml
<Label Content="Naam:" Target="{Binding ElementName=NameTextBox}" />
<TextBox x:Name="NameTextBox" />
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Content` | De inhoud van het label. | `<Label Content="Naam:" />` |
| `Target` | Koppelt het label aan een control. | `<Label Target="{Binding ElementName=NameTextBox}" />` |

## Uitgebreid besproken properties

### Target

Met `Target` kun je toetsenbordnavigatie en toegankelijkheid verbeteren.

## Wat kan er binnen dit component?

Een `Label` is een content control en kan tekst of andere eenvoudige content bevatten.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| `Label` gebruiken voor alle gewone tekst. | Onnodig zwaar of semantisch minder passend. | Gebruik `TextBlock` voor gewone tekstweergave. |

## Praktijkvoorbeeld

```xaml
<StackPanel>
    <Label Content="Naam:" />
    <TextBox />
</StackPanel>
```

