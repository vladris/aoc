input = [(i[0], int(i[1:-1])) for i in open("input").readlines()]

x, y, h = 0, 0, "E"

turn = {
    "L": { "E": "N", "N": "W", "W": "S", "S": "E" },
    "R": { "E": "S", "S": "W", "W": "N", "N": "E" }
}

for d, v in input:
    if d == "F": d = h

    if d == "N": y -= v
    elif d == "S": y += v
    elif d == "E": x += v
    elif d == "W": x -= v
    else:
        while v > 0:
            h = turn[d][h]
            v -= 90

print(abs(x) + abs(y))
