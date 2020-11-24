numbers = [int(x) for x in open('input').readline().split(',')] + [0] * 10 ** 5

def intcode(numbers, input):
    i, rel = 0, 0

    get = {
        0: lambda i: numbers[numbers[i]],
        1: lambda i: numbers[i],
        2: lambda i: numbers[rel + numbers[i]]
    }

    adjust = lambda m: rel if m == 2 else 0

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

            if numbers[numbers[i + 1] + adjust(m1)] == -1:
                yield -1

            i += 2
        elif opcode == 4:
            yield get[m1](i + 1)
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

queues = [[i] for i in range(50)]

def run(i):
    while True:
        if queues[i]:
            yield queues[i].pop(0)
        else:
            yield -1

def make_input(i):
    inp = run(i)
    return lambda: next(inp)

nics = [intcode(numbers[:], make_input(i)) for i in range(50)]
nat, sent = None, None

while True:
    idle = all([len(queue) == 0 for queue in queues])
    for nic in nics:
        dest = next(nic)

        if dest == -1:
            continue

        idle = False

        x, y = next(nic), next(nic) 

        if dest == 255:
            nat = (x, y)
        else:
            queues[dest] += [x, y]

    idle = idle and all([len(queue) == 0 for queue in queues])

    if idle:
        if sent and sent[1] == nat[1]:
            print(nat[1])
            exit()

        queues[0] += [*nat]
        sent = nat
