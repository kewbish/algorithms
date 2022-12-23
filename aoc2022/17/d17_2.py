from collections import defaultdict
from typing import Set, Tuple, List

# https://github.com/morgoth1145/advent-of-code/blob/e15277108f39ee8ec4559c872b0ec6d00b80c4c9/2022/17/solution.py


with open("input.txt") as x:
    jet_pattern = x.readline().strip()

ROCK1 = [[True, True, True, True]]
ROCK2 = [[False, True, False], [True, True, True], [False, True, False]]
ROCK3 = [[False, False, True], [False, False, True], [True, True, True]]
ROCK4 = [[True], [True], [True], [True]]
ROCK5 = [[True, True], [True, True]]
ROCKS = [ROCK1, ROCK2, ROCK3, ROCK4, ROCK5]
NUM = 1_000_000_000_000  # the elephants need to check their expectations :skull:

chamber: Set[Tuple[int, int]] = set((0, c) for c in range(7))
rock_index = 0
jet_index = 0
cache = defaultdict(list)

Rock = List[Tuple[int, int]]  # TIL!


def get_rock(rock_index: int, jet_index: int, working_rock: Rock) -> Tuple[Rock, Rock]:
    right = jet_pattern[jet_index % len(jet_pattern)] == ">"
    try_rock = [(r, c + (1 if right else -1)) for r, c in working_rock]
    if any(c < 0 or c >= 7 for _, c in try_rock) or any(pos in chamber for pos in try_rock):  # can't move
        try_rock = working_rock
    working_rock = try_rock
    try_rock = [(r - 1, c) for r, c in working_rock]
    return (try_rock, working_rock)


def rock_to_list(rock_index: int) -> Rock:
    rock = ROCKS[rock_index % 5]
    highest = max(r for r, _ in chamber)
    working_rock = [
        (highest + 3 + len(rock) - i, 2 + j) for i in range(len(rock)) for j in range(len(rock[0])) if rock[i][j]
    ]
    return working_rock


def simulate_chamber(chamber: Set[Tuple[int, int]], start_index: int, jet_index: int, remaining: int):
    for rock_index in range(start_index, remaining):
        working_rock = rock_to_list(rock_index)
        while True:
            try_rock, working_rock = get_rock(rock_index, jet_index, working_rock)
            jet_index += 1
            if any(pos in chamber for pos in try_rock):  # shouldn't keep going down
                chamber.update(working_rock)
                break
            working_rock = try_rock
    return chamber


for rock_index in range(NUM):
    start_key = (rock_index % 5, jet_index % len(jet_pattern))
    working_rock = rock_to_list(rock_index)
    move_x, move_y = 0, 0
    flag = True

    while flag:
        right = jet_pattern[jet_index % len(jet_pattern)] == ">"
        try_rock, working_rock = get_rock(rock_index, jet_index, working_rock)
        move_x += 1 if right else -1
        jet_index += 1
        if any(pos in chamber for pos in try_rock):  # shouldn't keep going down
            chamber.update(working_rock)

            key = (start_key, move_x, move_y)
            now_highest = max(r for r, _ in chamber)
            layout = tuple(max(r - now_highest for r, c in chamber if c == tc) for tc in range(7))
            stats = (now_highest, rock_index, layout)

            move_cache = cache[key]
            if len(move_cache) > 1:
                last_diff = move_cache[-1][0] - move_cache[-2][0]
                current_diff = now_highest - move_cache[-1][0]
                last_move_diff = move_cache[-1][1] - move_cache[-2][1]
                current_move_diff = rock_index - move_cache[-1][1]
                last_layout = move_cache[-1][2]

                if current_diff == last_diff and current_move_diff == last_move_diff:
                    remaining = NUM - rock_index - 1

                    cycle_length = rock_index - move_cache[-1][1]
                    cycles = remaining // cycle_length
                    jumpahead = cycle_length * cycles
                    future_tower = simulate_chamber(chamber, rock_index + 1 + jumpahead, jet_index, NUM)

                    print(max(r for r, _ in chamber) + current_diff * cycles)
                    flag = False

            move_cache.append(stats)
            break

        move_y -= 1
        working_rock = try_rock

    if not flag:
        break
