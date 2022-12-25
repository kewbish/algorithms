with open("input.txt") as x:
    numbers = x.read().splitlines()


# https://www.reddit.com/r/adventofcode/comments/zur1an/comment/j1kycd4/?utm_source=share&utm_medium=web2x&context=3


def to_snafu(num: int) -> str:
    if not num:
        return ""

    DIGIT_MAP = {0: "0", 1: "1", 2: "2", -1: "-", -2: "="}
    snafu_str = ""
    digit = num % 5
    for dec, snafu in DIGIT_MAP.items():
        if (dec + 5) % 5 == digit:
            return to_snafu((num - dec) // 5) + snafu
    return ""


def to_dec(num: str) -> int:
    num_digits = [int(x) if x.isnumeric() else -1 if x == "-" else -2 for x in num[::-1]]
    place = 0
    number = 0
    for digit in num_digits:
        number += digit * 5**place
        place += 1
    return number


sum_snafus = 0
for number in numbers:
    sum_snafus += to_dec(number)

print(to_snafu(sum_snafus))
