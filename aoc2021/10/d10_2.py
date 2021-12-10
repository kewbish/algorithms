with open("input.txt") as x:
    lines = x.read().splitlines()

pairs = {"(": ")", "{": "}", "<": ">", "[": "]"}
points = {")": 1, "]": 2, "}": 3, ">": 4}

context = []
p_array = []
p = 0
corrupted = False

for l in lines:
    context = []
    corrupted = False
    p = 0
    for char in l:
        if char in pairs.keys():
            context.append(char)
        elif char in pairs.values():
            if char != pairs[context[-1]]:
                corrupted = True
                p += points[char]
                break
            else:
                context = context[:-1]
    if not corrupted:
        context.reverse()
        for c in context:
            p = p * 5 + points[pairs[c]]
        p_array += [p]

print(sorted(p_array)[len(p_array) // 2])
