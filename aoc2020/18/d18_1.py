from re import sub, findall

with open("input.txt") as x:
    lines = x.read().splitlines()

def samef(exp):
    while "+" in exp or "*" in exp:
        first = findall("^(\d+ [\*\+] \d+)", exp)[0]
        exp = str(eval(first)) + exp[len(first):]
    return eval(exp)

def solve_li(li):
    while "(" in li:
        levels = findall("\(\d+ [\*\+] [\d+|\d+ \[\*\+\] \d+]+\)", li)
        for l in levels:
            li = li.replace(l, str(samef(l[1:-1])))
    return samef(li)

liarr = [solve_li(li) for li in lines]
print(sum(liarr))

