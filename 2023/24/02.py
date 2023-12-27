hails = []
for line in open('input').readlines():
    pos, vec = line.strip().split(' @ ')
    x, y, z = tuple(map(int, pos.split(', ')))
    dx, dy, dz = tuple(map(int, vec.split(', ')))
    hails.append(((x, y, z), (dx, dy, dz)))


def find(rng):
    for dx in range(-rng, rng):
        for dy in range(-rng, rng):
            x1, y1, z1 = hails[0][0]
            dx1, dy1, dz1 = hails[0][1]
            x2, y2, z2 = hails[1][0]
            dx2, dy2, dz2 = hails[1][1]

            # x + dx * t1 = x1 + dx1 * t1
            # y + dy * t1 = y1 + dy1 * t1
            # x + dx * t2 = x2 + dx2 * t2
            # y + dy * t2 = y2 + dy2 * t2

            # x = x1 + t1 * (dx1 - dx)        
            # t1 = (x2 - x1 + t2 * (dx2 - dx)) / (dx1 - dx)
            # y = y1 + (x2 - x1 + t2 * (dx2 - dx)) * (dy1 - dy) / (dx1 - dx)
            # t2 = ((y2 - y1) * (dx1 - dx) - (dy1 - dy) * (x2 - x1)) / ((dy1 - dy) * (dx2 - dx) + (dy - dy2) * (dx1 - dx))

            if (dy1 - dy) * (dx2 - dx) + (dy - dy2) * (dx1 - dx) == 0:
                continue

            t2 = ((y2 - y1) * (dx1 - dx) - (dy1 - dy) * (x2 - x1)) / ((dy1 - dy) * (dx2 - dx) + (dy - dy2) * (dx1 - dx))

            if not t2.is_integer() or t2 < 0:
                continue

            if (dx1 - dx) == 0:
                continue

            y = y1 + (x2 - x1 + t2 * (dx2 - dx)) * (dy1 - dy) / (dx1 - dx)

            if not y.is_integer():
                continue

            t1 = (x2 - x1 + t2 * (dx2 - dx)) / (dx1 - dx)

            if not t1.is_integer() or t1 < 0:
                continue

            x = x1 + t1 * (dx1 - dx)        

            # z + dz * t1 = z1 + dz1 * t1
            # z + dz * t2 = z2 + dz2 * t2        

            # dz = (z1 + dz1 * t1 - z2 - dz2 * t2) / (t1 - t2)
            # z = z1 + dz1 * t1 - dz * t1

            if t1 == t2:
                continue

            dz = (z1 + dz1 * t1 - z2 - dz2 * t2) / (t1 - t2)

            if not dz.is_integer():
                continue

            z = z1 + dz1 * t1 - dz * t1

            valid = True
            for hail in hails[2:]:
                xi, yi, zi = hail[0]
                dxi, dyi, dzi = hail[1]

                if dx != dxi:
                    ti = (xi - x) / (dx - dxi)
                elif dy != dyi:
                    ti = (yi - y) / (dy - dyi)
                elif dz != dzi:
                    ti = (zi - z) / (dz - dzi)
                else:
                    valid = False
                    break

                if not ti.is_integer() or ti < 0:
                    valid = False
                    break

                if x + dx * ti != xi + dxi * ti or y + dy * ti != yi + dyi * ti or z + dz * ti != zi + dzi * ti:
                    valid = False
                    break

            if valid:
                return int(x + y + z)


print(find(1000))
