import random

# --- Do not edit these functions! ---
def make_random_list(length):
    start = ord("A")
    items = []
    for i in range(start, start + length):
        items.append(chr(i))
    random.shuffle(items)
    return items
    
def print_list(items):
    print ' | '.join(items)


# This is your part! Fill in the two bubble sort 
# functinos below.

# Fill this is first. It takes a list, and two indexes
# and switches the items in those two spots.
def swap(items, index_1, index_2):
    pass

# Fill in this function to follow the bubble sort
# algorithm. It should use the swap() function.
def bubble_sort(items):
    pass


items = make_random_list(5)
print_list(items)
bubble_sort(items)
print_list(items)