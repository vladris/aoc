input = open("input").read().strip()

total = 0
for a, b in zip(input, input[1:] + input[0]):
    if a == b:
        total += int(a)

print(total)
