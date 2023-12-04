lines = ['.' + line.strip() + '.' for line in open('input').readlines()]
lines = ['.' * len(lines[0])] + lines + ['.' * len(lines[0])]

def scan():
    ln, ch = 1, 1
    while ln < len(lines) - 1:
        while ch < len(lines[0]) - 1:
            if lines[ln][ch].isdigit():
                i = ch
                while lines[ln][i].isdigit():
                    i += 1
                yield ln, ch, i
                ch = i
            ch += 1
        ln += 1
        ch = 1

def is_symbol(c):
    return not c.isdigit() and c != '.'

def any_symbol(args):
    ln, ch, end = args
    return any([is_symbol(c) for c in lines[ln - 1][ch - 1:end + 1]]) or \
        any([is_symbol(c) for c in lines[ln + 1][ch - 1:end + 1]]) or \
        is_symbol(lines[ln][ch - 1]) or is_symbol(lines[ln][end])

print(sum([int(lines[ln][ch:end]) for ln, ch, end in filter(any_symbol, scan())]))
