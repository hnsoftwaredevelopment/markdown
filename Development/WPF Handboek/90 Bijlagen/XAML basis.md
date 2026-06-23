# XAML basis

XAML is de markup-taal waarmee WPF-schermen worden beschreven.
Elementen worden geschreven als XML-elementen.

## Element met properties

```xaml
<Button Content="Opslaan" Width="120" />
```

## Element met child elements

```xaml
<Grid>
    <TextBlock Text="Voorbeeld" />
</Grid>
```

## Property element syntax

Sommige properties worden niet als attribuut geschreven, maar als child element.

```xaml
<Grid>
    <Grid.RowDefinitions>
        <RowDefinition Height="Auto" />
    </Grid.RowDefinitions>
</Grid>
```

