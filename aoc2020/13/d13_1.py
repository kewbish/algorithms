with open("input.txt") as x:
    mins, buses = x.readlines()
    mins = int(mins)
    buses = [int(b) for b in buses.split(",") if b != "x"]

towait = [[b, b - (mins % b)] for b in buses]
s_towait = sorted(towait, key=lambda x: x[1])

print(s_towait[0][0] * s_towait[0][1])
