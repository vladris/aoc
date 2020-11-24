offset = int(open('input').readline()[:7])
inp = [int(c) for c in open('input').readline()] * 10000
inp = inp[offset:]

def compute(inp, total):
    new_total = 0
    result = []
    for i in inp:
        v = abs(total) % 10
        result.append(v)
        total -= i
        new_total += v
    return result, new_total

total = sum(inp)

for i in range(100):
    inp, total = compute(inp, total)

print(inp[:8])