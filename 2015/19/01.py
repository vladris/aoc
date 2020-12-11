input = open("input").readlines()

trans = {}
for line in input[:-2]:
    src, dest = line.split(" => ")
    if src not in trans:
        trans[src] = []
    trans[src] += [dest.strip()]

mol = input[-1].strip()
newmols = set()

for src in trans:
    start = mol.find(src, 0)
    while start != -1:
        for dest in trans[src]:
            newmols.add(mol[:start] + dest + mol[start + len(src):])
        start = mol.find(src, start + 1)

print(len(newmols))