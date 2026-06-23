# Commands

## Wat is het?

Commands koppelen UI-acties aan logica, vaak in een ViewModel.

## Wanneer gebruik je het?

Gebruik commands voor knoppen, menu-items en keyboard-acties in MVVM.

## Basisvoorbeeld

```xaml
<Button Content="Opslaan"
        Command="{Binding SaveCommand}" />
```

## Belangrijkste onderdelen

| Onderdeel | Doel | Voorbeeld |
|---|---|---|
| `Command` | De actie die wordt uitgevoerd. | `<Button Command="{Binding SaveCommand}" />` |
| `CommandParameter` | Extra waarde voor het command. | `<Button CommandParameter="{Binding SelectedItem}" />` |
| `CanExecute` | Bepaalt of command beschikbaar is. | Knop wordt automatisch disabled. |

## Uitgebreid besproken properties

### CommandParameter

Met `CommandParameter` geef je extra context mee aan een command.

## Wat kan er binnen dit component?

Commands worden meestal gebruikt op controls zoals `Button`, `MenuItem` en via input bindings.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Click-events mengen met MVVM-commanding. | Logica raakt verspreid. | Kies bewust voor commands bij MVVM. |

## Praktijkvoorbeeld

```xaml
<Button Content="Verwijderen"
        Command="{Binding DeleteCommand}"
        CommandParameter="{Binding SelectedCustomer}" />
```

