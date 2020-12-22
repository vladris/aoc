input = open("input").readlines()

prog = []

for line in input:
    i, rest = line.strip().split(" ", 1)

    if i not in ["snd", "rcv"]:
        d, s = rest.split(" ")
        if not d.isalpha():
            d = int(d)
        
        if not s.isalpha():
            s = int(s)

        prog.append((i, d, s))
    else:
        prog.append((i, rest))

class Program:
    def __init__(self, id):
        self.regs = {"p": id}
        self.buffer = []
        self.counter = 0

    def connect(self, p):
        self.other, p.other = p, self

    def get(self, i):
        if isinstance(i, int):
            return i

        if i not in self.regs:
            self.regs[i] = 0
        return self.regs[i]

    def exec(self, prog):
        pc = 0
        while 0 <= pc < len(prog):
            instr = prog[pc]
            if instr[0] == "set":
                self.regs[instr[1]] = self.get(instr[2])
            elif instr[0] == "add":
                self.regs[instr[1]] += self.get(instr[2])
            elif instr[0] == "mul":
                self.regs[instr[1]] *= self.get(instr[2]) 
            elif instr[0] == "mod":
                self.regs[instr[1]] %= self.get(instr[2])
            elif instr[0] == "jgz" and self.get(instr[1]) > 0:
                pc += self.get(instr[2]) - 1
            elif instr[0] == "snd":
                self.counter += 1
                self.other.buffer.insert(0, self.get(instr[1]))
            elif instr[0] == "rcv":
                if not self.buffer:
                    yield

                if not self.buffer:
                    return

                self.regs[instr[1]] = self.buffer.pop()

            pc += 1

p1, p2 = Program(0), Program(1)
p1.connect(p2)

g1 = p1.exec(prog)
g2 = p2.exec(prog)

while g1 or g2:
    if g1:
        try:
            next(g1)
        except StopIteration:
            g1 = None

    if g2:
        try:
            next(g2)
        except StopIteration:
            g2 = None

print(p2.counter)
