input = open("input").readlines()

blocked = [tuple(map(int, line.split("-"))) for line in input]

i, total = 0, 0
while True:
    allowed = False
    while not allowed:
        allowed = True
        for b in blocked:
            if b[0] <= i <= b[1]:
                i, allowed = b[1] + 1, False
                break

    if i > 4294967295:
        break

    hi = list(filter(lambda b: b[0] > i, blocked))
    if len(hi) == 0:
        total += 4294967295 - i
        break

    m = min(hi, key=lambda b: b[0] - i)
    total += m[0] - i
    i = m[0]
    
print(total)
