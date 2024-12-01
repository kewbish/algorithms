from collections import Counter, defaultdict


with open("input.txt") as x:
    lines = x.readlines()

n1, n2 = [], []
for line in lines:
    chunks = line.strip().split(" ")
    n1.append(int(chunks[0]))
    n2.append(int(chunks[-1]))

similarity = 0
n2_counts = Counter(n2)
for i in range(len(n1)):
    similarity += n1[i] * n2_counts[n1[i]]

print(similarity)
