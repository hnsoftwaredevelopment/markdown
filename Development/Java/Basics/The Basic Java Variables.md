The Basic Java Variables

# The Basic Java Variables
A variable holds a value; that's its only purpose. For example, lets say you have a variable called X. X holds a value, but I haven't told you what it is yet. Let's do this:

```java
X = 4
```

There, now if I say what is the value of X, you would have to tell me 4. X right now equals 4 because that's how I have it set.

```java
X = "Hello world!"
```

Now X is equal to Hello world! A pretty simple concept, right?

Java variables work no different from regular math variables.

Java specifically has these variables as primitive types (don't worry about what a primitive type means):


- boolean
- byte
- char
- double
- float
- int
- long
- short

These are the basic variable types. There are other types of Java variables, but those are more complicated to deal with. The only more complicated type you've dealt with so far is String, so I'll discuss those as well. Of the list above, we'll go into detail with boolean, char, double, and int.

## Variable Names
Before we begin looking at the types, there's some rules we have to follow when picking variable names. In general, you can name your variables whatever you want, as long as they follow these simple guidelines:

- Java variables cannot start with a number or special symbol
- Java variables cannot be a keyword already

Java has certain words that are used in the language. Since Java uses these words for specific purposes, you cannot name your variables as those keywords. Try naming your variable "if" (without the quotes). Java tell you this is an error. Try naming your variable ")x" (again, without the quotes). Java won't allow this either because Java uses the closing parenthesis as a special symbol. I won't go over all the symbols you cannot use because the list is extensive. If you want to avoid problems just don't use any symbols in your variable names (it's bad coding style anyway).

### Boolean
A boolean is one of the special Java variables that stores either true or false. I say special because in true and false are actually values that the language recognizes. Here is an example:


```java
boolean x = true;
```

This is how a boolean variable is created. In Java, the type of variable has to go before the variable's name. In this case the variable's name is x, and it's type is boolean. We're also setting the variable equal to something, and here we're setting it to true. We could have easily just said:

```java
boolean x;
```


That just creates a variable x that is a boolean variable without setting its value.

I will go into more detail about how to use boolean variables in a later Java tutorial, for now we're just going to keep going over the basic types.

Keep in mind that all Java variables can be simply created without setting the value. However, any variables you create should eventually hold a value, or Java will give you a warning about creating variables you don't need.

### Char
A char variable is a variable that holds a single character. A character is a single letter, number, or symbol. For example, 'A' is a character, so is '1' and '&'. Those are all characters. Let's see what a character variable looks like.

```java
char c = 'g';
```

In this example, I've called the variable c, and it's type is char. In Java, a char must have single quotes around it (this is different from Strings which must have double quotes). This char is being equal to the letter 'g'.

Before I continue, let me say that 'g' and 'G' are <span style="color:red">NOT THE SAME THING</span>. These two characters are not equal because computers do not recognize them as the same symbol. More specifically, they have different ASCII values, but that's beyond what we're trying to learn in this lesson. Just remember that **capital letters are not the same as lower case letters and vice versa**.

### Double
A double variable is one that holds a decimal number. For example:

```java
double number = 4.67;
```

In this example the name of the variable is called number (it can be called anything you want, by the way) and the type is double. We're setting this value to 4.67, although the number does not have to be written as a decimal.

```java
double number = 4;
```

This is also valid, because 4 is the same as 4.0 in decimal.

### Int
An int variable holds an integer.

```java
int num = 2;
```

Unlike double, an int can ONLY hold integers. You cannot store a decimal inside of an int. You can store negative numbers in both ints and doubles however.

The examples below are both valid.

```java
int nume = -2;
double num = -2.67;
```

### String
The last type I want to introduce is String. String is more complicated because it's not one of the basic Java variables, but creating a String variable is no different than the basic types.

```java
String name = 'John';
```

A string variable must have quotes around the value in order for it to be a string. Strings can be made up of one letter, one word, whole sentences, or even entire paragraphs. You can also have empty strings.

```java
String name = "";
```

That string is empty because there is nothing inside of the quotation marks, not even a space.

