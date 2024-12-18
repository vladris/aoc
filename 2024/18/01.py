bytes = [tuple(map(int, line.strip().split(","))) for line in open("input").readlines()]

memory = set(bytes[:1024])

visited, queue = {}, [(0, 0, 0)]
while queue:
    i, j, at = queue.pop(0)
    if i < 0 or j < 0 or i > 70 or j > 70:
        continue

    if (i, j) in memory:
        continue

    if (i, j) in visited:
        if visited[(i, j)] <= at:
            continue
    else:
        visited[(i, j)] = at

    queue.append((i + 1, j, at + 1))
    queue.append((i - 1, j, at + 1))
    queue.append((i, j + 1, at + 1))
    queue.append((i, j - 1, at + 1))

print(visited[(70, 70)])
