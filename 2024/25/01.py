schematics = [s.split("\n") for s in open("input").read().split("\n\n")]

def overlap(s1, s2):
    for l1, l2 in zip(s1, s2):
        for c1, c2 in zip(l1, l2):
            if c1 == "#" and c2 == "#":
                return True
    return False


total = 0
for i in range(len(schematics)):
    for j in range(i + 1, len(schematics)):
        if not overlap(schematics[i], schematics[j]):
            total += 1

print(total)
