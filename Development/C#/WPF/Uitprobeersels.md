# Uitprobeersels
Uitprobeersels

## Werkende Countrypage

```
<Page x:Class="ModelbouwBeheer.PageCountryCode"
      xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" 
      xmlns:d="http://schemas.microsoft.com/expression/blend/2008" 
      xmlns:local="clr-namespace:ModelbouwBeheer"
      mc:Ignorable="d" 
      d:DesignHeight="450" d:DesignWidth="800"
      Title="PageCountryCode">

    <Page.CommandBindings>
        <CommandBinding Command="New"       CanExecute="CommonCommandBinding_CanExecute" />
        <CommandBinding Command="Save"      CanExecute="CommonCommandBinding_CanExecute" />
        <CommandBinding Command="Delete"    CanExecute="CommonCommandBinding_CanExecute" />
    </Page.CommandBindings>

    <Grid>

        <Label Content="Landcode"   HorizontalAlignment="Left"  Margin="29,55,0,0"   VerticalAlignment="Top"     Width="130"/>
        <Label Content="Landnaam"   HorizontalAlignment="Left"  Margin="29,76,0,0"   VerticalAlignment="Top"     Width="130"/>
        <Border BorderThickness="1" BorderBrush="Black" Grid.ColumnSpan="2" Margin="0,0,0,-0.4">
            <TextBox x:Name="inpCountryID" HorizontalAlignment="Left" Margin="274,60,0,0" TextWrapping="Wrap" Text="" VerticalAlignment="Top" Width="50" Visibility="Collapsed"/>
        </Border>
        <Border BorderThickness="1" BorderBrush="Black" Grid.ColumnSpan="2" Margin="0,0,0,-0.4">
            <TextBox x:Name="inpCountryCode" HorizontalAlignment="Left" Margin="174,60,0,0" TextWrapping="Wrap" Text="" VerticalAlignment="Top" Width="50">
                <TextBox.Background>
                    <SolidColorBrush Color="{DynamicResource {x:Static SystemColors.ControlColorKey}}"/>
                </TextBox.Background>
            </TextBox>
        </Border>
        <Border BorderThickness="1" BorderBrush="Black" Grid.ColumnSpan="2" Margin="0,0,0,-0.4">
            <TextBox x:Name="inpCountryName" HorizontalAlignment="Left" Margin="174,81,0,0" TextWrapping="Wrap" Text="" VerticalAlignment="Top" Width="150">
                <TextBox.Background>
                    <SolidColorBrush Color="{DynamicResource {x:Static SystemColors.ControlColorKey}}"/>
                </TextBox.Background>
            </TextBox>
        </Border>

        <StackPanel Name="CountryCodePageButtons"
                    Orientation="Horizontal" 
                    Height="36"
                    Width="124"
                    Margin="12,105,0,0"
                    VerticalAlignment="Top"
                    HorizontalAlignment="Left">
            <StackPanel.Resources>
                <Style TargetType="{x:Type Button}">
                    <Setter Property="Margin" Value="0,0,5,0"/>
                </Style>
            </StackPanel.Resources>
            <Button x:Name="btnAdd" Width="20" Height="20" HorizontalAlignment="Center" 
                    VerticalAlignment="Center" Command="New" ToolTip="Land toevoegen aan de tabel">
                <Image Source="resources/buttonAdd24.png" Width="20" Height="20" HorizontalAlignment="Center" VerticalAlignment="Center"/>
            </Button>

            <Button x:Name="btnCheck" Width="20" Height="20" HorizontalAlignment="Center" 
                    VerticalAlignment="Center" Command="Save" ToolTip="Land bijwerken" Click="BtnTbSave_Click">
                <Image Source="resources/buttonCheck24.png" Width="20" Height="20" HorizontalAlignment="Center" VerticalAlignment="Center"/>
            </Button>

            <Button x:Name="btnDelete" Width="20" Height="20" HorizontalAlignment="Center" 
                    VerticalAlignment="Center" Command="Delete"    ToolTip="Land verwijderen uit de tabel">
                <Image Source="resources/buttonDelete24.png" Width="20" Height="20" HorizontalAlignment="Center" VerticalAlignment="Center"/>
            </Button>
        </StackPanel>

        <Border BorderThickness="1" BorderBrush="Black" Margin="0,-3,10,2.6">
            <DataGrid x:Name="CountryCode_DataGrid" Margin="10.2,150.2,435.6,9.8" ItemsSource="{Binding}" 
                      AlternatingRowBackground="AliceBlue" AutoGenerateColumns="False" 
                      SelectionChanged="CountryCode_DataGrid_SelectionChanged" IsReadOnly="True">
                <DataGrid.Columns>
                    <DataGridTextColumn Header="Landcode" Binding="{Binding Path=country_code}" Width="80"/>
                    <DataGridTextColumn Header="Omschrijving" Binding="{Binding Path=country_name}" Width="*"/>
                </DataGrid.Columns>
            </DataGrid>
        </Border>
    </Grid>
</Page>
```

