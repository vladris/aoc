regs, prog = open("input").read().split("\n\n")

regs = [int(reg.strip()[11:]) for reg in regs.split("\n")]
prog = list(map(int, prog[8:].strip().split(",")))

def op(value):
    return value if value < 4 else regs[value - 4]


pc, out = 0, []
while pc < len(prog):
    match prog[pc]:
        case 0:
            regs[0] = regs[0] // 2 ** op(prog[pc + 1])
        case 1:
            regs[1] = regs[1] ^ prog[pc + 1]
        case 2:
            regs[1] = op(prog[pc + 1]) % 8
        case 3:
            if regs[0] != 0:
                pc = prog[pc + 1] - 2
        case 4:
            regs[1] = regs[1] ^ regs[2]
        case 5:
            out.append(str(op(prog[pc + 1]) % 8))
        case 6:
            regs[1] = regs[0] // 2 ** op(prog[pc + 1])
        case 7:
            regs[2] = regs[0] // 2 ** op(prog[pc + 1])
    pc += 2

print(",".join(out))
