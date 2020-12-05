with open("input.txt") as x:
    lines = x.readlines()

highest = 0
missing = 0
ids = []

for coded in lines:
    rows = list(range(128))
    cols = list(range(8))
    for i in coded:
        if i == "F":
            rows = rows[:len(rows)//2]
        elif i == "B":
            rows = rows[len(rows)//2:]
        elif i == "L":
            cols = cols[:len(cols)//2]
        elif i == "R":
            cols = cols[len(cols)//2:]
    id = rows[0] * 8 + cols[0]
    if id > highest:
        highest = id
    ids.append(id)

for i in range(min(ids), max(ids)):
    if i not in ids and i > 8 and i < 1024:
        missing = i

print(missing)
