with open("input.txt") as x:
    lines = x.read().split("\n\n")

sum = 0

for line in lines:
    line = line.replace("\n", "")
    unique = "".join(set(line))
    sum += len(unique) 

print(sum)
