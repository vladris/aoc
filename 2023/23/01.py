grid = [line.strip() for line in open('input').readlines()]

graph = {(0, grid[0].index('.')): {}, (len(grid) - 1, grid[-1].index('.')): {}}

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if grid[i][j] == '.':
            if sum([1 for dx, dy in d if grid[i + dx][j + dy] != '#']) > 2:
                graph[(i, j)] = {}


def walk(x, y, from_x, from_y):
    l = 1
    while (x, y) not in graph:
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in d:
            if (x + dx, y + dy) == (from_x, from_y):
                continue

            if grid[x + dx][y + dy] != '#':
                from_x, from_y, x, y = x, y, x + dx, y + dy
                break

        l += 1
    return x, y, l


for node in graph:
    x, y = node
    if x > 0 and grid[x - 1][y] not in '#v':
        nx, ny, l = walk(x - 1, y, x, y)
        if (nx, ny) not in graph[node]:
            graph[node][(nx, ny)] = l
    if x < len(grid) - 1 and grid[x + 1][y] not in '#^':
        nx, ny, l = walk(x + 1, y, x, y)
        if (nx, ny) not in graph[node]:
            graph[node][(nx, ny)] = l
    if y > 0 and grid[x][y - 1] not in '#>':
        nx, ny, l = walk(x, y - 1, x, y)
        if (nx, ny) not in graph[node]:
            graph[node][(nx, ny)] = l
    if y < len(grid[0]) - 1 and grid[x][y + 1] not in '#<':
        nx, ny, l = walk(x, y + 1, x, y)
        if (nx, ny) not in graph[node]:
            graph[node][(nx, ny)] = l

best = 0
def travel(n, visited=[]):
    global best

    if n == (len(grid) - 1, grid[-1].index('.')):
        path = sum([graph[n1][n2] for (n1, n2) in zip(visited, visited[1:] + [n])])
        if path > best:
            best = path
        return

    if n in visited:
        return

    for option in graph[n]:
        travel(option, visited + [n])


travel((0, grid[0].index('.')))

print(best)
