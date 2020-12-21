algs = {}
for line in open("input").readlines():
    ing, alg = line.strip().split("(contains ")
    ing, alg = ing.strip().split(" "), alg.strip(")").split(", ")
    for a in alg:
        if a not in algs:
            algs[a] = set(ing)
        algs[a].intersection_update(set(ing))

def unique():
    for a in algs:
        if len(algs[a]) == 1:
            return a, algs.pop(a)

result = []
while algs:
    i, u = unique()
    result.append((i, list(u)[0]))
    for a in algs:
        algs[a] -= u

print(",".join([t[1] for t in sorted(result)]))
