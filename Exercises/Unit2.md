# Unit 2 - In class exercises

## Breakfast 
1. Write a function called `make_coffee` that takes how many cups of coffee you want to make. It should print the amount of coffee and water you need to use assuming you need 1 tablespoon of coffee per cup of water, and 1.5 cup of water per cup of coffee.
2. Write a function called `cook_eggs` that takes a number of eggs and prints how long it will take to make the eggs. Assume that it take 2 minutes to cook each egg.
3. Write a function called `make_taost` that takes how many pieces of bread you want to make into toast and prints out how much butter and jam you need. Assume you need .5 tablespoons of butter and 1 tablespoon of jam per piece of toast.
4. Write a function called `get_cereal` that takes the number of bowl of cereal you want and prints out how many bowls and spoons are needed, how much milk is needed and how much cereal is needed. Assume each bowl of cereal needs 1 cup of cereal and .5 cups of milk.
5. Write a function called `make_grits` that takes how many servings of grits to make. It should print how many cups of water and grits is needed, and how long it will take to cook them. It takes 5 cups of water to cook each cup of grits and there is .25 cups of grits in a serving. No matter how much you’re cooking, it always takes 30 mins to cook.
6. Write a function called `prepare_breakfast`. It should take the number of people who are eating breakfest, and output everything you need to know to make a breakfest with toast, coffee, cereal, grits and eggs. __It should use the other functions you just wrote__

```
>>> prepare_breakfast(2)
You need 3.0 cups of water and 2 tablespoons of coffee
It will take you 4 minutes to cook your eggs
You need 1.0 tablespoons of butter and 2 tablespoons of jam
You need 2 bowls and spoons
You need 1.0 cups of milk and 2 cups of cereal
You need 2.5 cups of water and 0.5 cups of grits and it will take 30 minutes to cook them
>>> prepare_breakfast(10)
You need 15.0 cups of water and 10 tablespoons of coffee
It will take you 20 minutes to cook your eggs
You need 5.0 tablespoons of butter and 10 tablespoons of jam
You need 10 bowls and spoons
You need 5.0 cups of milk and 10 cups of cereal
You need 12.5 cups of water and 2.5 cups of grits and it will take 30 minutes to cook them
```

Write a function that makes breakfast the way you like it! For instance, I love grits, but don't care for cereal or toast, so I would like 3 servings of grits but no toast or cereal: 
```
def my_breakfast():
    make_coffee(1)
    cook_eggs(1)
    make_grits(3)
```

## Justify Strings
Base on Exercise 3.3 in Think Python

Python provides a built-in function called `len()` that returns the length of a string, so
the value of `len('allen')` is 5.
Write a function named `right_justify` that takes a string named `s` as a parameter and prints the
string with enough leading spaces so that the last letter of the string is in column 70 of the display.

Test it on a few strings: your name, `"supercalifragilisticexpialidocious"`, `"cat"`, `"The dog likes the toy"`

Sample code and output:
```
def right_justify(s):
    #Your code here

right_justify("allen")
right_justify("supercalifragilisticexpialidocious")
right_justify("cat")
right_justify("The dog likes the toy")
```
```
                                                                 allen
                                    supercalifragilisticexpialidocious
                                                                   cat
                                                 The dog likes the toy
```

Next, write a function named `center_justify` that does the same thing, but centers the string in a column 70 display.

Sample code and output:
```
def center_justify(s):
    #Your code here

right_justify("70 chars |")
center_justify("allen")
center_justify("supercalifragilisticexpialidocious")
center_justify("cat")
center_justify("The dog likes the toy")
```
```
                                                            70 chars |
                                 allen
                  supercalifragilisticexpialidocious
                                  cat
                         The dog likes the toy
```

Use your justify functions to output this demo day invitation!
```
                 ** Computer Science Class Demo Day **
When: 8am Friday
Where: Room 402
                          Demos will include:
                                      Interactive programming projects
                                                           Live coding
                                  How to write a 'hello world' program
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

_Hint_: To print more than one value on a line, you can print a comma-separated sequence: `print '+', '-'`.  
If the sequence ends with a comma, Python leaves the line unﬁnished, so the value printed next appears on the same line.
```
print '+',
print '-'
```

The output of both these statements is `'+ -'`.
A `print` statement all by itself ends the current line and goes to the next line.

Extra Challenge: Make `print_grid` take another argument for how many columns the grid should have. For example, `print_grid(4, 5)` should output: 
```
+----+----+----+----+----+
|    |    |    |    |    |
|    |    |    |    |    |
+----+----+----+----+----+
|    |    |    |    |    |
|    |    |    |    |    |
+----+----+----+----+----+
```

Super Extra Challenge: Make `print_grid` take yet another argument for how many *rows* the grid should have. For example, `print_grid(4, 5, 3)` should output: 
```
+----+----+----+----+----+
|    |    |    |    |    |
|    |    |    |    |    |
+----+----+----+----+----+
|    |    |    |    |    |
|    |    |    |    |    |
+----+----+----+----+----+
|    |    |    |    |    |
|    |    |    |    |    |
+----+----+----+----+----+
```
_Hint_: In python you can have a string with a newline in it by using `\n`. For example `print "Hello\nWorld"` would output
```
Hello
World
```
