def insert(arr, rightIndex, val):
    j = rightIndex - 1
    while j >= 0 and arr[j] > val:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = val


def insSort(arr):
    for i in range(1, len(arr)):
        insert(arr, i, arr[i])


array = [22, 11, 99, 88, 9, 7, 42]
insSort(array)
assert array == sorted(array), f"Should be {sorted(array)}"
print(f"The sorted arr is {array}")
