trees = [list(map(int, line.strip())) for line in open('input').readlines()]


def los(i, j, di, dj):
    h = trees[i][j]
    count, i, j = 0, i + di, j + dj
    while 0 <= i < len(trees) and 0 <= j < len(trees[0]):
        count += 1
        if h <= trees[i][j]:
            break
        i, j = i + di, j + dj
    return count


def score(i, j):
    return los(i, j, -1, 0) * los(i, j, 1, 0) * los(i, j, 0, -1) * los(i, j, 0, 1)


print(max([score(i, j) for j in range(len(trees[0]))
      for i in range(len(trees))]))
