import datetime
import re

input = open("input").readlines()

def datekey(s):
    return datetime.datetime.strptime(re.match(r"\[(.*)\]", s)[1], "%Y-%m-%d %H:%M")

guards, guard, start = {}, None, None
for line in sorted(input, key=datekey):
    m = re.match(r"\[....-\d+-\d+ \d+:(\d+)\] (Guard #(\d+)|falls asleep|wakes up)", line)
    if m[2].startswith("Guard"):
        if m[2] not in guards:
            guards[m[2]] = []
        guard = m[2]
    if m[2] == "falls asleep":
        start = int(m[1])
    if m[2] == "wakes up":
        guards[guard].append((int(start), int(m[1])))

best, g = 0, None
for guard in guards:
    asleep = 0
    for start, end in guards[guard]:
        asleep += end - start
    if asleep > best:
        best, g = asleep, guard

mins = [0] * 60
for start, end in guards[g]:
    while start < end:
        mins[start] += 1
        start += 1

best = 0
for i in range(60):
    if mins[i] > mins[best]:
        best = i

print(int(g.split("#")[1]) * best)
