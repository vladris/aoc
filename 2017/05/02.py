input = list(map(int, open("input").read().strip().split("\n")))

pc, steps = 0, 0

while pc < len(input):
    jmp = input[pc]
    input[pc] += 1 if input[pc] < 3 else -1
    pc += jmp
    steps += 1

print(steps)
