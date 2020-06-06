# Recursion
Examples of recursion in Python.  

Includes:
- Factorials, both iterative and recursive

Pseudocode:
```text
solve a subproblem of the problem
    use subproblem to solve problem
```

Factorials:
```text
compute factorial by:
    determining n
    multiplying n * (n - 1) * (n - 2) ... (n - x)
    if n is zero:
        return 1
    else multiplying function
```

Palindromes:
```text
compute palindrome by:
    if length of string is zero or one:
        return true
    else if string's last and first characters do not match:
        return false
    return palindrome? of string with first and last chars stripped
```

Powers:
```text
compute power by:
    if exp is zero:
        return 1
    if exp is negative:
        return reciprocal of power function
    if exp is odd:
        return x * power(x, exp-1)
    else exp is even:
        set y to power(x, n/2)
        return y * y
```

Notes:
- ensure a base case is set
- ensure recursion iterates with steps and isn't doing the same thing over and over again