def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    if n % 2 == 1:
        return x * power(x, n-1)
    else:
        y = power(x, n/2)
        return y * y


p = power(2, 6)
assert p == 64, "Should be 64"
print(f"2^6 is {p}")
