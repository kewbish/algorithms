from re import finditer

with open("input.txt") as x:
    lines = x.readlines()

llines = []
for li in lines:
    llines.append([l.group() for l in finditer("(e)|(w)|(ne)|(nw)|(se)|(sw)", li)])

dirs = {
    # [axial coords](redblobgames.com/grids/hexagons/)
    'e': lambda hx: (hx[0] + 1, hx[1]),
    'w': lambda hx: (hx[0] - 1, hx[1]),
    'ne': lambda hx: (hx[0] + 1, hx[1] - 1),
    'nw': lambda hx: (hx[0], hx[1] - 1),
    'se': lambda hx: (hx[0], hx[1] + 1),
    'sw': lambda hx: (hx[0] - 1, hx[1] + 1),
}

blset = set()
for li in llines:
    hx = (0, 0)
    for la in li:
        hx = dirs[la](hx)
    if hx in blset:
        blset.remove(hx)
    else:
        blset.add(hx)

print(len(blset))

