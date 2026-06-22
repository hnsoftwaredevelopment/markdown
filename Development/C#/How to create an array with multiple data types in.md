How to create an array with multiple data types in C#?

# How to create an array with multiple data types in C#?

When you declare the array as an Object, you can have different data types. Since System.Object is the base class of all other types, an item in an array of Objects can have a reference to any other type of object.

```C#
object[] TestArray = new object[4];
TestArray[0]=7;
TestArray[1]=System.DateTime.Now;
TestArray[2]="Tina";
TestArray[3]=true;
```

## How to Retrieve different data types from an Array?
In order to retrieve different data types from an Object array, you can convert an element to the appropriate data type.

```C#
int id = int.Parse(TestArray(0));
DateTime joiningDate = DateTime.Parse(TestArray(1));
int id = int.Parse(TestArray(0));
DateTime joiningDate = DateTime.Parse(TestArray(1));
``` 

As an alternative to Object array, you can use System.Collections.ArrayList.