monkeys = []
modulo = 1


class Monkey:
    def __init__(self, id, items, op, test, true_monkey, false_monkey):
        self.id = id
        self.items = items
        self.op = op
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.processed = 0


    def process(self):
        while self.items:
            self.processed += 1
            self.__process_item()


    def __process_item(self):
        new = eval(self.op, {'old': self.items.pop(0)}) % modulo
        if new % self.test == 0:
            monkeys[self.true_monkey].items.append(new)
        else:
            monkeys[self.false_monkey].items.append(new)


def parse_monkey(lines):
    if lines[0] == '\n':
        lines.pop(0)

    id = int(lines.pop(0).split(' ')[1][:-2])
    items = [int(i.strip()) for i in lines.pop(0).split(':')[1].split(',')]
    operation = lines.pop(0).split('=')[1].strip()
    test = int(lines.pop(0).split(' ')[-1])
    true_monkey = int(lines.pop(0).split(' ')[-1])
    false_monkey = int(lines.pop(0).split(' ')[-1])

    return Monkey(id, items, operation, test, true_monkey, false_monkey)


lines = open('input').readlines()
while lines:
    monkey = parse_monkey(lines)
    monkeys.append(monkey)
    modulo *= monkey.test

for i in range(10000):
    for monkey in monkeys:
        monkey.process()

fst, snd, *_ = sorted(monkeys, key=lambda m: m.processed, reverse=True)
print(fst.processed * snd.processed)

