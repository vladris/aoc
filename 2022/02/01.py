total = 0

for line in open("input").readlines():
    p1, p2 = line.strip().split(' ')
    p1, p2 = ord(p1) - ord('A') + 1, ord(p2) - ord('X') + 1

    if (p1 + 1 == p2) or (p1 == 3 and p2 == 1):
        total += 6
    elif p1 == p2:
        total += 3

    total += p2

print(total)
