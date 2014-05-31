### Question 1 (25 pts)

The following functions are all intended to check whether a string contains _any_ lowercase letters, but at least some of them are wrong. **For each function below, decide whether the function works correctly. If not, describe what the function actually does.** You can assume that the parameter s is always a string.

Note, islower() is a string method that returns true if all cased characters in the string are lowercase and there is at least one cased character. It returns false otherwise. 

```python
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else: 
            return False

            
def any_lowercase2(s):
    for c in s:
        if "c".islower():
            return "True"
        else:
            return "False"

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase(s):
    flag = False
    for c in s: 
        flag = flag or c.islower()
    return flag
    
def any_lowercase5(s):
    for c in s:
        if not c.islower()
            return False
    return True
```

### Question 2
