grid = [line.strip('\n') for line in open('input').readlines()]

portals = dict()
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c != '.':
            continue

        label = None
        if grid[y][x - 1].isupper():
            label = grid[y][x - 2] + grid[y][x - 1]
        elif grid[y][x + 1].isupper():
            label = grid[y][x + 1] + grid[y][x + 2]
        elif grid[y - 1][x].isupper():
            label = grid[y - 2][x] + grid[y - 1][x]
        elif grid[y + 1][x].isupper():
            label = grid[y + 1][x] + grid[y + 2][x]

        if label:
            if label not in portals:
                portals[label] = []
            portals[label].append((x, y))

start, end = portals['AA'], portals['ZZ']
del portals['AA'], portals['ZZ']

graph = dict()
for portal in portals.values():
    graph[portal[0]] = { portal[1]: 1 }
    graph[portal[1]] = { portal[0]: 1 }

graph[start[0]] = dict()
graph[end[0]] = dict()

def maze(src, x, y, dist, visited):
    if (x, y) in visited or grid[y][x] != '.':
        return

    visited.add((x, y))

    if (x, y) != src and (x, y) in graph:
        if src in graph[(x, y)]:
            graph[src][(x, y)] = min(graph[src][(x, y)], dist)
        else:
            graph[src][(x, y)] = dist

        graph[(x, y)][src] = graph[src][(x, y)]
        return

    maze(src, x - 1, y, dist + 1, set(visited))
    maze(src, x + 1, y, dist + 1, set(visited))
    maze(src, x, y - 1, dist + 1, set(visited))
    maze(src, x, y + 1, dist + 1, set(visited))

for x, y in graph:
    maze((x, y), x, y, 0, set())

def is_outer(node):
    return node[0] == 2 or node[0] == len(grid[0]) - 3 or node[1] == 2 or node[1] == len(grid) - 3

recursive_graph = dict()
for node in graph:
    if node == start[0] or node == end[0]:
        continue

    outer_node = is_outer(node)
    offset = 1 if outer_node else 0
    for depth in range(offset, len(portals) + offset):
        recursive_graph[(*node, depth)] = dict()
        for dest in graph[node]:
            if outer_node and (dest == start[0] or dest == end[0]):
                continue

            if graph[node][dest] == 1:
                recursive_graph[(*node, depth)][(*dest, depth - 1 if outer_node else depth + 1)] = 1
            else:
                recursive_graph[(*node, depth)][(*dest, depth)] = graph[node][dest]

recursive_graph[(*start[0], 0)], recursive_graph[(*end[0], 0)] = dict(), dict()
for dest in graph[start[0]]:
    if dest != end[0] and is_outer(dest):
        continue

    recursive_graph[(*start[0], 0)][(*dest, 0)] = graph[start[0]][dest]

queue, dist = set(recursive_graph.keys()), { node: 10 ** 6 for node in recursive_graph }
dist[(*start[0], 0)] = 0

while queue:
    node = min(queue, key=lambda n: dist[n])
    queue.remove(node)

    for dest in recursive_graph[node]:
        if dest not in queue:
            continue

        if dist[node] + recursive_graph[node][dest] < dist[dest]:
            dist[dest] = dist[node] + recursive_graph[node][dest]

print(dist[(*end[0], 0)])
