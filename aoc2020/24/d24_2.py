from re import finditer

dirs = {
    # [axial coords](redblobgames.com/grids/hexagons/)
    'e': lambda hx: (hx[0] + 1, hx[1]),
    'w': lambda hx: (hx[0] - 1, hx[1]),
    'ne': lambda hx: (hx[0] + 1, hx[1] - 1),
    'nw': lambda hx: (hx[0], hx[1] - 1),
    'se': lambda hx: (hx[0], hx[1] + 1),
    'sw': lambda hx: (hx[0] - 1, hx[1] + 1),
}

def nbhs(hx):
    return set({mv(hx) for mv in dirs.values()})

def bnbhs(hx):
    return len(nbhs(hx).intersection(blset))

with open("input.txt") as x:
    lines = x.readlines()

llines = []
for li in lines:
    llines.append([l.group() for l in finditer("(e)|(w)|(ne)|(nw)|(se)|(sw)", li)])

blset = set()
for li in llines:
    hx = (0, 0)
    for la in li:
        hx = dirs[la](hx)
    if hx in blset:
        blset.remove(hx)
    else:
        blset.add(hx)

for i in range(100):
    nblset = set()
    tonbh = set()
    for hx in blset:
        tonbh.update(nbhs(hx))
    for hx in tonbh:
        if hx in blset and bnbhs(hx) in [1, 2]:
            nblset.add(hx)
        elif bnbhs(hx) == 2:
            nblset.add(hx)
    blset = nblset

print(len(blset))
