from typing import FrozenSet, List
from collections import defaultdict
from functools import cache

with open("input.txt") as x:
    valves_ins = x.read().splitlines()
    # https://www.reddit.com/r/adventofcode/comments/zn6k1l/comment/j0fpyu4/?utm_source=share&utm_medium=web2x&context=3

valves = defaultdict(list)
valve_flows = {}
for valve in valves_ins:
    words = valve.split(" ")
    next_valves = [next_valve.replace(",", "") for next_valve in words[9:]]
    valves[words[1]] += next_valves
    valve_flows[words[1]] = int(words[4].replace(";", "").replace("rate=", ""))  # cohesion where


@cache
def findPressure(current: str, visited: FrozenSet[str], time: int, should_repeat: bool) -> int:
    if time <= 0:
        return findPressure("AA", visited, 26, False) if should_repeat else 0

    pressure = 0
    for next_valve in valves[current]:
        pressure = max(pressure, findPressure(next_valve, visited, time - 1, should_repeat))

    if current not in visited and valve_flows[current] != 0:
        new_visited = set(visited)
        new_visited.add(current)
        time -= 1
        new_pressure = time * valve_flows[current]
        for next_valve in valves[current]:
            pressure = max(
                pressure, new_pressure + findPressure(next_valve, frozenset(new_visited), time - 1, should_repeat)
            )

    return pressure


print(findPressure("AA", frozenset(), 26, True))
