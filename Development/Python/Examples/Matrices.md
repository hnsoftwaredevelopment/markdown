Matrices

[TOC]

------

# Add Two Matrices

*In this program, you'll learn to add two matrices using Nested loop and Next list comprehension, and display it.*

------

In Python, we can implement a matrix as nested list (list inside a list). We can treat each element as a row of the matrix.

For example X = [[1, 2], [4, 5], [3, 6]] would represent a 3x2 matrix. First row can be selected as X[0] and the element in first row, first column can be selected as X[0][0].

We can perform matrix addition in various ways in Python. Here are a couple of them.

```python
# Program to add two matrices using nested loop

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)
```

```asciiarmor
>>> [17, 15, 4]
>>> [10, 12, 6]
>>> [11, 13, 18]

```

In this program we have used nested for loops to iterate through each row and each column. At each point we add the corresponding elements in the two matrices and store it in the result.

## Matrix Addition using Nested List Comprehension

```python
# Program to add two matrices
# using list comprehension

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
   print(r)
```

The output of this program is the same as above. We have used nested list comprehension to iterate through each element in the matrix.

List comprehension allows us to write concise codes and we must try to use them frequently in Python. They are very helpful.

```asciiarmor
>>> [17, 15, 4]
>>> [10, 12, 6]
>>> [11, 13, 18]
```

------
# Transpose a Matrix
*In this example, you will learn to transpose a matrix (which is created by using a nested list).*

------

In Python, we can implement a matrix as nested list (list inside a list). We can treat each element as a row of the matrix.

For example X = [[12, 7], [4, 5], [3, 8]] would represent a 3x2 matrix. First row can be selected as X[0] and the element in first row, first column can be selected as X[0][0].

Transpose of a matrix is the interchanging of rows and columns. It is denoted as X'. The element at ith row and jth column in X will be placed at jth row and ith column in X'. So if X is a 3x2 matrix, X' will be a 2x3 matrix.

Here are a couple of ways to accomplish this in Python.

## Matrix Transpose using Nested Loop

```python
# Program to transpose a matrix using nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
```

```asciiarmor
>>> [12, 4, 3]
>>> [7, 5, 8]

```

In this program we have used nested for loops to iterate through each row and each column. At each point we place the X[i][j] element into result[j][i].

## Matrix Transpose using Nested List Comprehension

```python
''' Program to transpose a matrix using list comprehension'''

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

for r in result:
   print(r)
```

The output of this program is the same as above. We have used nested list comprehension to iterate through each element in the matrix.

List comprehension allows us to write concise codes and we must try to use them frequently in Python. They are very helpful.

```asciiarmor
>>> [12, 4, 3]
>>> [7, 5, 8]
```

------
# Multiply Two Matrices
*In this example you will learn to multiply matrices using two different ways: nested loop and, nested list comprenhension*

------

In Python we can implement a matrix as nested list (list inside a list).

We can treat each element as a row of the matrix.

For example X = [[1, 2], [4, 5], [3, 6]] would represent a 3x2 matrix. First row can be selected as X[0] and the element in first row, first column can be selected as X[0][0].

Multiplication of two matrices X and Y is defined only if the number of columns in X is equal to the number of rows Y.

If X is a n x m matrix and Y is a m x l matrix then, XY is defined and has the dimension n x l (but YX is not defined). Here are a couple of ways to implement matrix multiplication in Python.

## Matrix Multiplication using Nested Loop

```python
# Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
```

```asciiarmor
>>> [114, 160, 60, 27]
>>> [74, 97, 73, 14]
>>> [119, 157, 112, 23]

```

In this program, we have used nested for loops to iterate through each row and each column. We accumulate the sum of products in the result.

This technique is simple but computationally expensive as we increase the order of matrix.

For larger matrix operations we recommend optimized software packages like NumPy which is several (in the order of 1000) times faster than the above code.

## Matrix Multiplication using Nested List Comprehension

```python
# Program to multiply two matrices using list comprehension

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

# result is 3x4
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
   print(r)
```

he output of this program is the same as above. To understand the above code we must first know about built-in function zip() and unpacking argument list using * operator.

We have used nested list comprehension to iterate through each element in the matrix. The code looks complicated and unreadable at first. But once you get the hang of list comprehensions, you will probably not go back to nested loops.

```asciiarmor
>>> [114, 160, 60, 27]
>>> [74, 97, 73, 14]
>>> [119, 157, 112, 23]
```