## Ziet er niet mooi uit maar dit is de CountryPage nu

```
<Page x:Class="ModelbouwBeheer.PageCountryCode"
      xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" 
      xmlns:d="http://schemas.microsoft.com/expression/blend/2008" 
     xmlns:local="clr-namespace:ModelbouwBeheer"
      mc:Ignorable="d" 
      d:DesignHeight="450" d:DesignWidth="800"
      Title="PageCountryCode">
 
<Page.CommandBindings>
<CommandBinding Command="New"       CanExecute="CommonCommandBinding_CanExecute" />
<CommandBinding Command="Save"      CanExecute="CommonCommandBinding_CanExecute" />
<CommandBinding Command="Delete"    CanExecute="CommonCommandBinding_CanExecute" />
</Page.CommandBindings>
 
<Grid>
<Border BorderThickness="1"
                Grid.ColumnSpan="2" Margin="0,0,0,-0.4" 
                CornerRadius="6"
                BorderBrush="Gray"
                Background="AliceBlue">
<Label Content="Landcode"   HorizontalAlignment="Left"  Margin="29,55,0,0"   VerticalAlignment="Top"     Width="130"/>
<Label Content="Landnaam"   HorizontalAlignment="Left"  Margin="29,76,0,0"   VerticalAlignment="Top"     Width="130"/>
</Border>
<Border BorderThickness="1" BorderBrush="Black" Grid.ColumnSpan="2" Margin="0,0,0,-0.4">
<TextBox x:Name="inpCountryID" HorizontalAlignment="Left" Margin="274,60,0,0" TextWrapping="Wrap" Text="" VerticalAlignment="Top" Width="50" Visibility="Collapsed"/>
</Border>
<Border BorderThickness="1" BorderBrush="Black" Grid.ColumnSpan="2" Margin="0,0,0,-0.4">
<TextBox x:Name="inpCountryCode" HorizontalAlignment="Left" Margin="174,60,0,0" TextWrapping="Wrap" Text="" VerticalAlignment="Top" Width="50">
<TextBox.Background>
<SolidColorBrush Color="{DynamicResource {x:Static SystemColors.ControlColorKey}}"/>
</TextBox.Background>
</TextBox>
</Border>
<Border BorderThickness="1" BorderBrush="Black" Grid.ColumnSpan="2" Margin="0,0,0,-0.4">
<TextBox x:Name="inpCountryName" HorizontalAlignment="Left" Margin="174,81,0,0" TextWrapping="Wrap" Text="" VerticalAlignment="Top" Width="150">
<TextBox.Background>
<SolidColorBrush Color="{DynamicResource {x:Static SystemColors.ControlColorKey}}"/>
</TextBox.Background>
</TextBox>
</Border>
 
<StackPanel Name="CountryCodePageButtons"
                    Orientation="Horizontal" 
                    Height="36"
                    Width="124"
                    Margin="12,105,0,0"
                    VerticalAlignment="Top"
                    HorizontalAlignment="Left">
<StackPanel.Resources>
<Style TargetType="{x:Type Button}">
<Setter Property="Margin" Value="0,0,5,0"/>
</Style>
</StackPanel.Resources>
<Button x:Name="btnAdd" Width="20" Height="20" HorizontalAlignment="Center" 
                    VerticalAlignment="Center" Command="New" ToolTip="Land toevoegen aan de tabel">
<Image Source="resources/buttonAdd24.png" Width="20" Height="20" HorizontalAlignment="Center" VerticalAlignment="Center"/>
</Button>
 
<Button x:Name="btnCheck" Width="20" Height="20" HorizontalAlignment="Center" 
                    VerticalAlignment="Center" Command="Save" ToolTip="Land bijwerken" Click="BtnTbSave_Click">
<Image Source="resources/buttonCheck24.png" Width="20" Height="20" HorizontalAlignment="Center" VerticalAlignment="Center"/>
</Button>
 
<Button x:Name="btnDelete" Width="20" Height="20" HorizontalAlignment="Center" 
                    VerticalAlignment="Center" Command="Delete"    ToolTip="Land verwijderen uit de tabel">
<Image Source="resources/buttonDelete24.png" Width="20" Height="20" HorizontalAlignment="Center" VerticalAlignment="Center"/>
</Button>
</StackPanel>
 
<Border BorderThickness="1" BorderBrush="Black" Margin="0,-3,10,2.6">
<DataGrid x:Name="CountryCode_DataGrid" Margin="10.2,150.2,435.6,9.8" ItemsSource="{Binding}" 
                      AlternatingRowBackground="AliceBlue" AutoGenerateColumns="False" 
                      SelectionChanged="CountryCode\_DataGrid\_SelectionChanged" IsReadOnly="True">
<DataGrid.Columns>
<DataGridTextColumn Header="Landcode" Binding="{Binding Path=country_code}" Width="80"/>
<DataGridTextColumn Header="Omschrijving" Binding="{Binding Path=country_name}" Width="*"/>
</DataGrid.Columns>
</DataGrid>
</Border>
</Grid>
</Page>
```

