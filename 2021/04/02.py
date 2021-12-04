class Card:
    def __init__(self, lines):
        self.lines = lines

    def mark(self, n):
        self.lines = [[i if i != n else -1 for i in line] for line in self.lines]
        return self.check_row() or self.check_col()

    def check_row(self):
        return any([all(map(lambda x: x == -1, line)) for line in self.lines])

    def check_col(self):
        return any([all(map(lambda x: x == -1, [line[i] for line in self.lines]))
            for i in range(len(self.lines[0]))])

    def count(self):
        return sum([sum(filter(lambda x: x > 0, line)) for line in self.lines])

cards = []
with open("input") as f:
    nums = map(int, f.readline().split(","))
    f.readline()
    while True:
        card = [f.readline() for _ in range(6)]
        if not card[0]:
            break
        cards.append(Card([map(int, line.split()) for line in card[:5]]))

for n in nums:
    for card in cards[:]:
        if card.mark(n):
            if len(cards) == 1:
                print(card.count() * n)
                exit()
            cards.remove(card)
