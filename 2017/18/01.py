input = open("input").readlines()

regs = {}
prog = []

def get(i):
    return regs[i] if i in regs else i

for line in input:
    i, rest = line.strip().split(" ", 1)

    if i not in ["snd", "rcv"]:
        d, s = rest.split(" ")
        if not d.isalpha():
            d = int(d)
        else:
            regs[d] = 0
        
        if not s.isalpha():
            s = int(s)
        else:
            regs[s] = 0
        prog.append((i, d, s))
    else:
        regs[rest] = 0
        prog.append((i, rest))

pc = 0
while True:
    instr = prog[pc]
    if instr[0] == "set":
        regs[instr[1]] = get(instr[2])
    elif instr[0] == "add":
        regs[instr[1]] += get(instr[2])
    elif instr[0] == "mul":
        regs[instr[1]] *= get(instr[2]) 
    elif instr[0] == "mod":
        regs[instr[1]] %= get(instr[2])
    elif instr[0] == "jgz" and get(instr[1]) > 0:
        pc += get(instr[2]) - 1
    elif instr[0] == "snd":
        regs["snd"] = get(instr[1])
    elif get(instr[1]) != 0:
        print(regs["snd"])
        exit()
    pc += 1
