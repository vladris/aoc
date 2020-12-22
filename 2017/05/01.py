input = list(map(int, open("input").read().strip().split("\n")))

pc, steps = 0, 0

while pc < len(input):
    input[pc] += 1
    pc += input[pc] - 1
    steps += 1

print(steps)
