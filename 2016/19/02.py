i, prev, elf = 1, 1, 1
while i < 3005290:
    if elf == i:
        prev, elf = elf, 1
    elif elf < prev:
        elf += 1
    else:
        elf += 2
    i += 1

print(elf)
