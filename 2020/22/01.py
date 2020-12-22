p1, p2 = open("input").read().split("\n\n")

p1 = list(map(int, p1.strip().split("\n")[1:]))
p2 = list(map(int, p2.strip().split("\n")[1:]))

while p1 and p2:
    c1, c2 = p1.pop(0), p2.pop(0)
    if c1 > c2:
        p1 += [c1, c2]
    else:
        p2 += [c2, c1]

p = p1 if p1 else p2

total = 0
for i, c in enumerate(reversed(p)):
    total += (i + 1) * c

print(total)
