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

Notes:
- ensure a base case is set
- ensure recursion iterates with steps and isn't doing the same thing over and over again