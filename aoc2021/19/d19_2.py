from collections import defaultdict
from itertools import product
from itertools import permutations as iter_perms

with open("input.txt") as x:
    scanners = x.read().strip().split("\n\n")
    scanners = [s.split("\n") for s in scanners]
    scanners = [s[1:] for s in scanners]
    beacons = [[tuple(int(x) for x in s.split(",")) for s in scanner] for scanner in scanners]

AXIS_SWAPS = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
NEGATIVES = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]
COMBS = list(product(AXIS_SWAPS, NEGATIVES))


# if I generate *all* the permutations the right 24 must be in there smw !!
def permutations(beacon, pid):
    swap, neg = COMBS[pid]
    return [neg[0] * beacon[swap[0]], neg[1] * beacon[swap[1]], neg[2] * beacon[swap[2]]]


final_positions = set(beacons[0])  # first scanner as SOT
done_scanners = set([0])
not_done_scanners = set([sid for sid in range(1, len(scanners))])

scanner_positions = [None for _ in range(len(scanners))]
scanner_positions[0] = (0, 0, 0)


unknown_pos = {}
for sid in range(len(scanners)):
    for pid in range(48):
        unknown_pos[(sid, pid)] = [permutations(beacon, pid) for beacon in beacons[sid]]

while not_done_scanners:
    found_beacon = None
    for sid in not_done_scanners:
        if found_beacon:
            continue
        good_scan = [
            tuple(
                [
                    pos[0] + scanner_positions[0][0],
                    pos[1] + scanner_positions[0][1],
                    pos[2] + scanner_positions[0][2],
                ]
            )
            for pos in final_positions
        ]
        for pid in range(48):
            unknown_scan = unknown_pos[(sid, pid)]
            counts = defaultdict(int)
            for bid in range(len(beacons[sid])):
                for goodid in range(len(good_scan)):
                    offset_x = good_scan[goodid][0] - unknown_scan[bid][0]
                    offset_y = good_scan[goodid][1] - unknown_scan[bid][1]
                    offset_z = good_scan[goodid][2] - unknown_scan[bid][2]
                    counts[(offset_x, offset_y, offset_z)] += 1
            for (offset_x, offset_y, offset_z), count in counts.items():
                if count >= 12:
                    scanner_positions[sid] = (offset_x, offset_y, offset_z)
                    for pos in unknown_scan:
                        final_positions.add(tuple([pos[0] + offset_x, pos[1] + offset_y, pos[2] + offset_z]))
                    found_beacon = sid
    assert found_beacon
    not_done_scanners.remove(found_beacon)
    done_scanners.add(found_beacon)

scanner_pairs = list(iter_perms(scanner_positions, 2))
max_dist = 0
for pair in scanner_pairs:
    (p1x, p1y, p1z), (p2x, p2y, p2z) = pair
    pair_distance = abs(p1x - p2x) + abs(p1y - p2y) + abs(p1z - p2z)
    max_dist = max(max_dist, pair_distance)
print(max_dist)
