ranges, _ = open("input").read().split("\n\n")
ranges = [tuple(map(int, r.split("-"))) for r in ranges.split("\n")]

modified = True
while modified:
    modified = False
    for r1 in range(len(ranges) - 1):
        for r2 in range(r1 + 1, len(ranges)):
            if ranges[r1][1] < ranges[r2][0] or ranges[r1][0] > ranges[r2][1]:
                continue
            r = (min(ranges[r1][0], ranges[r2][0]), max(ranges[r1][1], ranges[r2][1]))
            ranges.pop(r2)
            ranges.pop(r1)
            ranges.append(r)
            modified = True
            break
        if modified:
            break

print(sum(r[1] - r[0] + 1 for r in ranges))
