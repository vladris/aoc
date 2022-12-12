grid = [list(map(ord, line.strip())) for line in open('input').readlines()]

dist, nodes, candidates = {}, set(), []


def neighbors(i, j):
    if i > 0 and grid[i - 1][j] >= grid[i][j] - 1:
        yield (i - 1, j)
    if i < len(grid) - 1 and grid[i + 1][j] >= grid[i][j] - 1:
        yield (i + 1, j)
    if j > 0 and grid[i][j - 1] >= grid[i][j] - 1:
        yield (i, j - 1)
    if j < len(grid[0]) - 1 and grid[i][j + 1] >= grid[i][j] - 1:
        yield (i, j + 1)


for i in range(len(grid)):
    for j in range(len(grid[0])):
        dist[(i, j)] = 10 ** 10
        nodes.add((i, j))
        if grid[i][j] == ord('S'):
            grid[i][j] = ord('a')
            s = (i, j)
        elif grid[i][j] == ord('E'):
            grid[i][j] = ord('z')
            e = (i, j)
            dist[e] = 0

while nodes:
    node = min(nodes, key=lambda n: dist[n])
    nodes.remove(node)
    if grid[node[0]][node[1]] == ord('a'):
        candidates.append(node)
    for neighbor in neighbors(*node):
        if dist[node] + 1 < dist[neighbor]:
            dist[neighbor] = dist[node] + 1

print(min([dist[node] for node in candidates]))
