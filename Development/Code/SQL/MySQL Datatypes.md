MySQL Datatypes

MySQL Datatypes
* * *
[TOC]
* * *
# MySQL Data Types
MySQL supports three categories of data types: string, numeric and date/time data types.

## String Data Types
String data types are normally used to store names, addresses, descriptions or any value that contains letters and numbers including binary data, like image or audio files.

### The CHAR and VARCHAR Types
The `CHAR` data type allows you to store fixed-length strings with a maximum size of 255 characters. Whereas the `VARCHAR` data type allows you to store variable-length strings with a maximum size of 65,535 characters (it was limited to 255 characters prior to MySQL 5.0.3).

The `CHAR` and `VARCHAR` data types are declared with a length that indicates the maximum number of characters you want to store. For example, `CHAR(5)` can hold up to 5 characters.

The main difference between the `CHAR` and `VARCHAR` data type is the way they stores the data. When values are stored in a `CHAR` column, they are right-padded with spaces to the specified length, but in `VARCHAR` column values are not padded when they are stored. This means if you store the value 'ab' in a `CHAR(4)` column the value will be stored as 'ab  ', whereas the same value will be stored in `VARCHAR(4)` column as 'ab'.

> **Tip**: Use `CHAR` data type to store the values that has fixed length, like country code. For values that has variable length like names or titles use `VARCHAR` to save the space.

> **Note**: The effective maximum length of a `VARCHAR` is subject to the maximum row size (65,535 bytes, which is shared among all columns) and the character set used.

### The BINARY and VARBINARY Types
The `BINARY` and `VARBINARY` types are similar to `CHAR` and `VARCHAR`, except that they contain binary strings rather than nonbinary string. The permissible maximum length is the same for `BINARY` and `VARBINARY` as it is for `CHAR` and `VARCHAR`, except that the length for `BINARY` and `VARBINARY` is a length in bytes rather than in characters.

### The TEXT and BLOB Types
The `TEXT` and `BLOB` data types are specifically made to hold large sets of data. The `TEXT` data type is used to to store long string of text like descriptions, blog comments, etc.

A `BLOB` is a binary large object that can hold a variable amount of data. It is especially useful when you need to store binary media files in the database, such as images or audio files.

The four `BLOB` types are `TINYBLOB`, `BLOB`, `MEDIUMBLOB`, and `LONGBLOB`. These differ only in the maximum length of the values they can hold. Similary, the four `TEXT` types are `TINYTEXT`, `TEXT`, `MEDIUMTEXT`, and `LONGTEXT`. These correspond to the four `BLOB` types and have the same maximum lengths and storage requirements.

The following table lists the MySQL string data types that come in pairs. The maximum length is in bytes, whether the type is binary or nonbinary.

|Binary data type|Nonbinary data type|Maximum length|
|:---- |:---- | ----:|
|BINARY|CHAR|255|
|VARBINARY|VARCHAR|65.535|
|TINYBLOB|TINYTEXT|255|
|BLOB|TEXT|65.535|
|MEDIUMBLOB|MEDIUMTEXT	|16.777.215|
|LONGBLOB|LONGTEXT|4.294.967.295|

### The ENUM Type
The `ENUM` dataype allows you to specify a list of possible values that can be stored in a column. For example, a column specified as gender `ENUM('male', 'female') NOT NULL` can have any of these values: '', 'male' or 'female'. You can specify up to a maximum of 65,535 distinct values in an `ENUM` list. If you insert an invalid value into an ENUM column i.e. a string which is not present in the list of permitted values, the empty string will be inserted.

### The SET Type
The `SET` data type allows you to specify a list of values to be inserted in the column, like `ENUM`. But, unlike the `ENUM` data type, which lets you choose only one value, the SET data type allows you to choose multiple values from the list of specified values.

For example, a column specified as option `SET('one', 'two') NOT NULL` can store any of these values: '', 'one', 'two' or 'one,two'. Multiple values separated by commas (,). For a `SET` data type, you can specify up to 64 distinct values.

## Numeric Data Types
Numeric data types are normally used to store data like price, salary etc.

### The INTEGER, INT, SMALLINT, TINYINT, MEDIUMINT, BIGINT Type
MySQL supports the SQL standard integer types `INTEGER` (or `INT`) and `SMALLINT`. MySQL also supports the integer types `TINYINT`, `MEDIUMINT`, and `BIGINT` as an extension to the SQL standard. The following table shows the range for each integer type.

