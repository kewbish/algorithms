with open("input.txt") as x:
    octopi = x.read().splitlines()
    octopi = [[int(c) for c in r] for r in octopi]

flashes = 0


def flash(r, c):
    global octopi
    global flashes
    flashes += 1
    octopi[r][c] = 0
    for rc in [-1, 0, 1]:
        for cc in [-1, 0, 1]:
            if 0 <= rc + r < 10 and 0 <= cc + c < 10 and octopi[rc + r][cc + c] != 0:
                octopi[rc + r][cc + c] += 1
                if octopi[rc + r][cc + c] >= 10:
                    flash(rc + r, cc + c)


def step():
    global octopi
    octopi = [[c + 1 for c in r] for r in octopi]
    for r in range(10):
        for c in range(10):
            if octopi[r][c] == 10:
                flash(r, c)


i = 0
while True:
    if all([not c for r in octopi for c in r]):
        break
    step()
    i += 1

print(i)
