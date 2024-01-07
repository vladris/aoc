grid = [line.strip() for line in open('input').readlines()]
grid = grid


def probe():
    dx, dy = len(grid) // 2, len(grid[0]) // 2
    tiles, progress = {(dx, dy)}, {(0, 0): {0: 1}}
    
    i = 0
    while len(progress) < 41:
        i += 1
        new_tiles = set()
        for x, y in tiles:
            if grid[(x - 1) % len(grid)][y % len(grid[0])] != '#':
                new_tiles.add((x - 1, y))
            if grid[(x + 1) % len(grid)][y % len(grid[0])] != '#':
                new_tiles.add((x + 1, y))
            if grid[x % len(grid)][(y - 1) % len(grid[0])] != '#':
                new_tiles.add((x, y - 1))
            if grid[x % len(grid)][(y + 1) % len(grid[0])] != '#':
                new_tiles.add((x, y + 1))

        tiles = new_tiles

        for x, y in tiles:
            sq_x, sq_y = x // len(grid), y // len(grid[0])
            if (sq_x, sq_y) not in progress:
                progress[(sq_x, sq_y)] = {}
            if i not in progress[(sq_x, sq_y)]:
                progress[(sq_x, sq_y)][i] = 0
            progress[(sq_x, sq_y)][i] += 1

    return progress


progress = probe()

def at(x, y, step):
    return progress[(x, y)][step] if step in progress[(x, y)] else 0


def count(steps):
    even, odd = (1, 0) if steps % 2 == 0 else (0, 1)

    for i in range(1, steps // len(grid)):
        if steps % 2 == 0:
            if i % 2 == 0:
                even += 4 * i
            else:
                odd += 4 * i
        else:
            if i % 2 == 0:
                odd += 4 * i
            else:
                even += 4 * i

    total = even * at(0, 0, len(grid) * 2) + odd * at(0, 0, len(grid) * 2 + 1)

    total += at(-3, 0, len(grid) * 3 + steps % len(grid))
    total += at(3, 0, len(grid) * 3 + steps % len(grid))
    total += at(0, -3, len(grid) * 3 + steps % len(grid))
    total += at(0, 3, len(grid) * 3 + steps % len(grid))

    i = steps // len(grid) - 1

    total += i * at(-1, -1, len(grid) * 2 + steps % len(grid))
    total += i * at(-1, 1, len(grid) * 2 + steps % len(grid))
    total += i * at(1, -1, len(grid) * 2 + steps % len(grid))
    total += i * at(1, 1, len(grid) * 2 + steps % len(grid))
    
    i += 1
    
    total += i * at(-2, -1, len(grid) * 2 + steps % len(grid))
    total += i * at(-2, 1, len(grid) * 2 + steps % len(grid))
    total += i * at(2, -1, len(grid) * 2 + steps % len(grid))
    total += i * at(2, 1, len(grid) * 2 + steps % len(grid))
    
    return total


print(count(26501365))
