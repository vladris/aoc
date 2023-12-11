grid = [line.strip() for line in open('input').readlines()]

start = None
for i, line in enumerate(grid):
    if 'S' in line:
        start = (i, line.index('S'))
        break

visited = {}
queue = []

if start[0] > 0 and grid[start[0] - 1][start[1]] in '7|F':
    queue.append((start[0] - 1, start[1], 1))
if start[1] > 0 and grid[start[0]][start[1] - 1] in 'L-F':
    queue.append((start[0], start[1] - 1, 1))
if start[0] < len(grid) - 1 and grid[start[0] + 1][start[1]] in 'J|L':
    queue.append((start[0] + 1, start[1], 1))
if start[1] < len(grid[0]) - 1 and grid[start[0]][start[1] + 1] in '7-J':
    queue.append((start[0], start[1] + 1, 1))

while queue:
    pipe = queue.pop(0)

    if (pipe[0], pipe[1]) in visited:
        continue

    if pipe[0] == -1 or pipe[1] == -1 or pipe[0] == len(grid) or pipe[1] == len(grid[0]):
        continue

    visited[(pipe[0], pipe[1])] = pipe[2]

    if grid[pipe[0]][pipe[1]] in 'J|L':
        queue.append((pipe[0] - 1, pipe[1], pipe[2] + 1))
    if grid[pipe[0]][pipe[1]] in '7|F':
        queue.append((pipe[0] + 1, pipe[1], pipe[2] + 1))
    if grid[pipe[0]][pipe[1]] in 'L-F':
        queue.append((pipe[0], pipe[1] + 1, pipe[2] + 1))
    if grid[pipe[0]][pipe[1]] in '7-J':
        queue.append((pipe[0], pipe[1] - 1, pipe[2] + 1))

print(max(visited.values()))
