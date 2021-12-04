with open("input.txt") as x:
    numbers, *bingo = x.read().split("\n\n")
    numbers = [int(num) for num in numbers.split(",")]
    boards = [[[int(v) for v in row.split()] for row in board.splitlines()] for board in bingo]


def test_win(board: list[list[int]], called: list[int]) -> bool:
    cols = list(zip(*board))
    return any(all(c in called for c in row) for row in board) or any(all(r in called for r in col) for col in cols)


for i in range(len(numbers)):
    called = numbers[: i + 1]
    for b in boards:
        if test_win(b, called):
            b = [it for sl in b for it in sl]
            not_called = sum(set(b) - set(called))
            print(not_called * numbers[i])
            exit(0)
