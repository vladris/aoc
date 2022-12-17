import re

dist, flows, to_open = {}, {}, set()

for line in open('input').readlines():
    m = re.match(
        'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)$', line)
    src, flow, *dst = m.groups()
    dst = [d.strip() for d in dst[0].split(',')]
    dist[src] = {d: 1 for d in dst} | {src: 0}
    flows[src] = int(flow)
    if flows[src] > 0:
        to_open.add(src)


for i in dist:
    for j in dist:
        if j not in dist[i]:
            dist[i][j] = 1000

for k in dist:
    for i in dist:
        for j in dist:
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]


best = 0


def search(current='AA', opened=set(), time=30, score=0):
    global best

    score += time * flows[current]

    if score >= best:
        best = score

    for node in to_open - opened:
        if time - dist[current][node] - 1 >= 0:
            search(node, opened | {node}, time -
                   dist[current][node] - 1, score)


search()

print(best)
