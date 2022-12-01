with open("./input.txt") as x:
    elves = x.read().split("\n\n")

calories = []
for elf in elves:
    calories.append(sum(map(int, elf.split())))

print(max(calories))
