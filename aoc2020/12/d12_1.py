with open("input.txt") as x:
    lines = x.read().splitlines()

x, y = 0, 0
dird = { "N": ["W", "E"], "E": ["N", "S"], "S": ["E", "W"], "W": ["S", "N"] }
dire = "E"

for li in lines:
    inst, num = li[:1], int(li[1:])
    if inst == "F":
        inst = dire
    if inst == "N":
        y += num
    elif inst == "E":
        x += num
    elif inst == "S":
        y -= num
    elif inst == "W":
        x -= num
    elif inst == "R":
        for d in range(int(num / 90)):
            dire = dird[dire][1]
    elif inst == "L":
        for d in range(int(num / 90)):
            dire = dird[dire][0]

print(abs(x) + abs(y))
