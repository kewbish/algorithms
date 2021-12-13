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


def fold_y(visible, axis):  # wanted to try with test input
    new_visible = set()
    for x, y in visible:
        new_y = y if y < axis else axis - (y - axis)
        new_visible.add((x, new_y))
    return new_visible


visible = set()
for point in points:
    visible.add(point)

ins = instructions[0]
direction, axis = ins.split("=")
axis = int(axis)
if direction == "x":
    visible = fold_x(visible, axis)
    print(len(visible))
elif direction == "y":
    visible = fold_y(visible, axis)
    print(visible)
    print(len(visible))
