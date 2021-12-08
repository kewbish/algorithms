with open("input.txt") as x:
    segments = x.read().splitlines()
    segments = [[output.split(" ") for output in s.split(" | ")] for s in segments]

c = 0
for s in segments:
    outputs = s[1]
    for o in outputs:
        if len(o) in [2, 4, 3, 7]:
            c += 1

print(c)
