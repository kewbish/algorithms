lines = [li for li in open("input.txt").read().split()]  # apparently readlines() was not working ok then

def trees_hit(right, down):
    pos = [0, 0]
    trees = 0
    while pos[0] < len(lines):
        if lines[pos[0]][pos[1]] == "#":
            trees += 1
        pos[0] += down 
        pos[1] = (pos[1] + right) % len(lines[0])
    return trees

ttrees = trees_hit(1, 1) * trees_hit(3, 1) * trees_hit(5, 1) * trees_hit(7, 1) * trees_hit(1, 2)
print(ttrees)
