from collections import defaultdict, namedtuple

with open("input.txt") as x:
    caves = defaultdict(list)
    cave_paths = x.read().splitlines()
    for path in cave_paths:
        start, end = path.split("-")
        caves[start].append(end)
        caves[end].append(start)

CaveState = namedtuple("CaveState", ["current", "visited"])
current = CaveState("start", {"start"})
states = [current]

paths = 0
while states:
    current, visited = states[0]
    states = states[1:]
    if current == "end":
        paths += 1
        continue
    for path in caves[current]:
        if path not in visited:
            states.append(CaveState(path, visited.union({path}) if path.islower() else visited))

print(paths)
