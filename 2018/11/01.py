gsn = 5235

def power(x, y):
    global gsn

    p = ((x + 10) * y + gsn) * (x + 10)
    if p > 100:
        p = p // 100 % 10
    return p - 5

def square(x, y):
    total = 0
    for i in range(3):
        for j in range(3):
            total += power(x + i, y + j)
    return total

bx, by, best = 0, 0, 0
for x in range(1, 299):
    for y in range(1, 299):
        p = square(x, y)
        if p > best:
            bx, by, best = x, y, p

print(f"{bx},{by}")
