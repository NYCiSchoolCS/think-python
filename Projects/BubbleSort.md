# Bubble Sort (100 pts total)

Implement the bubble sort algorithm in python. The bubble sort algorithm is as follows:

1. Loop over the items in the list.
1. Compare each item with the item to its right.
1. If the two items are in the wrong order, swap them.
1. Repeat steps 1-3 until you loop over the entire list without doing any swaps.

![bubble sort](/images/Bubble-sort-example.gif)
(via [Wikipedia](http://en.wikipedia.org/wiki/Bubble_sort))

_**Start from the [bubble sort starter code](BubbleSort.py).**_

## Step 1 - Swap Function (15 pts)

Fill in the code for the `swap(items, index_1, index_1)` function.
This function takes a list (`items`) and two indexes and switches the values at those loctions.

For example, if our list was `[A, B, C]` and we called `swap(list, 1, 2)` the the resulting list should be `[A, C, B]`.

## Step 2 - One Iteration (30 pts)

Implement one iteration of bubble sort.
That means your code should loop over the list once and swap any consecutive items that are not in the correct order.
Write this code in the `bubble_sort()` function that's in the starter code.

## Step 3 - All Iterations (30 pts)

Complete the bubble sort algorithm.
Your code should repeat steps 1-3 until it does one full iteration without doing any swaps.
This code should be added `bubble_sort()` function.

## Check your code style (15 pts)

You code should...

* Have good variable names.
* Be easy to understand.
* Have good comments explaining your code.
* Have function definitions that are the same as in the [starter code](BubbleSort.py).
* Not have any commented out, or not used code when you turn it in.
* Have your name in the file.

## Step 4 - Insertion Sort (10 pts)

Implement [Insertion Sort](http://en.wikipedia.org/wiki/Insertion_sort).

This should be another function called `insertion_sort()` just like your `bubble_sort()` function, but that uses the insertion sort algorithm.

The insertion sort algorithm is as follows:

1. Assume that the first element is "sorted." This starts the sorted section of your list.
1. Look at the next item and find where is belongs in the sorted list section.
1. Shift all other items down and incert the currect item into the correct spot in the sorted section.
1. Repeat steps 1 and 2 until you have incerted every item in the list.

![insertion sort](/images/Insertion-sort-example.gif)
(via [Wikipedia](http://en.wikipedia.org/wiki/Insertion_sort))

### Extra Credit (Up to 10 pts)

1. Also implement [Selection Sort](http://en.wikipedia.org/wiki/Selection_sort).
This should be another function called `selection_sort()` just like your other two sort functions.
1. See which sorting algorithm is faster!
Add `from time import time` to the top of your file.
Then use `time()` to get the current time in seconds.
If you get the time before and after sorting, you'll be able to tell how long the sort took.
Try sorting a long list of numbers (try `range(5000)`) so the sorting takes more time.