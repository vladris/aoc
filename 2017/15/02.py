seeds = [512, 191]

class Generator:
    def __init__(self, factor, seed, mod):
        self.factor = factor
        self.mod = mod
        self.n = seed

    def next(self):
        while True:
            self.n = (self.n * self.factor) % 2147483647
            if self.n % self.mod == 0:
                break
        return self.n

    def bits(self):
        return self.n & 0xffff

a = Generator(16807, seeds[0], 4)
b = Generator(48271, seeds[1], 8)

match = 0
for _ in range(5 * 10 ** 6):
    a.next()
    b.next()
    if a.bits() == b.bits():
        match += 1

print(match)
