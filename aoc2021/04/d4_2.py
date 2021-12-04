with open("input.txt") as x:
    numbers, *bingo = x.read().split("\n\n")
    numbers = [int(num) for num in numbers.split(",")]
    boards = [[[int(v) for v in row.split()] for row in board.splitlines()] for board in bingo]


def test_win(board: list[list[int]], called: list[int]) -> bool:
    cols = list(zip(*board))
    return any(all(c in called for c in row) for row in board) or any(all(r in called for r in col) for col in cols)


def final_score(board: list[list[int]], called: list[int]) -> int:
    b = [it for sl in board for it in sl]
    not_called = sum(set(b) - set(called))
    return not_called * called[-1]


for i in range(len(numbers)):
    called = numbers[: i + 1]
    done = []
    for bi, b in enumerate(boards):
        if test_win(b, called):
            done.append(bi)
            if bi == 0 and len(boards) == 1:
                print(final_score(boards[0], called))
                exit(0)
    boards = [b for bi, b in enumerate(boards) if bi not in done]
