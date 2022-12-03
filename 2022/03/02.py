import string

total = 0
lines = [line.strip() for line in open("input").readlines()]

i = 0
while i < len(lines):
    elf1, elf2, elf3 = lines[i:i+3]
    elem = set(elf1).intersection(set(elf2)).intersection(set(elf3)).pop()

    if elem in string.ascii_lowercase:
        total += ord(elem) - ord('a') + 1
    else:
        total += ord(elem) - ord('A') + 27

    i += 3

print(total)
