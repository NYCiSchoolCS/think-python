# Loops!

### Sum all the numbers

Write a program that adds the numbers from 0 to 10

Output:
```
55
```

Now change your program to ask you for a number first, and sum the numbers from 0 to that number.
Sample Output:
```
Enter a number: 40
780
```

Next, ask the user for every number to add.
Sample Output:
```
Enter a number: 3
Enter a number to sum: 6
Enter a number to sum: 4
Enter a number to sum: 8
18
```

### Count down with `for`!

Write a program that asks the user for a number, and then uses a `for` loop to print a count down from that number. Don't forget to launch the rocket at the end!

Sample Output:
```
Enter a number: 5
5
4
3
2
1
Blast off!
```


### Odd or even? Triangular?

1. Loop through numbers from 1 to 50 and print whether they are odd or even.
  Sample Output:
    ```
    1 Odd
    2 Even
    3 Odd
    4 Even
    5 Odd
    6 Even
    7 Odd
    .
    .
    .
    
    ```

2. The field of number theory deals with numbers and their relationships to each other. Mathematicians studying this have com up with lots of ways to classify numbers besides ood and even. One of these is Triangular.

  Triangular numbers can be aranged in a triangle. Groups of 1, 3, or 6 dots can be arranged in a triangle and so these numbers are triangular numbers. If you've ever gone bowling, you'll recognize that 10 is also triangular.

  It turns out that triangular numbers are the sum of consecutive integers:
  ```
   1  = 1
   3  = 1 + 2
   6  = 1 + 2 + 3
  10  = 1 + 2 + 3 + 4
  ```

  Write a function call isTriangular(n) that takes a number and returns whether or not the number is a triangular number. 
  Test your function on some numbers you know are triangular and some you know are not!
  ```
  >>> isTriangular(5)
  False
  >>> isTriangular(6)
  True
  >>> isTriangular(10)
  True
  >>> isTriangular(4)
  False
  ```
  
3. Add output for isTriangular() in your loop!
  Sample Output:
  ```
  1 Odd
  2 Even
  3 Odd, Triangular
  4 Even
  5 Odd
  6 Even, Triangular
  7 Odd
  .
  .
  .
  
  ```

