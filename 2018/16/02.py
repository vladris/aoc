import re

input, rest = open("input").read().split("\n\n\n")

samples = []
for m in re.finditer(r"Before: \[(.*)\]\n(.*)\nAfter:  \[(.*)\]", input, re.MULTILINE):
    samples.append((
        list(map(int, m[1].split(","))),
        list(map(int, m[2].split(" "))),
        list(map(int, m[3].split(",")))
    ))

def addr(rs, a, b, c): addi(rs, a, rs[b], c)
def addi(rs, a, b, c): rs[c] = rs[a] + b
def mulr(rs, a, b, c): muli(rs, a, rs[b], c)
def muli(rs, a, b, c): rs[c] = rs[a] * b
def banr(rs, a, b, c): bani(rs, a, rs[b], c)
def bani(rs, a, b, c): rs[c] = rs[a] & b
def borr(rs, a, b, c): bori(rs, a, rs[b], c)
def bori(rs, a, b, c): rs[c] = rs[a] | b
def setr(rs, a, b, c): seti(rs, rs[a], b, c)
def seti(rs, a, b, c): rs[c] = a
def gtir(rs, a, b, c): rs[c] = 1 if a > rs[b] else 0
def gtri(rs, a, b, c): rs[c] = 1 if rs[a] > b else 0
def gtrr(rs, a, b, c): rs[c] = 1 if rs[a] > rs[b] else 0
def eqir(rs, a, b, c): rs[c] = 1 if a == rs[b] else 0
def eqri(rs, a, b, c): rs[c] = 1 if rs[a] == b else 0
def eqrr(rs, a, b, c): rs[c] = 1 if rs[a] == rs[b] else 0

ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

def valid(before, i, after):
    o = []
    for op in ops:
        r = before[:]
        op(r, *i[1:])
        if r == after:
            o.append((i[0], op))
    return o

opids = {}

while ops:
    for sample in samples:
        o = valid(*sample)
        if len(o) != 1:
            continue

        o = o[0]
        opids[o[0]] = o[1]
        ops.remove(o[1])

rs = [0, 0, 0, 0]
for line in rest[1:-1].split("\n"):
    i, a, b, c = tuple(map(int, line.split(" ")))
    opids[i](rs, a, b, c)

print(rs[0])
