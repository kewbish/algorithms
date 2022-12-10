with open("input.txt") as x:
    instructions = x.readlines()

signal_strengths = 0
register = 1
counter = 0


def tick():
    global counter
    global signal_strengths
    counter += 1
    if counter >= 20 and (counter - 20) % 40 == 0:
        signal_strengths += register * counter


for instruction in instructions:
    tick()
    if instruction.startswith("addx"):
        tick()
        _, amount = instruction.split()
        amount = int(amount)
        register += amount

print(signal_strengths)
