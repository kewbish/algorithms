with open("input.txt") as x:
    card, door = x.read().strip().split("\n")
    card, door = [int(n) for n in [card, door]]

csn, dsn = 7, 7 
cls, dls = 0, 0
cx, dx = 1, 1

while cx != card:
    cx *= csn
    cx %= 20201227
    cls += 1

for i in range(cls):
    dx *= door
    dx %= 20201227

print(dx)
