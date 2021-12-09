from functools import reduce

with open("input.txt") as x:
    heights = x.read().splitlines()
    heights = [[int(c) for c in list(row)] for row in heights]

size_y = len(heights)
size_x = len(heights[0])


def is_low_point(r, c):
    cell = heights[r][c]
    lower = heights[r][c - 1] if c > 0 else 9999
    upper = heights[r][c + 1] if c + 1 < size_x else 9999
    left = heights[r - 1][c] if r > 0 else 9999
    right = heights[r + 1][c] if r + 1 < size_y else 9999
    return cell < lower and cell < upper and cell < left and cell < right


# trusting the natural recursion except there's no htdp
def find(r, c):
    cheights = heights
    if cheights[r][c] == 9:
        return 0  # no points
    cheights[r][c] = 9  # make a drainage high point
    pts = 1
    for rn, cn in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if rn < 0 or rn + 1 > size_y or cn < 0 or cn + 1 > size_x:
            continue
        pts += find(rn, cn)
    return pts


basins = []

for r in range(size_y):
    for c in range(size_x):
        if is_low_point(r, c):
            basins += [find(r, c)]

basin_sizes = reduce(lambda n, p: n * p, sorted(basins, reverse=True)[:3])

print(basin_sizes)
