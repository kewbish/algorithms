from itertools import product

with open("input.txt") as x:
    lines = x.read().splitlines()

def neighbours(state):
    ns = {} 
    for s in state:
        for d in list(product([-1, 0, 1], repeat=4)):
            if d != (0, 0, 0, 0):
                cur = tuple(i + ia for i, ia in zip(s, d))
                if cur not in ns.keys():
                    ns[cur] = 0
                ns[cur] += 1
    return ns

state = set() 
for i, row in enumerate(lines):
    for j, col in enumerate(row):
        if col == "#":
            state.add((i, j, 0, 0))

for i in range(6):
    ns = set() 
    nhb = neighbours(state)
    for coord, v in nhb.items():
        if v == 3 or (v == 2 and coord in state):
            # if 3nhbs or was a and has 2 nbhs (else would remain ia if 2nhbs and ia)
            ns.add(coord)
    state = ns

print(len(state))

