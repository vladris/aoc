lines = open('input').readlines()

valid = 0
for line in lines:
    counts, letter, password = line.split()
    minc, maxc = map(int, counts.split('-'))
    letter = letter[0]

    count = sum([1 for c in password if c == letter])
    if minc <= count and count <= maxc:
        valid += 1

print(valid)
