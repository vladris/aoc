def in_range(x1, y1, x2, y2):
    return x2 <= x1 <= y2 or x2 <= y1 <= y2 or \
        x1 <= x2 <= y1 or x1 <= y2 <= y1


total = 0
for line in open("input").readlines():
    r1, r2 = line.strip().split(',')
    x1, y1 = r1.split('-')
    x2, y2 = r2.split('-')
    total += in_range(int(x1), int(y1), int(x2), int(y2))

print(total)
