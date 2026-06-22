# Control Buttons on WPF from code
Control Buttons on WPF from code

```
<StackPanel Name="panel1" 
            Grid.Column="1"
            Height="Auto"
            Width="Auto" 
            Margin="427,60,0,0" 
            Grid.Row="2" 
            VerticalAlignment="Top"
            HorizontalAlignment="Left" >
    <StackPanel Height="144">

    </StackPanel>
</StackPanel>
```

This named Sttackpannel can be used in the code

```
public void GenerateControls()
{
    TextBox txtNumber = new TextBox();
    txtNumber.Name = "txtNumber";
    txtNumber.Text = "1776";
    txtNumber.Background= Brushes.Red;

    panel1.Children.Add(txtNumber);
    panel1.UpdateLayout();
}
```