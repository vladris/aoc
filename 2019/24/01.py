grid = [['.'] * 7] + [list('.' + line.strip() + '.') for line in open('input').readlines()] + [['.'] * 7]

def step():
    updates = []

    for i in range(1, 6):
        for j in range(1, 6):
            count = 0
            if grid[i - 1][j] == '#': count += 1
            if grid[i + 1][j] == '#': count += 1
            if grid[i][j - 1] == '#': count += 1
            if grid[i][j + 1] == '#': count += 1

            if grid[i][j] == '#' and count != 1:
                updates.append(('.', i, j))
            elif grid[i][j] == '.' and (count == 1 or count == 2):
                updates.append(('#', i, j))

    for c, i, j in updates:
        grid[i][j] = c

def biodiversity():
    score = 0
    for i in range(1, 6):
        for j in range(1, 6):
            if grid[i][j] == '#':
                score += 2 ** ((i - 1) * 5 + (j - 1))
    return score

layouts = {biodiversity()}
while True:
    step()
    score = biodiversity()
    if score in layouts:
        print(score)
        break
    layouts.add(score)
