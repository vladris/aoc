grid = [line.strip() for line in open('input').readlines()]

def swap(i, j, k, l):
    grid[i] = grid[i][:j] + '.' + grid[i][j + 1:]
    grid[k] = grid[k][:l] + 'O' + grid[k][l + 1:]


def tilt1_n(i, j):
    n = i - 1
    while n >= 0 and grid[n][j] == '.':
        n -= 1
    n += 1
    swap(i, j, n, j)


def tilt1_s(i, j):
    n = i + 1
    while n < len(grid) and grid[n][j] == '.':
        n += 1
    n -= 1
    swap(i, j, n, j)


def tilt1_w(i, j):
    n = j - 1
    while n >= 0 and grid[i][n] == '.':
        n -= 1
    n += 1
    swap(i, j, i, n)


def tilt1_e(i, j):
    n = j + 1
    while n < len(grid[0]) and grid[i][n] == '.':
        n += 1
    n -= 1
    swap(i, j, i, n)


def tilt_n():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                tilt1_n(i, j)

            
def tilt_s():
    for i in range(len(grid) - 1, -1, -1):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                tilt1_s(i, j)


def tilt_w():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                tilt1_w(i, j)


def tilt_e():
    for i in range(len(grid)):
        for j in range(len(grid[0]) - 1, -1, -1):
            if grid[i][j] == 'O':
                tilt1_e(i, j)


def cycle():
    tilt_n()
    tilt_w()
    tilt_s()
    tilt_e()
    return '\n'.join(grid)


pos = []
while (state := cycle()) not in pos:
    pos.append(state)

lead, loop = pos.index(state), len(pos) - pos.index(state)
d = (1000000000 - lead) % loop

grid = pos[lead + d - 1].split('\n')

total = 0
for i, line in enumerate(grid):
    total += sum([1 for c in line if c == 'O']) * (len(grid) - i)

print(total)
