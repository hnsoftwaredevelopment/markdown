# Grid

## Wat is het?

Een `Grid` is een layout-container waarmee je een scherm of onderdeel kunt verdelen in rijen en kolommen.
Het is een van de meest gebruikte layoutcontainers in WPF, vooral wanneer elementen netjes ten opzichte van elkaar moeten worden uitgelijnd.

## Wanneer gebruik je het?

Gebruik een `Grid` wanneer:

- je een layout wilt maken met rijen en kolommen;
- onderdelen op vaste plekken moeten staan;
- je meerdere elementen netjes wilt uitlijnen;
- delen van het scherm flexibel moeten mee schalen;
- je `Auto`, vaste maten en `*`-verdeling wilt combineren.

Gebruik liever een andere container wanneer:

- elementen alleen onder elkaar of naast elkaar hoeven te staan: gebruik dan vaak `StackPanel`;
- elementen absoluut gepositioneerd moeten worden: gebruik dan eventueel `Canvas`;
- elementen automatisch moeten doorlopen naar een volgende regel: gebruik dan `WrapPanel`.

## Basisvoorbeeld

```xml
<Grid ShowGridLines="True">
    <Grid.RowDefinitions>
        <RowDefinition Height="Auto" />
        <RowDefinition Height="*" />
    </Grid.RowDefinitions>

    <Grid.ColumnDefinitions>
        <ColumnDefinition Width="200" />
        <ColumnDefinition Width="*" />
    </Grid.ColumnDefinitions>
</Grid>
```

## Belangrijkste properties

| Property | Doel | Voorbeeld |
|---|---|---|
| `ShowGridLines` | Toont hulplijnen voor rijen en kolommen tijdens ontwikkeling. | `<Grid ShowGridLines="True">` |
| `Background` | Stelt de achtergrondkleur of brush in. | `<Grid Background="White">` |
| `Margin` | Stelt ruimte buiten de Grid in. | `<Grid Margin="10">` |
| `Width` | Geeft de Grid een vaste breedte. | `<Grid Width="300">` |
| `Height` | Geeft de Grid een vaste hoogte. | `<Grid Height="200">` |
| `MinWidth` | Bepaalt de minimale breedte. | `<Grid MinWidth="100">` |
| `MinHeight` | Bepaalt de minimale hoogte. | `<Grid MinHeight="40">` |
| `MaxWidth` | Bepaalt de maximale breedte. | `<Grid MaxWidth="800">` |
| `MaxHeight` | Bepaalt de maximale hoogte. | `<Grid MaxHeight="600">` |
| `HorizontalAlignment` | Bepaalt horizontale uitlijning. | `<Grid HorizontalAlignment="Stretch">` |
| `VerticalAlignment` | Bepaalt verticale uitlijning. | `<Grid VerticalAlignment="Top">` |
| `Visibility` | Bepaalt of de Grid zichtbaar is en layout-ruimte inneemt. | `<Grid Visibility="Collapsed">` |
| `DataContext` | Bepaalt de binding-context voor de Grid en child controls. | `<Grid DataContext="{Binding User}">` |
| `Style` | Koppelt een style aan de Grid. | `<Grid Style="{StaticResource GridStyle}">` |

## Uitgebreid besproken properties

### ShowGridLines

Met `ShowGridLines` kun je de randen van rijen en kolommen zichtbaar maken.
Dit is vooral handig tijdens het bouwen of debuggen van een layout.

Gebruik:

```xml
<Grid ShowGridLines="True">
</Grid>
```

Let op: `ShowGridLines` is bedoeld als hulpmiddel tijdens ontwikkeling, niet als visuele border voor een productie-interface.

### MinHeight

Met `MinHeight` stel je de minimale hoogte van de Grid in.
De Grid kan hoger worden als de inhoud of layout daarom vraagt, maar wordt niet lager dan deze waarde.

Gebruik:

```xml
<Grid MinHeight="40">
</Grid>
```

### Background

