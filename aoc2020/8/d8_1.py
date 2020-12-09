with open("input.txt") as x:
    lines = x.readlines()
    lines = [li.strip() for li in lines]

pc = 0
visited = [0 for li in lines]
acc = 0

while visited[pc] == 0:
    visited[pc] = 1
    inst, amt = lines[pc].split()
    amt = int(amt)
    if inst == 'acc':
        acc += amt
    pc += 1 if inst != 'jmp' else amt

print(acc)
