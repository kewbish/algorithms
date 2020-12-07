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
    if any('no other' in k for k in bags[key]):
        return 1 # this is just early return (0 + 1) => 1 
    for i in bags[key]:
        i = i.split(" ")
        check += (int(i[0]) * rec_check(" ".join(i[1:3]), 0))
        # trust the natural recursion
    return check + 1 # + new level

for key in bags:
    if key == "shiny gold":
        paths = rec_check(key, 0) - 1 # undo addition from final line of rec_check

print(paths)

