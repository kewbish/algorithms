with open("input.txt") as x:
    instructions = x.readlines()

register = 1
counter = 0
rows = []
current_row = []


def tick():
    global counter
    global current_row
    counter += 1
    if counter - 1 > 0 and (counter - 1) % 40 == 0:
        rows.append(current_row.copy())
        current_row = []
    current_row.append("█" if ((counter - 1) % 40) in range(register - 1, register + 2) else " ")


for instruction in instructions:
    tick()
    if instruction.startswith("addx"):
        tick()
        _, amount = instruction.split()
        amount = int(amount)
        register += amount
rows.append(current_row.copy())

for row in rows:
    print("".join(row))
