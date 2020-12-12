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
            cch = lines[r + r_a][c + c_a]
            mltp = 1
            while 0 <= r + mltp * r_a <= rows - 1 and 0 <= c + mltp * c_a <= cols - 1:
                if cch != ".":
                    break
                else:
                    cch = lines[r + mltp * r_a][c + mltp * c_a]
                    mltp += 1
            x += 1 if cch == "#" else 0
    return x

while True: 
    last = [] 
    for r, row in enumerate(lines):
        nr = ""
        for c, seat in enumerate(row):
            nhb = neighbours(lines, r, c)
            if seat == "L" and nhb == 0:
                nr += "#"
            elif seat == "#" and nhb >= 5:
                nr += "L"
            else:
                nr += lines[r][c]
        last.append(nr)
    last = [list(li) for li in last]
    if lines == last:
        break
    lines = last
    # print("\n".join("".join(li) for li in lines), "---")
    # ^ use above if you want cool visualization idk it was for debugging at first but it looked v cool so I left it in

fintot = sum(x.count("#") for x in lines)
print(fintot)
