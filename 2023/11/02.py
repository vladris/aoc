grid = [line.strip() for line in open('input').readlines()]

def empty_row(i):
    return '#' not in grid[i]

def empty_col(i):
    return '#' not in [row[i] for row in grid]

rows = [i for i in range(len(grid)) if empty_row(i)]
cols = [i for i in range(len(grid[0])) if empty_col(i)]

stars = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            stars.append((i, j))

dist = 0
for s1 in range(len(stars) - 1):
    for s2 in range(s1 + 1, len(stars)):
        dist += abs(stars[s1][0] - stars[s2][0]) + abs(stars[s1][1] - stars[s2][1])
        top, bottom = min(stars[s1][0], stars[s2][0]), max(stars[s1][0], stars[s2][0])
        left, right = min(stars[s1][1], stars[s2][1]), max(stars[s1][1], stars[s2][1])

        for row in rows:
            if top <= row <= bottom:
                dist += 999999
        
        for col in cols:
            if left <= col <= right:
                dist += 999999

print(dist)