## Dit is een nettere test van de CurrencyPAge alleen de orientatie is nog niet helemaal goed

```yaml
<Page x:Class="ModelbouwBeheer.PageCurrencies"
      xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" 
      xmlns:d="http://schemas.microsoft.com/expression/blend/2008" 
      xmlns:local="clr-namespace:ModelbouwBeheer"
      mc:Ignorable="d" 
      d:DesignHeight="450" d:DesignWidth="800"
      Title="PageCurrencies">

    <StackPanel>
        <DockPanel Margin="3" VerticalAlignment="Top">
            <Border CornerRadius="6"
            BorderBrush="Gray"
            Background="AliceBlue"
            BorderThickness="2" >
                <StackPanel  Background="AliceBlue" Height="100" Orientation="Vertical">
                    <StackPanel  Orientation="Vertical"  VerticalAlignment="Top">
                        <StackPanel  Orientation="Horizontal"  VerticalAlignment="Top">
                            <Label Content="Valuta ode:"  HorizontalAlignment="Left" Height="30" Width="100"/>
                            <TextBox Name="FrmCurrencyCode" HorizontalAlignment="Left" Height="30"  Width="50"/>
                        </StackPanel>

                        <StackPanel  Orientation="Horizontal"  VerticalAlignment="Top">
                            <Label Content="Omschrijving" Height="30" Width="100"/>
                            <TextBox Name="FrmCurrencyDescription" HorizontalAlignment="Left" Height="30" Width="80"/>
                        </StackPanel>

                        <StackPanel  Orientation="Horizontal"  VerticalAlignment="Top">
                            <Label Content="Koers" Height="30" Width="100"/>
                            <TextBox Name="FrmValutaCurrencyConversionRate" HorizontalAlignment="Left" Height="30" Width="80"/>
                        </StackPanel>
                    </StackPanel>
                </StackPanel>
            </Border>
            <StackPanel Background="AliceBlue" Height="300" Orientation="Vertical"> 
                
            </StackPanel>
        </DockPanel>
    </StackPanel>
</Page>

```