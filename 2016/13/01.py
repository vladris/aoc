def isopen(x, y):
    n = x*x + 3*x + 2*x*y + y + y*y + 1352
    b = 0
    while n:
        if n & 1:
            b += 1
        n >>= 1
    return b % 2 == 0

dist = {}

def move(x, y, d):
    if not isopen(x, y):
        return

    if (x, y) in dist and dist[(x, y)] <= d:
        return

    dist[(x, y)] = d

    if x > 0:
        move(x - 1, y, d + 1)
    if y > 0:
        move(x, y - 1, d + 1)
    move(x + 1, y, d + 1)
    move(x, y + 1, d + 1)

move(1, 1, 0)
print(dist[(31, 39)])