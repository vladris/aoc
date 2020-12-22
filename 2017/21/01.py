import math

pat = [
    ".#.",
    "..#",
    "###"
]

input = open("input").readlines()

rules = {}
for line in input:
    f, t = line.strip().split(" => ")
    rules[f] = t

def flip(p):
    return [line[::-1] for line in p]

def rotate(p):
    new_p = []
    for i in range(len(p[0])):
        new_p.append("".join(reversed([line[i] for line in p])))
    return new_p

def transform(p):
    for _ in range(2):
        for _ in range(4):
            p = rotate(p)
            yield p
        p = flip(p)
        yield p

def split(p):
    ps = []
    step = 2 if len(p) % 2 == 0 else 3
    for i in range(0, len(p), step):
        for j in range(0, len(p), step):
            c = []
            for k in range(step):
                c.append(p[i + k][j:j + step])
            ps.append(c)
    return ps

def merge(ps):
    new_p, l = [], int(math.sqrt(len(ps)))

    for i in range(0, len(ps), l):
        for k in range(len(ps[0])):
            line = ""
            for j in range(l):
                line += ps[i + j][k]
            new_p.append(line)
    return new_p
                
def update(p):
    for pt in transform(p):
        f = "/".join(pt)
        if f in rules:
            return rules[f].split("/")

for _ in range(5):
    pat = merge([update(p) for p in split(pat)])

print(sum([1 for c in "".join(pat) if c == "#"]))
