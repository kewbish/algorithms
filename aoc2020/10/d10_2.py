with open("input.txt") as x:
    lines = x.readlines()
    lines = [int(li.strip()) for li in lines]

lines = sorted(lines)
lines = [0] + lines + [lines[-1] + 3] # final adapter
cache = {}

def numways(cur):
    if cur in cache:
        return cache[cur]
    if cur == (len(lines) - 1):
        return 1
    ways = 0
    for x in range(cur + 1, min(cur + 4, len(lines))):
        if lines[x] - lines[cur] <= 3:
            ways += numways(x)
    cache[cur] = ways
    return ways

tways = numways(0) 
print(tways)

# thx kaneki

