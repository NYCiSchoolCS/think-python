# Unit 2 - In class exercises

## Exercise 3.3 in Think Python

Python provides a built-in function called `len()` that returns the length of a string, so
the value of `len('allen')` is 5.
Write a function named `right_justify` that takes a string named `s` as a parameter and prints the
string with enough leading spaces so that the last letter of the string is in column 70 of the display.

Test it on a few strings: your name, `"supercalifragilisticexpialidocious"`, `"cat"`, `"The dog likes the toy"`

Sample output:
```
                                                                 allen
                                    supercalifragilisticexpialidocious
                                                                   cat
                                                 The dog likes the toy
```


## Print a Grid
Based on Exercise 3.5 in Think Python

Write a function called `print_grid` that takes a width and draws a 4x4 grid of that width and height 2.

Sample code and output:
```
def def print_grid(width):
    #Your code here

print_grid(3)
print_grid(18)
```
```
+---+---+
|   |   |
|   |   |
+---+---+
|   |   |
|   |   |
+---+---+
+------------------+------------------+
|                  |                  |
|                  |                  |
+------------------+------------------+
|                  |                  |
|                  |                  |
+------------------+------------------+
```

Once you've finished, change your program to only use 3 `|` characters, 3 `+` characters, and 2 `-` characters. You may need to add more functions to do this.

Challenge: Use only **2** `|` characters, **2** `+` characters, and **1** `-` character in your program.

_Hint_: to print more than one value on a line, you can print a comma-separated sequence: `print '+', '-'`.  
If the sequence ends with a comma, Python leaves the line unﬁnished, so the value printed
next appears on the same line.
```
print '+',
print '-'
```

The output of both these statements is `'+ -'`.
A `print` statement all by itself ends the current line and goes to the next line.

Extra Challenge: Make `print_grid` take another argument for how many columns the table should have. For example, `print_grid(4, 5)` should output: 
```
+----+----+----+----+----+
|    |    |    |    |    |
|    |    |    |    |    |
+----+----+----+----+----+
|    |    |    |    |    |
|    |    |    |    |    |
+----+----+----+----+----+
```
