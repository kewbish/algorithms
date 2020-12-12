with open("input.txt") as x:
    lines = x.read().splitlines()
    rows = len(lines)
    cols = len(lines[0])
    lines = [list(li) for li in lines]

def neighbours(lines, r, c):
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1)]
    x = 0
    for r_a, c_a in dirs:
        if 0 <= r + r_a <= rows - 1 and 0 <= c + c_a <= cols - 1:
            x += 1 if lines[r + r_a][c + c_a] == "#" else 0
    return x

while True: 
    last = [] 
    for r, row in enumerate(lines):
        nr = ""
        for c, seat in enumerate(row):
            nhb = neighbours(lines, r, c)
            if seat == "L" and nhb == 0:
                nr += "#"
            elif seat == "#" and nhb >= 4:
                nr += "L"
            else:
                nr += lines[r][c]
        last.append(nr)
    last = [list(li) for li in last]
    if lines == last:
        break
    lines = last

fintot = sum(x.count("#") for x in lines)
print(fintot)
