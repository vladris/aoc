input = [int(c) for c in "685974213"]

def move(l, i):
    minl, maxl, c = min(l), max(l), l[i]
    o, j = [], i + 1
    for _ in range(3):
        if j == len(l):
            j = 0
        o.append(l.pop(j))

    i = l.index(c)
    j = l[i] - 1

    while j not in l:
        j -= 1
        if j < minl:
            j = maxl

    for _ in range(3):
        l.insert(l.index(j) + 1, o.pop())
        
    return (l.index(c) + 1) % len(l)

i = 0
for c in range(100):
    i = move(input, i)

while input[0] != 1:
    input = input[1:] + input[0:1]

for c in input[1:]:
    print(c, end="")
print()
