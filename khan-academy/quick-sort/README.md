# Quick Sort
Quick sort in Python.

Pseudocode:
```text
if low is less than high:
    partition the array by:
        setting a highest pivot
        while element is less than the pivot:
            swap the elements around pivot, so
                elements end up properly on the correct side of the pivot
    recursively re-partition and sort each subarray and eventually the array
    the elements do not need to be combined, in correct order
```

Notes:
- nlogn
- works best when partitions are balanced
- when random pivots are chosen, use median of threes (randomly choose three elements and median as pivot)
    - more elements are even better