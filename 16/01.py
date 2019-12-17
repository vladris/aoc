inp = [int(c) for c in open('input').readline()]

def pattern(digit, length):
    digit += 1
    p = [0] * digit + [1] * digit + [0] * digit + [-1] * digit
    p = p * (length // len(p) + 1)
    return p[1:length + 1]

def compute_digit(inp, digit):
    return abs(sum([i[0] * i[1] for i in zip(inp, pattern(digit, len(inp)))])) % 10

def compute(inp):
    result = []
    for i in range(len(inp)):
        result.append(compute_digit(inp, i))
    return result

for i in range(100):
    inp = compute(inp)

print(inp[:8])