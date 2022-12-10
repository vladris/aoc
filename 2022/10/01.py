clock, value = 1, 1

cycles = [20, 60, 100, 140, 180, 220, 10 ** 100]
cycle, total = 0, 0

for line in open('input').readlines():
    op, *val = line.strip().split(' ')
    
    clock += 1
    if clock >= cycles[cycle]:
        total += cycles[cycle] * value
        cycle += 1

    if op == 'addx':
        value += int(val[0])
        clock += 1


print(total)
