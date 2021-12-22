x, y = open("input").readline()[13:].strip().split(", ")

# x, y = "x=20..30", "y=-10..-5"

areax = map(int, x[2:].split(".."))
areay = map(int, y[2:].split(".."))

def hit(vx, vy):
    x, y, maxy = 0, 0, 0
    while x <= areax[1] and y >= areay[0]:
        x += vx
        y += vy
        maxy = max(maxy, y)

        if vx != 0:
            vx = vx - 1 if vx > 0 else vx + 1
        vy -= 1

        if areax[0] <= x and x <= areax[1] and areay[0] <= y and y <= areay[1]:
            return True, maxy
    return False, maxy

best = 0
for x in range(1, areax[1] + 1):
    for y in range(areay[0], -areay[0]):
        k, my = hit(x, y)
        if k: best = max(best, my)

print(best)
