directions = [s.strip() for s in open("input").read().split(",")]

x, y, h, visited = 0, 0, 0, set()

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for d in directions:
    if d[0] == "L":
        h = h - 1 if h > 0 else 3
    elif d[0] == "R":
        h = h + 1 if h < 3 else 0

    d = int(d[1:])
    while d:
        x += move[h][0]
        y += move[h][1]
        d -= 1

        if (x, y) in visited:
            print(abs(x) + abs(y))
            exit()
        visited.add((x, y))
