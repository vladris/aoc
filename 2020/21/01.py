ings, algs, counts = set(), {}, {}
for line in open("input").readlines():
    ing, alg = line.strip().split("(contains ")
    ing, alg = ing.strip().split(" "), alg.strip(")").split(", ")
    ings = ings.union(ing)
    for i in ing:
        if i not in counts:
            counts[i] = 0
        counts[i] += 1
    for a in alg:
        if a not in algs:
            algs[a] = set(ing)
        algs[a].intersection_update(set(ing))

alla = set()
for a in algs:
    alla = alla.union(algs[a])

total = 0
for safe in ings - alla:
    total += counts[safe]

print(total)
