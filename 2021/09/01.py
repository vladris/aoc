grid = map(lambda s: map(int, list(s.strip())), open("input").readlines())

grid = [[10] * (len(grid[0]) + 2)] + [[10] + row + [10] for row in grid] + [[10] * (len(grid[0]) + 2)]

total = 0

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        if (grid[i - 1][j] > grid[i][j] and 
            grid[i + 1][j] > grid[i][j] and
            grid[i][j - 1] > grid[i][j] and
            grid[i][j + 1] > grid[i][j]):
            total += 1 + grid[i][j]

print(total)
