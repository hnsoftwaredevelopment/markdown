# PasswordBox

## Wat is het?

Een `PasswordBox` is een invoerveld voor wachtwoorden.

## Wanneer gebruik je het?

Gebruik een `PasswordBox` wanneer ingevoerde tekst niet zichtbaar mag zijn.

## Basisvoorbeeld

```xaml
<PasswordBox />
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `PasswordChar` | Teken waarmee invoer wordt verborgen. | `<PasswordBox PasswordChar="*" />` |
| `MaxLength` | Maximum aantal tekens. | `<PasswordBox MaxLength="50" />` |

## Uitgebreid besproken properties

### Password

De `Password` property bevat de ingevoerde waarde, maar wordt meestal voorzichtig gebruikt vanwege security en binding-beperkingen.

## Wat kan er binnen dit component?

Een `PasswordBox` bevat normaal geen child elements.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Verwachten dat `Password` standaard goed bindbaar is. | Binding werkt anders dan bij `TextBox.Text`. | Gebruik bewust code-behind, commands of een veilige aanpak. |

## Praktijkvoorbeeld

```xaml
<PasswordBox MaxLength="100" />
```

