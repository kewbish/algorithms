with open("input.txt") as x:
    buffer = x.readlines()[0]

for i in range(len(buffer) - 4):
    if len(set(buffer[i : i + 4])) == 4:
        print(i + 4)
        break
