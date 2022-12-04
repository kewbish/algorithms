with open("input.txt") as x:
    assignments = x.readlines()


def is_overlapping(x1, x2, y1, y2):
    return max(x1, y1) <= min(x2, y2)


overlaps = 0
for assignment in assignments:
    first, second = assignment.split(",")
    first_begin, first_end = first.split("-")
    first_begin = int(first_begin)
    first_end = int(first_end)
    second_begin, second_end = second.split("-")
    second_begin = int(second_begin)
    second_end = int(second_end)
    # first_range = set(i for i in range(first_begin, first_end + 1))
    # second_range = set(i for i in range(second_begin, second_end + 1))
    # if first_range.intersection(second_range):
    #     overlaps += 1
    if is_overlapping(first_begin, first_end, second_begin, second_end):
        overlaps += 1


print(overlaps)
