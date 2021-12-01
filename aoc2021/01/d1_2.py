with open("input.txt") as x:
    lines = x.readlines()
    levels = [int(line) for line in lines]

sump = 0
c = 0
for i, l in enumerate(levels[:-2]):
    if i == 0:
        continue
    prev1 = levels[i - 1] if i - 1 >= 0 else 0
    prev2 = levels[i + 1] if i + 1 <= len(levels) else 0
    nsum = prev1 + prev2 + l
    if nsum > sump:
        c += 1
    sump = nsum

print(c)
