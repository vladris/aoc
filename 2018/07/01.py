dep = {}
for line in open("input"):
    p, c = line[5], line[36]
    if c not in dep:
        dep[c] = set()
    if p not in dep:
        dep[p] = set()
    dep[c].add(p)

while dep:
    p = "Z"
    for k in dep:
        if not dep[k]:
            p = min(p, k)

    del dep[p]
    for k in dep:
        dep[k].difference_update(p)
    print(p, end="")
