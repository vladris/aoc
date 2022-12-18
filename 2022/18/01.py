cubes = [tuple(map(int, l.strip().split(','))) for l in open('input').readlines()]

surface = 0
for c1 in cubes:
    surface += 6
    for c2 in cubes:
        if abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2]) == 1:
            surface -= 1

print(surface)
