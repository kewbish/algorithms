with open("input.txt") as x:
    lines = x.readlines()
    lines = [int(x) for x in lines]

csum, tar = 0, 177777905
i, j = 0, 0

for i in range(len(lines)):
    for j in range(i, len(lines)):
        # massively inefficient
        if sum(lines[i:j + 1]) == tar:
            rng = lines[i:j + 1]
            print((min(rng) + max(rng)))
            break
    else:
        continue
    break
