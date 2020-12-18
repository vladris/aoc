input = open("input").readlines()

program = [line.strip().split(" ") for line in input]

pc, regs = 0, {r: 0 for r in "abcd"}

while pc < len(program):
    instr = program[pc]
    if instr[0] == "cpy":
        regs[instr[2]] = int(instr[1]) if instr[1] not in "abcd" else regs[instr[1]]
    elif instr[0] == "inc":
        regs[instr[1]] += 1
    elif instr[0] == "dec":
        regs[instr[1]] -= 1
    elif (int(instr[1] if instr[1] not in "abcd" else regs[instr[1]])) != 0:
        pc += int(instr[2]) - 1
    pc += 1

print(regs["a"])
