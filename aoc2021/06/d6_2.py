with open("input.txt") as x:
    fish = x.read().strip().split(",")
    fish = [int(f) for f in fish]

num_at_each = [0] * 9

for f in fish:
    num_at_each[f] += 1

for _ in range(256):
    new_fish = [0] * 9
    for i in range(1, 9):
        new_fish[i - 1] = num_at_each[i]
    new_fish[8] += num_at_each[0]
    new_fish[6] += num_at_each[0]
    num_at_each = new_fish

print(sum(num_at_each))
