input = open("input").readlines()

program = [line.strip().split(" ") for line in input]

def run(val):
    pc, regs = 0, {r: 0 for r in "abcd"}
    regs["a"] = val
    seq = 0
    while pc < len(program):
        instr = program[pc]
        if instr[0] == "cpy":
            if instr[2] in "abcd":
                regs[instr[2]] = int(instr[1]) if instr[1] not in "abcd" else regs[instr[1]]
        elif instr[0] == "inc":
            regs[instr[1]] += 1
        elif instr[0] == "dec":
            regs[instr[1]] -= 1
        elif instr[0] == "jnz" and (int(instr[1] if instr[1] not in "abcd" else regs[instr[1]])) != 0:
            pc += (int(instr[2]) if instr[2] not in "abcd" else regs[instr[2]]) - 1
        elif instr[0] == "out":
            if seq % 2 != int(instr[1] if instr[1] not in "abcd" else regs[instr[1]]):
                return False
            seq += 1
            if seq == 100:
                return True

        pc += 1

i = 0
while True:
    if (run(i)):
        break
    i += 1

print(i)
