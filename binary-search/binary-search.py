def bs(array, val):
    minv = 0
    maxv = len(array) - 1
    current = 0
    while minv <= maxv:
        current = (maxv + minv) // 2
        if array[current] == val:
            return current
        elif array[current] < val:
            minv = current + 1
        else:
            maxv = current - 1
    return -1


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
          41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for i, prime_index in enumerate(primes):
    pi = bs(primes, primes[i])
    assert pi == i, f"Should be {i}."
    print(f"Index of {primes[i]} is {pi}.")
