inp = open("input").read().split(",")
inp = [(int(r[0]), int(r[1])) for r in list(map(lambda r: r.split("-"), inp))]

total = 0

for r in inp:
    for i in range(r[0], r[1] + 1):
        si, s = str(i), 1
        while s <= len(si) // 2:
            if si[:s] * (len(si) // s) == si:
                total += i
                break
            s += 1

print(total)