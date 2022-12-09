with open("input.txt") as x:
    motions = x.readlines()


head = (0, 0)
tail = (0, 0)
visited = set()

DIRECTION_MAP = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
for motion in motions:
    direction, amount = motion.split()
    amount = int(amount)
    for step in range(amount):
        visited.add(tail)
        head = (head[0] + DIRECTION_MAP[direction][0], head[1] + DIRECTION_MAP[direction][1])
        if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
            tail_new_row = tail[0]
            if head[0] < tail[0]:
                tail_new_row -= 1
            elif head[0] > tail[0]:
                tail_new_row += 1
            tail_new_column = tail[1]
            if head[1] < tail[1]:
                tail_new_column -= 1
            elif head[1] > tail[1]:
                tail_new_column += 1
            tail = (tail_new_row, tail_new_column)
    visited.add(tail)


print(len(visited))
