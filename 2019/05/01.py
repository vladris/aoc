numbers = [int(x) for x in open('input').readline().split(',')]

def test(numbers, input, output):
    i = 0

    get = {
        0: lambda i: numbers[numbers[i]],
        1: lambda i: numbers[i] 
    }

    while numbers[i] != 99:
        opcode = numbers[i] % 100
        m1, m2 = numbers[i] // 100 % 10, numbers[i] // 1000 % 10

        if opcode == 1:
            numbers[numbers[i + 3]] = get[m1](i + 1) + get[m2](i + 2)
            i += 4
        elif opcode == 2:
            numbers[numbers[i + 3]] = get[m1](i + 1) * get[m2](i + 2)
            i += 4
        elif opcode == 3:
            numbers[numbers[i + 1]] = input()
            i += 2
        elif opcode == 4:
            output(get[m1](i + 1))
            i += 2

test(numbers, lambda: 1, print)
