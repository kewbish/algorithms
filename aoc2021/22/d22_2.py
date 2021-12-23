# ignorance was bliss

with open("input.txt") as x:
    raw_instructions = x.read().splitlines()
    instructions = []
    for i in raw_instructions:
        state, ranges = i.split(" ")
        x, y, z = ranges.split(",")
        minx, maxx = x[2:].split("..")
        miny, maxy = y[2:].split("..")
        minz, maxz = z[2:].split("..")
        minx, maxx, miny, maxy, minz, maxz = list(map(int, [minx, maxx, miny, maxy, minz, maxz]))
        instructions.append([state, [minx, maxx], [miny, maxy], [minz, maxz]])


def intersection(cube_1, cube_2):
    for axis_1, axis_2 in zip(cube_1, cube_2):
        if axis_1[0] > axis_2[1] or axis_1[1] < axis_2[0]:
            return None
    return tuple((max(axis_1[0], axis_2[0]), min(axis_1[1], axis_2[1])) for axis_1, axis_2 in zip(cube_1, cube_2))


def difference(cube_1, cube_2):
    intersect = intersection(cube_1, cube_2)
    if not intersect:
        return [cube_1]
    xb1, yb1, zb1 = cube_1
    xb2, yb2, zb2 = intersect
    new_cubes = []
    new_cubes.append((xb1, yb1, (zb1[0], zb2[0] - 1)))
    new_cubes.append((xb1, yb1, (zb2[1] + 1, zb1[1])))
    new_cubes.append(((xb1[0], xb2[0] - 1), yb1, zb2))
    new_cubes.append(((xb2[1] + 1, xb1[1]), yb1, zb2))
    new_cubes.append((xb2, (yb1[0], yb2[0] - 1), zb2))
    new_cubes.append((xb2, (yb2[1] + 1, yb1[1]), zb2))
    return [(x, y, z) for x, y, z in new_cubes if x[0] <= x[1] and y[0] <= y[1] and z[0] <= z[1]]


cubes = []
for i in instructions:
    state, x, y, z = i
    new_cubes = []
    for cube in cubes:
        new_cubes.extend(difference(cube, (x, y, z)))
    if state == "on":
        new_cubes.append((x, y, z))
    cubes = new_cubes


volume = 0
for cube in cubes:
    x, y, z = cube
    volume += (x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1)  # off by one
print(volume)
