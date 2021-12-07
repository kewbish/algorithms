from collections import defaultdict

with open("input.txt") as x:
    crabs = x.read().strip().split(",")
    crabs = [int(c) for c in crabs]

fuel = defaultdict(int)
for i in range(min(crabs), max(crabs)):
    fuel[i] = sum([abs(c - i) for c in crabs])

print(min(fuel.items(), key=lambda f: f[1])[1])
