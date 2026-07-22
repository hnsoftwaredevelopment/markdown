Convert_DecBinHexOct

# Python Program to Convert Decimal to Binary, Octal and Hexadecimal
*In this program, you'll learn to convert decimal to binary, octal and hexadecimal, and display it.*

------

Decimal system is the most widely used number system. But computer only understands binary. Binary, octal and hexadecimal number systems are closely related and we may require to convert decimal into these systems. Decimal system is base 10 (ten symbols, 0-9, are used to represent a number) and similarly, binary is base 2, octal is base 8 and hexadecimal is base 16.

A number with the prefix '0b' is considered binary, '0o' is considered octal and '0x' as hexadecimal. For example:

```python
# Python program to convert decimal number into binary, octal and hexadecimal number system

# Change this line for a different result
dec = 344

print("The decimal value of",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")
```

```asciiarmor
>>> 60 = 0b11100 = 0o74 = 0x3c
```