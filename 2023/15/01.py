seqs = open('input').read().split(',')

total = 0
for seq in seqs:
    i = 0
    for c in seq:
        i = (i + ord(c)) * 17 % 256
    total += i

print(total)
