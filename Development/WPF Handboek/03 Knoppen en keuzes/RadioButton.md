# RadioButton

## Wat is het?

Een `RadioButton` laat de gebruiker een keuze maken uit een groep opties.

## Wanneer gebruik je het?

Gebruik `RadioButton` wanneer slechts een optie tegelijk gekozen mag worden.

## Basisvoorbeeld

```xaml
<StackPanel>
    <RadioButton Content="Klein" GroupName="Size" />
    <RadioButton Content="Groot" GroupName="Size" />
</StackPanel>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Content` | Tekst of inhoud naast de knop. | `<RadioButton Content="Optie A" />` |
| `IsChecked` | Of deze optie geselecteerd is. | `<RadioButton IsChecked="True" />` |
| `GroupName` | Groepeert opties. | `<RadioButton GroupName="Size" />` |

## Uitgebreid besproken properties

### GroupName

Met `GroupName` bepaal je welke radio buttons samen een keuzegroep vormen.

## Wat kan er binnen dit component?

Een `RadioButton` is een content control.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Geen duidelijke groep maken. | Opties kunnen elkaar onverwacht beinvloeden. | Gebruik `GroupName` wanneer nodig. |

## Praktijkvoorbeeld

```xaml
<StackPanel>
    <RadioButton GroupName="Theme" Content="Licht" />
    <RadioButton GroupName="Theme" Content="Donker" />
</StackPanel>
```

