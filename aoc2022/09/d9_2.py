from typing import Tuple, List

with open("input.txt") as x:
    motions = x.readlines()


ropes: List[Tuple[int, int]] = [(0, 0) for _ in range(10)]
visited = set()

DIRECTION_MAP = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
for motion in motions:
    direction, amount = motion.split()
    amount = int(amount)
    for step in range(amount):
        visited.add(ropes[-1])
        ropes[0] = (ropes[0][0] + DIRECTION_MAP[direction][0], ropes[0][1] + DIRECTION_MAP[direction][1])
        for knot in range(1, 10):
            if abs(ropes[knot - 1][0] - ropes[knot][0]) > 1 or abs(ropes[knot - 1][1] - ropes[knot][1]) > 1:
                knot_new_row = ropes[knot][0]
                if ropes[knot - 1][0] < ropes[knot][0]:
                    knot_new_row -= 1
                elif ropes[knot - 1][0] > ropes[knot][0]:
                    knot_new_row += 1
                knot_new_column = ropes[knot][1]
                if ropes[knot - 1][1] < ropes[knot][1]:
                    knot_new_column -= 1
                elif ropes[knot - 1][1] > ropes[knot][1]:
                    knot_new_column += 1
                ropes[knot] = (knot_new_row, knot_new_column)
    visited.add(ropes[-1])


print(len(visited))
