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
        if x + 3 < len(grid[x]):
            pxr = p + grid[x + 1][y] + grid[x + 2][y] + grid[x + 3][y]
            for i in range(4, 11):
                if x + i < len(grid):
                    pxr += grid[x + i][y]
                    search(x + i, y, 'H', pxr)

        if x - 3 >= 0:
            pxl = p + grid[x - 1][y] + grid[x - 2][y] + grid[x - 3][y]
            for i in range(4, 11):
                if x - i >= 0:
                    pxl += grid[x - i][y]
                    search(x - i, y, 'H', pxl)

    if d != 'V':
        if y + 3 < len(grid[0]):
            pyd = p + grid[x][y + 1] + grid[x][y + 2] + grid[x][y + 3]
            for i in range(4, 11):
                if y + i < len(grid[0]):
                    pyd += grid[x][y + i]
                    search(x, y + i, 'V', pyd)

        if y - 3 >- 0:
            pyu = p + grid[x][y - 1] + grid[x][y - 2] + grid[x][y - 3]
            for i in range(4, 11):
                if y - i >= 0:
                    pyu += grid[x][y - i]
                    search(x, y - i, 'V', pyu)


search(0, 0, None, 0)
print(end)
