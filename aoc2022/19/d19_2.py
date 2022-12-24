from typing import List, Tuple

# https://www.reddit.com/r/adventofcode/comments/zpihwi/comment/j0t8lq0/


class Blueprint:
    ore_robot: int = 0
    clay_robot: int = 0
    obsidian_robot: Tuple[int, int] = (0, 0)  # ore, clay
    geode_robot: Tuple[int, int] = (0, 0)  # ore, obsidian

    def __init__(self, input: str) -> None:
        input = input.split(": ")[1]
        robots = [[word for word in row.split(" ")] for row in input.split(". ")]
        self.ore_robot = int(robots[0][4])
        self.clay_robot = int(robots[1][4])
        self.obsidian_robot = (int(robots[2][4]), int(robots[2][7]))
        self.geode_robot = (int(robots[3][4]), int(robots[3][7]))


with open("input.txt") as x:
    blueprints = x.read().splitlines()
    blueprints = [Blueprint(blueprint) for blueprint in blueprints][:3]

total_geodes = 1

for blueprint in blueprints:
    max_bp_geodes = 0
    queue: List[Tuple[int, int, int, int, int, int, int, int, int]] = [
        (0, 0, 0, 0, 1, 0, 0, 0, 32)
    ]  # ore, clay, obsidian, geodes, respective robots, time remaining
    visited = set()
    while queue:
        ore, clay, obsidian, geodes, ore_robots, clay_robots, obsidian_robots, geode_robots, remaining = queue.pop(0)

        max_bp_geodes = max(max_bp_geodes, geodes)
        if remaining == 0:
            continue

        # throw away extra resources - clever!
        ore_max = max(
            [blueprint.ore_robot, blueprint.clay_robot, blueprint.obsidian_robot[0], blueprint.geode_robot[0]]
        )
        # refactor into max statements
        ore_robots = min(ore_robots, ore_max)
        clay_robots = min(clay_robots, blueprint.obsidian_robot[1])
        obsidian_robots = min(obsidian_robots, blueprint.geode_robot[1])
        ore = min(ore, remaining * ore_max - ore_robots * (remaining - 1))
        clay = min(clay, remaining * blueprint.obsidian_robot[1] - clay_robots * (remaining - 1))
        obsidian = min(obsidian, remaining * blueprint.geode_robot[1] - obsidian_robots * (remaining - 1))

        state = (ore, clay, obsidian, geodes, ore_robots, clay_robots, obsidian_robots, geode_robots, remaining)
        if state in visited:
            continue
        visited.add(state)

        queue.append(
            (
                ore + ore_robots,
                clay + clay_robots,
                obsidian + obsidian_robots,
                geodes + geode_robots,
                ore_robots,
                clay_robots,
                obsidian_robots,
                geode_robots,
                remaining - 1,
            )
        )
        if ore >= blueprint.ore_robot:
            queue.append(
                (
                    ore + ore_robots - blueprint.ore_robot,
                    clay + clay_robots,
                    obsidian + obsidian_robots,
                    geodes + geode_robots,
                    ore_robots + 1,
                    clay_robots,
                    obsidian_robots,
                    geode_robots,
                    remaining - 1,
                )
            )
        if ore >= blueprint.clay_robot:
            queue.append(
                (
                    ore + ore_robots - blueprint.clay_robot,
                    clay + clay_robots,
                    obsidian + obsidian_robots,
                    geodes + geode_robots,
                    ore_robots,
                    clay_robots + 1,
                    obsidian_robots,
                    geode_robots,
                    remaining - 1,
                )
            )
        if ore >= blueprint.obsidian_robot[0] and clay >= blueprint.obsidian_robot[1]:
            queue.append(
                (
                    ore + ore_robots - blueprint.obsidian_robot[0],
                    clay + clay_robots - blueprint.obsidian_robot[1],
                    obsidian + obsidian_robots,
                    geodes + geode_robots,
                    ore_robots,
                    clay_robots,
                    obsidian_robots + 1,
                    geode_robots,
                    remaining - 1,
                )
            )
        if ore >= blueprint.geode_robot[0] and obsidian >= blueprint.geode_robot[1]:
            queue.append(
                (
                    ore + ore_robots - blueprint.geode_robot[0],
                    clay + clay_robots,
                    obsidian + obsidian_robots - blueprint.geode_robot[1],
                    geodes + geode_robots,
                    ore_robots,
                    clay_robots,
                    obsidian_robots,
                    geode_robots + 1,
                    remaining - 1,
                )
            )
    total_geodes *= max_bp_geodes

# well that took a very very long time
print(total_geodes)