Met `Background` stel je de achtergrond van de Grid in.
Dit kan een kleur zijn, maar ook een brush.

Gebruik:

```xml
<Grid Background="LightGray">
</Grid>
```

Let op: een Grid zonder achtergrond heeft visueel geen kleur. Voor bepaalde muisinteracties op lege ruimte kan het handig zijn om expliciet een `Background` te zetten, bijvoorbeeld `Transparent`.

```xml
<Grid Background="Transparent">
</Grid>
```

### Margin

Met `Margin` stel je de buitenruimte van de Grid in.

Gebruik:

```xml
<Grid Margin="10">
</Grid>
```
Hier zijn alle marges links, boven, rechts en onder gelijk allen 10.

Of met vier waarden, handig als alle marges anders kunnen zijn:

```xml
<Grid Margin="5,10,5,10">
</Grid>
```

De volgorde is: links, boven, rechts, onder.
Spaties tussen de verschillende waarden zorgen voor een betere leesbaarheid maar tussen de waarden mag ook enkel een spatie staan om ze te scheiden.

Wanneer, zoals in het voorbeeld met 4 waarden, links en rechts gelijk zijn (5) en boven en onder gelijk (10) kun je ook volstaan met 2 waarden.

```xml
<Grid Margin="5,10">
</Grid>
```

## Wat kan er binnen dit component?

Binnen een `Grid` plaats je meestal:

- `Grid.RowDefinitions`
- `Grid.ColumnDefinitions`
- child controls zoals `TextBlock`, `Button`, `TextBox`, `StackPanel` of een andere `Grid`
- resources via `Grid.Resources`

Voorbeeld:

```xml
<Grid>
    <Grid.RowDefinitions>
        <RowDefinition Height="Auto" />
        <RowDefinition Height="*" />
    </Grid.RowDefinitions>

    <TextBlock Grid.Row="0" Text="Titel" />
    <Button Grid.Row="1" Content="Opslaan" />
</Grid>
```

## RowDefinitions

Met `Grid.RowDefinitions` definieer je de rijen van de Grid.

```xml
<Grid.RowDefinitions>
    <RowDefinition Height="Auto" />
    <RowDefinition Height="*" />
    <RowDefinition Height="40" />
</Grid.RowDefinitions>
```

Veelgebruikte waarden:

| Waarde | Betekenis                                                             |
| ------ | --------------------------------------------------------------------- |
| `Auto` | De rij wordt zo hoog als de inhoud nodig heeft.                       |
| `*`    | De rij gebruikt de beschikbare resterende ruimte.                     |
| `2*`   | De rij krijgt twee keer zoveel resterende ruimte als een rij met `*`. |
| `40`   | De rij krijgt een vaste hoogte van 40 device-independent pixels.      |

## ColumnDefinitions

Met `Grid.ColumnDefinitions` definieer je de kolommen van de Grid.

```xml
<Grid.ColumnDefinitions>
    <ColumnDefinition Width="Auto" />
    <ColumnDefinition Width="*" />
    <ColumnDefinition Width="200" />
</Grid.ColumnDefinitions>
```

Veelgebruikte waarden:

| Waarde | Betekenis                                                                 |
| ------ | ------------------------------------------------------------------------- |
| `Auto` | De kolom wordt zo breed als de inhoud nodig heeft.                        |
| `*`    | De kolom gebruikt de beschikbare resterende ruimte.                       |
| `2*`   | De kolom krijgt twee keer zoveel resterende ruimte als een kolom met `*`. |
| `200`  | De kolom krijgt een vaste breedte van 200 device-independent pixels.      |

## Attached properties voor child controls

Deze properties zet je op elementen binnen de Grid, niet op de Grid zelf.

