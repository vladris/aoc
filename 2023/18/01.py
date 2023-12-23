digs = [line.split(' ')[:2] for line in open('input').readlines()]
digs = [(line[0], int(line[1])) for line in digs]

x, y, grid = 0, 0, {(0, 0)}
for dig in digs:
    match dig[0]:
        case 'U':
            for i in range(dig[1]):
                y -= 1
                grid.add((x, y))
        case 'R':
            for i in range(dig[1]):
                x += 1
                grid.add((x, y))
        case 'D':
            for i in range(dig[1]):
                y += 1
                grid.add((x, y))
        case 'L':
            for i in range(dig[1]):
                x -= 1
                grid.add((x, y))

x, y = min([x for x, _ in grid]), min([y for _, y in grid])
while (x, y) not in grid:
    y += 1

queue = [(x + 1, y + 1)]
while queue:
    x, y = queue.pop(0)

    if (x, y) in grid:
        continue

    grid.add((x, y))
    queue += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

print(len(grid))
