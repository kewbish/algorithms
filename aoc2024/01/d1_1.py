with open("input.txt") as x:
    lines = x.readlines()

n1, n2 = [], []
for line in lines:
    chunks = line.strip().split(" ")
    n1.append(int(chunks[0]))
    n2.append(int(chunks[-1]))

n1 = sorted(n1)
n2 = sorted(n2)

difference = 0

for i in range(len(n1)):
    difference += abs(n1[i] - n2[i])

print(difference)
