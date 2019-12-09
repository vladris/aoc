numbers = [int(x) for x in open('input').readline().split(',')] + [0] * 10 ** 5

def test(numbers, input, output):
    i, rel = 0, 0

    get = {
        0: lambda i: numbers[numbers[i]],
        1: lambda i: numbers[i],
        2: lambda i: numbers[rel + numbers[i]]
    }

    adjust = lambda m: rel if m == 2 else 0

    def assign(mode, i, val):
        if mode == 0:
            numbers[numbers[i]] = val
        elif mode == 2:
            numbers[rel + numbers[i]] = val

    while numbers[i] != 99:
        opcode = numbers[i] % 100
        m1, m2, m3 = numbers[i] // 100 % 10, numbers[i] // 1000 % 10, numbers[i] // 10000 % 10

        if opcode == 1:
            numbers[numbers[i + 3] + adjust(m3)] = get[m1](i + 1) + get[m2](i + 2)
            i += 4
        elif opcode == 2:
            numbers[numbers[i + 3] + adjust(m3)] = get[m1](i + 1) * get[m2](i + 2)
            i += 4
        elif opcode == 3:
            numbers[numbers[i + 1] + adjust(m1)] = input()
            i += 2
        elif opcode == 4:
            output(get[m1](i + 1))
            i += 2
        elif opcode == 5:
            i = get[m2](i + 2) if get[m1](i + 1) else i + 3
        elif opcode == 6:
            i = get[m2](i + 2) if not get[m1](i + 1) else i + 3
        elif opcode == 7:
            numbers[numbers[i + 3] + adjust(m3)] = 1 if get[m1](i + 1) < get[m2](i + 2) else 0
            i += 4
        elif opcode == 8:
            numbers[numbers[i + 3] + adjust(m3)] = 1 if get[m1](i + 1) == get[m2](i + 2) else 0
            i += 4
        elif opcode == 9:
            rel += get[m1](i + 1)
            i += 2

test(numbers, lambda: 2, print)
