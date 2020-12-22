input = open("input").readlines()

comp = set()
for line in input:
    a, b = line.strip().split("/")
    comp.add((int(a), int(b)))

best = 0

def build(bridge, s, port, rest):
    global best

    if rest:
        for a, b in rest:
            if a == port:
                build(bridge + [(a, b)], s + a + b, b, rest - {(a, b)})
            if b == port:
                build(bridge + [(b, a)], s + a + b, a, rest - {(a, b)})

    best = max(best, s)

build([], 0, 0, comp)
print(best)
