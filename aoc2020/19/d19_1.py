from re import fullmatch  # apparently match would mess up

with open("input.txt") as x:
    rules, lines = x.read().split("\n\n")
    rules, lines = [arr.split("\n") for arr in [rules, lines]]

ruld = {}
for r in rules:
    ruld[r.split(": ")[0]] = r.split(": ")[1]

finrul = {}
while "0" not in finrul.keys():
    for k, v in ruld.items():
        if v.startswith('"'):
            finrul[k] = v[1]
        else:
            vals = v.split(" ")
            lid = True
            for va in vals:
                if va == "|":
                    continue
                if va not in finrul.keys():
                    lid = False
            if lid:
                r = ""
                for va in vals:
                    if va != "|":
                        r = r + finrul[va]
                    else:
                        r += "|"
                finrul[k] = f"({r})"

valid = [1 if fullmatch(finrul["0"], l) else 0 for l in lines]
print(sum(valid))
