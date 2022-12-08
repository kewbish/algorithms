with open("input.txt") as x:
    grid = x.readlines()
    grid = [[int(c) for c in r.strip()] for r in grid]

R_HALF, C_HALF = len(grid) // 2, len(grid[0]) // 2

visited = set()
visible = 0

for c in range(len(grid[0])):
    r = 0
    down_max = -1
    while r < len(grid):
        if grid[r][c] > down_max:
            down_max = grid[r][c]
            if (r, c) not in visited:
                visible += 1
                visited.add((r, c))
        r += 1
    up_max = -1
    r = len(grid) - 1
    while r >= 0:
        if grid[r][c] > up_max:
            up_max = grid[r][c]
            if (r, c) not in visited:
                visible += 1
                visited.add((r, c))
        r -= 1
for r in range(len(grid)):
    c = 0
    right_max = -1
    while c < len(grid[0]):
        if grid[r][c] > right_max:
            right_max = grid[r][c]
            if (r, c) not in visited:
                visible += 1
                visited.add((r, c))
        c += 1
    left_max = -1
    c = len(grid[0]) - 1
    while c > 0:
        if grid[r][c] > left_max:
            left_max = grid[r][c]
            if (r, c) not in visited:
                visible += 1
                visited.add((r, c))
        c -= 1

print(visible)
