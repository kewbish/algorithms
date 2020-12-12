with open("input.txt") as x:
    lines = x.read().splitlines()

x, y = 0, 0
wx, wy = 10, 1 

for li in lines:
    inst, num = li[:1], int(li[1:])
    if inst == "F":
        x += wx * num
        y += wy * num
    if inst == "N":
        wy += num
    elif inst == "E":
        wx += num
    elif inst == "S":
        wy -= num
    elif inst == "W":
        wx -= num
    elif inst == "R":
        while num > 0:
            wx, wy = wy, -wx # why did I think trig was involved => even if i used trig it woulda ended up like this
            num -= 90
    elif inst == "L":
        while num > 0:
            wx, wy = -wy, wx
            num -= 90

print(abs(x) + abs(y))

