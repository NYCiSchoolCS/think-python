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

### Question 2 (WIP)
Debug the following code:

```python
make_tweet(sentence):

    if len(sentence) > 140:
        return sentence[0:140]
    else:
        return sentence
    
```
