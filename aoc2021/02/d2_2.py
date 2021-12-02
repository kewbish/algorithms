with open("input.txt") as x:
    commands = x.readlines()
    commands = [c.split(" ") for c in commands]

x = 0
y = 0
aim = 0
for c in commands:
    if c[0] == "forward":
        x += int(c[1])
        y += aim * int(c[1])
    elif c[0] == "down":
        aim += int(c[1])
    elif c[0] == "up":
        aim -= int(c[1])
    print(x, y, aim)

print(x * y)
