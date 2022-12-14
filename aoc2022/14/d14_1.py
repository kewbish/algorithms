with open("input.txt") as x:
    cave = x.read().splitlines()
    cave = [[ins for ins in caveline.split(" -> ")] for caveline in cave]
    cave = [[[int(coord) for coord in ins.split(",")] for ins in caveline] for caveline in cave]

max_x, max_y = 0, 0
for caveline in cave:
    for ins in caveline:
        max_x = max(ins[0], max_x)
        max_y = max(ins[1], max_y)
cave_grid = [["." for _ in range(max_x + 1)] for __ in range(max_y + 1)]
for caveline in cave:
    for i in range(0, len(caveline) - 1):
        x1, y1 = caveline[i]
        x2, y2 = caveline[i + 1]
        for c in range(min(x1, x2), max(x1, x2) + 1):
            for r in range(min(y1, y2), max(y1, y2) + 1):
                cave_grid[r][c] = "#"


sand = 0
done = False
while True:
    sand_x, sand_y = (500, 0)
    if done or cave_grid[sand_y][sand_x] == "o":
        break
    while True:
        if sand_y + 1 >= len(cave_grid):
            done = True
            break
        elif cave_grid[sand_y + 1][sand_x] == ".":
            sand_y += 1
            continue
        elif 0 <= sand_x - 1 and cave_grid[sand_y + 1][sand_x - 1] == ".":
            sand_x -= 1
            sand_y += 1
            continue
        elif sand_x + 1 < len(cave_grid[0]) and cave_grid[sand_y + 1][sand_x + 1] == ".":
            sand_x += 1
            sand_y += 1
            continue
        else:
            cave_grid[sand_y][sand_x] = "o"  # type: ignore
            sand += 1
            break

print(sand)
