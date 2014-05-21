Recall [this calculator exercises](Unit_4.md#sum-all-the-numbers)

In the end, we had a loop, and asked to user for a letter indicating what operator to use, and a number.
"A" for add, "S" for subtract, "D" for division and "M" multiplication.
We also asked the user how many numbers to enter.

```
Enter A to add, or S to subtract, D to divide, M to multiply
How many numbers? 3
What would you like to do? A
(0) Enter a number: 15
What would you like to do? D
(15) Enter a number: 3
What would you like to do? M
(5) Enter a number: 10
50
```

Here's the code for that exercises:
```python
print "Enter A to add, or S to subtract, D to divide, M to multiply"
num_of_nums = int(raw_input("How many numbers? "))
total = 0
for i in range(num_of_nums):
    operator = raw_input("(" + str(total) + ") What would you like to do? ")
    number = int(raw_input("Enter a number: "))
    operator = operator.upper()
    if operator == "A":
        total += number
    elif operator == "S":
        total -= number
    elif operator == "M":
        total *= number
    elif operator == "D":
        total /= number
        
print "Your total is " + str(total)
```

Change the code to except a string like `"A,5 M,7 S,3 D,8"`. This would add 5, multiply by 7, subtract 3, and then divide by 8. 

```
string_var = "A m y, E r i c a"
string_var.split() # outputs ['A', 'm', 'y,', 'E', 'r', 'i', 'c', 'a']
string_var.split(',') # outputs ['A m y', ' E r i c a']
```
