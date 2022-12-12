from typing import List, Tuple


with open("input.txt") as x:
    grid = x.readlines()
    grid = [[char for char in line] for line in grid]

starting = (0, 0)
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "S":
            starting = (r, c)

# min_path_so_far = float("inf")


# def backtrack(r: int, c: int, visited: List[Tuple[int, int]]) -> None:
#     global min_path_so_far
#     if grid[r][c] == "E":
#         min_path_so_far = min(min_path_so_far, len(visited))
#         return
#     elif len(visited) > min_path_so_far:
#         return
#     DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#     for delta_r, delta_c in DIRECTIONS:
#         new_r = delta_r + r
#         new_c = delta_c + c
#         if (
#             0 <= new_r < len(grid)
#             and 0 <= new_c < len(grid[0])
#             and (ord("z") if grid[new_r][new_c] == "E" else ord(grid[new_r][new_c]))
#             - (ord("a") if (r, c) == starting else ord(grid[r][c]))
#             <= 1
#             and (
#                 new_r,
#                 new_c,
#             )
#             not in visited
#         ):
#             backtrack(new_r, new_c, visited + [(new_r, new_c)])
#
#
# backtrack(starting[0], starting[1], [])

queue: List[Tuple[int, int, int]] = [(*starting, 0)]
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
            - (ord("a") if (r, c) == starting else ord(grid[r][c]))
            <= 1
            and (
                new_r,
                new_c,
            )
            not in visited
        ):
            queue.append((new_r, new_c, steps + 1))
