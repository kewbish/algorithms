with open("input.txt") as x:
    cubes = x.read().splitlines()
    cubes = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""".splitlines()

cube_set = set()

for cube in cubes:
    cube_set.add(tuple(int(coord) for coord in cube.split(",")))

surface_areas = 0

for x, y, z in cube_set:
    OFFSETS = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, 1], [0, 0, -1]]
    for delta_x, delta_y, delta_z in OFFSETS:
        new_x, new_y, new_z = delta_x + x, delta_y + y, delta_z + z
        if (new_x, new_y, new_z) not in cube_set:
            surface_areas += 1

print(surface_areas)
