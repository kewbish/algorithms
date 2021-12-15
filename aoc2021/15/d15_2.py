with open("input.txt") as x:
    chitons = x.read().splitlines()
    chitons = [[int(c) for c in list(chiton_row)] for chiton_row in chitons]

# jk it's not leetcode, back to the pseudo-htdp it is

rows = 5 * len(chitons)
columns = 5 * len(chitons[0])

points = [(0, 0, 0)]
seen = {(0, 0)}
while points:
    points.sort(key=lambda p: p[0])
    cur_distance, x, y = points.pop(0)
    if x + 1 == columns and y + 1 == rows:
        print(cur_distance)
        break
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dx, dy = direction
        nx = x + dx  # have to use x later so don't change in place
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= columns or ny >= rows:
            continue
        newy, newym = divmod(ny, rows // 5)
        newx, newxm = divmod(nx, columns // 5)
        new_data = chitons[newym][newxm] + newy + newx
        while new_data > 9:
            new_data -= 9
        if (nx, ny) not in seen:
            seen.add((nx, ny))
            points.append((cur_distance + new_data, nx, ny))
