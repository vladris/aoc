directions = [s.strip() for s in open("input").read().split(",")]

x, y, h = 0, 0, 0

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for d in directions:
    if d[0] == "L":
        h = h - 1 if h > 0 else 3
    elif d[0] == "R":
        h = h + 1 if h < 3 else 0

    x += int(d[1:]) * move[h][0]
    y += int(d[1:]) * move[h][1]

print(abs(x) + abs(y))