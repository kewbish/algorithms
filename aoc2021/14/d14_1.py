from collections import defaultdict

with open("input.txt") as x:
    polymer, instructions = x.read().split("\n\n")
    instructions = instructions.splitlines()
    mapping = {}
    for ins in instructions:
        key, value = ins.split(" -> ")
        mapping[key] = value

pairs = [polymer[i : i + 2] for i in range(len(polymer) - 1)]

pair_counter = defaultdict(int)
for pair in pairs:
    pair_counter[pair] += 1


def step():
    global pair_counter
    new_counter = defaultdict(int)
    for pair in pair_counter.keys():
        # oh don't you just love having friends who do aoc before you
        new_counter[pair[0] + mapping[pair]] += pair_counter[pair]
        new_counter[mapping[pair] + pair[1]] += pair_counter[pair]
    pair_counter = new_counter


for _ in range(10):
    step()

character_counter = defaultdict(int)
for pair in pair_counter:
    character_counter[pair[0]] += pair_counter[pair]
character_counter[polymer[-1]] += 1
print(max(character_counter.values()) - min(character_counter.values()))
