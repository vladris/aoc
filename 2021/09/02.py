from functools import reduce

grid = map(lambda s: map(int, list(s.strip())), open("input").readlines())

grid = [[10] * (len(grid[0]) + 2)] + [[10] + row + [10] for row in grid] + [[10] * (len(grid[0]) + 2)]

def basin(i, j):
    if grid[i][j] >= 9:
        return 0
    
    grid[i][j] = 9
    return 1 + basin(i - 1, j) + basin(i + 1, j) + basin(i, j - 1) + basin(i, j + 1)

basins = []

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        if (grid[i - 1][j] > grid[i][j] and 
            grid[i + 1][j] > grid[i][j] and
            grid[i][j - 1] > grid[i][j] and
            grid[i][j + 1] > grid[i][j]):
            basins.append(basin(i, j))

print(reduce(lambda x, y: x * y, sorted(basins)[-3:]))
