# Use of variables in WPF
Use of variables in WPF

You can define your "variables" in resources, but I would prefer to use styles, to set Properties to same value:

```
xmlns:Sys="clr-namespace:System;assembly=mscorlib"    

<Window.Resources>
    <Sys:Double x:Key="yourVar">30.0</Sys:Double>
</Window.Resources>

<ComboBox>            
    <ComboBox.Items>
        <ComboBoxItem FontSize="{Binding Source={StaticResource yourVar}}">1</ComboBoxItem>
        <ComboBoxItem>2</ComboBoxItem>
        <ComboBoxItem>3</ComboBoxItem>
    </ComboBox.Items>
</ComboBox>
```

## Question on Stackoverflow

I have the following two buttons in XAML:

```
<Button Content="Previous"	Margin="10,0,0,10"/>
<Button Content="Next"		Margin="0,0,10,10"/>

```

How can I define "10" to be a variable so I can change it in one place, something like this:

PSEUDO CODE:

```
<variable x:key="theMargin"/>
<Button Content="Previous"
        Margin="{Variable theMargin},0,0,{Variable theMargin}"/>
<Button Content="Next"
        Margin="0,0,{Variable theMargin},{Variable theMargin}"/>
```

### Answer

Try this:

add to the head of the xamlfile

```
xmlns:System="clr-namespace:System;assembly=mscorlib"
```

Then Add this to the resource section:

```
<System:Double x:Key="theMargin">2.35</System:Double>
```

Lastly, use a thickness on the margin:

```
<Button Content="Next">
   <Button.Margin>
      <Thickness Top="{StaticResource theMargin}" Left="0" Right="0"
                  Bottom ="{StaticResource theMargin}" />
   </Button.Margin>
</Button>
```

A lot of system types can be defined this way: int, char, string, DateTime, etc

### ANSWER 2

Similiar to previous answer, you can add a thickness resource to use, thereby defining each margin direction independently

```
<UserControl.Resources>
    <Thickness x:Key="myMargin" Top="5" Left="10" Right="10" Bottom ="5"></Thickness>
</UserControl.Resources>
```

Then just use the Thickness as the Margin:

```
<Button Content="Next" Margin="{StaticResource myMargin}"/>
```

### ANSWER 3

Why don't you try adding the value as a StaticResource?

Resources.Add("theMargin", 10); Then you can get that value like this:

```
<Button Content="Previous"
        Margin="{StaticResource theMargin},0,0,{StaticResource theMargin}"/>
<Button Content="Next"
        Margin="0,0,{StaticResource theMargin},{StaticResource theMargin}"/>
```