with open("input.txt", "r") as x:
    lines = x.readlines()

lines = [list(map(int, line.strip().split(" "))) for line in lines]


safe = 0
for line in lines:
    for i in range(len(line)):
        new_line = line[:i] + line[i + 1 :]
        if abs(new_line[0] - new_line[1]) > 3:
            continue
        is_increasing = new_line[0] < new_line[1]
        is_unsafe = False
        for i in range(1, len(new_line)):
            if (
                abs(new_line[i] - new_line[i - 1]) > 3
                or (is_increasing and new_line[i] <= new_line[i - 1])
                or (not is_increasing and new_line[i] >= new_line[i - 1])
            ):
                is_unsafe = True
                break
        if not is_unsafe:
            safe += 1
            break

print(safe)
