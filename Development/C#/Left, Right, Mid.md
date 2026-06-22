Left, Right, Mid

# Left, Right, Mid

[Link to the tutorial](https://kodify.net/csharp/strings/left-right-mid/)

|Feature|Description|C# equivalent|
|---|---|---|
|Left|Get specific number of characters (count) from left part|string.Substring(0, count)|
|Right|Get specific number of characters (count) from right side|string.Substring(string.Length - count, count)|
|Mid|Get a specific number of characters (count) starting at a certain point (index)|string.Substring(index, count)|
|Mid|Get all characters starting at a certain point (index)|string.Substring(index)|


# More info
## Get the left part of a C# string
To get the left part of a string we call the Substring() method on that particular string. We use two arguments with the method. Since we want the left part, the first argument is 0. The second argument is the number of characters from the string's left side. This way string.Substring(0, count) returns the string's left side.

Here's a quick example:

```C#
string example = "Hello, World!";

// Get the 5 characters from the left of the string
string exampleLeft = example.Substring(0, 5);

// Output
Console.WriteLine($"Original string: {example}");
Console.WriteLine($"Left string:     {exampleLeft}");
```

Here we first make the example string variable. Then we call Substring() on that string. With the 0 and 5 method arguments we get five characters from the string's left side.

Keep in mind that the source string shouldn't be empty or too short. Else Substring() generates an exception that, when unhandled, crashes the application.

Here's what the above C# code outputs:

Original string: Hello, World!
Left string:     Hello

## Fetch a string's left segment with a C# extension method
When we have to fetch a string's left part repeatedly, then an extension method saves time and hassle. Here's one way to turn the above example in a string extension method:

```C#
using System;

public static class MyExtensions
{
    /// <summary>
    /// Returns the left part of this string instance.
    /// </summary>
    /// <param name="count">Number of characters to return.</param>
    public static string Left(this string input, int count)
    {
        return input.Substring(0, Math.Min(input.Length, count));
    }
}
```

This Left() string extension method returns the left part of a string. But it also checks with Math.Min() if we don't request too many characters. That prevents the ArgumentOutOfRangeException exception that Substring() otherwise triggers.

Here's how we use that Left() string method:

```C#
using System;

class Kodify_Example
{
    static void Main()
    {
        string example = "Hello, World!";

        // Get the 5 characters from the left of the string
        string exampleLeft = example.Left(5);

        // Output
        Console.WriteLine($"Original string: {example}");
        Console.WriteLine($"Left string:     {exampleLeft}");
    }
}
```

Here's what this mini example outputs:

Original string: Hello, World!
Left string:     Hello

## Get the right part of a C# string
To get the right part of a string we call the Substring() method on that particular string. We give that method two arguments. The first is the start index. To fetch the right part that index is the string's length minus the number of characters we want. (We get that length with the string's Length property.)

The second argument says how many of characters to return from the string's right side. This way string.Substring(string.Length - 10, 10) returns 10 characters from the string's right part.

Here's an example:

```C#
string example = "Hello, World!";

// Get 6 characters from the right of the string
string exampleRight = example.Substring(example.Length - 6, 6);

// Output
Console.WriteLine($"Original string: {example}");
Console.WriteLine($"Right string:    {exampleRight}");
```

This code calls the Substring() method on the example string. To get the string's last six characters, the first argument of that method is example.Length - 6. That says we want to start six characters from the string's end. The second argument is just 6. That gets us six characters from the source string.

With code like this we have to watch out to not request more characters than the string has. Because when we do, Substring() generates the ArgumentOutOfRangeException exception. That error, when unhandled, crashes our application.

Here's what the above code snippet outputs:

Original string: Hello, World!
Right string:    World!

## Fetch a string's right part with a C# extension method
When we repeatedly have to get the right part of strings, an extension method is easier to work with. Here's how we turn the Substring() code in a separate method:

```C#
using System;

public static class MyExtensions
{
    /// <summary>
    /// Returns the right part of the string instance.
    /// </summary>
    /// <param name="count">Number of characters to return.</param>
    public static string Right(this string input, int count)
    {
        return input.Substring(Math.Max(input.Length - count, 0), Math.Min(count, input.Length));
    }
}
```

This Right() extension method returns the right part of a string. But it also uses the Math.Max() and Math.Min() methods to prevent that we request more characters than the string actually holds.

That prevents ArgumentOutOfRangeException errors that Substring() otherwise generates. (Should we request more characters than the string actually holds, then Right() just returns the complete string.)

To use that Right() extension method, we do:

```C#
using System;

class Kodify_Example
{
    static void Main()
    {
        string example = "Hello, World!";

        // Get 6 characters from the right of the string
        string exampleRight = example.Right(6);

        // Output
        Console.WriteLine($"Original string: {example}");
        Console.WriteLine($"Right string:    {exampleRight}");
    }
}
```

The output this console application example generates is:

