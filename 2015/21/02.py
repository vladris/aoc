from itertools import combinations

weapons = [
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
]

armors = [
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5)
]

rings = [
    (0, 0, 0),
    (0, 0, 0),
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
]

def equip():
    global weapon, armors, rings
    for weapon in weapons:
        for armor in armors:
            for r1, r2 in combinations(rings, 2):
                yield (weapon[0] + armor[0] + r1[0] + r2[0],
                    weapon[1] + armor[1] + r1[1] + r2[1],
                    weapon[2] + armor[2] + r1[2] + r2[2])

def hit(a, b):
    dmg = max(1, a[1] - b[2])
    return b[0] - dmg, b[1], b[2]

def fight(you, boss):
    boss = hit(you, boss)
    if boss[0] <= 0:
        return True
    you = hit(boss, you)
    if you[0] <= 0:
        return False
    return fight(you, boss)

max_cost = 0
for cost, dmg, arm in equip():
    if not fight((100, dmg, arm), (100, 8, 2)):
        max_cost = max(max_cost, cost)

print(max_cost)
