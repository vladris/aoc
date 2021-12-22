x, y = open("input").readline()[13:].strip().split(", ")

areax = map(int, x[2:].split(".."))
areay = map(int, y[2:].split(".."))

def hit(vx, vy):
    x, y = 0, 0
    while x <= areax[1] and y >= areay[0]:
        x += vx
        y += vy

        if vx != 0:
            vx = vx - 1 if vx > 0 else vx + 1
        vy -= 1

        if areax[0] <= x and x <= areax[1] and areay[0] <= y and y <= areay[1]:
            return True
    return False

count = 0
for x in range(1, areax[1] + 1):
    for y in range(areay[0], -areay[0]):
        if hit(x, y):
            count += 1

print(count)
