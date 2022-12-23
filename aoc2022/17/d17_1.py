from typing import Set, Tuple

# https://github.com/morgoth1145/advent-of-code/blob/e15277108f39ee8ec4559c872b0ec6d00b80c4c9/2022/17/solution.py


with open("input.txt") as x:
    jet_pattern = x.readline().strip()

ROCK1 = [[True, True, True, True]]
ROCK2 = [[False, True, False], [True, True, True], [False, True, False]]
ROCK3 = [[False, False, True], [False, False, True], [True, True, True]]
ROCK4 = [[True], [True], [True], [True]]
ROCK5 = [[True, True], [True, True]]
ROCKS = [ROCK1, ROCK2, ROCK3, ROCK4, ROCK5]

chamber: Set[Tuple[int, int]] = set((0, c) for c in range(7))
rock_index = 0
jet_index = 0

for _ in range(2022):
    rock = ROCKS[rock_index % 5]
    highest = max(r for r, _ in chamber)
    working_rock = [
        (highest + 3 + len(rock) - i, 2 + j) for i in range(len(rock)) for j in range(len(rock[0])) if rock[i][j]
    ]
    while True:
        right = jet_pattern[jet_index % len(jet_pattern)] == ">"
        jet_index += 1
        try_rock = [(r, c + (1 if right else -1)) for r, c in working_rock]
        if any(c < 0 or c >= 7 for _, c in try_rock) or any(pos in chamber for pos in try_rock):  # can't move
            try_rock = working_rock
        working_rock = try_rock
        try_rock = [(r - 1, c) for r, c in working_rock]
        if any(pos in chamber for pos in try_rock):  # shouldn't keep going down
            chamber.update(working_rock)
            break
        working_rock = try_rock
    rock_index += 1

print(max(r for r, _ in chamber))
