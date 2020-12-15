line = input()
lines = line.split(",")

visited = {}
last = int(lines[-1])
for i, li in enumerate(lines):
    if li not in visited:
        visited[int(li)] = i + 1

for i in range(len(lines), 30000000):
    if last not in visited:
        visited[last] = i
        last = 0
    else:
        past = i - visited[last]
        visited[last] = i
        last = past
    if i % 1000000 == 0:
        print("This is fine ✨")

print(last)


