cups = list(input())
cups = [int(c) for c in cups]

for i in range(100):
    nxt = cups[1:4]
    dest = cups[0] - 1
    if dest == 0:
        dest = max(cups)
    while dest in nxt:
        dest -= 1
        if dest == 0:
            dest = max(cups)
    indes = cups.index(dest)
    cups = cups[:indes][4:] + [dest] + nxt + cups[indes + 1:] + [cups[0]]

onein = cups.index(1)
cups = "".join(str(a) for a in (cups[onein + 1:] + cups[:onein]))
print(cups)
