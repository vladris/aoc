dep = {}
for line in open("input"):
    p, c = line[5], line[36]
    if c not in dep:
        dep[c] = set()
    if p not in dep:
        dep[p] = set()
    dep[c].add(p)

done, sec, workers, idle = set(), 0, {}, 5
while len(done) < len(dep):
    for k in workers:
        workers[k] += 1
        if workers[k] == ord(k) - ord("A") + 61:
            done.add(k)
            idle += 1

    for k in done:
        if k in workers:
            del workers[k]

    while idle > 0:
        p = chr(ord("Z") + 1)
        for k in dep:
            if k in done or k in workers:
                continue
            if done.issuperset(dep[k]):
                p = min(p, k)
        if p == chr(ord("Z") + 1):
            break
        workers[p] = 0
        idle -= 1

    sec += 1

print(sec - 1)