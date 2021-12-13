from collections import defaultdict

with open("input.txt") as x:
    points, instructions = x.read().split("\n\n")
    points = points.splitlines()
    points = [tuple(map(int, point.split(","))) for point in points]
    instructions = instructions.splitlines()
    instructions = [instruction[11:] for instruction in instructions]


def fold_x(visible, axis):
    new_visible = set()
    for x, y in visible:
        new_x = x if x < axis else axis - (x - axis)
        new_visible.add((new_x, y))
    return new_visible


def fold_y(visible, axis):
    new_visible = set()
    for x, y in visible:
        new_y = y if y < axis else axis - (y - axis)
        new_visible.add((x, new_y))
    return new_visible


visible = set()
for point in points:
    visible.add(point)

for ins in instructions:
    direction, axis = ins.split("=")
    axis = int(axis)
    if direction == "x":
        visible = fold_x(visible, axis)
    elif direction == "y":
        visible = fold_y(visible, axis)


largest_x = max(v[0] for v in visible)
largest_y = max(v[1] for v in visible)
display = ""
for y in range(largest_y + 1):
    for x in range(largest_x + 1):
        display += "#" if (x, y) in visible else " "
    display += "\n"
print(display.strip())
