cubes = [tuple(map(int, l.strip().split(','))) for l in open('input').readlines()]

visited, queue, area = set(), [(-1, -1, -1)], 0
while queue:
    (x, y, z) = queue.pop(0)

    if (x, y, z) in visited:
        continue

    if not (-1 <= x <= 22 and -1 <= y <= 22 and -1 <= z <= 22):
        continue

    if (x, y, z) in cubes:
        area += 1
        continue

    visited.add((x, y, z))
    queue.append((x - 1, y, z))
    queue.append((x + 1, y, z))
    queue.append((x, y - 1, z))
    queue.append((x, y + 1, z))
    queue.append((x, y, z - 1))
    queue.append((x, y, z + 1))

print(area)
