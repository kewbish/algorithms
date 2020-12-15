with open("input.txt") as x:
    lines = x.read().splitlines()

mask = {} 
mem = {}

for li in lines:
    if li.startswith("mask"):
        mask = {}
        msk = list(li.split(" = ")[1])
        for i, mch in enumerate(msk):
            if mch == "X":
                continue
            else:
                mask[i] = mch
    if not li.startswith("mask"):
        loc, dec = li.split(" = ")
        loc = int(loc.replace("mem[", "").replace("]", ""))
        dec = int(dec)
        binary = list("{0:036b}".format(dec))
        for k in mask.keys():
            binary[k] = mask[k]
        mem[loc] = int("".join(binary), 2)

print(sum(mem.values()))
        
