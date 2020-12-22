input = open("input").read().strip()

total = 0
for a, b in zip(input, input[len(input) // 2:] + input[:len(input) // 2]):
    if a == b:
        total += int(a)

print(total)
