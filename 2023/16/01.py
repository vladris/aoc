grid = [line.strip() for line in open('input').readlines()]

queue = [(0, -1, (0, 1))]
visited = set()
while queue:
    x, y, d = queue.pop(0)

    x, y = x + d[0], y + d[1]
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        continue

    if (x, y, d) in visited:
        continue
    visited.add((x, y, d))

    if grid[x][y] == '.':
        queue.append((x, y, d))
    elif grid[x][y] == '/':
        if d == (0, 1):
            d = (-1, 0)
        elif d == (1, 0):
            d = (0, -1)
        elif d == (0, -1):
            d = (1, 0)
        # d == (-1, 0)
        else:
            d = (0, 1)
        queue.append((x, y, d))
    elif grid[x][y] == '\\':
        if d == (0, 1):
            d = (1, 0)
        elif d == (1, 0):
            d = (0, 1)
        elif d == (0, -1):
            d = (-1, 0)
        # d == (-1, 0)
        else:
            d = (0, -1)
        queue.append((x, y, d))
    elif grid[x][y] == '-':
        if d == (0, 1) or d == (0, -1):
            queue.append((x, y, d))
        else:
            queue.append((x, y, (0, 1)))
            queue.append((x, y, (0, -1)))
    # grid[x][y] == '|'
    else:
        if d == (1, 0) or d == (-1, 0):
            queue.append((x, y, d))
        else:
            queue.append((x, y, (1, 0)))
            queue.append((x, y, (-1, 0)))


print(len(set([(x, y) for x, y, _ in visited])))
