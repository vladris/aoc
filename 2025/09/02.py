points = [line.strip().split(",") for line in open("input").readlines()]
points = [(int(x), int(y)) for x, y in points]

xs = {x: i * 2 for i, x in enumerate(sorted({x for x, _ in points}))}
ys = {y: i * 2 for i, y in enumerate(sorted({y for _, y in points}))}

grid = [[" " for _ in range(max(xs.values()) + 1)] for _ in range(max(ys.values()) + 1)]
for i in range(len(points)):
    fx, fy = points[i]
    tx, ty = points[(i + 1) % len(points)]
    fx, fy, tx, ty = xs[fx], ys[fy], xs[tx], ys[ty]
    if fx == tx:
        for y in range(min(fy, ty), max(fy, ty) + 1):
            grid[y][fx] = "#"
    elif fy == ty:
        for x in range(min(fx, tx), max(fx, tx) + 1):
            grid[fy][x] = "#"

def fill(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if grid[cy][cx] != " ":
            continue
        grid[cy][cx] = "#"
        stack.append((cx + 1, cy))
        stack.append((cx - 1, cy))
        stack.append((cx, cy + 1))
        stack.append((cx, cy - 1))

start = points[0]
for p in points:
    if p[1] < start[1] or (p[1] == start[1] and p[0] < start[0]):
        start = p

fill(xs[start[0]] + 1, ys[start[1]] + 1)

def filled(pt1, pt2):
    x1, y1 = xs[pt1[0]], ys[pt1[1]]
    x2, y2 = xs[pt2[0]], ys[pt2[1]]
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if grid[y][x] != "#":
                return False
    return True

best = 0
for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        area = (1 + abs(points[i][0] - points[j][0])) * \
               (1 + abs(points[i][1] - points[j][1]))
        if area < best:
            continue
        if filled(points[i], points[j]):
            best = area
            
print(best)
