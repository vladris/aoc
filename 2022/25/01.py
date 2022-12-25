def to_dec(n):
    digits = {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}
    return sum([5 ** i * digits[d] for i, d in enumerate(n[::-1])])


def to_snafu(n):
    s = ''
    while n:
        s = ['0', '1', '2', '=', '-'][n % 5] + s
        n = n // 5 + (1 if s[0] in '-=' else 0)

    return s


print(to_snafu(sum([to_dec(line.strip()) for line in open('input').readlines()])))
