from itertools import product

with open("input.txt") as x:
    lines = x.read().splitlines()

mask = {} 
mem = {}

def combinations(addrs):
    alls = []
    inds = [i for i, c in enumerate(addrs) if c == "X"]
    for t in product("01", repeat=len(inds)):
        for i, c in zip(inds, t):
            addrs[i] = c
        alls.append("".join(addrs))
    return alls

for li in lines:
    if li.startswith("mask"):
        mask = {}
        msk = list(li.split(" = ")[1])
        for i, mch in enumerate(msk):
            mask[i] = mch
    if not li.startswith("mask"):
        loc, dec = li.split(" = ")
        loc = int(loc.replace("mem[", "").replace("]", ""))
        dec = int(dec)
        binary = list("{0:036b}".format(loc))
        for i, k in mask.items():
            if k == "0":
                continue
            elif k == "1":
                binary[i] = "1" 
            elif k == "X":
                binary[i] = "X"
        combs = combinations(binary)
        for c in combs:
            mem[int(c, 2)] = dec

print(sum(mem.values()))

