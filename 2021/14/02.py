with open("input") as f:
    template = f.readline().strip()
    f.readline()
    insertions = {k: v for k, v in [line.strip().split(" -> ") for line in f.readlines()]}

pairs = {}
for pair in zip(template, template[1:]):
    if pair[0] + pair[1] not in pairs:
        pairs[pair[0] + pair[1]] = 0
    pairs[pair[0] + pair[1]] += 1

def step(pairs, count):
    if count == 0:
        return pairs

    newPairs = {}
    for pair in pairs:
        p1, p2 = pair[0] + insertions[pair], insertions[pair] + pair[1]
        if p1 not in newPairs:
            newPairs[p1] = 0
        if p2 not in newPairs:
            newPairs[p2] = 0
        newPairs[p1] += pairs[pair]
        newPairs[p2] += pairs[pair]

    return step(newPairs, count - 1)

pairs = step(pairs, 40)
counts = {template[-1]: 1}

for pair in pairs:
    if pair[0] not in counts:
       counts[pair[0]] = 0
    counts[pair[0]] += pairs[pair]

print(max(counts.values()) - min(counts.values()))
