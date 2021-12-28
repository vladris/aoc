graph = {
    0: [1],
    1: [0, 2],
    2: [1, 3, 11],
    3: [2, 4],
    4: [3, 5, 13],
    5: [4, 6],
    6: [5, 7, 15],
    7: [6, 8],
    8: [7, 9, 17],
    9: [8, 10],
    10: [9],
    11: [2, 12],
    12: [11],
    13: [4, 14],
    14: [13],
    15: [6, 16],
    16: [15],
    17: [8, 18],
    18: [17]
}

paths = {}

def chart(cur, path=[]):
    for n in graph[cur]:
        if n in path:
            continue
        chart(n, path[:] + [cur])

    if not path:
        return

    if path[0] not in paths:
        paths[path[0]] = {}

    paths[path[0]][cur] = path[1:] + [cur]

for n in graph:
    chart(n)

dest = {
    "A": [11, 12],
    "B": [13, 14],
    "C": [15, 16],
    "D": [17, 18]
}

energy = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}

class Pod:
    def __init__(self, type, loc, pods):
        self.type = type
        self.loc = loc
        self.pods = pods

    def done(self):
        dests = dest[self.type]
        if self.loc not in dests:
            return False
        
        for i in dests[dests.index(self.loc) + 1:]:
            if self.pods.at(i).type != self.type:
                return False

        return True

    def available(self, loc):
        for i in paths[self.loc][loc]:
            if self.pods.at(i):
                return False
        return True

    def move(self, loc):
        self.pods.energy += energy[self.type] * len(paths[self.loc][loc])
        self.pods.pods[self.loc], self.pods.pods[loc] = None, self
        self.loc = loc

    def options(self):
        if self.done():
            return

        if self.loc > 10:
            for i in [0, 1, 3, 5, 7, 9, 10]:
                if self.available(i):
                    yield i

        dests = dest[self.type]
        if self.loc in dests:
            return

        if self.available(dests[1]):
            yield dests[1]
            return

        pod = self.pods.at(dests[1])
        if pod and pod.type != self.type:
            return

        if self.available(dests[0]):
            yield dests[0]

class Pods:
    def __init__(self):
        self.pods = {i: None for i in range(27)}
        self.energy = 0

    def add(self, type, loc):
        self.pods[loc] = Pod(type, loc, self)

    def at(self, i):
        return self.pods[i]

    def done(self):
        return all(pod.done() if pod else True for pod in self.pods.values())

    def clone(self):
        new = Pods()
        for pod in self.pods.values():
            if not pod:
                continue
            new.add(pod.type, pod.loc)
        new.energy = self.energy
        return new

    def hash(self):
        return "".join(p.type if p else "." for p in self.pods.values())

pods = Pods()
with open("input") as f:
    f.readline()
    f.readline()
    l = f.readline()
    pods.add(l[3], 11)
    pods.add(l[5], 13)
    pods.add(l[7], 15)
    pods.add(l[9], 17)
    l = f.readline()
    pods.add(l[3], 12)
    pods.add(l[5], 14)
    pods.add(l[7], 16)
    pods.add(l[9], 18)

best, seen = 10 ** 9, {}

def search(pods):
    global best

    if pods.energy >= best:
        return

    if pods.done():
        best = pods.energy
        return

    h = pods.hash()
    if h in seen and pods.energy >= seen[h]:
        return
    seen[h] = pods.energy

    for i in range(19):
        pod = pods.at(i)
        if not pod:
            continue

        for m in pod.options():
            npods = pods.clone()
            npods.at(i).move(m)
            search(npods)

search(pods)
print(best)
