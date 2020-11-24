w1, w2 = [line.strip().split(',') for line in open('input').readlines()]

def line(x, y, to):
    d = int(to[1:])
    if to[0] == 'R': return x + d, y, [(x, y), (x + d, y)]
    if to[0] == 'L': return x - d, y, [(x - d, y), (x, y)]
    if to[0] == 'U': return x, y - d, [(x, y - d), (x, y)]
    if to[0] == 'D': return x, y + d, [(x, y), (x, y + d)]

def intersection(line1, line2):
    if line1[0][0] <= line2[0][0] and line1[1][0] >= line2[0][0] \
        and line1[0][1] >= line2[0][1] and line1[0][1] <= line2[1][1]:
        return abs(line2[0][0]) + abs(line1[0][1])
    if line1[0][1] <= line2[0][1] and line1[1][1] >= line2[0][1] \
        and line1[0][0] >= line2[0][0] and line1[0][0] <= line2[1][0]:
        return abs(line1[0][0]) + abs(line2[0][1])
    return 0

x, y, lines = 0, 0, []
for to in w1:
    x, y, ln = line(x, y, to)
    lines.append(ln)

x, y, dist = 0, 0, 10 ** 6
for to in w2:
    x, y, ln = line(x, y, to)
    for i in lines:
        d = intersection(ln, i)
        if d:
            dist = min(dist, d)

print(dist)
