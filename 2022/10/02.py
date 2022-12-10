clock, value, crt = 1, 1, ''

def draw(clock, value):
    col = ((clock - 1) % 40)
    result = '#' if abs(col - value) <= 1 else '.'
    if col == 39:
        result += '\n'
    return result 


for line in open('input').readlines():
    op, *val = line.strip().split(' ')

    crt += draw(clock, value)
    clock += 1

    if op == 'addx':
        crt += draw(clock, value)
        clock += 1
        value += int(val[0])

print(crt)
