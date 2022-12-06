with open("input.txt") as x:
    buffer = x.readlines()[0]

for i in range(len(buffer) - 14):
    if len(set(buffer[i : i + 14])) == 14:
        print(i + 14)
        break
