with open("input.txt") as x:
    lines = x.readlines()
    lines = [int(x) for x in lines]

i = 0

while i + 25 < len(lines):
    beg = set(lines[i:i + 25])
    target = lines[i + 25]
    if not any((target - num) in beg for num in beg):
        print(target)
        break
    i += 1
