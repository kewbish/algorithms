with open("input.txt") as x:
    lines = x.readlines()

num = 0

for l in lines:
    no, ch, pwd = l.split()
    low, high = no.split("-")
    ch = ch.strip(":")
    if pwd.count(ch) <= int(high) and pwd.count(ch) >= int(low):
        num += 1

print(num)
