from functools import reduce

with open("input") as f:
    scanners = []
    while True:
        line = f.readline()
        if not line:
            break
        beacons = []
        while True:
            line = f.readline().strip()
            if not line:
                break
            beacons.append(tuple(map(int, line.split(","))))
        scanners.append(beacons)

def rotate(dir, pt):
    return {
        0: (pt), 1: (pt[0], -pt[1], -pt[2]), 2: (pt[0], pt[2], -pt[1]), 3: (pt[0], -pt[2], pt[1]), 
        4: (-pt[0], pt[1], -pt[2]), 5: (-pt[0], -pt[1], pt[2]), 6: (-pt[0], -pt[2], -pt[1]), 7: (-pt[0], pt[2], pt[1]),
        8: (pt[1], pt[2], pt[0]), 9: (pt[1], -pt[2], -pt[0]), 10: (pt[1], pt[0], -pt[2]), 11: (pt[1], -pt[0], pt[2]),
        12: (-pt[1], pt[2], -pt[0]), 13: (-pt[1], -pt[2], pt[0]), 14: (-pt[1], -pt[0], -pt[2]), 15: (-pt[1], pt[0], pt[2]),
        16: (pt[2], pt[0], pt[1]), 17: (pt[2], -pt[0], -pt[1]), 18: (pt[2], pt[1], -pt[0]), 19: (pt[2], -pt[1], pt[0]),
        20: (-pt[2], pt[0], -pt[1]), 21: (-pt[2], -pt[0], pt[1]), 22: (-pt[2], -pt[1], -pt[0]), 23: (-pt[2], pt[1], pt[0]),
    }[dir]

def translate(by, pt):
    return pt[0] - by[0], pt[1] - by[1], pt[2] - by[2]

def overlap(s1, s2):
    count = 0
    for p1 in s1:
        for p2 in s2:
            if p1 == p2:
                count += 1
                if count >= 12:
                    return True
    return False

def match(i1, i2):
    s1 = scanners[i1]
    for sr in rot[i2]:
        for pi1 in range(len(s1) - 11):
            for pi2 in range(len(sr) - 11):
                p1, p2 = s1[pi1], sr[pi2]
                pd = p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]
                st = [translate(pd, pt) for pt in sr]

                if overlap(s1, st):
                    scanners[i2] = sr
                    return pd

rot = {i: [[rotate(d, pt) for pt in scanners[i]] for d in range(24)] for i in range(1, len(scanners))}

tovisit, loc = [0], {0: (0, 0, 0)}
while tovisit:
    p = tovisit.pop(0)
    for i in range(len(scanners)):
        if i in loc:
            continue
        pd = match(p, i)
        if not pd:
            continue
        loc[i] = (loc[p][0] - pd[0], loc[p][1] - pd[1], loc[p][2] - pd[2])
        if i not in tovisit:
            tovisit.append(i)

dist = 0
for s1 in loc:
    for s2 in loc:
        if s1 == s2:
            continue
        dist = max(dist, abs(loc[s1][0] - loc[s2][0]) + abs(loc[s1][1] - loc[s2][1]) + abs(loc[s1][2] - loc[s2][2]))

print(dist)
