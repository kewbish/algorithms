# Binary Search
Binary search in Python.  

Pseudocode:
```text
set min to zero
set max to the length of the array
set guess to zero (doesn't matter)

while min is less than equal to max (so the bounds don't get crossed over)
    set guess to average / middle of min and max
    if guess is target
        return guess
    else if guess is less than target
        therefore, move the min bound up
        set min to guess + 1 so guess will not equal min
    else
        therefore, guess is more than target
        therefore, move the max bound down
        set max to guess - 1 so guess will not equal max

guess could not be found
    therefore, return -1 (arbitrary value)
```

Emoji binary search is based on [this freeCodeCamp article](https://www.freecodecamp.org/news/binary-search-algorithm-7170ae244438/).  