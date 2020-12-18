input = open("input").readlines()

program = [line.strip().split(" ") for line in input]

pc, regs = 0, {r: 0 for r in "abcd"}
regs["a"] = 12

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
        if pc == 9:
            regs["a"] = regs["b"] * (regs["d"] + 1)
            regs["c"] = 0
            regs["d"] = 0
        else:
            pc += (int(instr[2]) if instr[2] not in "abcd" else regs[instr[2]]) - 1
    elif instr[0] == "tgl":
        at = pc + (int(instr[1]) if instr[1] not in "abcd" else regs[instr[1]])
        if at < len(program):
            if len(program[at]) == 2:
                program[at][0] = "inc" if program[at][0] != "inc" else "dec"
            else:
                program[at][0] = "jnz" if program[at][0] != "jnz" else "cpy"

    pc += 1

print(regs["a"])
