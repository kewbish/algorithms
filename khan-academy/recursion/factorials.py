def recFactorial(n):
    if n == 0:
        return 1
    return n * recFactorial(n - 1)


def iterFactorial(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


assert recFactorial(3) == iterFactorial(3), "Should be 3! (6)"
print(f"Factorial of 3 is {recFactorial(3)}")
