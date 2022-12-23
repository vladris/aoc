import re

grid = [line.strip('\n').ljust(150, ' ') for line in open('input').readlines()]
dirs, grid = [m.group() for m in re.finditer('(\d+)|L|R', grid[-1])], grid[:-2]
dirs = [int(d) if str.isdecimal(d) else d for d in dirs]

size = 50
facing = [(1, 0), (0, 1), (-1, 0), (0, -1)]

connections = {
    (1, 0): [(2, 0, 0), (1, 1, 1), (0, 2, 0), (0, 3, 0)],
    (2, 0): [(1, 2, 2), (1, 1, 2), (1, 0, 2), (0, 3, 3)],
    (1, 1): [(2, 0, 3), (1, 2, 1), (0, 2, 1), (1, 0, 3)],
    (0, 2): [(1, 2, 0), (0, 3, 1), (1, 0, 0), (1, 1, 0)],
    (1, 2): [(2, 0, 2), (0, 3, 2), (0, 2, 2), (1, 1, 3)],
    (0, 3): [(1, 2, 3), (2, 0, 1), (1, 0, 1), (0, 2, 3)],
}

x, y, d = grid[0].index('.'), 0, 0


def move(x, y, d):
    nx = x + facing[d][0]
    ny = y + facing[d][1]
    nd = d

    if (x // size, y // size) != (nx // size, ny // size):
        nx, ny, nd = switch_region(x, y, d)

    match grid[ny][nx]:
        case '#': return (x, y, d)
        case '.': return (nx, ny, nd)


def switch_region(x, y, d):
    nrx, nry, nd = connections[(x // size, y // size)][d]
    nx, ny = nrx * size, nry * size
    rx, ry = x % size, y % size

    if (d, nd) in [(0, 0), (1, 3), (2, 2), (3, 1)]:
        return nx + size - rx - 1, ny + ry, nd
    if (d, nd) in [(0, 2), (1, 1), (2, 0), (3, 3)]:
        return nx + rx, ny + size - ry - 1, nd
    if (d, nd) in [(0, 1), (1, 0), (2, 3), (3, 2)]:
        return nx + size - ry - 1, ny + size - rx - 1, nd
    if (d, nd) in [(0, 3), (1, 2), (2, 1), (3, 0)]:
        return nx + ry, ny + rx, nd


for step in dirs:
    if isinstance(step, int):
        while step > 0:
            x, y, d = move(x, y, d)
            step -= 1
    elif step == 'L':
        d = (d - 1) % 4 
    else:
        d = (d + 1) % 4

print(1000 * (y + 1) + 4 * (x + 1) + d)
