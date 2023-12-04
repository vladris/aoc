lines = ['.' + line.strip() + '.' for line in open('input').readlines()]
lines = ['.' * len(lines[0])] + lines + ['.' * len(lines[0])]

def number(ln, ch):
    if not lines[ln][ch].isdigit():
        return None

    start, end = ch, ch

    while lines[ln][start].isdigit():
        start -= 1

    while lines[ln][end].isdigit():
        end += 1

    return int(lines[ln][start + 1:end])


def scan():
    ln, ch = 1, 1
    while ln < len(lines) - 1:
        while ch < len(lines[0]) - 1:
            if lines[ln][ch] == '*':
                yield ln, ch
            ch += 1
        ln += 1
        ch = 1


total = 0
for ln, ch in scan():
    numbers = []
    if n := number(ln, ch - 1):
        numbers.append(n)
    if n := number(ln, ch + 1):
        numbers.append(n)
    if n := number(ln - 1, ch):
        numbers.append(n)
    else:
        if n := number(ln - 1, ch - 1):
            numbers.append(n)
        if n := number(ln - 1, ch + 1):
            numbers.append(n)
    if n := number(ln + 1, ch):
        numbers.append(n)
    else:
        if n := number(ln + 1, ch - 1):
            numbers.append(n)
        if n := number(ln + 1, ch + 1):
            numbers.append(n)

    if len(numbers) != 2:
        continue

    total += numbers[0] * numbers[1]

print(total)
