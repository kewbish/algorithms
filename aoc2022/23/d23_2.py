from collections import defaultdict


with open("input.txt") as x:
    grove = x.read().splitlines()
    grove = [[pos for pos in row] for row in grove]

elves = set()
for r in range(len(grove)):
    for c in range(len(grove[0])):
        if grove[r][c] == "#":
            elves.add((r, c))


around_check = [[4, 3, 5], [0, 1, 7], [6, 5, 7], [2, 3, 1]]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
AROUND = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
i = 0
while True:
    i += 1
    propositions = defaultdict(list)
    for elf in elves:
        around_elves = []
        for delta_r, delta_c in AROUND:
            other_elf_r, other_elf_c = elf[0] + delta_r, elf[1] + delta_c
            around_elves.append((other_elf_r, other_elf_c) in elves)
        if not any(around_elves):
            propositions[elf].append(elf)
            continue
        if not any(around_elves[i] for i in around_check[0]):
            propositions[(directions[0][0] + elf[0], directions[0][1] + elf[1])].append(elf)
        elif not any(around_elves[i] for i in around_check[1]):
            propositions[(directions[1][0] + elf[0], directions[1][1] + elf[1])].append(elf)
        elif not any(around_elves[i] for i in around_check[2]):
            propositions[(directions[2][0] + elf[0], directions[2][1] + elf[1])].append(elf)
        elif not any(around_elves[i] for i in around_check[3]):
            propositions[(directions[3][0] + elf[0], directions[3][1] + elf[1])].append(elf)
        else:
            propositions[elf].append(elf)
    new_elves = set()
    for proposition, prop_elves in propositions.items():
        if len(prop_elves) > 1:
            new_elves.update(prop_elves)
        else:
            new_elves.add(proposition)
    if elves == new_elves:
        print(i)
        break
    first = directions.pop(0)
    directions.append(first)
    first = around_check.pop(0)
    around_check.append(first)
    elves = new_elves
