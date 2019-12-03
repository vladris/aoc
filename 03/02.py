w1, w2 = [line.strip().split(',') for line in open('input').readlines()]

def line(x, y, dist, to):
    d = int(to[1:])
    if to[0] == 'R': return x + d, y, dist + d, [(x, y), (x + d, y), dist]
    if to[0] == 'L': return x - d, y, dist + d, [(x, y), (x - d, y), dist]
    if to[0] == 'U': return x, y - d, dist + d, [(x, y), (x, y - d), dist]
    if to[0] == 'D': return x, y + d, dist + d, [(x, y), (x, y + d), dist]

def intersection(ln1, ln2):
    line1, line2 = sorted(ln1[:2]), sorted(ln2[:2])
    if line1[0][0] <= line2[0][0] and line1[1][0] >= line2[0][0] \
        and line1[0][1] >= line2[0][1] and line1[0][1] <= line2[1][1]:
        return ln1[2] + ln2[2] + abs(ln1[0][0] - ln2[0][0]) + abs(ln2[0][1] - ln1[0][1])
    if line1[0][1] <= line2[0][1] and line1[1][1] >= line2[0][1] \
        and line1[0][0] >= line2[0][0] and line1[0][0] <= line2[1][0]:
        return ln1[2] + ln2[2] + abs(ln1[0][1] - ln2[0][1]) + abs(ln2[0][0] - ln1[0][0])
    return 0

x, y, dist, lines = 0, 0, 0, []
for to in w1:
    x, y, dist, ln = line(x, y, dist, to)
    lines.append(ln)

x, y, dist, min_sum = 0, 0, 0, 10 ** 6
for to in w2:
    x, y, dist, ln = line(x, y, dist, to)
    for i in lines:
        d = intersection(ln, i)
        if d:
            min_sum = min(min_sum, d)

print(min_sum)
