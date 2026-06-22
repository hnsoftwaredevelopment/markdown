# Multidimensional lists

Best practice for this is to create a class for it

```C#
public class Person {
    public string Name {get; set;}
    public string Email {get; set;}
}

var people = new List<Person>();
```

But can also be done using a tuple
```C#
var people = new List<(string Name, string Email)>
{
  ("Joe Bloggs", "joe@bloggs.com"),
  ("George Forman", "george@formangrills.co"),
  ("Peter Pan", "me@neverland.com")
};

var georgeEmail = people[1].Email;
```