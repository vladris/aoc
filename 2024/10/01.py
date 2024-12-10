map = [list(map(int, list(line.strip()))) for line in open("input").readlines()]
map = [[-1] + line + [-1] for line in map]
map = [[-1] * len(map[0])] + map + [[-1] * len(map[0])]

def hike(i, j):
    if map[i][j] == 9:
        return {(i, j)}

    d = map[i][j] + 1
    
    result = set()
    if map[i - 1][j] == d:
        result |= hike(i - 1, j)
    if map[i][j - 1] == d:
        result |= hike(i, j - 1)
    if map[i + 1][j] == d:
        result |= hike(i + 1, j)
    if map[i][j + 1] == d:
        result |= hike(i, j + 1)

    return result


total = 0
for i, line in enumerate(map):
    for j, c in enumerate(line):
        if c == 0:
            total += len(hike(i, j))

print(total)
