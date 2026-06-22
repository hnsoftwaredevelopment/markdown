Add Binding for toolbar

# Add Binding for toolbar

![78a349082dd70be87c15179dc13e6aa0.png](attachments/52e288eb5ef440ada8206a5d6df4f627.png)


```XAML
    <Window.CommandBindings>
        <CommandBinding Command="New"       CanExecute="CommonCommandBinding_CanExecute" />
        <CommandBinding Command="Save"      CanExecute="CommonCommandBinding_CanExecute" />
        <CommandBinding Command="Delete"    CanExecute="CommonCommandBinding_CanExecute" />
    </Window.CommandBindings>
```