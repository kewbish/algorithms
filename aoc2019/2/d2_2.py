def run_prog(i, j):
    with open("input.txt") as x:
        line = x.readline().strip()
    codes = [int(li) for li in line.split(",")]
    codes[1] = i
    codes[2] = j

    for ind in range(0, len(codes), 4):
        if codes[ind] == 1:
            codes[codes[ind+3]] = codes[codes[ind+1]] + codes[codes[ind+2]]
        elif codes[ind] == 2:
            codes[codes[ind+3]] = codes[codes[ind+1]] * codes[codes[ind+2]]
        elif codes[ind] == 99:
            break

    return codes[0]

for i in range(100):
    for j in range(100):
        res = run_prog(i, j)
        if res == 19690720:
            print(100 *i + j)
            break

