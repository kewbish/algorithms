with open("input.txt") as x:
    fish = x.read().strip().split(",")
    fish = [int(f) for f in fish]

for _ in range(80):
    nf = []
    for f in fish:
        if f == 0:
            nf += [8, 6]  # new fish, old fish
        else:
            nf.append(f - 1)
    fish = nf

print(len(fish))
