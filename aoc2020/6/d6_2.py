with open("input.txt") as x:
    lines = x.read().strip().split("\n\n")

sum = 0

for line in lines:
    lg = line.split("\n")
    unique = set(lg[0])
    for la in lg[1:]:
        unique = unique.intersection(set(la))
    sum += len(unique) 

print(sum)

