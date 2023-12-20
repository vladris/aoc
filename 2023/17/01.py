grid = [[int(c) for c in line.strip()] for line in open('input').readlines()]

best, end = {}, 1000000

def search(x, y, d, p):
    global end

    if p >= end:
        return

    if x == len(grid) - 1 and y == len(grid[0]) - 1:
        if p < end:
            end = p
        return

    if (x, y, d) in best and best[(x, y, d)] <= p:
        return

    best[(x, y, d)] = p
    
    if d != 'H':
        pxr = p
        for i in range(1, 4):
            if x + i < len(grid):
                pxr += grid[x + i][y]
                search(x + i, y, 'H', pxr)

        pxl = p
        for i in range(1, 4):
            if x - i >= 0:
                pxl += grid[x - i][y]
                search(x - i, y, 'H', pxl)

    if d != 'V':
        pyd = p
        for i in range(1, 4):
            if y + i < len(grid[0]):
                pyd += grid[x][y + i]
                search(x, y + i, 'V', pyd)

        pyu = p
        for i in range(1, 4):
            if y - i >= 0:
                pyu += grid[x][y - i]
                search(x, y - i, 'V', pyu)


search(0, 0, None, 0)
print(end)
