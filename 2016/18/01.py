row = open("input").read().strip()

row = [c == "." for c in row]

total = sum(row)
for _ in range(39):
    next = []
    for i in range(len(row)):
        prev = [True] + row + [True]
        next += [prev[i] == prev[i + 2]]
    row = next
    total += sum(row)

print(total)
