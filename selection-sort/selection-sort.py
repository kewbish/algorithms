def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def indexOfMinimum(arr, start):
    minv = arr[start]
    mini = start
    for i in range(mini + 1, len(arr)):
        if arr[i] < minv:
            mini = i
            minv = arr[i]
    return mini


def selSort(arr):
    for i in range(len(arr)):
        j = indexOfMinimum(arr, i)
        swap(arr, i, j)
    return arr


array = [22, 11, 99, 88, 9, 7, 42]
sorted_array = selSort(array)
assert sorted_array == sorted(array), f"Should be {sorted(array)}"
print(f"The sorted array is {sorted_array}")
