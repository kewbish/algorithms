cups = list(input())
cups = [int(c) for c in cups]
cups += [i for i in range(10, 1000001)]

llist = {} # k ⇒ cup number, v ⇒ next cup number 
for i, c in enumerate(cups):
    if i == len(cups) - 1:
        llist[c] = cups[0]
    else:
        llist[c] = cups[i + 1]

cur = cups[0]

for i in range(10000001):
    j = llist[cur] # shifting llist
    k = llist[j]
    l = llist[k]
    llist[cur] = llist[l]
    dest = cur - 1
    if dest == 0:
        dest = 1000000
    while dest in [j, k, l]:
        dest -= 1
        if dest == 0:
            dest = 1000000
    llist[l] = llist[dest]
    llist[dest] = j # next selected cup
    cur = llist[cur]

print(llist[1] * llist[llist[1]])

# did not expect to reuse cs50 knowledge but here we are

