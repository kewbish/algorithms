with open("input.txt") as x:
    target_x, target_y = x.read().strip()[13:].split(", ")
    target_x = list(map(int, target_x[2:].split("..")))
    target_y = list(map(int, target_y[2:].split("..")))

max_highest = 0


def check(dx, dy):
    global target_y
    global target_x
    global max_highest
    highest_y = 0
    x, y = 0, 0
    while y >= min(target_y):
        x += dx
        y += dy
        dx = dx - 1 if dx > 0 else dx + 1 if dx < 0 else 0
        dy -= 1
        highest_y = max(y, highest_y)
        if target_x[0] <= x <= target_x[1] and target_y[0] <= y <= target_y[1]:
            max_highest = max(max_highest, highest_y)
            return True
        elif dx > 0 and x > target_x[1]:
            return False
        elif dy < 0 and y < target_y[0]:
            return False
        elif dx == 0 and (x < target_x[0] or x > target_x[1]):
            return False


for dx in range(200):
    for dy in range(-200, 1000):
        check(dx, dy)

print(max_highest)
