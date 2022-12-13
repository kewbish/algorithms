with open("input.txt") as x:
    signals = x.read().split("\n\n")
    signals = [signal.split("\n") for signal in signals]


def compare(left, right) -> int:  # 0 is wrong, 1 is continue checking, 2 is right ordering
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 2
        elif left == right:
            return 1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        for new_left, new_right in zip(left, right):
            result = compare(new_left, new_right)
            if result == 0:
                return 0
            elif result == 2:
                return 2
        if len(left) < len(right):
            return 2
        elif len(right) < len(left):
            return 0
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(right, int) and isinstance(left, list):
        return compare(left, [right])
    return -1


in_order = 0
for i in range(len(signals)):
    signal1, signal2 = signals[i][0], signals[i][1]
    signal1 = eval(signal1)
    signal2 = eval(signal2)
    in_order += (i + 1) if compare(signal1, signal2) == 2 else 0

print(in_order)
