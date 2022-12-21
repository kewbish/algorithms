from sympy.solvers import solve
from sympy import Symbol
from typing import Dict, List


class Monkey:
    operation: str = ""
    name: str = ""
    raw_value: int | str | None = None
    depends_on: List[str] = []

    def __init__(self, input: str) -> None:
        name, instruction = input.split(":")
        self.name = name
        self.operation = instruction.strip()
        try:
            self.raw_value = int(instruction)
        except:
            dependencies = instruction.strip().split(" ")
            self.depends_on = [dependencies[0], dependencies[2]]


with open("input.txt") as x:
    monkeys = x.read().splitlines()
    monkeys = {monkey.split(":")[0]: Monkey(monkey) for monkey in monkeys}


def findOrder(monkeys: Dict[str, Monkey]) -> List[str]:
    def dfs(monkey: str) -> None:
        nonlocal can_finish
        nonlocal topological_sort

        if not can_finish:
            return

        working.add(monkey)

        for prereq in monkeys[monkey].depends_on:
            if prereq in working:
                can_finish = False
            elif prereq not in visited:
                dfs(prereq)

        visited.add(monkey)
        working.remove(monkey)
        topological_sort.append(monkey)

    visited = set()
    can_finish = True
    topological_sort = []
    working = set()

    for k in monkeys:
        if k not in visited:
            dfs(k)

    return topological_sort if can_finish else []


monkeys["humn"].raw_value = "human"

monkey_values = {}
monkey_order = findOrder(monkeys)
for monkey in monkey_order:
    if not monkeys[monkey].depends_on:
        monkey_values[monkey] = monkeys[monkey].raw_value
    else:
        first, op, second = monkeys[monkey].operation.split(" ")
        monkey_values[monkey] = "(" + str(monkey_values[first]) + f" {op} " + str(monkey_values[second]) + ")"

human = Symbol("human")
eqn = " - ".join(
    [monkey_values[monkey] for monkey in monkeys["root"].depends_on]
)  # sympy assumes all eqns are equal to 0
print(solve(eqn, human)[0])
