with open("input.txt") as x:
    crates, instructions = x.read().split("\n\n")

crates = crates.splitlines()[:-1]
instructions = instructions.splitlines()
crates_other_way = [[crate[i + 1 : i + 2] for i in range(0, len(crate), 4)] for crate in crates]
crates = list(zip(*crates_other_way))
crates = [[i for i in crate if i.strip()] for crate in crates]
crates = [crate[::-1] for crate in crates]

for instruction in instructions:
    words = instruction.split()
    number, from_i, to_i = words[1], words[3], words[5]
    number = int(number)
    from_i = int(from_i) - 1
    to_i = int(to_i) - 1
    temp = crates[from_i][-number:]
    crates[from_i] = crates[from_i][:-number]
    crates[to_i] += temp[::-1]

message = ""
for crate_stack in crates:
    message += crate_stack[-1]

print(message)
