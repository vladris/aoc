ranges, ids = open("input").read().split("\n\n")
ranges = [tuple(map(int, r.split("-"))) for r in ranges.split("\n")]
ids = [int(i) for i in ids.split("\n")]

total = 0
for i in ids:
    in_range = False
    for r in ranges:
        if r[0] <= i <= r[1]:
            in_range = True
            break

    if in_range:
        total += 1

print(total)
