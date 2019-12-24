grid = [line.strip() for line in open('input').readlines()]

def start():
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == '@':
                return y, x

def count_keys():
    total = 0
    for line in grid:
        for c in line:
            if c.islower():
                total += 1
    return total

x, y = start()
best_paths, queue = dict(), []

queue.append((x, y, 0, set()))
total = count_keys()

best = 10 ** 6

while queue:
    x, y, dist, keys = queue.pop(0)

    if dist > best or grid[y][x] == '#':
        continue

    if grid[y][x].isupper() and grid[y][x].lower() not in keys:
        continue

    if grid[y][x].islower():
        keys.add(grid[y][x])

        if len(keys) == total:
            if dist < best:
                best = dist
            continue

    key = (x, y, ''.join(sorted(keys)))
    if key in best_paths and best_paths[key] <= dist:
        continue
    best_paths[key] = dist

    queue.append((x - 1, y, dist + 1, set(keys)))
    queue.append((x + 1, y, dist + 1, set(keys)))
    queue.append((x, y - 1, dist + 1, set(keys)))
    queue.append((x, y + 1, dist + 1, set(keys)))

print(best)