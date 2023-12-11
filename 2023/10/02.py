grid = [line.strip() for line in open('input').readlines()]

def update(ln, i, c):
    grid[ln] = grid[ln][:i] + c + grid[ln][i + 1:]

start = None
for i, line in enumerate(grid):
    if 'S' in line:
        start = (i, line.index('S'))

        if grid[start[0] - 1][start[1]] in '7|F':
            if grid[start[0]][start[1] - 1] in 'L-F':
                update(start[0], start[1], 'J')
            elif grid[start[0] + 1][start[1]] in 'J|L':
                update(start[0], start[1], '|')
            elif grid[start[0]][start[1] + 1] in '7-J':
                update(start[0], start[1], 'L')
        elif grid[start[0]][start[1] - 1] in 'L-F':
            if grid[start[0] + 1][start[1]] in 'J|L':
                update(start[0], start[1], '7')
            elif grid[start[0]][start[1] + 1] in '7-J':
                update(start[0], start[1], '-')
        elif grid[start[0] + 1][start[1]] in 'J|L':
            if grid[start[0]][start[1] + 1] in '7-J':
                update(start[0], start[1], 'F')
        break

visited = set()
queue = [start]

while queue:
    pipe = queue.pop(0)

    if pipe in visited:
        continue

    if pipe[0] == -1 or pipe[1] == -1 or pipe[0] == len(grid) or pipe[1] == len(grid[0]):
        continue

    visited.add((pipe[0], pipe[1]))

    if grid[pipe[0]][pipe[1]] in 'J|L':
        queue.append((pipe[0] - 1, pipe[1]))
    if grid[pipe[0]][pipe[1]] in '7|F':
        queue.append((pipe[0] + 1, pipe[1]))
    if grid[pipe[0]][pipe[1]] in 'L-F':
        queue.append((pipe[0], pipe[1] + 1))
    if grid[pipe[0]][pipe[1]] in '7-J':
        queue.append((pipe[0], pipe[1] - 1))


def scan_line(ln):
    total, i, inside, start = 0, -1, False, None
    while i < len(grid[0]) - 1:
        i += 1
        if (ln, i) not in visited:
            if inside:
                total += 1
        else:
            if grid[ln][i] == '|':
                inside = not inside
                continue
            
            # grid[ln][i] in 'LF'
            start = grid[ln][i]
            i += 1
            while grid[ln][i] == '-':
                i += 1

            if start == 'L' and grid[ln][i] == '7' or \
               start == 'F' and grid[ln][i] == 'J':
               inside = not inside
    return total

print(sum([scan_line(ln) for ln in range(len(grid))]))
