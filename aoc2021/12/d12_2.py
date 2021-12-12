from collections import defaultdict, namedtuple

with open("input.txt") as x:
    caves = defaultdict(list)
    cave_paths = x.read().splitlines()
    for path in cave_paths:
        start, end = path.split("-")
        caves[start].append(end)
        caves[end].append(start)

CaveState = namedtuple("CaveState", ["current", "visited", "twice_visited"])
current = CaveState("start", {"start"}, False)
states = [current]

paths = 0
while states:
    current, visited, twice_visited = states.pop(0)  # rotating arrays is slow apparently
    if current == "end":
        paths += 1
        continue
    for path in caves[current]:
        if path not in visited:
            states.append(CaveState(path, visited.union({path}) if path.islower() else visited, twice_visited))
        elif path in visited and path != "start" and path != "end" and not twice_visited:
            states.append(CaveState(path, visited, path))

print(paths)
