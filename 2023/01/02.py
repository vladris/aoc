total = 0
digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in open('input').readlines():
    d1, d2 = 0, 0

    i = 0
    while d1 == 0:
        for digit in digits:
            if line[i:].startswith(digit):
                d1 = digits.index(digit) + 1
        if line[i].isdigit():
            d1 = int(line[i])
        i += 1

    i = -1
    while d2 == 0:
        for digit in digits:
            if line[:i].endswith(digit):
                d2 = digits.index(digit) + 1
        if line[i].isdigit():
            d2 = int(line[i])
        i -= 1

    print('d1:', d1, 'd2:', d2)
    total += d1 * 10 + d2

print(total)
