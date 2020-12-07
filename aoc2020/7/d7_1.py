with open("input.txt") as x:
    lines = x.readlines()

bags = {}
paths = 0

for li in lines:
    o, i = li.strip().replace(".", "").split(" bags contain ")
    inlist = i.split(", ")
    val = []
    for inner in inlist:
        if inner != 'no other bags':
            inner = inner.split(" ")
            val.append(f"{inner[0]} {' '.join(inner[1:3])}")
        else:
            val.append('no other')
    bags[o] = val

def rec_check(key, check):
    if any('shiny gold' in k for k in bags[key]):
        return 1
    elif any('no other' in k for k in bags[key]):
        return 0
    for i in bags[key]:
        i = " ".join(i.split(" ")[1:3])
        check += rec_check(i, check)
    return 1 if check else 0

for key in bags:
    if rec_check(key, 0):
        paths += 1

print(paths)
