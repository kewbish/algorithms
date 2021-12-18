from functools import reduce
from math import ceil, floor

with open("input.txt") as x:
    numbers = list(map(eval, x.read().splitlines()))


def add_sn(x, y):
    return reduce_sn([x, y])


def reduce_sn(x):
    while True:
        has_exploded, x, _, _ = explode(x, 0)
        if not has_exploded:
            prev = x
            x = split(x)
            if x == prev:
                break
    return x


def split(x):
    if isinstance(x, int):
        if x >= 10:
            return [floor(x / 2), ceil(x / 2)]
        else:
            return x
    elif isinstance(x, list):
        left = split(x[0])
        if left != x[0]:
            return [left, x[1]]
        right = split(x[1])
        return [x[0], right]


# apparently eval → string → eval wasn't a good solution
def explode(x, depth):
    if isinstance(x, int):
        return False, x, 0, 0
    if depth < 4:
        has_exploded, next_x, left, right = explode(x[0], depth + 1)
        if has_exploded:
            x = [next_x, explode_to_right(x[1], right)]
            return True, x, left, 0
        has_exploded, next_x, left, right = explode(x[1], depth + 1)
        if has_exploded:
            x = [explode_to_left(x[0], left), next_x]
            return True, x, 0, right
        return False, x, 0, 0
    else:
        return True, 0, x[0], x[1]


def explode_to_left(x, to_add):
    if isinstance(x, int):
        return x + to_add
    elif isinstance(x, list):
        return [x[0], explode_to_left(x[1], to_add)]


def explode_to_right(x, to_add):
    if isinstance(x, int):
        return x + to_add
    elif isinstance(x, list):
        return [explode_to_right(x[0], to_add), x[1]]


def magnitude(x):
    if isinstance(x, int):
        return x
    return magnitude(x[0]) * 3 + magnitude(x[1]) * 2


print(magnitude(reduce(add_sn, numbers)))
