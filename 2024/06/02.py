grid = [list(line.strip()) for line in open("input").readlines()]

def find_start(grid):
    for i, l in enumerate(grid):
        for j, c in enumerate(l):
            if c == "^":
                return i, j


def rotate(di, dj):
    match (di, dj):
        case (-1, 0):
            return (0, 1)
        case (0, 1):
            return (1, 0)
        case (1, 0):
            return (0, -1)
        case (0, -1):
            return (-1, 0)


def traverse(grid, i, j, di = -1, dj = 0):
    trace = set()
    while True:
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
            return False

        if grid[ni][nj] == "#":
            di, dj = rotate(di, dj)
        else:
            grid[i][j] = "X"
            i, j = ni, nj
            if (i, j, di, dj) in trace:
                return True
            trace.add((i, j, di, dj))


def obstacles(grid, i, j):
    marked_grid = [row[:] for row in grid]
    traverse(marked_grid, i, j)

    for oi in range(len(grid)):
        for oj in range(len(grid[0])):
            if oi == i and oj == j:
                continue

            if marked_grid[oi][oj] == "X":
                new_grid = [row[:] for row in grid]
                new_grid[oi][oj] = "#"
                yield new_grid
            

i, j = find_start(grid)
print(sum([traverse(new_grid, i, j) for new_grid in obstacles(grid, i, j)]))
