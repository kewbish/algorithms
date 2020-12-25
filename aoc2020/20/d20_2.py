from collections import defaultdict
from itertools import combinations

# [mebeim/aoc](github.com/mebeim/aoc/blob/master/2020/README.md)
# oops

with open("input.txt") as x:
    lines = x.read().strip().split("\n\n")
    lines = [li.split("\n") for li in lines]
    blocks = {int(la[0].replace("Tile ", "").replace(":", "")): la[1:] for la in lines}

def edge(block, ed):
    if ed == 'n':
        return block[0]
    elif ed == 's':
        return block[-1]
    elif ed == 'e':
        return "".join([li[-1] for li in block])
    elif ed == 'w':
        return "".join([li[0] for li in block])

def rotate(block):
    nb = []
    for b in range(len(block[0])):
        nr = ''.join(row[b] for row in block)[::-1]
        nb.append(nr)
    return nb

def oriens(block):
    yield block
    for i in range(3):
        block = rotate(block)
        yield block

def arrangs(block):
    yield from oriens(block)
    yield from oriens(block[::-1])

def matching_block(block, blocks, so, st):
    prev = edge(block, so)
    for oid, o in blocks.items():
        if block is o:
            continue
        for o in arrangs(o):
            if prev == edge(o, st):
                blocks.pop(oid)
                return o

def matching_row(prev, blocks, bpr):
    yield prev
    for i in range(bpr - 1):
        b = matching_block(prev, blocks, 'e', 'w')
        prev = b
        yield prev

def strip_edges(block):
    return [row[1:-1] for row in block[1:-1]]

matching = defaultdict(str)
corners = {}
for id1, id2 in combinations(blocks, 2):
    one, two = blocks[id1], blocks[id2]
    for so in 'nsew':
        for st in 'nsew':
            eo, et = edge(one, so), edge(two, st)
            if eo == et or eo == et[::-1]:
                matching[id1] += so
                matching[id2] += st
for bid, ed in matching.items():
    if len(ed) == 2:
        corners[bid] = ed

tlbid, sides = corners.popitem()
tl = blocks[tlbid]
if sides in ('ne', 'en'):
    tl = rotate(tl)
elif sides in ('nw', 'wn'):
    tl = rotate(rotate(tl))
elif sides in ('sw', 'ws'):
    tl = rotate(rotate(rotate(tl)))

imgdm = int(len(blocks) ** 0.5)

blocks.pop(tlbid)

first = tl
image = []

while True:
    ir = matching_row(first, blocks, imgdm)
    ir = map(strip_edges, ir)
    image.extend(map("".join, zip(*ir)))
    if not blocks:
        break
    first = matching_block(first, blocks, 's', 'n')

monster = [(0, 18), (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19), (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)]

for i in arrangs(image):
    n = 0
    for r in range(len(image) - 3):
        for c in range(len(image) - 20):
            if all(i[r + ra][c + ca] == "#" for ra, ca in monster):
                n += 1
    if n != 0:
        break

all_water = sum(r.count("#") for r in image)
print(all_water - n * 15)
