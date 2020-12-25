input = (14082811, 5249543)

def transform(subject, loop):
    value = 1
    for _ in range(loop):
        value *= subject 
        value %= 20201227
    return value

def loop(target):
    value, l = 1, 0
    while value != target:
        value *= 7
        value %= 20201227
        if l % 10000 == 0:
            print(target, l, value)
        l += 1
    return l

l1 = loop(input[0])

print(transform(input[1], l1))
