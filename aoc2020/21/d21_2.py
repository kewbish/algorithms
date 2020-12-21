with open("input.txt") as x:
    lines = x.read().splitlines()
    lines = [li.strip() for li in lines]

alr = {}
ings = set()
allr = []

for li in lines:
    ing, alg = li.split(" (contains ")
    ing = ing.split()
    ings |= set(ing)
    allr += ing
    alg = alg.replace(")", "")
    alg = alg.split(", ")
    for a in alg:
        alr[a] = set.intersection(alr[a], set(ing)) if a in alr else set(ing)

while sum(len(a) for a in alr.values()) != len(alr):
    given = [a for a in alr.values() if len(a) == 1]
    for g in given:
        (v, ) = g 
        for oth in alr.values():
            if v in oth and len(oth) != 1:
                oth.remove(v)

alph = [k for k in sorted(alr.keys())]
print(",".join(["".join(list(alr[a])) for a in alph]))
