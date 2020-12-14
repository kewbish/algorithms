with open(r'input.txt', 'r') as f:
    input = list(map(int, f.read().strip().split()))

fuel = [0, 0]
for mass in input:
    fuel[0] += int(mass/3-2)

for mass in input:
    while int(mass/3-2) > 0:
        mass = int(mass/3-2)
        fuel[1] += mass
print(fuel)
