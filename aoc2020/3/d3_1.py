lines = [li for li in open("input.txt").read().split()]  # apparently readlines() was not working ok then

pos = [0, 0]
trees = 0
while pos[0] < len(lines):
    if lines[pos[0]][pos[1]] == "#":
        trees += 1
    pos[0] += 1
    pos[1] = (pos[1] + 3) % len(lines[0])

print(trees)