### Using Java Variables
Setting variables equal to values is great, but wouldn't it be nice if we could use these variables to perform operations? Let's first look at outputting these variables onto the screen so we can see that we've set our variables right.

If you have your Hello world! Program, we're going to be modifying it to perform some math, so pull that up if you have it. If not, you'll have to create a new Java file or project in Eclipse, which you can learn how to do in the previous tutorials.

We're going to make the computer do 5 + 8. First, we need a variable that equals 5, so under the code where you had the computer output "Hello world!" add the following:

```java
int num1 = 5;
```

This says that a new variable called num1 holds an integer and it will hold the number 5.

Next add this:

```java
int num2 = 8;
```

This does the same as above, except this variable is called num2 and it is holding the number 8.

Lastly add this code under those two lines:

```java
int num3 = num1 + num2;
```

This tells the computer to add the values stored in num1 and num2 together and store the answer into num3. Num1 is 5, adds it to num2 which is 8, and stores the number 13 into num3.

Now let's output these values, add these three lines under the new code:

```java
System.out.println(num1);
System.out.println(num2);
System.out.println(num3);
```

Let's look at what we've done. Notice how there are no quotes inside of the parenthesis. That is because we are putting variables into the statement. If we had done:

```java
System.out.println("num1");
```

It would literally print out the word num1, and not our value. Run the program and see the results; you should get the numbers 5, 8, and 13 on the screen.

In general, numbers do not need quotes around them to be displayed. So:

```java
System.out.println(1);
```
will display the number 1.

This math works the exact same way with doubles. I encourage you to play around with double values and get them to display on the screen.

The same can be done with Strings as they work similarly. Try this:

```java
String str1 = "Hello";
String str2 = " World";
String str3 = str1 + str2;
```

This will "add" the values in str1 and str2 and put them into str3, so str3 will now have the value “Hello world!”. Try copying the code above and printing them out using System.out.println. Remember that because these are variable names, you do not need to put the variable names in quotes.

Note: You cannot do this with booleans and chars, because of the way those types of variables work. You can add chars together, but you'll probably get results you weren't expecting. I will leave that fact for a more advanced tutorial, so don't worry about it!

### Basic Math

Note: You cannot do this with booleans and chars, because of the way those types of variables work. You can add chars together, but you'll probably get results you weren't expecting. I will leave that fact for a more advanced tutorial, so don't worry about it!

```java
*Addition*
;
```

Division is a bit trickier, because if you divide two integers you may not get an integer as the answer. If you do decide to store the answer as an integer, the decimal portion will get chopped off. In this example:



The value you will get stored in num will be 1. The .66666 repeating is chopped off because an integer cannot hold that kind of value. To fix this you can do:



Now the variable num can hold the decimal answer.

Order of Operations
Some of you have learned in school (either recently or a long time ago!) about order of operations. As a refresher, remember that multiplication and division are usually done before addition and subtraction.

Ex: 4 + 5 x 3 = 19

This does not equal 27. You have to multiply the 5 and 3 first, and then add the 4. This is basic math you should know.

Java obeys the same order of operation. Java also reads values from left to right. The only way to make it go in a different order is with parenthesis, because operations in parenthesis always go first. Here's what I mean:

In Java:



As always though, the sets of parenthesis are read from left to right, so for example:



In this case the 4 and the 5 are still added together first, then the 3 and the 2 are multiplied, and finally everything is multiplied together to get the answer of 54.

If the math confuses you, you should review your math skills. This is programming for beginners, and I cannot be teaching math along the way or the articles would get far too long. Don't worry though, you really only need to know basic math : )

This was quite a long article, but a necessary one as you will quickly see. A full tutorial on everything there is to know about Java variables would fill pages and pages, so I tried to keep it as brief as possible to get exactly what you need to use them.

Do experiment with these variable types, as you will need to use many of them in most programs you will create. Spend extra time playing with all of the different Java variables, because you'll be using them a lot, and it's best to get used to them right now.

Use this Java tutorial as a guide, and remember that you can always come back to this tutorial later if you need to look up how Java variables are done.



Read more: https://www.java-made-easy.com/java-variables.html#ixzz6IloQuusq