import re

lines = open("input").readlines()

grid = [[0 for _ in range(1000)] for _ in range(1000)]

for line in lines:
    m = re.match(r"(.*) (\d+),(\d+) through (\d+),(\d+)", line)
    instr, x1, y1, x2, y2 = m[1], int(m[2]), int(m[3]), int(m[4]), int(m[5])

    act = {
        "turn on": lambda l: l + 1,
        "turn off": lambda l: max(l - 1, 0),
        "toggle": lambda l: l + 2
    }

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] = act[instr](grid[x][y])

print(sum([sum(line) for line in grid]))