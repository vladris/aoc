input = [(i[0], int(i[1:-1])) for i in open("input").readlines()]

x, y, wx, wy = 0, 0, 10, -1

for d, v in input:
    if d == "F":
        x += wx * v
        y += wy * v
    elif d == "N": wy -= v
    elif d == "S": wy += v
    elif d == "E": wx += v
    elif d == "W": wx -= v
    elif d == "L":
        while v > 0:
            wx, wy = wy, -wx
            v -= 90
    elif d == "R":
        while v > 0:
            wx, wy = -wy, wx
            v -= 90

print(abs(x) + abs(y))
