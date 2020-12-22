with open("input.txt") as x:
    p1, p2 = x.read().strip().split("\n\n")
    p1, p2 = [a.split("\n") for a in [p1, p2]]
    p1, p2 = [a[1:] for a in [p1, p2]]
    p1 = [int(p) for p in p1]
    p2 = [int(p) for p in p2]

# look Kaneki I used recursion
def recur_crab(p1, p2):
    seen = set()
    while p1 and p2:
        # True is p1 winning
        strseen = str([p1, p2])
        if strseen in seen:
            return True, p1, p2
        seen.add(strseen)

        p1c = p1.pop(0)
        p2c = p2.pop(0)
        if len(p1) >= p1c and len(p2) >= p2c:
            win, p1d, p2d = recur_crab(p1[:p1c], p2[:p2c])
        else:
            win = p1c > p2c

        if win:
            p1 += [p1c, p2c]
        else:
            p2 += [p2c, p1c]
    return p1, p1, p2

win, p1, p2 = recur_crab(p1, p2)
deck = p1 if win else p2

sum = 0
for i, d in enumerate(deck):
    sum += d * (len(deck) - i)

print(sum)

