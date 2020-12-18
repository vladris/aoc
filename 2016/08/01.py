import re

input = open("input").readlines()

grid = [[False for _ in range(50)] for _ in range(6)]

for line in input:
    m = re.match(r"rect (\d+)x(\d+)", line)
    if m:
        for j in range(int(m[2])):
            for i in range(int(m[1])):
                grid[j][i] = True
        continue

    m = re.match(r"rotate column x=(\d+) by (\d+)", line)
    if m:
        col = int(m[1])
        for _ in range(int(m[2])):
            last = grid[-1][col]
            for j in range(5, 0, -1):
                grid[j][col] = grid[j - 1][col]
            grid[0][col] = last
        continue

    m = re.match(r"rotate row y=(\d+) by (\d+)", line)
    if m:
        row = int(m[1])
        for _ in range(int(m[2])):
            last = grid[row][-1]
            for i in range(49, 0, -1):
                grid[row][i] = grid[row][i - 1]
            grid[row][0] = last

print(sum([sum(row) for row in grid]))
