total = 0

for line in open("input").readlines():
    p1, p2 = line.strip().split(' ')
    p1, p2 = ord(p1) - ord('A'), ord(p2) - ord('X')

    total += p2 * 3

    if p2 == 0:
        total += (p1 - 1) % 3 + 1
    elif p2 == 1:
        total += p1 + 1
    else:
        total += (p1 + 1) % 3 + 1

print(total)
