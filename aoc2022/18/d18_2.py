with open("input.txt") as x:
    cubes = x.read().splitlines()

cube_set = set()

for cube in cubes:
    cube_set.add(tuple(int(coord) for coord in cube.split(",")))

OFFSETS = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, 1], [0, 0, -1]]

max_x, max_y, max_z = 0, 0, 0
min_x, min_y, min_z = 0, 0, 0
for x, y, z in cube_set:
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    max_z = max(z, max_z)
    min_x = min(x, min_x)
    min_y = min(y, min_y)
    min_z = min(z, min_z)

outside = set()


def reachable(x: int, y: int, z: int):
    if (x, y, z) in cube_set:
        return False

    visited = set()
    queue = [(x, y, z)]
    while queue:
        cube = queue.pop(0)
        x, y, z = cube
        if cube in visited:
            continue
        visited.add(cube)
        if (
            cube in outside
            or x not in range(min_x, max_x + 1)
            or y not in range(min_y, max_y + 1)
            or z not in range(min_z, max_z + 1)
        ):
            outside.update(visited - cube_set)
            return True
        if cube not in cube_set:
            for delta_x, delta_y, delta_z in OFFSETS:
                new_x, new_y, new_z = delta_x + x, delta_y + y, delta_z + z
                queue.append((new_x, new_y, new_z))  # type: ignore


surface_areas = 0
for x, y, z in cube_set:
    for delta_x, delta_y, delta_z in OFFSETS:
        new_x, new_y, new_z = delta_x + x, delta_y + y, delta_z + z
        if reachable(new_x, new_y, new_z):
            surface_areas += 1


print(surface_areas)
