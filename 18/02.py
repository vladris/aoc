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
grid[y - 1] = grid[y - 1][:x - 1] + '@#@' + grid[y - 1][x + 2:]
grid[y] = grid[y].replace('.@.', '###')
grid[y + 1] = grid[y + 1][:x - 1] + '@#@' + grid[y + 1][x + 2:]

best_paths = dict()
queue = [([(x - 1, y - 1, 0), (x + 1, y - 1, 0), (x - 1, y + 1, 0), (x + 1, y + 1, 0)], 0, set())]
total = count_keys()

best = 10 ** 6

while queue:
    coords, move, keys = queue.pop(0)
    x, y, dist = coords[move]

    t_dist = sum([c[2] for c in coords])

    if t_dist > best or grid[y][x] == '#':
        continue
        
    if grid[y][x].isupper() and grid[y][x].lower() not in keys:
        continue

    if grid[y][x].islower():
        keys.add(grid[y][x])

    if len(keys) == total:
        if t_dist < best:
            best = t_dist
        continue

    key = (x, y, ''.join(sorted(keys)))
    if key in best_paths and best_paths[key] <= dist:
        continue
    best_paths[key] = dist

    if grid[y][x] != '.':
        for k in range(4):
            if k != move:
                queue.append((coords[:], k, set(keys)))

    coords[move] = (x - 1, y, dist + 1)
    queue.append((coords[:], move, set(keys)))
    coords[move] = (x + 1, y, dist + 1)
    queue.append((coords[:], move, set(keys)))
    coords[move] = (x, y - 1, dist + 1)
    queue.append((coords[:], move, set(keys)))
    coords[move] = (x, y + 1, dist + 1)
    queue.append((coords[:], move, set(keys)))

# 1626
print(best)