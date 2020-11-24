def val(chem):
    count, name = chem.strip().split(' ')
    return int(count), name

reactions = {}
for line in open('input').readlines():
    inp, out = line.split('=>')
    reactions[val(out)] = [val(i) for i in inp.split(',')]

def key(chem):
    for c in reactions:
        if c[1] == chem:
            return c

depth = {}
def compute_depth(chem):
    depth[chem] = 0 if chem == 'ORE' else 1 + max([compute_depth(c[1]) for c in reactions[key(chem)]])
    return depth[chem]

compute_depth('FUEL')

chems = reactions[key('FUEL')]
while len(chems) > 1:
    replace = max(chems, key=lambda c: depth[c[1]])
    chems.remove(replace)
    count = replace[0] / key(replace[1])[0]
    chems = sorted(chems + [(c[0] * count, c[1]) for c in reactions[key(replace[1])]], key=lambda c: c[1])

    i = 0
    while i < len(chems) - 1:
        if chems[i][1] == chems[i + 1][1]:
            chems[i] = (chems[i][0] + chems[i + 1][0], chems[i][1])
            chems.remove(chems[i + 1])
        else:
            i += 1
            
print(int(10 ** 12 / chems[0][0]))