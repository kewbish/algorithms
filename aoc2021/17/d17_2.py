with open("input.txt") as x:
    target_x, target_y = x.read().strip()[13:].split(", ")
    target_x = list(map(int, target_x[2:].split("..")))
    target_y = list(map(int, target_y[2:].split("..")))


def check(dx, dy):
    global target_y
    global target_x
    x, y = 0, 0
    while y >= min(target_y):
        x += dx
        y += dy
        dx = dx - 1 if dx > 0 else dx + 1 if dx < 0 else 0
        dy -= 1
        if target_x[0] <= x <= target_x[1] and target_y[0] <= y <= target_y[1]:
            return 1
        elif dx > 0 and x > target_x[1]:
            return 0
        elif dy < 0 and y < target_y[0]:
            return 0
        elif dx == 0 and (x < target_x[0] or x > target_x[1]):
            return 0


c = 0
for dx in range(1000):
    for dy in range(-1000, 1000):
        c += check(dx, dy)
print(c)
