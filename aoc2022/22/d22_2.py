# https://github.com/morgoth1145/advent-of-code/blob/da432e32c212831fcbb6c8ae000407b63912ec24/2022/22/solution.py

from typing import Dict, Tuple


with open("input.txt") as x:
    path_map, instructions = x.read().split("\n\n")
    path_map = path_map.split("\n")
    max_width = max(len(path) for path in path_map)
    path_map = [path.ljust(max_width) for path in path_map]

grid = {}
row, col = -1, -1
for r in range(len(path_map)):
    for c in range(len(path_map[0])):
        if path_map[r][c] in ".#":
            if row == -1 and col == -1:
                row = r
                col = c
            grid[(r, c)] = path_map[r][c]

path = []
last_step = ""
for char in instructions:
    if char in "LR":
        path += [int(last_step), char]
        last_step = ""
    else:
        last_step += char
if last_step:
    path.append(int(last_step))

dc = 1
dr = 0

facing: Dict[Tuple[int, int], int] = {(0, 1): 0, (0, -1): 2, (1, 0): 1, (-1, 0): 3}

# let's pretend I divined the same thing
def wrap(x: int, y: int, dx: int, dy: int) -> Tuple[int, int, int, int]:
    if dx == 1:
        if x == 150:
            return 100, 151 - y, -1, 0
        if x == 100:
            if 51 <= y <= 100:
                return 100 + (y - 50), 50, 0, -1
            if 101 <= y <= 150:
                return 150, 51 - (y - 100), -1, 0
        if x == 50:
            return 50 + (y - 150), 150, 0, -1
    elif dx == -1:
        if x == 51:
            if 1 <= y <= 50:
                return 1, 151 - y, 1, 0
            if 51 <= y <= 100:
                return y - 50, 101, 0, 1
        if x == 1:
            if 101 <= y <= 150:
                return 51, 1 + (150 - y), 1, 0
            if 151 <= y <= 200:
                return y - 150 + 50, 1, 0, 1
    elif dy == 1:
        if y == 50:
            return 100, x - 50, -1, 0
        if y == 150:
            return 50, x + 100, -1, 0
        if y == 200:
            return x + 100, 1, 0, 1
    else:
        if y == 1:
            if 51 <= x <= 100:
                return 1, x + 100, 1, 0
            if 101 <= x <= 150:
                return x - 100, 200, 0, -1
        if y == 101:
            return 51, x + 50, 1, 0
    return -1, -1, -1, -1


for instruction in path:
    if isinstance(instruction, int):
        for _ in range(instruction):
            new_r, new_c = row + dr, col + dc
            cell = grid.get((new_r, new_c))
            if not cell:
                # change of basis!
                new_c, new_r, new_dc, new_dr = wrap(col + 1, row + 1, dc, dr)
                new_r -= 1
                new_c -= 1

                cell = grid.get((new_r, new_c))
                if cell == "#":
                    break

                row, col = new_r, new_c
                dr, dc = new_dr, new_dc
            elif grid.get((new_r, new_c)) == "#":
                break
            row, col = new_r, new_c
    elif instruction == "L":
        dr, dc = -dc, dr
    else:
        dr, dc = dc, -dr

print(1000 * (row + 1) + 4 * (col + 1) + facing[(dr, dc)])