|Data Type|Range (Signed)|Range (Unsigned)|
|:---- | ----:| ----:|
|TINYINT|-128 to 127|0 to 255|
|SMALLINT|-32.768 to 32.767|0 to 65.535|
|MEDIUMINT|-8.388.608 to 8.388.607|0 to 16.777.215|
|INT|-2.147.483.648 to 2.147.483.647|0 to 4.294.967.295|
|BIGINT|-9.223.372.036.854.775.808 to 9.223.372.036.854.775.807|0 to 18.446.744.073.709.551.615|
Numeric data types have additional attributes `SIGNED` and `UNSIGNED`. Numeric data types are `SIGNED` by default and their range goes from negative to positive value. Adding the `UNSIGNED` attribute to the numeric column disallows negative values and move the range up in such a way that minimum value starts from zero instead of a negative number.

### The DECIMAL, NUMERIC Type
The `DECIMAL` and `NUMERIC` data types are used to store exact numeric values. These data types are also known as "Fixed-Point" or "Exact Value" Types and typically used when it is important to preserve exact precision, for example storing the monetary data like product price. In MySQL, `NUMERIC` is implemented as `DECIMAL`.

When declaring a `DECIMAL` or `NUMERIC` column, the precision and scale can be specified, like `DECIMAL(P,S)` or `NUMERIC(P,S)`, where *P* is the precision and *S* is the scale. The precision specifies the maximum number of digits (including the digits after the decimal point) that can be stored in the column, whereas the scale represents the number of digits that can be stored after the decimal point. For example, the price `DECIMAL(6,2)` column can store any value with six digits and two decimals i.e. in the range from -9999.99 to 9999.99.

### The FLOAT, DOUBLE Type
The `FLOAT` and `DOUBLE` types represent approximate numeric data values. That's why these data types are also known as "Floating-Point" or "Approximate Value" types

MySQL support syntax: `FLOAT(M,D)` or `DOUBLE PRECISION(M,D)`. Here, (*M*,*D*) means than values can be stored with up to *M* digits in total, of which *D* digits may be after the decimal point. For example, a column defined as `FLOAT(7,3)` will look like -9999.999 when displayed. MySQL performs rounding when storing values, so if you insert 9999.0009 into a `FLOAT(7,3)` column, the approximate result is 9999.001.

> **Note**: Comparing floating-point values may lead to problems, because they are approximate and not stored as exact values. Therefore to store the values that can be used in comparison like price, salary, etc. use the DECIMAL data type instead.

## Date and Time Data Types
Date and Time data types are normally used to store data like date of birth, hiring date, date and time when a record is created or updated inside table, etc.

### The DATE Type
The `DATE` data type is used to store a date. MySQL stores and retrieves `DATE` values in 'YYYY-MM-DD' format, where YYYY, MM, and DD are the year, month, and day parts of the time. The supported range is '1000-01-01' to '9999-12-31'.

### The TIME Type
The `TIME` data type can be used to store time-of-day or a time interval. MySQL stores and retrieves `TIME` values in 'HH:MM:SS' format, where HH, MM, and SS are the hours, minutes, and seconds parts of the time (or 'HHH:MM:SS' format for large hours values). The supported range for TIME values is '-838:59:59' to '838:59:59'.

The hours part may be large because in MySQL the `TIME` type can be used not only to store a time of day (which must be less than 24 hours), but also elapsed time or a time interval between two events (which may be much greater than 24 hours, or even negative).

> Note: By default, values that lie outside the TIME range but are otherwise valid are clipped to the closest endpoint of the range. For example, '860:00:00' is converted to '838:59:59'. Invalid TIME values are converted to '00:00:00'.

### The DATETIME, and TIMESTAMP Types
The `DATETIME` and `TIMESTAMP` data types are used to store combined date-and-time values in 'YYYY-MM-DD HH:MM:SS' format. These data types are typically used to store data like date and time when an order is dispatched, when a row is created or modified inside a table, etc.

Both data types are similar in many respects, but there are some differences — The supported range for `DATETIME` is '1000-01-01 00:00:00' to '9999-12-31 23:59:59'. Whereas, the `TIMESTAMP` has a range of '1970-01-01 00:00:01' UTC to '2038-01-19 03:14:07' UTC.

Also `TIMESTAMP` and `DATETIME` have special auto-initialization and auto-update properties, but these properties are not available for DATETIMEM before MySQL 5.6.5.

> **Note**: MySQL converts TIMESTAMP values from the current time zone to UTC for storage, and back from UTC to the current time zone for retrieval.

### The YEAR Type
The `YEAR` data type is used to store a four digit year value in YYYY format.

It can be declared either as `YEAR` or `YEAR(4)`. The supported range for `YEAR` values is 1901 to 2155. Invalid `YEAR` values are converted to 0000.

> **Note**: Older version of MySQL also allows the storage of two digit year value using YEAR(2), but it is deprecated now and support for it is removed in MySQL 5.7.5.