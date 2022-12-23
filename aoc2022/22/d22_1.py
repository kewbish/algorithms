# works cited: https://github.com/morgoth1145/advent-of-code/blob/da432e32c212831fcbb6c8ae000407b63912ec24/2022/22/solution.py

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

for instruction in path:
    if isinstance(instruction, int):
        for _ in range(instruction):
            new_r, new_c = row + dr, col + dc
            if not grid.get((new_r, new_c)):
                cur_row, cur_col = row, col
                while (cur_row, cur_col) in grid:
                    new_r, new_c = cur_row, cur_col
                    cur_row -= dr
                    cur_col -= dc
            elif grid.get((new_r, new_c)) == "#":
                break
            row, col = new_r, new_c
    elif instruction == "L":
        # rotation matrix!
        dr, dc = -dc, dr
    else:
        dr, dc = dc, -dr

print(1000 * (row + 1) + 4 * (col + 1) + facing[(dr, dc)])
