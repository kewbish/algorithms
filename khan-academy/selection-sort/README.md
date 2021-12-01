# Selection Sort
Selection sort in Python.  

Pseudocode:  
```text
for each index in array:
    find minimum of array from that index onward by:
        setting minimum values
        looping over all the elements
            if element is less than current minimum:
                set element as new minimum
    swap the minimum element with the current element
```

Notes:
- two for loops -> n^2 running time
- pretty slow, there are better implementations