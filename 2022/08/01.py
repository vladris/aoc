trees = [list(map(int, line.strip())) for line in open('input').readlines()]


def line(i, j, di, dj):
    i, j = i + di, j + dj
    while 0 <= i < len(trees) and 0 <= j < len(trees[0]):
        yield trees[i][j]
        i, j = i + di, j + dj


total = 0
for i in range(len(trees)):
    for j in range(len(trees[0])):
        total += any([all([h < trees[i][j] for h in line(i, j, -1, 0)]),
                      all([h < trees[i][j] for h in line(i, j, 1, 0)]),
                      all([h < trees[i][j] for h in line(i, j, 0, -1)]),
                      all([h < trees[i][j] for h in line(i, j, 0, 1)])])

print(total)
