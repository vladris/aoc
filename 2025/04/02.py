grid = open("input").readlines()
grid = ["." + line.strip() + "." for line in grid]
grid = ["." * len(grid[0])] + grid + ["." * len(grid[0])]

total = 0
while True:
    moved = []
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] != "@":
                continue
            n = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    if grid[i + di][j + dj] == "@":
                        n += 1
            if n <= 3:
                total += 1
                moved.append((i, j))

    if not moved:
        break

    for i, j in moved:
        grid[i] = grid[i][:j] + "." + grid[i][j+1:]

print(total)
