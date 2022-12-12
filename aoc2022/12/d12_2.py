from typing import List, Tuple


with open("input.txt") as x:
    grid = x.readlines()
    grid = [[char for char in line] for line in grid]

queue: List[Tuple[int, int, int]] = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] in ["S", "a"]:
            queue.append((r, c, 0))

visited = set()
while queue:
    r, c, steps = queue.pop(0)
    if (r, c) in visited:
        continue
    if grid[r][c] == "E":
        print(steps)
        break
    visited.add((r, c))
    DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for delta_r, delta_c in DIRECTIONS:
        new_r = delta_r + r
        new_c = delta_c + c
        if (
            0 <= new_r < len(grid)
            and 0 <= new_c < len(grid[0])
            and (ord("z") if grid[new_r][new_c] == "E" else ord(grid[new_r][new_c]))
            - (ord("a") if (r, c) == "S" else ord(grid[r][c]))
            <= 1
            and (
                new_r,
                new_c,
            )
            not in visited
        ):
            queue.append((new_r, new_c, steps + 1))
