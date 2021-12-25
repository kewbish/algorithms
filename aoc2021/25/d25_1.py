from copy import deepcopy

with open("input.txt") as x:
    cucumbers = x.read().splitlines()
    cucumbers = [list(c) for c in cucumbers]

rows = len(cucumbers)
columns = len(cucumbers[0])

step = 0
has_moved = False
while True:
    step += 1
    has_moved = False
    new_cumbers = deepcopy(cucumbers)
    for r in range(rows):
        for c in range(columns):
            if cucumbers[r][c] == ">" and cucumbers[r][(c + 1) % columns] == ".":
                has_moved = True
                new_cumbers[r][c] = "."
                new_cumbers[r][(c + 1) % columns] = ">"
    new_new_cumbers = deepcopy(new_cumbers)
    for r in range(rows):
        for c in range(columns):
            if new_cumbers[r][c] == "v" and new_cumbers[(r + 1) % rows][c] == ".":
                has_moved = True
                new_new_cumbers[r][c] = "."
                new_new_cumbers[(r + 1) % rows][c] = "v"
    cucumbers = new_new_cumbers
    if not has_moved:
        print(step)
        exit(0)
