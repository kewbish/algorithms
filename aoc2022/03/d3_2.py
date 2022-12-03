with open("input.txt") as x:
    rucksacks = x.readlines()
    rucksacks_grouped = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]

priorities = 0
for rucksack_group in rucksacks_grouped:
    first = set(c for c in rucksack_group[0])
    second = set(c for c in rucksack_group[1])
    third = set(c for c in rucksack_group[2])
    overlap = first.intersection(second).intersection(third)
    for overlapper in overlap:
        if overlapper.isupper():
            priorities += ord(overlapper) - ord("A") + 1 + 26
        elif overlapper.islower():
            priorities += ord(overlapper) - ord("a") + 1

print(priorities)
