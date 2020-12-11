input = open("input").readlines()

trans = {}
for line in input[:-2]:
    src, dest = line.strip().split(" => ")
    trans[dest] = src

def transform(mol, i):
    if mol == "e":
        print(i)
        exit()

    for dest in trans:
        if dest in mol:
            transform(mol.replace(dest, trans[dest], 1), i + 1)

transform(input[-1].strip(), 0)
