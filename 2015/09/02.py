from itertools import permutations
import re

lines = open("input").readlines()
places = set()
graph = {}

for line in lines:
    m = re.match(r"(\w+) to (\w+) = (\d+)", line)
    graph[m[1] + "-" + m[2]] = int(m[3])
    graph[m[2] + "-" + m[1]] = int(m[3])
    places |= { m[1], m[2] }

longest = 0
paths = set()
for p in permutations(places):
    s = sum(graph[x + "-" + y] for x, y in zip(p, p[1:]))
    longest = max(longest, s)

print(longest)