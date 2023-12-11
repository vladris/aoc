grid = [line.strip() for line in open('input').readlines()]

def empty_row(i):
    return '#' not in grid[i]

def insert_row(i):
    grid.insert(i, '.' * len(grid[0]))

def empty_col(i):
    return '#' not in [row[i] for row in grid]

def insert_col(i):
    global grid
    grid = [row[:i] + '.' + row[i:] for row in grid]

rows = [i for i in range(len(grid)) if empty_row(i)]
cols = [i for i in range(len(grid[0])) if empty_col(i)]

for i in rows[::-1]:
    insert_row(i)

for i in cols[::-1]:
    insert_col(i)

stars = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            stars.append((i, j))

dist = 0
for s1 in range(len(stars) - 1):
    for s2 in range(s1 + 1, len(stars)):
        dist += abs(stars[s1][0] - stars[s2][0]) + abs(stars[s1][1] - stars[s2][1])

print(dist)
