from functools import cmp_to_key

with open("input.txt") as x:
    signals = x.read().splitlines()
    signals = [eval(signal) for signal in signals if signal]
    signals += [[[2]], [[6]]]  # type: ignore


def compare(left, right) -> int:  # -1 is wrong, 0 is continue checking, 1 is right ordering
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1
    elif isinstance(left, list) and isinstance(right, list):
        for new_left, new_right in zip(left, right):
            result = compare(new_left, new_right)
            if result == -1:
                return -1
            elif result == 1:
                return 1
        if len(left) < len(right):
            return 1
        elif len(right) < len(left):
            return -1
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(right, int) and isinstance(left, list):
        return compare(left, [right])
    return 0


signals.sort(key=cmp_to_key(compare), reverse=True)
first_divider = signals.index([[2]]) + 1
second_divider = signals.index([[6]]) + 1
print(first_divider * second_divider)
