with open("input.txt") as x:
    lines = x.readlines()
    levels = [int(line) for line in lines]

prev = levels[0]
c = 0
for l in levels:
    if l > prev:
        c += 1
    prev = l

print(c)
