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

best, bestcount, g = 0, 0, None
for guard in guards:
    mins = [0] * 60
    for start, end in guards[guard]:
        while start < end:
            mins[start] += 1
            if mins[start] > bestcount:
                best, bestcount, g = start, mins[start], guard
            start += 1

print(int(g.split("#")[1]) * best)
