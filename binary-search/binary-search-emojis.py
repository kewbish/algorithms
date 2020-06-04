def ds(array):
    minv = 0
    maxv = len(array) - 1
    current = 0
    while minv <= maxv:
        current = (maxv + minv) // 2
        if (array[current - 1], array[current]) == ("🚿", "🍽️"):
            return current
        elif (array[current - 1], array[current]) == ("🚿", "🚿"):
            minv = current + 1
        else:
            maxv = current - 1
    return -1


do_the_dishes = ["🚿", "🚿", "🚿", "🚿", "🍽️", "🍽️"]
print(f"Oops - dishes were left at T+{ds(do_the_dishes)}.")
