from itertools import permutations

numbers = [int(x) for x in open('input').readline().split(',')]

def test(numbers, input):
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
            yield get[m1](i + 1)
            i += 2
        elif opcode == 5:
            i = get[m2](i + 2) if get[m1](i + 1) else i + 3
        elif opcode == 6:
            i = get[m2](i + 2) if not get[m1](i + 1) else i + 3
        elif opcode == 7:
            numbers[numbers[i + 3]] = 1 if get[m1](i + 1) < get[m2](i + 2) else 0
            i += 4
        elif opcode == 8:
            numbers[numbers[i + 3]] = 1 if get[m1](i + 1) == get[m2](i + 2) else 0
            i += 4

class Input:
    def __init__(self, values):
        self.values = values

    def __call__(self):
        result, self.values = self.values[0], self.values[1:]
        return result

def run(numbers, seq):
    out = 0
    inps = [Input([seq[i]]) for i in range(5)]
    inps[0].values += [0]
    amps = [test(numbers[:], inp) for inp in inps]

    try:
        while True:
            for i in range(5):
                out = next(amps[i])
                inps[(i + 1) % 5].values += [out]
    except StopIteration:
        return out

best = 0
for perm in permutations(list(range(5, 10))):
    best = max(best, run(numbers, perm))

print(best)
