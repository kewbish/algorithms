with open("input.txt") as x:
    lines = x.readlines()
    lines = [int(li.strip()) for li in lines]

lines = sorted(lines)
sums = { 1: 0, 3: 0 }
cur = 0

for x in lines:
    sums[x - cur] += 1
    cur = x

print(sums[1] * (sums[3] + 1))
