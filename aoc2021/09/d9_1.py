with open("input.txt") as x:
    heights = x.read().splitlines()
    heights = [[int(c) for c in list(row)] for row in heights]

size_y = len(heights)
size_x = len(heights[0])
risk = 0

for r in range(size_y):
    for c in range(size_x):
        cell = heights[r][c]
        lower = heights[r][c - 1] if c > 0 else 9999
        upper = heights[r][c + 1] if c + 1 < size_x else 9999
        left = heights[r - 1][c] if r > 0 else 9999
        right = heights[r + 1][c] if r + 1 < size_y else 9999
        if cell < lower and cell < upper and cell < left and cell < right:
            risk += 1 + heights[r][c]

print(risk)
