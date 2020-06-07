def merSort(array):
    if len(array) > 1:
        q = len(array) // 2
        il = array[:q]
        jl = array[q:]
        merSort(il)
        merSort(jl)
        i, j = 0, 0
        k = 0
        while i < len(il) and j < len(jl):
            if il[i] < jl[j]:
                array[k] = il[i]
                i += 1
            else:
                array[k] = jl[j]
                j += 1
            k += 1
        while i < len(il):
            array[k] = il[i]
            i += 1
            k += 1
        while j < len(jl):
            array[k] = jl[j]
            j += 1
            k += 1
    return array


arr = [3, 7, 12, 14, 2, 6, 9, 11]
merSort(arr)
assert arr == sorted(arr), f"Should be {sorted(arr)}."
print(f"{arr}")
