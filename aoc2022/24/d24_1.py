from collections import defaultdict

# my own BFS was wonky (maybe because I was trying to backtrack lol), works cited: https://www.reddit.com/r/adventofcode/comments/zu28ij/comment/j1grx6c/?utm_source=share&utm_medium=web2x&context=3

with open("input.txt") as x:
    blizzard_map = x.read().splitlines()
    #     blizzard_map = """#.######
    # #>>.<^<#
    # #.<..<<#
    # #>v.><>#
    # #<^v^^>#
    # ######.#""".splitlines()
    blizzard_map = [[cell for cell in row] for row in blizzard_map]

DIRECTIONS_MAP = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
blizzards = []
walls = []

for r in range(len(blizzard_map)):
    for c in range(len(blizzard_map[0])):
        if blizzard_map[r][c] == "#":
            walls.append((r, c))
        elif not blizzard_map[r][c] == ".":
            # blizzards.append((r, c, *DIRECTIONS_MAP[blizzard_map[r][c]]))
            blizzards.append(
                (r, c, DIRECTIONS_MAP[blizzard_map[r][c]][0], DIRECTIONS_MAP[blizzard_map[r][c]][1])
            )  # to appease pypy
# sneaky little elves!
walls.append((-1, 1))
walls.append((len(blizzard_map), len(blizzard_map[0]) - 2))


time_elapsed = 0
reachable = {(0, 1)}
while (len(blizzard_map) - 1, len(blizzard_map[0]) - 2) not in reachable:
    time_elapsed += 1

    new_blizzards = []
    cannot_pass = set(walls)

    # thought I was being clever but turns out there's a possibility even the new position is clipped into a wall :pensive:
    # for r, c, dr, dc in blizzards:
    #     if (dr, dc) == (0, 1):
    #         if (r, c + 1) in walls:
    #             new_blizzards.append((r, 1, 0, 1))
    #         else:
    #             new_blizzards.append((r, c + 1, 0, 1))
    #     elif (dr, dc) == (0, -1):
    #         if (r, c - 1) in walls:
    #             new_blizzards.append((r, len(blizzard_map[0]) - 2, 0, -1))
    #         else:
    #             new_blizzards.append((r, c - 1, 0, -1))
    #     elif (dr, dc) == (1, 0):
    #         if (r + 1, c) in walls:
    #             new_blizzards.append((1, c, 1, 0))
    #         else:
    #             new_blizzards.append((r + 1, c, 1, 0))
    #     elif (dr, dc) == (-1, 0):
    #         if (r - 1, c) in walls:
    #             new_blizzards.append((len(blizzard_map) - 1, c, -1, 0))
    #         else:
    #             new_blizzards.append((r - 1, c, -1, 0))

    for r, c, dr, dc in blizzards:
        r += dr
        c += dc
        if (r, c) in walls:
            r -= dr
            c -= dc
            while (r, c) not in walls:
                r -= dr
                c -= dc
            r += dr
            c += dc
        new_blizzards.append((r, c, dr, dc))
    cannot_pass.update((r, c) for r, c, _, _ in new_blizzards)

    blizzards = new_blizzards

    next_steps = set()
    for row, col in reachable:
        DIRECTIONS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for delta_r, delta_c in DIRECTIONS:
            new_r, new_c = row + delta_r, col + delta_c
            if (new_r, new_c) in cannot_pass:
                continue
            next_steps.add((new_r, new_c))
        if (row, col) not in cannot_pass:
            next_steps.add((row, col))

    reachable = next_steps

print(time_elapsed)

# row, col, grid, time_elapsed, waited_last_turn, visited = queue.pop(0)
# visited.add((row, col))
# if (row, col) == (len(blizzard_map) - 1, len(blizzard_map[0]) - 2):
#     fastest_ways = min(fastest_ways, time_elapsed)
#     continue
# new_grid = defaultdict(list)
# if (row, col) in grid:  # inside a blizzard or wall, break
#     continue
# for pos, list_entries in grid.items():
#     for entry in list_entries:
#         if entry == (0, 0):  # wall
#             new_grid[pos] = [(0, 0)]
#         elif entry == (0, 1):
#             if (pos[0], pos[1] + 1) in grid and grid[(pos[0], pos[1] + 1)] == [(0, 0)]:
#                 new_grid[(pos[0], 1)].append((0, 1))
#             else:
#                 new_grid[(pos[0], pos[1] + 1)].append((0, 1))
#         elif entry == (0, -1):
#             if (pos[0], pos[1] - 1) in grid and grid[(pos[0], pos[1] - 1)] == [(0, 0)]:
#                 new_grid[(pos[0], len(blizzard_map[0]) - 2)].append((0, -1))
#             else:
#                 new_grid[(pos[0], pos[1] - 1)].append((0, -1))
#         elif entry == (-1, 0):
#             if (pos[0] + 1, pos[1]) in grid and grid[(pos[0] + 1, pos[1])] == [(0, 0)]:
#                 new_grid[(1, pos[1])].append((-1, 0))
#             else:
#                 new_grid[(pos[0] + 1, pos[1])].append((-1, 0))
#         elif entry == (1, 0):
#             if (pos[0] - 1, pos[1]) in grid and grid[(pos[0] - 1, pos[1])] == [(0, 0)]:
#                 new_grid[(len(blizzard_map) - 2, pos[1])].append((1, 0))
#             else:
#                 new_grid[(pos[0] - 1, pos[1])].append((1, 0))
# DIRECTIONS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
# for delta_r, delta_c in DIRECTIONS:
#     new_r, new_c = row + delta_r, col + delta_c
#     if (
#         (new_r, new_c) not in visited
#         and 1 <= new_r < len(blizzard_map)
#         and 1 <= new_c < len(blizzard_map[0]) - 1
#         and (new_r, new_c) not in new_grid
#     ):
#         queue.append((new_r, new_c, new_grid, time_elapsed + 1, False, visited))
# if not waited_last_turn:
#     queue.append((row, col, new_grid, time_elapsed + 1, True, visited))

# print(fastest_ways)
