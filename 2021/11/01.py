grid = [[int(c) for c in line.strip()] for line in open("input").readlines()]
flashed = []

def valid(i, j):
    return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

def inc(i, j):
    if not valid(i, j): return
    grid[i][j] += 1

def flash(i, j):
    if not valid(i, j) or grid[i][j] < 10 or (i, j) in flashed: return

    flashed.append((i, j))

    for ni in range(i - 1, i + 2):
        for nj in range(j - 1, j + 2):
            if ni == i and nj == j: continue
            inc(ni, nj)
            flash(ni, nj)

def traverse():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            yield i, j

def step():
    global flashed

    for i, j in traverse():
        inc(i, j)

    flashed = []
    for i, j in traverse():
        flash(i, j)

    for i, j in traverse():
        if grid[i][j] > 9:
            grid[i][j] = 0

    return len(flashed)
    
print(sum(step() for _ in range(100)))
