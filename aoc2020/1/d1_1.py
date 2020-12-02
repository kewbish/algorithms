with open("input.txt") as x:
    lines = x.readlines()

s_lines = sorted([int(li) for li in lines]) 

low = 0
high = 199
while low < high:
    ps = s_lines[low] + s_lines[high]
    if ps < 2020:
        low += 1
    elif ps > 2020:
        high -= 1
    elif ps == 2020:
        print(s_lines[low] * s_lines[high])
