grid = [list(map(int, list(line.strip()))) for line in open("input").readlines()]

dist = [[0] * len(grid) for _ in range(len(grid))]

for i in range(len(grid)):
    for j in range(len(grid)):
        if i > 0: dist[i][j] = dist[i - 1][j] + grid[i][j]
        elif j > 0: dist[i][j] = dist[i][j - 1] + grid[i][j]

update = True
while update:
    update = False
    for i in range(len(grid)):
        for j in range(len(grid)):
            opts = []
            if i > 0: opts.append(dist[i - 1][j])
            if i < len(grid) - 1: opts.append(dist[i + 1][j])
            if j > 0: opts.append(dist[i][j - 1])
            if j < len(grid) - 1: opts.append(dist[i][j + 1])

            best = min(opts)
            if best + grid[i][j] < dist[i][j]:
                dist[i][j] = best + grid[i][j]
                update = True

print(dist[-1][-1])
