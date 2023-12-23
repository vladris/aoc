digs = [line.strip().split(' ')[-1][2:-1] for line in open('input').readlines()]
digs = [(int(line[-1]), int(line[:-1], 16)) for line in digs]

x, y, points = 0, 0, [(0, 0)]
for dig in digs:
    match dig[0]:
        case 0: x += dig[1]
        case 1: y += dig[1]
        case 2: x -= dig[1]
        case 3: y -= dig[1]

    if dig[1] < 10:
        print(dig[1])
    points.append((x, y))

xs, ys = sorted({x for x, _ in points}), sorted({y for _, y in points})

queue, total, visited = [(1, 1)], 0, set()
while queue:
    x, y = queue.pop(0)

    e = min([i for i in xs if i > x])
    s = max([i for i in ys if i < y])
    w = max([i for i in xs if i < x])
    n = min([i for i in ys if i > y])

    if (n, e) in visited:
        continue
    visited.add((n, e))

    total += (e - w - 1) * (n - s - 1)

    found_n, found_s, found_e, found_w = False, False, False, False
    for l1, l2 in zip(points, points[1:]):
        if l1[1] == l2[1]:
            if l1[1] == n and (l1[0] < x < l2[0] or l2[0] < x < l1[0]):
                found_n = True
            if l1[1] == s and (l1[0] < x < l2[0] or l2[0] < x < l1[0]):
                found_s = True
        elif l1[0] == l2[0]:
            if l1[0] == e and (l1[1] < y < l2[1] or l2[1] < y < l1[1]):
                found_e = True
            if l1[0] == w and (l1[1] < y < l2[1] or l2[1] < y < l1[1]):
                found_w = True
                
    if not found_n:
        total += e - w - 1
        queue.append((x, n + 1))
    if not found_s:
        queue.append((x, s - 1))
    if not found_e:
        total += n - s - 1
        queue.append((e + 1, y))
    if not found_w:
        queue.append((w - 1, y))

    if not found_n and not found_e:
        if (e, n) not in points:
            total += 1

total += sum([dig[1] for dig in digs])

print(total)
