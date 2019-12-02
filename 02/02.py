program = [int(x) for x in open('input').readline().split(',')]

for noun in range(100):
    for verb in range(100):
        numbers = program[:]
        numbers[1], numbers[2] = noun, verb

        i = 0
        while numbers[i] != 99:
            op = (lambda x, y: x + y) if numbers[i] == 1 else (lambda x, y: x * y)
            numbers[numbers[i + 3]] = op(numbers[numbers[i + 1]], numbers[numbers[i + 2]])
            i += 4

        if numbers[0] == 19690720:
            print(noun * 100 + verb)
            exit()