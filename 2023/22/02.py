class Point:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)


bricks = [line.strip().split('~') for line in open('input').readlines()]
bricks = [(Point(*p1.split(',')), Point(*p2.split(','))) for p1, p2 in bricks]

def intersect(brick1, brick2):
    if brick1[0].x > brick2[1].x or brick1[1].x < brick2[0].x:
        return False
    
    if brick1[0].y > brick2[1].y or brick1[1].y < brick2[0].y:
        return False
    
    if brick1[0].z > brick2[1].z or brick1[1].z < brick2[0].z:
        return False
    
    return True


def slide_down(brick, delta):
    return (Point(brick[0].x, brick[0].y, brick[0].z - delta), Point(brick[1].x, brick[1].y, brick[1].z - delta))


def fall(brick):
    if min(brick[0].z, brick[1].z) == 1:
        return 0

    result, orig = 0, brick
    while True:
        brick = slide_down(brick, 1)
        for b in bricks:
            if b == orig:
                continue

            if intersect(brick, b):
                return result

        result += 1
        if min(brick[0].z, brick[1].z) == 1:
            return result


bricks = sorted(bricks, key=lambda b: min(b[0].z, b[1].z))

for i, brick in enumerate(bricks):
    if delta := fall(brick):
        bricks[i] = slide_down(brick, delta)

supported_by = {}
for i, brick in enumerate(bricks):
    supported_by[i] = set()

    if brick[0].z == 1 or brick[1].z == 1:
        continue

    nb = slide_down(brick, 1)
    for j, b in enumerate(bricks):
        if i == j:
            continue

        if intersect(nb, b):
            supported_by[i].add(j)


def count_falling(i):
    sup = {k: supported_by[k].copy() for k in supported_by.keys()}
    queue, removed = [i], set()
    while queue:
        i = queue.pop(0)
        
        if i in removed:
            continue
        removed.add(i)

        for j in sup:
            if i in sup[j]:
                sup[j].remove(i)
                if len(sup[j]) == 0:
                    queue.append(j)

    return len(removed) - 1


print(sum(count_falling(i) for i in range(len(supported_by))))
