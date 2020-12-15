line = input()
lines = line.split(",")

visited = {}
last = int(lines[-1])
for i, li in enumerate(lines):
    if li not in visited:
        visited[int(li)] = i + 1

for i in range(len(lines), 2020):
    if last not in visited:
        visited[last] = i
        last = 0
    else:
        past = i - visited[last]
        visited[last] = i
        last = past

print(last)

