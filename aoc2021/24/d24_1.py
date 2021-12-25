from functools import lru_cache


with open("input.txt") as x:
    instructions = x.read().splitlines()
    instructions = [i.split(" ") for i in instructions]


# def monad_valid(monad):
#     global instructions
#     monad = list(map(int, list(monad)))
#     state = {"w": 0, "x": 0, "y": 0, "z": 0}
#     input_index = 0
#     for i in instructions:
#         if i[0] == "inp":
#             state[i[1]] = monad[input_index]
#             input_index += 1
#         elif i[0] == "add":
#             try:
#                 to_add = int(i[2])
#             except:
#                 to_add = i[2]
#             state[i[1]] += to_add if isinstance(to_add, int) else state[to_add]
#         elif i[0] == "mul":
#             try:
#                 to_mul = int(i[2])
#             except:
#                 to_mul = i[2]
#             state[i[1]] *= to_mul if isinstance(to_mul, int) else state[to_mul]
#         elif i[0] == "div":
#             try:
#                 to_div = int(i[2])
#             except:
#                 to_div = i[2]
#             state[i[1]] //= to_div if isinstance(to_div, int) else state[to_div]
#         elif i[0] == "mod":
#             state[i[1]] = state[i[1]] % int(i[2])
#         elif i[0] == "eql":
#             try:
#                 to_eql = int(i[2])
#             except:
#                 to_eql = i[2]
#             state[i[1]] = 1 if state[i[1]] == (to_eql if isinstance(to_eql, int) else state[to_eql]) else 0
#     return state["z"] == 0
#
# # til that 9^14 is quite large
# for monad in range(99999999999999, 0, -1):
#     if monad % 1000000:
#         print(monad)
#     monad = str(monad)
#     if "0" in monad:
#         continue
#     if monad_valid(monad):
#         print(monad)
#         break

# til also that the input repeats every like 18 rows
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


@lru_cache(maxsize=None)  # ok pypy
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
print(max(solutions))
