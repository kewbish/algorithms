from typing import List


class Monkey:
    items: List[int] = []
    operation_string: str = ""
    divisible_by: int = 1
    if_true: int = 0
    if_false: int = 0
    inspects: int = 0

    def __init__(self, monkey_str: str) -> None:
        lines = monkey_str.split("\n")[1:]
        self.items = [int(i) for i in lines[0].strip().replace("Starting items: ", "").split(", ")]
        self.operation_string = lines[1].strip().replace("Operation: new = ", "")
        self.divisible_by = int(lines[2].strip().split()[-1])
        self.if_true = int(lines[3].strip().split()[-1])
        self.if_false = int(lines[4].strip().split()[-1])


with open("input.txt") as x:
    monkeys = x.read().split("\n\n")
    monkeys = [Monkey(monkey) for monkey in monkeys]

for round_i in range(20):
    for monkey in monkeys:
        while monkey.items:
            item = monkey.items.pop(0)
            monkey.inspects += 1
            new_i = eval(monkey.operation_string.replace("old", str(item)))
            new_i //= 3
            if new_i % monkey.divisible_by == 0:
                monkeys[monkey.if_true].items.append(new_i)
            else:
                monkeys[monkey.if_false].items.append(new_i)

monkeys.sort(key=lambda m: m.inspects)
print(monkeys[-1].inspects * monkeys[-2].inspects)
