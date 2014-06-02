## String & Lists Worksheet

**Due:** Friday, June 6 in class

**Instructions:**
* Please submit your answers on a separate piece of paper.
* You can use Python to answer the questions.
* **Please work on the problems individually.** 


### Question 1 (25 pts)

The following functions are all intended to check whether a string contains _any_ lowercase letters, but at least some of them are wrong. 

**For each function below, decide whether the function works as intended. If not, describe what the function actually does.** You can assume that the parameter s is always a string.

Note, ```islower()``` is a string method that returns ```True``` if all cased characters in the string are lowercase and there is at least one cased character. It returns ```False``` otherwise. 

```python
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else: 
            return False
```

```python         
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
```

```python
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
```

```python
def any_lowercase4(s):
    flag = False
    for c in s: 
        flag = flag or c.islower()
    return flag
```

```python
def any_lowercase5(s):
    for c in s:
        if not c.islower()
            return False
    return True
```

### Question 2 (10 pts)
The following code throws an error when you try to run it. The error is
```
Traceback (most recent call last):
  File "test.py", line 7, in <module>
    print quantity[i] + " " + ingredients[i]
    
IndexError: list index out of range
```

1. Explain why there is an error.
2. Rewrite the code so it runs without errors. Note, there are multiple correct answers. 

```python
ingredients = ["butter", "apples", "sugar", "nutmeg"]
quantity = ["one stick", "10", "1 cup"]

print "Ingredient:"

for i in range(len(ingredients)):
    print quantity[i] + " " + ingredients[i]
    
```

### Question 3 (10 pts)

The following code should print the items in food_list that are capitalized, the code throws an error when you try to run it. The error is 
```
Traceback (most recent call last):
  File "test.py", line 4, in <module>
    if food[0].upper() == food[0]:
TypeError: 'int' object has no attribute '__getitem__'
```

1. Explain why there is an error. 
2. Rewrite the code so it runs without errors. 


```python
food_list = ["Apple", "pear", "Banana", "mango"]

for food in range(len(food_list)):
    if food[0].upper() == food[0]:
        print food
    
```
