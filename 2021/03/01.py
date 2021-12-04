lines = open("input").readlines()

bits = [0] * 12
for line in lines:
    num = map(int, list(line.strip()))
    for i, bit in enumerate(num):
        bits[i] += bit

gamma = 0
for bit in bits:
    gamma = gamma * 2 + int(bit > len(lines) / 2)

print(gamma * (gamma ^ 0b111111111111))
