points = []
for y, line in enumerate(open('input').readlines()):
    for x, c in enumerate(line):
        if c == '#':
            points.append((x, y))

def slope(p1, p2):
    return (p1[1] - p2[1]) / (p1[0] - p2[0]) if p1[0] != p2[0] else None

def direction(p1, p2):
    return p1[0] < p2[0] if p1[0] != p2[0] else p1[1] < p2[1]

pt, best = None, 0
for point in points:
    visible = len(set([(slope(point, p), direction(point, p)) for p in points if p != point]))
    if visible > best:
        pt, best = point, visible
    
print(pt, best)
