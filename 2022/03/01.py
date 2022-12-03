import string

total = 0

for line in open("input").readlines():
    mid = len(line) // 2
    fst, snd = line[:mid], line[mid:]
    dup = set(fst).intersection(set(snd)).pop()

    if dup in string.ascii_lowercase:
        total += ord(dup) - ord('a') + 1
    else:
        total += ord(dup) - ord('A') + 27

print(total)
