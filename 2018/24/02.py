import re

class Group:
    def __init__(self, team, units, hp, attack, attack_type, initiative):
        self.team = team
        self.units = units
        self.hp = hp
        self.attack = attack
        self.attack_type = attack_type
        self.initiative = initiative
        self.weak = []
        self.immune = []

    def add_weak(self, weak):
        self.weak = weak

    def add_immune(self, immune):
        self.immune = immune

    def pow(self):
        if self.team == "imm":
            return self.units * (self.attack + boost) 
        else:
            return self.units * self.attack

    def __str__(self):
        return f"{self.team} {self.units} {self.hp} {self.attack} {self.attack_type} {self.immune} {self.weak}"

def readgroup(f):
    f.readline()
    while True:
        line = f.readline().strip()
        if not line:
            return
        yield line

def parse(team, line):
    m = re.match(r"(\d+) units each with (\d+) hit points( \(.*\))? with an attack that does (\d+) (\w+) damage at initiative (\d+)", line)
    g = Group(team, int(m[1]), int(m[2]), int(m[4]), m[5], int(m[6]))
    if m[3]:
        ps = m[3].strip(" ()").split(";")
        for p in ps:
            p = p.strip()
            if p.startswith("weak to "):
                g.add_weak(p[8:].split(", "))
            else:
                g.add_immune(p[10:].split(", "))
    return g

def damage(src, dest):
    if src.attack_type in dest.immune:
        return 0

    dmg = src.pow()
    if src.attack_type in dest.weak:
        dmg *= 2

    return dmg

def selnext(groups):
    while groups:
        n = groups[0]
        for g in groups:
            if g.pow() > n.pow():
                n = g
            elif g.pow() == n.pow() and g.initiative > n.initiative:
                n = g
        groups.remove(n)
        yield n

def seltarget(g, targets):
    if not targets:
        return None

    bt = targets[0]
    for t in targets:
        if damage(g, t) > damage(g, bt):
            bt = t
        elif damage(g, t) == damage(g, bt):
            if t.pow() > bt.pow():
                bt = t
            elif t.pow() == bt.pow():
                if t.initiative > bt.initiative:
                    bt = t
    return bt if damage(g, bt) != 0 else None

def selcombat(imm, inf):
    immt, inft, combat = imm[:], inf[:], {}
    for g in selnext(imm + inf):
        if g.team == "imm":
            t = seltarget(g, inft)
            if t:
                inft.remove(t)
                combat[g] = t
        else:
            t = seltarget(g, immt)
            if t:
                immt.remove(t)
                combat[g] = t
    return combat

def run():
    imm, inf = [], []
    with open("input") as f:
        for line in readgroup(f):
            imm.append(parse("imm", line))

        for line in readgroup(f):
            inf.append(parse("inf", line))

    while True:
        combat = selcombat(imm, inf)
        if not combat:
            break

        progress = False
        for g in sorted(combat.keys(), key=lambda g: g.initiative, reverse=True):
            if g not in combat:
                continue

            dmg = damage(g, combat[g])
            casualties = dmg // combat[g].hp
            if casualties:
                progress = True
            combat[g].units -= casualties
            if combat[g].units <= 0 and combat[g] in combat:
                del combat[combat[g]]

        if not progress:
            return 0

        imm = list(filter(lambda g: g.units > 0, imm))
        inf = list(filter(lambda g: g.units > 0, inf))

    return sum(map(lambda g: g.units, imm))

boost, result = 0, 0
while not result:
    boost += 1
    result = run()

print(result)
