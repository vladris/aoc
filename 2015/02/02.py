lines = open("input").readlines()

total = 0
for line in lines:
    l, w, h = map(int, line.split("x"))
    total += 2 * min(l + w, l + h, w + h) + l * w * h

print(total)