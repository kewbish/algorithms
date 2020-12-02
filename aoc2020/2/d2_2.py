with open("input.txt") as x:
    lines = x.readlines()

num = 0

for l in lines:
    no, ch, pwd = l.split()
    pos1, pos2 = no.split("-")
    pos1, pos2 = [int(p) for p in (pos1, pos2)]
    ch = ch.strip(":")
    if (pwd[pos1 - 1] == ch) != (pwd[pos2 - 1] == ch):
        num += 1

print(num)
