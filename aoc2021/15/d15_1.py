with open("input.txt") as x:
    chitons = x.read().splitlines()
    chitons = [[int(c) for c in list(chiton_row)] for chiton_row in chitons]

# am I leetcoding
rows = len(chitons)
columns = len(chitons[0])

for x in range(1, columns):
    chitons[0][x] += chitons[0][x - 1]
for y in range(1, rows):
    chitons[y][0] += chitons[y - 1][0]
for y in range(1, rows):
    for x in range(1, columns):
        chitons[y][x] += min(chitons[y - 1][x], chitons[y][x - 1])

print(chitons[rows - 1][columns - 1] - chitons[0][0])
