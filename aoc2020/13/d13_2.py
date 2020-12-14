with open("input.txt") as x:
    mins, buses = x.readlines()
    buses = {i: int(b) for i, b in enumerate(buses.split(",")) if b != "x"}

cur = -1
nxt = 1

while len(buses) > 0:
    cur += nxt # starts at zero
    for off, bid in [li for li in buses.items()]:
        if cur % bid == (bid - off) % bid:
            nxt *= buses[off] # increase step size for lcm of next bus also
            del buses[off]

print(cur)

