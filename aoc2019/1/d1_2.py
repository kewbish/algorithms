from math import floor

with open("input.txt") as x:
    lines = x.read().splitlines()
    lines = [int(li) for li in lines]

fuels = []

for li in lines:
    fuel = floor(li / 3) - 2
    fuels.append(fuel)
    while fuel > 6:
        fuel = floor(fuel / 3) - 2
        fuels.append(fuel)

fuels = sum(fuels)
print(fuels)
