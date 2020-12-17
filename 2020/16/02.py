import re

intervals = {}

def inside(num, interval1, interval2):
    return (interval1[0] <= num <= interval1[1]) or (interval2[0] <= num <= interval2[1])

def inside_any(num):
    return any(map(lambda i: inside(num, *i), intervals.values()))

with open("input") as f:
    while True:
        m = re.match(r"(.*): (\d+)-(\d+) or (\d+)-(\d+)", f.readline())
        if not m:
            break
        intervals[m[1]] = ((int(m[2]), int(m[3])), (int(m[4]), int(m[5])))

    f.readline()
    ticket = list(map(int, f.readline().split(",")))
    f.readline()
    f.readline()

    pos = [set(intervals.keys()) for i in range(len(intervals.keys()))]

    for line in f.readlines():
        nums = list(map(int, line.split(",")))
        if not all(map(inside_any, nums)):
            continue

        for i, num in enumerate(nums):
            p = set()
            for k in intervals:
                if inside(num, *intervals[k]):
                    p.add(k)
            pos[i].intersection_update(p)           

    final = [None for _ in range(len(intervals.keys()))]
    for _ in range(len(pos)):
        for i, s in enumerate(pos):
            if len(s) == 1:
                final[i] = list(s)[0]
                break

        pos = [p.difference(s) for p in pos]

    total = 1
    for i, d in enumerate(final):
        if d.startswith("departure"):
            total *= ticket[i]
    print(total)
