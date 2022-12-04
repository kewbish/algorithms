with open("input.txt") as x:
    assignments = x.readlines()

overlaps = 0
for assignment in assignments:
    first, second = assignment.split(",")
    first_begin, first_end = first.split("-")
    first_begin = int(first_begin)
    first_end = int(first_end)
    second_begin, second_end = second.split("-")
    second_begin = int(second_begin)
    second_end = int(second_end)
    if first_begin <= second_begin <= second_end <= first_end or second_begin <= first_begin <= first_end <= second_end:
        overlaps += 1

print(overlaps)
