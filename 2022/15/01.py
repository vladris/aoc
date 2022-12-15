import re

y, segments = 2000000, set()

for line in open('input').readlines():
    m = re.match('Sensor at x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+)$', line)
    sx, sy, bx, by = map(int, m.groups())
    radius = abs(sx - bx) + abs(sy - by)

    if abs(sy - y) <= radius:
        segments.add(((sx - (radius - abs(sy - y)),
                     (sx + (radius - abs(sy - y))))))


def intersect(s1, s2):
    return s1[1] >= s2[0] and s2[1] >= s1[0]


def union(s1, s2):
    return (min(s1[0], s2[0]), max(s1[1], s2[1]))


done = False
while not done:
    done = True
    for s1 in segments:
        for s2 in segments:
            if s1 == s2:
                continue

            if intersect(s1, s2):
                segments.remove(s1)
                segments.remove(s2)
                segments.add(union(s1, s2))
                done = False
                break

        if not done:
            break

print(sum([s[1] - s[0] for s in segments]))
