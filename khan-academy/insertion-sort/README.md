# Insertion Sort
Insertion sort in Python.  

Pseudocode:
```text
for each element in array:
    given sort starts at index 1
    shift all elements behind index that are more than the element to the right by:
        set arbitrary value to index minus 1
        while the value is >= 0 where value is not the smallest and element at value is greater than inserted element:
            set element to index plus 1
            decrement arb. value
        set value + 1 to inserted element, where the new space is
```

Notes:
- Usually O(n^2) time as well (two 'for' loops)
- Python's for-loops are unlike Javascripts, here, we need to use while instead