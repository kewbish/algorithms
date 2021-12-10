with open("input.txt") as x:
    lines = x.read().splitlines()

pairs = {"(": ")", "{": "}", "<": ">", "[": "]"}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}

context = []
p = 0

for l in lines:
    for char in l:
        if char in pairs.keys():
            context.append(char)
        elif char in pairs.values():
            if char != pairs[context[-1]]:
                p += points[char]
                break
            else:
                context = context[:-1]

print(p)
