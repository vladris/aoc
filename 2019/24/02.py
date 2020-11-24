def line_to_list(line):
    return [1 if c == '#' else 0 for c in line]

def make_empty():
    return [[0 for _ in range(5)] for _ in range(5)]

grids = [make_empty() for _ in range(200)] + [[line_to_list(line.strip()) for line in open('input').readlines()]] + [make_empty() for _ in range(200)]

def get(src_d, src_x, src_y, dest_x, dest_y):
    if dest_x == 2 and dest_y == 2:
        if src_x == 1 and src_y == 2:
            return sum([grids[src_d + 1][0][y] for y in range(5)])
        elif src_x == 3 and src_y == 2:
            return sum([grids[src_d + 1][4][y] for y in range(5)])
        elif src_x == 2 and src_y == 1:
            return sum([grids[src_d + 1][x][0] for x in range(5)])
        elif src_x == 2 and src_y == 3:
            return sum([grids[src_d + 1][x][4] for x in range(5)])
    elif dest_x == -1:
        return grids[src_d - 1][1][2] 
    elif dest_x == 5:
        return grids[src_d - 1][3][2]
    elif dest_y == -1:
        return grids[src_d - 1][2][1]
    elif dest_y == 5:
        return grids[src_d - 1][2][3]
    else:
        return grids[src_d][dest_x][dest_y]

def count():
    total = 0
    for grid in grids:
        for line in grid:
            for cell in line:
                total += cell
    return total

def step():
    updates = []
    for d in range(1, len(grids) - 1):
        for i in range(5):
            for j in range(5):
                if i == 2 and j == 2:
                    continue

                c = get(d, i, j, i - 1, j)
                c += get(d, i, j, i + 1, j)
                c += get(d, i, j, i, j - 1)
                c += get(d, i, j, i, j + 1)

                if grids[d][i][j] == 1 and c != 1:
                    updates.append((0, d, i, j))
                elif grids[d][i][j] == 0 and (c == 1 or c == 2):
                    updates.append((1, d, i, j))

    for v, d, i, j in updates:
        grids[d][i][j] = v

for _ in range(200):
    step()

print(count())