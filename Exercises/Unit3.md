# Unit 3 - In class exercises

## Fermat's Last Theorem

Fermat’s Last Theorem says that there are no integers a, b, and c such that
$a^n + b^n = c^n$ for any values of n greater than 2.

1.  Write a function named ```check_fermat``` that takes four parameters—a, b, c and n—and that checks to see if Fermat's theorem holds.

If n is greater than 2 and it turns out to be true that $a^n + b^n = c^n$, the program should print,
“Holy smokes, Fermat was wrong!” Otherwise the program should print, “No, that doesn’t work.”.

2. Write a function that prompts the user to input values for a, b, c and n, converts them to
integers, and uses ```check_fermat``` to check whether they violate Fermat’s theorem.


## Pig Latin

1. Write a function ```pig_latin``` that takes in a single word, then converts the word to
Pig Latin.


To review, Pig Latin takes the first letter of a word, puts it at the end, and appends
"ay". The only exception is if the first letter is a vowel, in which case we keep it
as it is and append "hay" to the end.

###Some Useful Python Code:
Suppose variable word is a string. You can get the first letter of the word using
``` word[0]```, and everything but the first letter of the word using ```word[1:]```.

For example:

```python
word = "beach"
word[0]  # "b"
word[1:] # "each"
```

## Recursion (Challenge Problem)
It is legal for functions to call themselves. Consider the following function:

```python
def countdown(n):
    if n <= 0:
       print "Blastoff!"
    else:
       print n
       countdown(n-1)
```
If n is 0 or negative, it prints "Blastoff!". Otherwise, it prints n and calls the countdown function--itself--with n-1 as an argument.

1. What happens if you call ```countdown(3)```? What does the computer output and why?

2. Write a function called ```do_n``` that takes a function object and a number, n, as arguments, and that calls the given function n times.

3. Write a function called ```exp`` that takes two parameters, x and n, and returns x to the n power.