| Property          | Doel                                        | Voorbeeld             |
| ----------------- | ------------------------------------------- | --------------------- |
| `Grid.Row`        | Plaatst een element in een rij.             | `Grid.Row="1"`        |
| `Grid.Column`     | Plaatst een element in een kolom.           | `Grid.Column="2"`     |
| `Grid.RowSpan`    | Laat een element meerdere rijen beslaan.    | `Grid.RowSpan="2"`    |
| `Grid.ColumnSpan` | Laat een element meerdere kolommen beslaan. | `Grid.ColumnSpan="3"` |

Voorbeeld:

```xml
<Grid>
    <Grid.RowDefinitions>
        <RowDefinition Height="Auto" />
        <RowDefinition Height="*" />
    </Grid.RowDefinitions>

    <Grid.ColumnDefinitions>
        <ColumnDefinition Width="200" />
        <ColumnDefinition Width="*" />
    </Grid.ColumnDefinitions>

    <TextBlock Grid.Row="0" Grid.Column="0" Text="Naam" />
    <TextBox Grid.Row="0" Grid.Column="1" />
    <Button Grid.Row="1" Grid.Column="0" Grid.ColumnSpan="2" Content="Opslaan" />
</Grid>
```

## Veelgemaakte fouten

| Fout                                                                                                | Gevolg                                               | Oplossing                                                                |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------ |
| Geen `RowDefinitions` of `ColumnDefinitions` maken, maar wel `Grid.Row` of `Grid.Column` gebruiken. | Elementen komen mogelijk niet waar je verwacht.      | Definieer eerst de benodigde rijen en kolommen.                          |
| `ShowGridLines` gebruiken als echte border.                                                         | De hulplijnen zien er niet uit als productie-opmaak. | Gebruik `Border` of styling voor echte lijnen.                           |
| Te veel vaste hoogtes en breedtes gebruiken.                                                        | De layout schaalt slecht mee.                        | Combineer `Auto`, `*` en vaste maten bewust.                             |
| Vergeten dat indexen bij 0 beginnen.                                                                | Een element staat in de verkeerde rij of kolom.      | De eerste rij is `Grid.Row="0"` en de eerste kolom is `Grid.Column="0"`. |

## Praktijkvoorbeeld

```xml
<Grid Margin="10">
    <Grid.RowDefinitions>
        <RowDefinition Height="Auto" />
        <RowDefinition Height="*" />
        <RowDefinition Height="Auto" />
    </Grid.RowDefinitions>

    <TextBlock Grid.Row="0"
               Text="Klantgegevens"
               FontSize="18"
               FontWeight="Bold" />

    <Grid Grid.Row="1" Margin="0,10,0,10">
        <Grid.ColumnDefinitions>
            <ColumnDefinition Width="120" />
            <ColumnDefinition Width="*" />
        </Grid.ColumnDefinitions>

        <Grid.RowDefinitions>
            <RowDefinition Height="Auto" />
            <RowDefinition Height="Auto" />
        </Grid.RowDefinitions>

        <TextBlock Grid.Row="0" Grid.Column="0" Text="Naam:" />
        <TextBox Grid.Row="0" Grid.Column="1" />

        <TextBlock Grid.Row="1" Grid.Column="0" Text="Plaats:" />
        <TextBox Grid.Row="1" Grid.Column="1" />
    </Grid>

    <Button Grid.Row="2"
            HorizontalAlignment="Right"
            Content="Opslaan" />
</Grid>
```

**Resultaat van bovenstaande code:**
![[Pasted image 20260527195416.png]]

Zoals je ziet definieert dit voorbeeld pas in een specifieke grid.row de kolom definities, hierdoor kun je de indeling per rij, kolom (grid.column geselecteerd) of zelfs per cel (grid.row + grid.column geselecteerd) laten afwijken van de andere cellen, rijen of kolommen in de grid.

Dit maakt het gebruik van de grid als basis voor je gebruikers interface zo krachtig.

## Valkuil
Je kunt hiermee echter ook zover gaan dat je code er erg onoverzichtelijk gaat uitzien en je moeilijk terug kunt vinden welke definitie je nu moet aanpassen om een bepaalde rij, kolom, of cel aan te passen.
