grid, moves = open("input").read().split("\n\n")

grid = [list(row) for row in grid.split("\n")]
moves = "".join(moves.split("\n"))

i, j = len(grid) // 2 - 1, len(grid[0]) // 2 - 1

for move in moves:
    if move == "^":
        t = i - 1
        while grid[t][j] == "O":
            t -= 1
        if grid[t][j] == ".":
            grid[t][j] = "O"
            grid[i - 1][j] = "@"
            grid[i][j] = "."
            i -= 1
    elif move == "v":
        t = i + 1
        while grid[t][j] == "O":
            t += 1
        if grid[t][j] == ".":
            grid[t][j] = "O"
            grid[i + 1][j] = "@"
            grid[i][j] = "."
            i += 1
    elif move == "<":
        t = j - 1
        while grid[i][t] == "O":
            t -= 1
        if grid[i][t] == ".":
            grid[i][t] = "O"
            grid[i][j - 1] = "@"
            grid[i][j] = "."
            j -= 1
    elif move == ">":
        t = j + 1
        while grid[i][t] == "O":
            t += 1
        if grid[i][t] == ".":
            grid[i][t] = "O"
            grid[i][j + 1] = "@"
            grid[i][j] = "."
            j += 1


gps = 0
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == "O":
            gps += i * 100 + j
print(gps)
