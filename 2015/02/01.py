lines = open("input").readlines()

total = 0
for line in lines:
    l, w, h = map(int, line.split("x"))
    total += 2 * l * w + 2 * l * h + 2 * w * h + min(l * w, l * h, w * h)

print(total)