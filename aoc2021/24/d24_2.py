from functools import lru_cache


with open("input.txt") as x:
    instructions = x.read().splitlines()
    instructions = [i.split(" ") for i in instructions]


num_blocks = len(instructions) // 18
add_xs = [int(instructions[i * 18 + 5][2]) for i in range(num_blocks)]
add_ys = [int(instructions[i * 18 + 15][2]) for i in range(num_blocks)]
div_zs = [int(instructions[i * 18 + 4][2]) for i in range(num_blocks)]


def check_monad(index, z, w):
    x = add_xs[index] + (z % 26)
    z //= div_zs[index]
    if x != w:
        z *= 26
        z += w + add_ys[index]
    return z


max_pos_zs = [26 ** len([x for x in range(num_blocks) if div_zs[x] == 26 and x >= i]) for i in range(num_blocks)]
digits = list(range(1, 10))


@lru_cache(maxsize=None)
def find_monads(index, z):
    if index == 14:
        return [""] if z == 0 else []
    if z >= max_pos_zs[index]:
        return []
    cur_x = add_xs[index] + (z % 26)
    w_pos = [cur_x] if cur_x in range(1, 10) else digits
    to_ret = []
    for w in w_pos:
        next_z = check_monad(index, z, w)
        next_digit = find_monads(index + 1, next_z)
        for pos in next_digit:
            to_ret.append(str(w) + pos)
    return to_ret


solutions = find_monads(0, 0)
solutions = list(map(int, solutions))
print(min(solutions))
