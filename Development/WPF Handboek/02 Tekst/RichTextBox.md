# RichTextBox

## Wat is het?

Een `RichTextBox` toont en bewerkt rich text met opmaak.

## Wanneer gebruik je het?

Gebruik een `RichTextBox` wanneer tekst vet, cursief, met alinea's of andere opmaak moet worden bewerkt.

## Basisvoorbeeld

```xaml
<RichTextBox>
    <FlowDocument>
        <Paragraph>Voorbeeldtekst</Paragraph>
    </FlowDocument>
</RichTextBox>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `Document` | De inhoud als `FlowDocument`. | `<RichTextBox><FlowDocument /></RichTextBox>` |
| `IsReadOnly` | Alleen lezen. | `<RichTextBox IsReadOnly="True" />` |

## Uitgebreid besproken properties

### Document

De inhoud van een `RichTextBox` staat in een `FlowDocument`, niet in een simpele `Text` property.

## Wat kan er binnen dit component?

Meestal een `FlowDocument` met paragrafen, runs en andere flow content.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Een simpele `Text` property verwachten. | Die is er niet zoals bij `TextBox`. | Werk met `FlowDocument`. |

## Praktijkvoorbeeld

```xaml
<RichTextBox MinHeight="120">
    <FlowDocument>
        <Paragraph>
            <Bold>Belangrijk:</Bold>
            <Run Text=" tekst met opmaak." />
        </Paragraph>
    </FlowDocument>
</RichTextBox>
```

