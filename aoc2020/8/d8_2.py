with open("input.txt") as x:
    ops = x.readlines()
    ops = [li.strip() for li in ops]

def valid(lines):
    pc = 0
    visited = [0 for li in lines]
    acc = 0
    while True:
        if visited[pc] != 0:
            return ['no', acc]
        visited[pc] = 1
        inst, amt = lines[pc].split()
        amt = int(amt)
        if inst == 'acc':
            acc += amt
        pc += 1 if inst != 'jmp' else amt
        if pc >= len(lines):
            return ['ok', acc] 

for i, li in enumerate(ops):
    if 'nop' in li:
        ops[i] = li.replace('nop', 'jmp')
    elif 'jmp' in li:
        ops[i] = li.replace('jmp', 'nop')
    val = valid(ops)
    if val[0] == 'ok':
        print(val[1])
        break
    else:
        ops[i] = li # reset things
