input = open("input").readlines()

program = []
for line in input:
    i, x, y = line.strip().split(" ")
    if not x.isalpha():
        x = int(x)
    if not y.isalpha():
        y = int(y)
    program.append((i, x, y))

regs = {c: 0 for c in "abcdefgh"}

def get(v):
    return regs[v] if v in regs else v

pc, mul = 0, 0
while 0 <= pc < len(program):
    i, x, y = program[pc]
    if i == "set":
        regs[x] = get(y)
    elif i == "sub":
        regs[x] -= get(y)
    elif i == "mul":
        mul += 1
        regs[x] *= get(y)
    elif i == "jnz":
        if get(x) != 0:
            pc += get(y) - 1
    pc += 1

print(mul)
