with open("input.txt") as x:
    lines = x.read().splitlines()
    rules = lines[:20]
    ticket = lines[22]
    nearby = lines[25:]

ruld = {} 
for r in rules:
    f, rules = r.split(": ")
    rules = rules.split(" or ")
    rules = [rule.split("-") for rule in rules]
    ruld[f] = [[int(n) for n in r] for r in rules]
ticket = ticket.split(",")
ticket = [int(t) for t in ticket]
nearby = [n.split(",") for n in nearby]

gset = set()
for r in ruld.values():
    lset = set(range(r[0][0], r[0][1]))
    rset = set(range(r[1][0], r[1][1]))
    gset = gset | lset | rset

inval = []
for n in nearby:
    for i in n:
        i = int(i)
        if i not in gset:
            inval.append(n)
            break

val = []
for n in nearby:
    if n not in inval:
        val.append([int(ni) for ni in n])

vval = []
for i in range(len(nearby[0])):
    vval.append([ticket[i] for ticket in val]) # group by column

final = {}
for i, v in enumerate(vval):
    for j, r in ruld.items():
        if all((r[0][0] <= int(n) <= r[0][1] or r[1][0] <= int(n) <= r[1][1]) for n in v):
            final.setdefault(j, []).append(i)

cf = {} 
for f1 in final:
    for f2 in final:
        overl = set(final[f1]).difference(set(final[f2]))
        if len(overl) == 1:
            cf[f1] = overl.pop()

sum = 1
for i, k in cf.items():
    if i.startswith("departure"):
        sum *= ticket[k]
print(sum)
