grid = [line.strip() for line in open('input').readlines()]

def tilt(i, j):
    n = i - 1
    while n >= 0 and grid[n][j] == '.':
        n -= 1
    n += 1

    grid[i] = grid[i][:j] + '.' + grid[i][j + 1:]
    grid[n] = grid[n][:j] + 'O' + grid[n][j + 1:]


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'O':
            tilt(i, j)

total = 0
for i, line in enumerate(grid):
    total += sum([1 for c in line if c == 'O']) * (len(grid) - i)

print(total)
