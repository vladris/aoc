input = open("input").readlines()

program = []

for line in input:
    op, r = line.strip().split(maxsplit=1)
    if op in ["jie", "jio"]:
        r, offset = r.split(",")
        program.append((op, r, int(offset)))
    elif op == "jmp":
        program.append((op, int(r)))
    else:
        program.append((op, r))

reg, pc = { "a": 0, "b": 0 }, 0

while pc < len(program):
    instr = program[pc]
    if   instr[0] == "hlf": reg[instr[1]] //= 2
    elif instr[0] == "tpl": reg[instr[1]] *= 3
    elif instr[0] == "inc": reg[instr[1]] += 1
    elif instr[0] == "jmp": pc += instr[1] - 1
    elif instr[0] == "jie": pc += instr[2] - 1 if reg[instr[1]] % 2 == 0 else 0
    elif instr[0] == "jio": pc += instr[2] - 1 if reg[instr[1]] == 1 else 0
    pc += 1

print(reg["b"])
