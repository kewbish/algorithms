with open("input.txt") as x:
    p1, p2 = x.read().strip().split("\n\n")
    p1, p2 = [a.split("\n") for a in [p1, p2]]
    p1, p2 = [a[1:] for a in [p1, p2]]
    p1 = [int(p) for p in p1]
    p2 = [int(p) for p in p2]

while p1 and p2:
    p1c = p1.pop(0)
    p2c = p2.pop(0)
    if p1c > p2c:
        p1 += [p1c, p2c]
    elif p2c > p1c:
        p2 += [p2c, p1c]

deck = p2 if p2 else p1

sum = 0
for i, d in enumerate(deck):
    sum += d * (len(deck) - i)

print(sum)
