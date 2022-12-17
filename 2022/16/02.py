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
cache = {}


def search(me=('AA', 0), elephant=('AA', 0), opened=set(), time=26, score=0):
    global best

    if score > best:
        best = score

    key = str(me) + str(elephant) + str(time)
    if key in cache:
        if cache[key] > score:
            return

    cache[key] = score

    for node in to_open - opened:
        me_next, elephant_next, score_next = me, elephant, score
        if me[1] == 0:
            me_next = (node, dist[me[0]][node] + 1)
            score_next += (time - dist[me[0]][node] - 1) * flows[node]
        else:
            elephant_next = (node, dist[elephant[0]][node] + 1)
            score_next += (time - dist[elephant[0]][node] - 1) * flows[node]

        dt = min(me_next[1], elephant_next[1])
        me_next = (me_next[0], me_next[1] - dt)
        elephant_next = (elephant_next[0], elephant_next[1] - dt)

        if time - dt >= 0:
            search(me_next, elephant_next, opened |
                   {node}, time - dt, score_next)


search()

print(best)
