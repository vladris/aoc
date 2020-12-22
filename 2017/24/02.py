input = open("input").readlines()

comp = set()
for line in input:
    a, b = line.strip().split("/")
    comp.add((int(a), int(b)))

l, best = 0, 0

def build(bridge, s, port, rest):
    global l, best

    if rest:
        for a, b in rest:
            if a == port:
                build(bridge + [(a, b)], s + a + b, b, rest - {(a, b)})
            if b == port:
                build(bridge + [(b, a)], s + a + b, a, rest - {(a, b)})
        
    if len(bridge) > l:
        l = len(bridge)
        best = s
    elif len(bridge) == l:
        best = max(best, s)


build([], 0, 0, comp)
print(best)
