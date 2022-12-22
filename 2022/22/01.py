import re

grid = [line.strip('\n').ljust(150, ' ') for line in open('input').readlines()]
dirs, grid = [m.group() for m in re.finditer('(\d+)|L|R', grid[-1])], grid[:-2]
dirs = [int(d) if str.isdecimal(d) else d for d in dirs]

facing = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y, d = grid[0].index('.'), 0, 0


def move(x, y, d):
    nx = (x + d[0]) % len(grid[0])
    ny = (y + d[1]) % len(grid)
    match grid[ny][nx]:
        case ' ': 
            nx, ny = move(nx, ny, d)
            return (nx, ny) if grid[ny][nx] != ' ' else (x, y)
        case '#': return (x, y)
        case '.': return (nx, ny)


for step in dirs:
    if isinstance(step, int):
        while step > 0:
            x, y = move(x, y, facing[d])
            step -= 1
    elif step == 'L':
        d = (d - 1) % 4 
    else:
        d = (d + 1) % 4

print(1000 * (y + 1) + 4 * (x + 1) + d)
