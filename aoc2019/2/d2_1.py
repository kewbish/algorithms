with open("input.txt") as x:
    line = x.readline().strip()
codes = [int(li) for li in line.split(",")]
codes[1] = 12
codes[2] = 2

for ind in range(0, len(codes), 4):
    if codes[ind] == 1:
        codes[codes[ind+3]] = codes[codes[ind+1]] + codes[codes[ind+2]]
    elif codes[ind] == 2:
        codes[codes[ind+3]] = codes[codes[ind+1]] * codes[codes[ind+2]]
    elif codes[ind] == 99:
        break

print(codes[0])

