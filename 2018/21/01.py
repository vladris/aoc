input = open("input").readlines()

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

ops = {
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr,
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtir": gtir,
    "gtri": gtri,
    "gtrr": gtrr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr
}

ip = int(input[0][4:])
prog = []

for line in input[1:]:
    r, a, b, c = line.split()
    prog.append((r, int(a), int(b), int(c)))

for j in range(10 ** 6):
    rs = [0] * 6
    rs[0] = j
    counter = 0
    while 0 <= rs[ip] < len(prog):
        counter += 1
        if counter == 10000:
            break
        pc = rs[ip]
        ops[prog[pc][0]](rs, prog[pc][1], prog[pc][2], prog[pc][3])
        rs[ip] += 1

    if counter < 10000:
        print(j)
        exit()
