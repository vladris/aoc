from itertools import permutations
import re

input = open("input").readlines()

peeps = set()
happiness = {}

for line in input:
    m = re.match(r"(\w+).*(gain|lose) (\d+).*\s(\w+)\.", line)
    h = int(m[3]) * (1 if m[2] == "gain" else -1)
    happiness[m[1] + "-" + m[4]] = h
    peeps.add(m[1])

for p in peeps:
    happiness[p + "-me"] = 0
    happiness["me-" + p] = 0

peeps.add("me")

best = 0
for p in permutations(peeps):
    best = max(best, sum(map(
        lambda x: happiness[x[0] + "-" + x[1]] + happiness[x[1] + "-" + x[0]],
        zip(p, (*p[1:], p[0])))))

print(best)