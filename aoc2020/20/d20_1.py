from collections import defaultdict
from itertools import permutations

with open("input.txt") as x:
    lines = x.read().strip().split("\n\n")
    lines = [li.split("\n") for li in lines]
    blocks = {int(la[0].replace("Tile ", "").replace(":", "")): la[1:] for la in lines}

sides = {}
for b, arr in blocks.items():
    nar = list([arr[0], arr[-1], "".join([row[0] for row in arr]), "".join([row[-1] for row in arr])])
    sides[b] = nar

matches = defaultdict(list)
for i in permutations(sides.keys(), 2): # apparently this exists, thxu itertools
    for ae, ax in enumerate(sides[i[0]]):
        for be, bx in enumerate(sides[i[1]]):
            revax, revbx = ax[::-1], bx[::-1]
            if (ax == bx) or (ax == revbx) or (bx == revax) or (revbx == revax):
                matches[i[0]].append(i[1])

corners = [int(m) for m in matches if len(matches[m]) == 2]
prod = 1
for c in corners:
    prod *= c

print(prod)
