# Veelgebruikte properties

Deze bijlage verzamelt properties die bij veel WPF-controls terugkomen.
De exacte beschikbaarheid kan per component verschillen, omdat properties afkomstig kunnen zijn van basisklassen zoals `FrameworkElement`, `UIElement`, `Control` of `Panel`.

| Property | Doel | Voorbeeld |
|---|---|---|
| `Name` / `x:Name` | Naam voor gebruik in XAML, code-behind of binding. | `<Grid x:Name="MainGrid" />` |
| `Margin` | Ruimte buiten een element. | `<Button Margin="10" />` |
| `Padding` | Ruimte binnen een control. Niet elk element heeft deze property. | `<Button Padding="8,4" />` |
| `Width` | Vaste breedte. | `<TextBox Width="200" />` |
| `Height` | Vaste hoogte. | `<TextBox Height="30" />` |
| `MinWidth` | Minimale breedte. | `<Grid MinWidth="100" />` |
| `MinHeight` | Minimale hoogte. | `<Grid MinHeight="40" />` |
| `MaxWidth` | Maximale breedte. | `<Grid MaxWidth="800" />` |
| `MaxHeight` | Maximale hoogte. | `<Grid MaxHeight="600" />` |
| `HorizontalAlignment` | Horizontale uitlijning. | `<Button HorizontalAlignment="Right" />` |
| `VerticalAlignment` | Verticale uitlijning. | `<Button VerticalAlignment="Center" />` |
| `Visibility` | Zichtbaarheid en layout-gedrag. | `<Grid Visibility="Collapsed" />` |
| `IsEnabled` | Schakelt interactie uit of in. | `<Button IsEnabled="False" />` |
| `Opacity` | Transparantie van 0 tot 1. | `<Grid Opacity="0.5" />` |
| `ToolTip` | Tooltiptekst bij hover. | `<Button ToolTip="Opslaan" />` |
| `Style` | Verwijst naar een style. | `<Button Style="{StaticResource PrimaryButtonStyle}" />` |
| `DataContext` | Binding-context voor een element en zijn children. | `<Grid DataContext="{Binding Customer}" />` |

