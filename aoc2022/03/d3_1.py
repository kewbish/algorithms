with open("input.txt") as x:
    rucksacks = x.readlines()

priorities = 0
for rucksack in rucksacks:
    overlap = set()
    first, second = rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]
    for item in first:
        if item in second:
            overlap.add(item)
    for overlapper in overlap:
        if overlapper.isupper():
            priorities += ord(overlapper) - ord("A") + 1 + 26
        elif overlapper.islower():
            priorities += ord(overlapper) - ord("a") + 1

print(priorities)
