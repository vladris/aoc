grid, units, damage = [], {}, 3

def move(fi, fj, ti, tj):
    grid[ti][tj] = grid[fi][fj]
    units[(ti, tj)] = units[(fi, fj)]

    grid[fi][fj] = "."
    del units[(fi, fj)]

def attack(ti, tj):
    global damage

    units[(ti, tj)][1] -= damage if units[(ti, tj)][0] == "G" else 3
    if units[(ti, tj)][1] <= 0:
        grid[ti][tj] = "."
        del units[(ti, tj)]

def inrange(i, j):
    best, di, dj = 10 ** 6, None, None
    for ti, tj in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
        if (ti, tj) in units and units[(ti, tj)][0] != grid[i][j]:
            if units[(ti, tj)][1] < best:
                best = units[(ti, tj)][1]
                di, dj = ti, tj
    return di, dj if di else None

def targets(i, j):
    targets = []
    for ti, tj in units:
        if units[(ti, tj)][0] != grid[i][j]:
            targets.append((ti, tj))
    return targets

def dists(i, j):
    dist = {(i, j): 0}
    queue = [(i - 1, j, 1), (i, j - 1, 1), (i, j + 1, 1), (i + 1, j, 1)]
    while queue:
        i, j, d = queue.pop(0)
        if grid[i][j] != ".":
            continue
        if (i, j) in dist and dist[(i, j)] <= d:
            continue
        dist[(i, j)] = d
        queue.append((i - 1, j, d + 1))
        queue.append((i, j - 1, d + 1))
        queue.append((i, j + 1, d + 1))
        queue.append((i + 1, j, d + 1))
    return dist

def unitmove(i, j, moved):
    tgts = targets(i, j)
    if not tgts:
        moved.add((i, j))
        return False

    di, dj = inrange(i, j)
    if di:
        attack(di, dj)
        moved.add((i, j))
        return True

    ds = dists(i, j)
    best, di, dj = 10 ** 6, None, None
    for ti, tj in tgts:
        for pi, pj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            if (ti + pi, tj + pj) in ds:
                if ds[(ti + pi, tj + pj)] < best:
                    best = ds[(ti + pi, tj + pj)]
                    di, dj = ti + pi, tj + pj
                elif ds[(ti + pi, tj + pj)] == best:
                    if ti + pi < di or (ti + pi == di and tj + pj < dj):
                        di, dj = ti + pi, tj + pj

    if not di:
        moved.add((i, j)) 
        return True

    ds = dists(di, dj)
    best, mi, mj = 10 ** 6, None, None
    for pi, pj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        if (i + pi, j + pj) in ds:
            if ds[(i + pi, j + pj)] < best:
                best = ds[(i + pi, j + pj)]
                mi, mj = i + pi, j + pj

    move(i, j, mi, mj)
    i, j = mi, mj

    di, dj = inrange(i, j)
    if di:
        attack(di, dj)
    moved.add((i, j))
    return True

def turn():
    moved = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in moved:
                continue

            if grid[i][j] not in ".#":
                if not unitmove(i, j, moved):
                    return False
    return True

def game():
    global grid, units

    grid = [[c for c in line.strip()] for line in open("input").readlines()]
    units = {}
    elves = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] not in ".#":
                units[(i, j)] = [grid[i][j], 200]
                if grid[i][j] == "E":
                    elves += 1

    moves = 0
    while turn():
        moves += 1

    if elves > sum(map(lambda k: units[k][0] == "E", units)):
        return 0

    return moves * sum(map(lambda x: x[1], units.values()))

result = 0
while not result:
    damage += 1
    result = game()

print(result)
