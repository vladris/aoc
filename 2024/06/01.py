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


i, j = find_start(grid)
di, dj = -1, 0

while True:
    ni, nj = i + di, j + dj
    if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]):
        break

    if grid[ni][nj] == "#":
        di, dj = rotate(di, dj)
    else:
        grid[i][j] = "X"
        i, j = ni, nj
        
print(sum([c in line for line in grid for c in line if c == "X"]) + 1)
