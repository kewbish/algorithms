from collections import defaultdict

with open("input.txt") as x:
    commands = x.read().lstrip("$ ").split("\n$ ")
    commands = [command.splitlines() for command in commands]

filepaths = defaultdict(int)

current_dir = "/"
for command in commands:
    if command[0] == "cd /":
        current_dir = "/"
    elif command[0] == "cd ..":
        current_dir = current_dir[: current_dir.rindex("/") - 1]
    elif command[0].startswith("cd"):
        to = command[0].split(" ")[1]
        current_dir += to + "/"
    elif command[0] == "ls":
        for content in command[1:]:
            first, last = content.split()
            if first != "dir":
                filepath = current_dir + last
                filepaths[(filepath, "file")] += int(first)
                filepaths[("/", "dir")] += int(first)
                filepath_chunks = filepath.split("/")[1:]
                for i in range(1, len(filepath_chunks)):
                    filepaths[("/" + "/".join(filepath_chunks[:-i]), "dir")] += int(first)

total_size = filepaths[("/", "dir")]

min_deleted = float("inf")
for k, v in filepaths.items():
    if k[0] != "/" and k[1] == "dir" and total_size - v <= 70_000_000 - 30_000_000:
        min_deleted = min(min_deleted, v)

print(min_deleted)