Original string: Hello, World!
Right string:    World!

## Get the mid part of a C# string
The programming languages with a Mid() string method often provide two versions. One that returns a string segment that begins at some character index. The other returns a certain number of characters starting from a character index. Let's see how we implement both in C#.

## Get all characters starting somewhere in the string
To get the mid part of a string that begins at a specific index, we call the Substring() method on that string. We provide that method with one argument: the start index. The pattern for that looks like: input.Substring(index). This has the string method return all characters from that index till the end of that string.

Here's how that looks in C#:

```C#
string example = "Hello, World!";

// Get all characters from the 4th character onward
string exampleMid = example.Substring(4);

// Output
Console.WriteLine($"Original string:    {example}");
Console.WriteLine($"Mid string:         {exampleMid}");
```

This code executes Substring() on the example variable. We pass a value of 4 to that method. That returns a substring that begins at the fourth character.

Note that we shouldn't specify a start index that's beyond the source string's length. When we do, Substring() generates the ArgumentOutOfRangeException exception.

This is what the above code snippet outputs:

Original string:    Hello, World!
Mid string:         o, World!

## Get a number of characters from somewhere in the string
To get a mid string of a certain length, we call C#‘s Substring() method on a string. We give that method two arguments. The first is the start index. The second is how many characters to return. That looks like: string.Substring(index, count).

For example:

```C#
string example = "Hello, World!";

// Get 6 characters from the string, starting at character 4
string exampleMid = example.Substring(4, 6);

// Output
Console.WriteLine($"Original string:    {example}");
Console.WriteLine($"Partial mid string: {exampleMid}");
```

Here we call Substring() on the example variable. That method's first argument is 4. That returns a substring that begins at the fourth character. The second argument is 6. That makes the returned mid string 6 characters long.

When we fetch a mid string like that, we shouldn't request more characters than the string has. Neither should we begin at a start index that's outside the string's range. In both scenarios the Substring() method triggers the ArgumentOutOfRangeException exception.

Here's what the above example outputs:

Original string:    Hello, World!
Partial mid string: o, Wor

## Fetch a string's mid part with a C# extension method
When we turn the above code examples into C# extension methods, repeatedly fetching a mid string becomes a lot easier. Here are two extension methods for both ways to get a mid string:

```C#
using System;

public static class MyExtensions
{
    /// <summary>
    /// Returns the mid part of this string instance.
    /// </summary>
    /// <param name="start">Character index to start return the midstring from.</param>
    /// <returns>Substring or empty string when start is outside range.</returns>
    public static string Mid(this string input, int start)
    {
        return input.Substring(Math.Min(start, input.Length));
    }

    /// <summary>
    /// Returns the mid part of this string instance.
    /// </summary>
    /// <param name="start">Starting character index number.</param>
    /// <param name="count">Number of characters to return.</param>
    /// <returns>Substring or empty string when out of range.</returns>
    public static string Mid(this string input, int start, int count)
    {
        return input.Substring(Math.Min(start, input.Length), Math.Min(count, Math.Max(input.Length - start, 0)));
    }
}
```

The first Mid() string extension method has us provide one argument: the start index from which to return the mid string. The second Mid() extension method adds an additional argument: the number of characters to return.

The extension methods use the Math.Min() and Math.Max() methods to prevent ArgumentOutOfRangeException exceptions. This way we don't request a start index outside the string's range. And neither can ask for more characters than the string got.

Here's how we use those two extension methods:

```C#
using System;

class Kodify_Example
{
    static void Main()
    {
        string example = "Hello, World!";

        // Get all characters starting from character 4
        string exampleMid1 = example.Mid(4);

        // Get 6 characters from the string, starting at character 4
        string exampleMid2 = example.Mid(4, 6);

        // Output
        Console.WriteLine($"Original string:    {example}");
        Console.WriteLine($"Full mid string:    {exampleMid1}");
        Console.WriteLine($"Partial mid string: {exampleMid2}");
    }
}
```

The output that this console application generates is:

Original string:    Hello, World!
Full mid string:    o, World!
Partial mid string: o, Wor

## Summary
C# doesn't have methods that return the left, right, or mid part of a string. But we can implement those behaviours with Substring(). That string method can work with two arguments. The first is the start index to get the substring from. The other is the number of characters to return.

For a left string we start at 0 and then return a certain number of characters: string.Substring(0, count). We get the right string when we count back from a string's length: string.Substring(string.Length - count, count).

There are two ways to get a mid string. We can return all characters from a certain start index: input.Substring(index). Or we return a specific number of characters beginning at a start index: string.Substring(index, count).

Regardless of how we use Substring(), we cannot start outside the string's range. Nor can we request more characters than the source string got.

References
Microsoft Docs (n.d.). String.Substring Method. Retrieved on November 22, 2019, from https://docs.microsoft.com/en-us/dotnet/api/system.string.substring

Published November 29, 2019.
