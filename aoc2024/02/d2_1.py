with open("input.txt", "r") as x:
    lines = x.readlines()

lines = [list(map(int, line.strip().split(" "))) for line in lines]

safe = 0
for line in lines:
    if abs(line[0] - line[1]) > 3:
        continue
    is_increasing = line[0] < line[1]
    is_unsafe = False
    for i in range(1, len(line)):
        if (
            abs(line[i] - line[i - 1]) > 3
            or (is_increasing and line[i] <= line[i - 1])
            or (not is_increasing and line[i] >= line[i - 1])
        ):
            is_unsafe = True
            break
    if is_unsafe:
        continue
    safe += 1

print(safe)
