grid = [list(line.strip()) for line in open("input").readlines()]

def east():
    global grid
    moved, ng = False, [line[:] for line in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != ">":
                continue

            if j < len(grid[0]) - 1:
                if grid[i][j + 1] == ".":
                    ng[i][j + 1] = ">"
                    ng[i][j] = "."
                    moved = True
            else:
                if grid[i][0] == ".":
                    ng[i][0] = ">"
                    ng[i][j] = "."
                    moved = True

    grid = ng
    return moved

def south():
    global grid
    moved, ng = False, [line[:] for line in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "v":
                continue

            if i < len(grid) - 1:
                if grid[i + 1][j] == ".":
                    ng[i + 1][j] = "v"
                    ng[i][j] = "."
                    moved = True
            else:
                if grid[0][j] == ".":
                    ng[0][j] = "v"
                    ng[i][j] = "."
                    moved = True

    grid = ng
    return moved

def step():
    e = east()
    s = south()
    return e or s

i = 1
while step():
    i += 1

print(i)
