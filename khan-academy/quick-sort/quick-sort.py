def partition(array, p, r):
    q, j = p, p
    while j < r:
        if array[j] <= array[r]:
            array[j], array[q] = array[q], array[j]
            q += 1
        j += 1
    array[q], array[r] = array[r], array[q]
    return q


def quiSort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quiSort(array, p, q - 1)
        quiSort(array, q + 1, r)


arr = [9, 7, 5, 11, 12, 2, 14, 3, 10, 4, 6]
quiSort(arr, 0, len(arr) - 1)
assert arr == sorted(arr), f"Should be {sorted(arr)}"
print(arr)
