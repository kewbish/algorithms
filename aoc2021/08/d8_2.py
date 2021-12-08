from itertools import permutations

with open("input.txt") as x:
    segments = x.read().splitlines()
    segments = [[output.split(" ") for output in s.split(" | ")] for s in segments]

expected = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

total = 0
for digits, challenge in segments:
    d1 = set(list([digit for digit in digits if len(digit) == 2][0]))
    d7 = set(list([digit for digit in digits if len(digit) == 3][0]))
    d4 = set(list([digit for digit in digits if len(digit) == 4][0]))
    d8 = set(list([digit for digit in digits if len(digit) == 7][0]))
    d9 = set(list([digit for digit in digits if len(digit) == 6 and len(set(list(digit)) - set.union(d4, d7)) == 1][0]))
    d0 = set(
        list(
            [digit for digit in digits if len(digit) == 6 and set(list(digit)) != d9 and all(s in digit for s in d7)][0]
        )
    )
    d6 = set(
        list([digit for digit in digits if len(digit) == 6 and set(list(digit)) != d9 and set(list(digit)) != d0][0])
    )
    d3 = set(list([digit for digit in digits if len(digit) == 5 and all(s in digit for s in d7)][0]))
    e = min(d8 - d9)
    d2 = set(list([digit for digit in digits if len(digit) == 5 and e in digit][0]))
    d5 = set(
        list([digit for digit in digits if len(digit) == 5 and set(list(digit)) != d3 and set(list(digit)) != d2][0])
    )

    ds = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]

    n = ""
    for digit in challenge:
        n = n + str(ds.index(set(list(digit))))

    total = total + int(n)

c = 0
for s in segments:
    wirings, output = s
    pone = set([w for w in wirings if len(w) == 2][0])
    pseven = set([w for w in wirings if len(w) == 3][0])
    pfour = set([w for w in wirings if len(w) == 4][0])
    peight = set([w for w in wirings if len(w) == 7][0])
    pnine = set([w for w in wirings if len(w) == 6 and len(set(list(w)) - set.union(pfour, pseven)) == 1][0])
    pthree = set([w for w in wirings if len(w) == 5 and all(seven in w for seven in pseven)][0])
    pzero = set(
        [w for w in wirings if len(w) == 6 and set(list(w)) != pnine and all(seven in w for seven in pseven)][0]
    )
    psix = set([w for w in wirings if len(w) == 6 and set(list(w)) != pnine and set(list(w)) != pzero][0])
    sege = (peight - pnine).pop()
    ptwo = set([w for w in wirings if len(w) == 5 and set(list(w)) != pthree and sege in w][0])
    pfive = set([w for w in wirings if len(w) == 5 and set(list(w)) != pthree and set(list(w)) != ptwo][0])
    plist = [pzero, pone, ptwo, pthree, pfour, pfive, psix, pseven, peight, pnine]
    output = [set(o) for o in output]
    total = (
        1000 * plist.index(output[0])
        + 100 * plist.index(output[1])
        + 10 * plist.index(output[2])
        + plist.index(output[3])
    )
    c += total

print(c)
