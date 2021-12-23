from collections import defaultdict

with open("input.txt") as x:
    raw_instructions = x.read().splitlines()[:20]
    instructions = []
    for i in raw_instructions:
        state, ranges = i.split(" ")
        x, y, z = ranges.split(",")
        minx, maxx = x[2:].split("..")
        miny, maxy = y[2:].split("..")
        minz, maxz = z[2:].split("..")
        minx, maxx, miny, maxy, minz, maxz = list(map(int, [minx, maxx, miny, maxy, minz, maxz]))
        instructions.append([state, [minx, maxx], [miny, maxy], [minz, maxz]])

cube_states = defaultdict(bool)
for i in instructions:
    state, x, y, z = i
    for xid in range(x[0], x[1] + 1):
        for yid in range(y[0], y[1] + 1):
            for zid in range(z[0], z[1] + 1):
                cube_states[(xid, yid, zid)] = True if state == "on" else False

print(len(list(filter(lambda k: k == True, cube_states.values()))))
