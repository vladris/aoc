seeds = [512, 191]

class Generator:
    def __init__(self, factor, seed):
        self.factor = factor
        self.n = seed

    def next(self):
        self.n = (self.n * self.factor) % 2147483647
        return self.n

    def bits(self):
        return self.n & 0xffff

a = Generator(16807, seeds[0])
b = Generator(48271, seeds[1])

match = 0
for _ in range(4 * 10 ** 7):
    a.next()
    b.next()
    if a.bits() == b.bits():
        match += 1

print(match)
