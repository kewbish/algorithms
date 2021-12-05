from collections import defaultdict

with open("input.txt") as x:
    pipes = x.read().splitlines()
    pipes = [[int(coords) for coords in p.replace(" -> ", ",").split(",")] for p in pipes]

touched = defaultdict(int)
for p in pipes:
    if p[0] == p[2]:  # vertical line
        if p[1] < p[3]:  # go down
            for y in range(p[1], p[3] + 1):
                touched[(p[0], y)] += 1
        else:  # go up
            for y in range(p[3], p[1] + 1):
                touched[(p[0], y)] += 1
    elif p[1] == p[3]:  # horizontal line
        if p[0] < p[2]:  # go right
            for x in range(p[0], p[2] + 1):
                touched[(x, p[1])] += 1
        else:  # go left
            for x in range(p[2], p[0] + 1):
                touched[(x, p[1])] += 1
    else:  # diagonal line
        dx = 1 if p[2] - p[0] > 0 else -1
        dy = 1 if p[3] - p[1] > 0 else -1
        x = p[0]
        y = p[1]
        while x != p[2] and y != p[3]:
            touched[(x, y)] += 1
            x += dx
            y += dy
        touched[(p[2], p[3])] += 1


sump = len(list(filter(lambda t: t >= 2, touched.values())))
print(sump)
