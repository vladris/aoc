gsn = 5235

def power(x, y):
    global gsn

    p = ((x + 10) * y + gsn) * (x + 10)
    if p > 100:
        p = p // 100 % 10
    return p - 5

pow = {}
for x in range(1, 301):
    for y in range(1, 301):
        pow[(x, y)] = power(x, y)

sq, col, row = {}, {}, {}

def square(x, y, w):
    w -= 1

    if (x, y) not in sq:
        sq[(x, y)] = 0
    total = sq[(x, y)] 

    if (x + w, y) not in col:
        col[(x + w, y)] = 0
    total += col[(x + w, y)]

    if (x, y + w) not in row:
        row[(x, y + w)] = 0
    total += row[(x, y + w)]

    total += power(x + w, y + w)

    col[(x + w, y)] += power(x + w, y + w)
    row[(x, y + w)] += power(x + w, y + w)
    sq[(x, y)] = total

    return total

bx, by, bw, best = 0, 0, 0, 0
for w in range(1, 301):
    for x in range(1, 301 - w):
        for y in range(1, 301 - w):
            p = square(x, y, w)
            if p > best:
                bx, by, bw, best = x, y, w, p

print(f"{bx},{by},{bw}")
