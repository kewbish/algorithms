from collections import defaultdict
from typing import Tuple

# my own BFS was wonky (maybe because I was trying to backtrack lol), works cited: https://www.reddit.com/r/adventofcode/comments/zu28ij/comment/j1grx6c/?utm_source=share&utm_medium=web2x&context=3

with open("input.txt") as x:
    blizzard_map = x.read().splitlines()
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


def journey(starting: Tuple[int, int], target: Tuple[int, int]):
    global blizzards  # can just update one state since we journey immediately back

    time_elapsed = 0
    reachable = {starting}
    while target not in reachable:
        time_elapsed += 1

        new_blizzards = []
        cannot_pass = set(walls)

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

    return time_elapsed


print(
    journey((0, 1), (len(blizzard_map) - 1, len(blizzard_map[0]) - 2))
    + journey((len(blizzard_map) - 1, len(blizzard_map[0]) - 2), (0, 1))
    + journey((0, 1), (len(blizzard_map) - 1, len(blizzard_map[0]) - 2))
)
