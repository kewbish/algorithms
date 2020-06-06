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

Towers of Hanoi notes:
- check if number of disks is zero, therefore must be possible
- set a spare peg, and 'solve' Hanoi for number of disks, but minus one, to that spare peg
    - this will hanoify until that peg
- move the bottom disk (not necessarily 'bottom', just bottom of current stack), which is now exposed to the desired peg
- resolve the hanoi from the spare peg to the target peg

Notes:
- ensure a base case is set
- ensure recursion iterates with steps and isn't doing the same thing over and over again
- less efficient than iteration, and also less intuitive so why would I use this smh