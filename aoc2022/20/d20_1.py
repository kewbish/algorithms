with open("input.txt") as x:
    lines = x.read().splitlines()
    lines = [(int(x), i) for i, x in enumerate(lines)]

original_numbers = lines.copy()
for number in original_numbers:
    position = lines.index(number)
    lines.pop(position)
    lines.insert((position + int(number[0])) % len(lines), number)

zero_index = 0
for i in range(len(lines)):
    if lines[i][0] == 0:
        zero_index = i
        break
print(
    int(
        lines[(zero_index + 1000) % len(lines)][0]
        + lines[(zero_index + 2000) % len(lines)][0]
        + lines[(zero_index + 3000) % len(lines)][0]
    )
)
