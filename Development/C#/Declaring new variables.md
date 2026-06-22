Declaring new variables

Declaring new variables

To declare an array you want to use for storing doubles it is doc enough to say

```C# 
double number[];
```

This declaration will give an error when you try to use the array number[] in the code, the aray does not excis, you have to declare a new array containing doubles for number[]

The declaration should look more like:

```C# 
double number[] = new double[];
```

But again, this is better,  but still incorrect, you have to declare the maximum size of the array before you can use is. So if you want to store 3 numbers in the array **number** the declaration of the array looks like:

```C# 
double number[] = new double[3];
```

In the code you can assign data to the array x, for example:

```C# 
number[0] = 5.5;
number[1] = 8.3;
number[2] = 7.6;
```

If you already know what values will be assigne you can include this data in the declaration, so you don't need to assign the the data to the array in the code anymore.

The declaration then looks like

```C# 
double number[] = new double[3] {5.5, 8.3, 7.6};
```

If you declare and assing like this, you don't have to set the maximum size of the array, C# can see that for itself.

```C# 
double number[] = new double[] {5.5, 8.3, 7.6};
```

Same foor assigning the type to the array, it can see doubles in the values, so no need to specify the type in the declaration.

```C# 
var number[] = new[] {5.5, 8.3, 7.6};
```

In addition to the above code, we want to go throug the list of numbers and add them together in the variable result.

```C# 
var number[] = new[] {5.5, 8.3, 7.6};

var result = 0.0;

foreache(var number in numbers)
{
	result += number;
}

Console.WriteLine(result);
```

