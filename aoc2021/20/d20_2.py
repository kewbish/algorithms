from collections import defaultdict

with open("input.txt") as x:
    enhancement, image = x.read().strip().split("\n\n")
    enhancement = [1 if e == "#" else 0 for e in enhancement]
    image = image.replace(".", "0").replace("#", "1")
    image = [list(map(int, row)) for row in image.splitlines()]


image_pixels = defaultdict(int)
for r in range(len(image)):
    for c in range(len(image[0])):
        if image[r][c] == 1:
            image_pixels[(r, c)] = 1


def enhance(pixels, borders):
    new_pixels = defaultdict(lambda: borders)
    smallest_r = min(pixels.keys(), key=lambda p: p[0])[0] - 1
    largest_r = max(pixels.keys(), key=lambda p: p[0])[0] + 1
    smallest_c = min(pixels.keys(), key=lambda p: p[1])[1] - 1
    largest_c = max(pixels.keys(), key=lambda p: p[1])[1] + 1
    for r in range(smallest_r, largest_r + 1):
        for c in range(smallest_c, largest_c + 1):
            neighbours = ""
            for rid in range(r - 1, r + 2):
                for cid in range(c - 1, c + 2):
                    neighbours += "1" if pixels[(rid, cid)] else "0"
            enhancement_index = int(neighbours, 2)
            new_pixels[(r, c)] = enhancement[enhancement_index]
    borders = enhancement[int((str(borders) * 9), 2)]
    return new_pixels, borders


borders = 0
for _ in range(50):
    image_pixels, borders = enhance(image_pixels, borders)
print(len(list(filter(lambda p: p == 1, image_pixels.values()))))
