---
<<<<<<< Updated upstream:Development/Code/C#/WPF/ComboBox.md
tags:
  - wpf
icon: bi-filetype-xml
---
# ComboBox
\[TOC\]
=======
category: WPF
tags:
  - combobox
---
```insta-toc

```
>>>>>>> Stashed changes:Development/C#/WPF/ComboBox.md

In this part, we’re looking at the ComboBox control in WPF. Starting from the simplest example to more complex ones.

[Video 26 ComboBox control](https://youtu.be/m5laJbNeIxg)

## XAML Code

```
<Window.Resources>
      <Style TargetType="ComboBox">
          <Setter Property="FontSize" Value="24"/>
      </Style>
  </Window.Resources>
  <Grid>
      <Grid.ColumnDefinitions>
          <ColumnDefinition/>
          <ColumnDefinition/>
      </Grid.ColumnDefinitions>
      <StackPanel>
          <ComboBox IsEditable="True" >
              <ComboBoxItem>item 1</ComboBoxItem>
              <ComboBoxItem>item 2</ComboBoxItem>
          </ComboBox>
           
          <ComboBox>
              <ComboBoxItem>
                  <StackPanel Orientation="Horizontal">
                      <Ellipse Fill="Red" Width="10" Height="10"/>
                      <TextBlock Text="item 1"/>
                  </StackPanel>
              </ComboBoxItem>
          </ComboBox>
 
          <StackPanel Orientation="Horizontal" >
              <ComboBox x:Name="cbo1" Width="150" />
              <TextBox x:Name="tbx1" Width="150" FontSize="24"/>
              <Button Content="ADD" Width="100" Click="Button_Click"/>
          </StackPanel>
 
          <ComboBox Name="cboStudents" 
                    ItemsSource="{Binding students}"
                    DisplayMemberPath="Name"
                    SelectionChanged="cboStudents_SelectionChanged"/>
          <ListBox Height="100" Background="Beige"
                  Name="lbxScores" />
          <ListBox Height="100" Background="AliceBlue"
                 ItemsSource="{Binding ElementName=cboStudents,
              Path=SelectedItem.Scores}"/>
      </StackPanel>
 
      <StackPanel Grid.Column="1" Name="SP2" Loaded="SP2_Loaded"/>
  </Grid>
```

## C# Code

```
public partial class MainWindow : Window
   {
       public List<Student> students { get; set; } = Students.GetStudents();
       public MainWindow()
       {
           InitializeComponent();
           DataContext = this;
       }
 
       private void Button_Click(object sender, RoutedEventArgs e)
       {
           cbo1.Items.Add(tbx1.Text);
       }
 
       private void SP2_Loaded(object sender, RoutedEventArgs e)
       {
           ComboBox cbo = new ComboBox();
           //ComboBoxItem cbi = new ComboBoxItem();
           //cbi.Content = "Added dynamically";
           //cbo.Items.Add(cbi);
           List<string> itemlist = new List<string>() { "item 1", "item 2", "item 3" };
           cbo.ItemsSource = itemlist;
           SP2.Children.Add(cbo);
       }
 
       private void cboStudents_SelectionChanged(object sender, SelectionChangedEventArgs e)
       {
           var cbo = sender as ComboBox;
           var selItem = cbo.SelectedItem as Student;
           lbxScores.Items.Clear();
           foreach (var score in selItem.Scores)
           {
               lbxScores.Items.Add(score);
           }
       }
   }
   public class Students
   {
       public static List<Student> GetStudents()
       {
           return new List<Student>()
           {
               new Student(){Name="John", Scores=new List<int>(){1,2,3}},
               new Student(){Name="Jane", Scores=new List<int>(){4,5,6}}
           };
       }
   }
   public class Student
   {
       public string Name { get; set; }
       public List<int> Scores { get; set; }
 
   }
```