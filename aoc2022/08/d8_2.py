with open("input.txt") as x:
    grid = x.readlines()
    grid = [[int(c) for c in r.strip()] for r in grid]

visible = 0
max_score = 0

for r in range(len(grid)):
    for c in range(len(grid[0])):
        up, down, left, right = 0, 0, 0, 0
        for left_ind in range(c - 1, -1, -1):
            left += 1
            if grid[r][left_ind] >= grid[r][c]:
                break
        for right_ind in range(c + 1, len(grid[0])):
            right += 1
            if grid[r][right_ind] >= grid[r][c]:
                break
        for down_ind in range(r - 1, -1, -1):
            down += 1
            if grid[down_ind][c] >= grid[r][c]:
                break
        for up_ind in range(r + 1, len(grid)):
            up += 1
            if grid[up_ind][c] >= grid[r][c]:
                break
        max_score = max(max_score, up * down * left * right)

print(max_score)
