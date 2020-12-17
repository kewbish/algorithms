with open("input.txt") as x:
    lines = x.read().splitlines()
    rules = lines[:20]
    ticket = lines[22]
    nearby = lines[25:]

rularr = {} 
for r in rules:
    f, rules = r.split(": ")
    rules = rules.split(" or ")
    rules = [rule.split("-") for rule in rules]
    ruld[f] = [[int(n) for n in r] for r in rules]
ticket = [t.split(",") for t in ticket]
nearby = [n.split(",") for n in nearby]

gset = set()
for r in rularr:
    lset = set(range(r[0][0], r[0][1]))
    rset = set(range(r[1][0], r[1][1]))
    gset = gset | lset | rset

inval = []
for n in nearby:
    for i in n:
        i = int(i)
        if i not in gset:
            inval.append(i)

print(sum(inval))
