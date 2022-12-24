from collections import defaultdict

with open("input.txt") as x:
    valves_ins = x.read().splitlines()

valves = defaultdict(list)
valve_flows = {}
for valve in valves_ins:
    words = valve.split(" ")
    next_valves = [next_valve.replace(",", "") for next_valve in words[9:]]
    valves[words[1]] += next_valves
    valve_flows[words[1]] = int(words[4].replace(";", "").replace("rate=", ""))  # cohesion where


queue = []
queue.append(["AA", [], 0])  # current valve, visited, current pressure
cache = {}

for t in range(30):
    new_queue = []
    for current, visited, pressure in queue:
        key = (current, "".join(visited))
        if key in cache and pressure <= cache[key]:
            continue

        cache[key] = pressure

        if current not in visited and valve_flows[current] != 0:
            new_queue.append([current, visited + [current], pressure + valve_flows[current] * (30 - t - 1)])
        for next_valve in valves[current]:
            new_queue.append([next_valve, visited, pressure])

    queue = new_queue

max_pressure = max(pressure for _, _, pressure in queue)

print(max_pressure)
