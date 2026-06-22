String Escape Sequences

# String Escape Sequences
Escape sequence	Character name	Unicode encoding
|Esc|Character name|Unicode encoding|
|:---:|:---|:---|
|\\'|Single quote|0x0027|
|\\"|Double quote|0x0022|
|\\\\|Backslash|0x005C|
|\\0|Null|0x0000|
|\\a|Alert|0x0007|
|\\b|Backspace|0x0008|
|\\f|Form feed|0x000C|
|\\n|New line|0x000A|
|\\r|Carriage return|0x000D|
|\\t|Horizontal tab|0x0009|
|\\v|Vertical tab|0x000B|
|\\u|Unicode escape sequence (UTF-16)|\\uHHHH (range: 0000 - FFFF; example: \\u00E7 = "ç")|
|\\U|Unicode escape sequence (UTF-32)|\\U00HHHHHH (range: 000000 - 10FFFF; example: \\U0001F47D = "👽")|
|\\x|Unicode escape sequence similar to "\u" except with variable length|\xH[H][H][H] (range: 0 - FFFF; example: \x00E7 or \x0E7 or \xE7 = "ç")|