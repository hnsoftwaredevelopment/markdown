---
tags:
  - wpf
icon: bi-filetype-xml
---
# Add buttons from code
Add buttons from code

To add buttons dynamicly to a WPF you can use:

```
for(int i=0; i<5; i++)
{
    System.Windows.Controls.Button newBtn = new Button();

    newBtn.Content = i.ToString();
    newBtn.Name = "Button" + i.ToString();

    sp.Children.Add(newBtn);
}
```

## Remove a button

```
sp.Children.Remove((UIElement)this.FindName("Button0"));
```

## Another way

You also can encapsulate the whole thing, there normally should be no point in naming the button. Something like this:

```
public class SomeDataModel
{
    public string Content { get; set; }

    public ICommand Command { get; set; }

    public SomeDataModel(string content, ICommand command)
    {
        Content = content;
        Command = command;
    }
}
```

Then you can create models and put them into a bindable collection:

```
private readonly ObservableCollection<SomeDataModel> _MyData = new ObservableCollection<SomeDataModel>();
public ObservableCollection<SomeDataModel> MyData { get { return _MyData; } }
```

Then you just need to add and remove items from that and create buttons on the fly:

```
<ItemsControl ItemsSource="{Binding MyData}">
    <ItemsControl.ItemTemplate>
        <DataTemplate>
            <Button Content="{Binding Content}" Command="{Binding Command}"/>
        </DataTemplate>
    </ItemsControl.ItemTemplate>
</ItemsControl>
```

[WPF Documentation](https://docs.microsoft.com/en-us/dotnet/desktop/wpf/?view=netframeworkdesktop-4.8)