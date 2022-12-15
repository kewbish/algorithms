from collections import defaultdict
from typing import List


class Beacon:
    x: int = 0
    y: int = 0
    closest_x: int = 0
    closest_y: int = 0

    def __init__(self, input: str) -> None:
        input = input.replace(":", "")
        input = input.replace(",", "")
        words = input.split(" ")
        self.x = int(words[2].split("=")[1])
        self.y = int(words[3].split("=")[1])
        self.closest_x = int(words[8].split("=")[1])
        self.closest_y = int(words[9].split("=")[1])


with open("input.txt") as x:
    beacons_ins = x.read().splitlines()
    beacons = [Beacon(ins) for ins in beacons_ins]

Y = 2000000
beacon_og = set()
intervals = []

for beacon in beacons:
    if beacon.closest_y == Y:
        beacon_og.add((beacon.closest_y, beacon.closest_x))
    distance = abs(beacon.closest_x - beacon.x) + abs(beacon.closest_y - beacon.y)
    offset = distance - abs(beacon.y - Y)
    if offset < 0:
        continue
    intervals.append([beacon.x - offset, beacon.x + offset])

# is it stealing code if I'm stealing from myself
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    result = [intervals[0]]

    for start, end in intervals[1:]:
        running_end = result[-1][1]
        if start <= running_end:
            result[-1][1] = max(running_end, end)
        else:
            result.append([start, end])

    return result


count = sum(high - low + 1 for low, high in merge(intervals))
print(count - len(beacon_og))
