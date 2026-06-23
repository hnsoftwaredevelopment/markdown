# TreeView

## Wat is het?

Een `TreeView` toont hierarchische data als een boomstructuur.

## Wanneer gebruik je het?

Gebruik een `TreeView` voor mappen, categorieen, menu-structuren of parent-child data.

## Basisvoorbeeld

```xaml
<TreeView ItemsSource="{Binding Nodes}" />
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `ItemsSource` | De root-items. | `<TreeView ItemsSource="{Binding Nodes}" />` |
| `SelectedItem` | Het geselecteerde item. | Niet direct bindbaar zonder extra aanpak. |

## Uitgebreid besproken properties

### ItemsSource

Bij hierarchische data gebruik je vaak een `HierarchicalDataTemplate`.

## Wat kan er binnen dit component?

Directe items of templates voor hierarchische data.

## Veelgemaakte fouten

| Fout | Gevolg | Oplossing |
|---|---|---|
| Verwachten dat `SelectedItem` eenvoudig TwoWay bindt. | Binding werkt niet zoals bij veel andere controls. | Gebruik een behavior of passende MVVM-oplossing. |

## Praktijkvoorbeeld

```xaml
<TreeView ItemsSource="{Binding Categories}" />
```

