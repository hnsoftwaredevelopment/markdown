# Button

## Wat is het?

Een `Button` is een klikbare control waarmee de gebruiker een actie start.

## Wanneer gebruik je het?

Gebruik een `Button` voor acties zoals opslaan, annuleren, zoeken of openen.

## Basisvoorbeeld

```xaml
<Button Content="Opslaan" />
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Content` | De inhoud van de knop. | `<Button Content="Opslaan" />` |
| `Command` | Koppelt de knop aan een command. | `<Button Command="{Binding SaveCommand}" />` |
| `IsDefault` | Activeert de knop met Enter. | `<Button IsDefault="True" />` |
| `IsCancel` | Activeert de knop met Escape. | `<Button IsCancel="True" />` |

## Uitgebreid besproken properties

### Command

Met `Command` koppel je de knop aan logica in bijvoorbeeld een ViewModel.

## Wat kan er binnen dit component?

Omdat `Button` een content control is, kan de inhoud tekst zijn maar ook complexere XAML.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Alleen click-events gebruiken in MVVM-schermen. | Logica komt snel in code-behind terecht. | Gebruik waar passend `Command`. |

## Praktijkvoorbeeld

```xaml
<Button Content="Opslaan"
        Command="{Binding SaveCommand}"
        Padding="10,6" />
```

