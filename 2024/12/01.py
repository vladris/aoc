grid = [line.strip() for line in open("input").readlines()]

visited = set()

def area(i, j):
    if (i, j) in visited:
        return 0, 0

    visited.add((i, j))
    result_a, result_p = 1, 0

    if i == 0 or grid[i - 1][j] != grid[i][j]:
        result_p += 1
    else:
        a, p = area(i - 1, j)
        result_a += a
        result_p += p

    if i == len(grid) - 1 or grid[i + 1][j] != grid[i][j]:
        result_p += 1
    else:
        a, p = area(i + 1, j)
        result_a += a
        result_p += p

    if j == 0 or grid[i][j - 1] != grid[i][j]:
        result_p += 1
    else:
        a, p = area(i, j - 1)
        result_a += a
        result_p += p

    if j == len(grid[0]) - 1 or grid[i][j + 1] != grid[i][j]:
        result_p += 1
    else:
        a, p = area(i, j + 1)
        result_a += a
        result_p += p

    return result_a, result_p


total = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        a, p = area(i, j)
        total += a * p

print(total)
