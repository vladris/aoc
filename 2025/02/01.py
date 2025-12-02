import math

inp = open("input").read().split(",")
inp = [(int(r[0]), int(r[1])) for r in list(map(lambda r: r.split("-"), inp))]

total = 0

for r in inp:
    for i in range(r[0], r[1] + 1):
        d = int(math.log(i, 10)) + 1
        if d % 2 == 1:
            continue
        d = d // 2
        if i // (10**d) == i % (10**d):
            total += i

print(total)